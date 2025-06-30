import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()
GITHUB_TOKEN = os.environ["GITHUB_API_KEY"]
ORG_NAME = os.environ["ORG_NAME"] 

HEADERS = {
    "Authorization": f"Bearer " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

def get_user_id(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"❌ User '{username}' not found or invalid.")
        return None


def invite_user(user_id, username):
    url = f"https://api.github.com/orgs/{ORG_NAME}/invitations"
    data = {"invitee_id": user_id}
    response = requests.post(url, headers=HEADERS, json=data)
    
    if response.status_code == 201:
        print(f"✅ Invite sent to {username}.")
    elif response.status_code == 422:
        print(f"⚠️ {username} has already been invited or is already a member.")
    else:
        print(f"❌ Failed to invite {username}: {response.text}")



def process_excel(file_path):
    df = pd.read_excel(file_path)
    
    for index, row in df.iterrows():
        username = str(row['GitHubUsername']).strip()
        print(f"\n🎯 Processing {username}...")
        
        user_id = get_user_id(username)
        
        if user_id:
            invite_user(user_id, username)
        
        time.sleep(5)  




process_excel("members.xlsx")
