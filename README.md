# Shopify Order Tag Email Automation MVP

## === Directory Structure ===
### shopify-email-automation/
├── app/
│   ├── main.py         # FastAPI webhook handler
│   ├── sendgrid_utils.py  # Email logic
│   ├── shopify_utils.py   # Shopify GraphQL tag updater
│   ├── db_utils.py     # DynamoDB interaction (optional)
│   └── __init__.py
├── Dockerfile          # To deploy on AWS Lambda with container
├── requirements.txt
├── .env                # Keys
└── README.md
