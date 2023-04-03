import json
import os
import requests

def lambda_handler(event, context):
    # Extract the URL of the issue from the payload
    # NOTE THAT EVENT IS ALREADY IN JSON.
    issue_url = event['issue']['html_url']
    
    # Send payload to Slack webhook URL
    slack_url = os.environ['SLACK_URL']
    slack_payload = {
        "text": f"Issue Created: {issue_url}"
    }
    response = requests.post(slack_url, json=slack_payload)
    
    # Construct and return a response
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Webhook received successfully"})
    }
    
    return response
