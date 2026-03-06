import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os 
def send_to_github(report):


    # API Setup
    token = os.getenv('github_token')
    url = "https://api.github.com/repos/sharathmuthyam/AtomLab-Deployment-Orchestrator/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Create the payload
    payload = {
        "title": f"🚨 Failure Detected: {report['timestamp']}",
        "body": f"The orchestrator found errors.\n\nSummary: {report['summary']}",
        "labels": ["bug", "orchestrator-alert"]
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        # This will tell you if the token worked or not
        if response.status_code == 201:
            print("🚀 Success! GitHub Issue created.")
        else:
            print(f"❌ GitHub rejected the request! Status: {response.status_code}")
            print(f"Message: {response.text}") 
    except Exception as e:
        print(f"Network error: {e}")