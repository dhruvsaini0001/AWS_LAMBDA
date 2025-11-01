## For setup Lambda : first you have to create a function in a AWS Lambda
<img width="1896" height="1041" alt="image" src="https://github.com/user-attachments/assets/d38eb8f0-945a-4ada-858f-70c5ef8f717a" />
## after creating function you have to write code in editor and dont forget to deploy (select model from AWS Bedrock which one is suited for your project)
<img width="1919" height="988" alt="image" src="https://github.com/user-attachments/assets/b02f046a-2b59-47fb-8221-8d603ed64cde" />
## After deploy code you have to create a Layer for library you use in my case i use boto3 for creating layer I i installed boto3 in a folder and then compress it for  upload 
For installed library you write python boto3 -t python/  ( you change boto3 to your library ) 
<img width="1909" height="814" alt="image" src="https://github.com/user-attachments/assets/838a2588-8da0-437f-97c0-d8a5526f5ec8" />
## after that you have to create a trigger for that i use API gateway 
<img width="1915" height="843" alt="image" src="https://github.com/user-attachments/assets/86e9ff3c-3218-4a79-944a-17c29bc1e2ee" />
## next you have to create routes of api
<img width="1887" height="993" alt="Screenshot 2025-11-01 081635" src="https://github.com/user-attachments/assets/1d816e2c-f23b-446d-bb01-00e1d26dca6f" />
## next you have to stages for your api
<img width="1906" height="964" alt="Screenshot 2025-11-01 081659" src="https://github.com/user-attachments/assets/bcce86bb-c134-4152-8865-62c09010b6bc" />

## After performing these steps your lambda look lilke this 
<img width="1069" height="1032" alt="Screenshot 2025-11-01 081427" src="https://github.com/user-attachments/assets/742aa5de-7df9-42b3-a66d-97098aa9a3c4" />

## next for tesitng purpose i use postman 
for that you have to copy your invoke url from api gateway stages
and write your route after / 
looks like https://5km6fwoud6.execute-api.us-east-1.amazonaws.com/devenvironment/blog-generation
paste this in postman for check 
<img width="1917" height="993" alt="image" src="https://github.com/user-attachments/assets/419d18cc-57f6-4c9d-af62-97db8e4bab5e" />





