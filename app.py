import json
import boto3
import botocore.config
from datetime import datetime

def blog_generate_using_bedrock(blogtopic: str) -> str:
    """
    Invokes the Bedrock model (Claude Sonnet 4.5) to generate a blog post.
    """
    prompt = f"Write a detailed, SEO-friendly 200-word blog on the topic: {blogtopic}."

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ]
            }
        ]
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3})
        )

        model_id = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId=model_id,
            contentType="application/json",
            accept="application/json"
        )

        response_content = response.get("body").read()
        response_data = json.loads(response_content)

        blog_details = response_data.get("content", [{}])[0].get("text", "")
        return blog_details.strip()

    except Exception as e:
        print(f"❌ Error generating the blog: {e}")
        return ""


def save_blog_details_s3(s3_key, s3_bucket, blog_text):
    """
    Saves the generated blog text to an S3 bucket.
    """
    s3 = boto3.client("s3")
    try:
        print(f"📦 Uploading blog to s3://{s3_bucket}/{s3_key}")
        s3.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=blog_text.encode("utf-8"),
            ContentType="text/plain"
        )
        print("✅ Blog successfully saved to S3.")
    except Exception as e:
        print(f"❌ Error saving blog to S3: {e}")


def lambda_handler(event, context):
    """
    AWS Lambda entry point for Bedrock blog generation + S3 save.
    """
    try:
        if isinstance(event.get("body"), str):
            event_body = json.loads(event["body"])
        else:
            event_body = event.get("body", {})
    except json.JSONDecodeError:
        return {"statusCode": 400, "body": json.dumps("Invalid JSON body")}

    blogtopic = event_body.get("blog_topic")
    if not blogtopic:
        return {"statusCode": 400, "body": json.dumps('Missing "blog_topic" in request body')}

    # ✅ Correct bucket name (no trailing spaces)
    s3_bucket = "awsbedrockcoursedhruv"
    print(f"🧠 Generating blog for topic: {blogtopic}")

    blog_text = blog_generate_using_bedrock(blogtopic)

    if blog_text:
        current_time = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        safe_topic = "".join(c for c in blogtopic if c.isalnum() or c in (" ", "_")).rstrip()
        s3_key = f"blog-output/{safe_topic.replace(' ', '_')}_{current_time}.txt"

        save_blog_details_s3(s3_key, s3_bucket, blog_text)

        s3_path = f"s3://{s3_bucket}/{s3_key}"
        print(f"✅ Blog saved at {s3_path}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Blog generation completed successfully",
                "s3_path": s3_path,
                "preview": blog_text[:300] + "..."
            })
        }

    else:
        print("❌ No blog was generated.")
        return {"statusCode": 500, "body": json.dumps("Blog generation failed. Check Lambda logs.")}
