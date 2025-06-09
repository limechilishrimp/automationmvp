Shopify MVP: Order Status Automation

This project is a serverless FastAPI application designed to automate post-purchase order status handling for a Shopify store.

✅ What It Does

When an order is updated in Shopify:

If it is unfulfilled and tagged as received,

An email is sent to the customer from a domain email (via SendGrid),

The order is then tagged in-progress.

⚙️ Tech Stack

🛒 Shopify Webhooks + Admin GraphQL API

📦 FastAPI (Python)

☁️ AWS Lambda + API Gateway (via Serverless Framework)

💌 SendGrid for transactional email

(Optional) 🗂️ DynamoDB for order log tracking

🚀 Deployment Steps

Create a virtual environment and install requirements

Deploy via Serverless to AWS Lambda

Register your webhook URL in Shopify Admin for "Order Updated"

Use CloudWatch to view webhook logs

📩 Shopify Webhook Payload Example

Webhook data is printed on receipt and looks like:

{
  "id": 123456789,
  "email": "customer@example.com",
  "tags": "received",
  "fulfillment_status": null,
  ...
}

📁 File Structure

├── fastapi_app.py      # FastAPI route logic
├── handler.py          # Mangum adapter for Lambda
├── requirements.txt    # Python dependencies
├── serverless.yml      # Serverless Framework config
└── README.md

🧪 Testing

Use Shopify Admin to send a test webhook

Check logs via:

serverless logs -f shopifyWebhook

✅ Status

In-progress

MIT License. Built for Shopify order ops automation MVP.