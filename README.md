
# 🚀 AWS Lambda Setup Guide (with API Gateway & AWS Bedrock)

This guide walks you through setting up an **AWS Lambda** function integrated with **API Gateway** for deploying and testing serverless applications — including model calls via **AWS Bedrock**.

---

## 🧩 Step 1: Create a Lambda Function

Create a new function in **AWS Lambda**.
Choose **Author from scratch** and configure the function name, runtime, and permissions.

![Create Lambda Function](https://github.com/user-attachments/assets/d38eb8f0-945a-4ada-858f-70c5ef8f717a)

---

## 💻 Step 2: Write and Deploy Your Code

After the function is created, write your Python (or preferred language) code in the **code editor**.
Select the **model from AWS Bedrock** that best fits your use case.
Then click **Deploy** to save and activate the function.

![Write and Deploy Code](https://github.com/user-attachments/assets/b02f046a-2b59-47fb-8221-8d603ed64cde)

---

## 📦 Step 3: Create a Layer for External Libraries

If your code depends on external libraries (like `boto3`), create a **Lambda Layer**.

1. Install the library into a folder:

   ```bash
   pip install boto3 -t python/
   ```

   *(Replace `boto3` with your library name)*

2. Zip the `python/` folder:

   ```bash
   zip -r layer.zip python/
   ```

3. Upload this ZIP as a **new layer** in the AWS Lambda console.

![Create Lambda Layer](https://github.com/user-attachments/assets/838a2588-8da0-437f-97c0-d8a5526f5ec8)

---

## ⚡ Step 4: Add a Trigger (API Gateway)

To make your Lambda accessible via an API endpoint, create a **trigger** using **API Gateway**.

![Create API Gateway Trigger](https://github.com/user-attachments/assets/86e9ff3c-3218-4a79-944a-17c29bc1e2ee)

---

## 🔀 Step 5: Configure API Routes

Set up the routes (resources and methods) for your API.
Example route: `/blog-generation`

![Create API Routes](https://github.com/user-attachments/assets/1d816e2c-f23b-446d-bb01-00e1d26dca6f)

---

## 🚉 Step 6: Create API Stages

Create and deploy a **stage** for your API (e.g., `devenvironment`).

![Create API Stages](https://github.com/user-attachments/assets/bcce86bb-c134-4152-8865-62c09010b6bc)

---

## ✅ Step 7: Final Lambda Setup

Your Lambda function should now look like this after all configurations:

![Final Lambda Setup](https://github.com/user-attachments/assets/742aa5de-7df9-42b3-a66d-97098aa9a3c4)

---

## 🧪 Step 8: Test Using Postman

To test your API:

1. Copy your **Invoke URL** from the API Gateway stage.
2. Append your route after `/`.
   Example:

   ```
   https://5km6fwoud6.execute-api.us-east-1.amazonaws.com/devenvironment/blog-generation
   ```
3. Paste this URL in **Postman** and send a test request.

![Postman Testing](https://github.com/user-attachments/assets/419d18cc-57f6-4c9d-af62-97db8e4bab5e)

---

## 🎯 Summary

You’ve now successfully:

* Created and deployed a Lambda function
* Added necessary dependencies using layers
* Exposed it via an API Gateway
* Tested it using Postman

Your serverless function is now live and callable from any client application! 🚀

Radhe Radhe 🙏 
