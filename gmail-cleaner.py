import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time

def get_gmail_service():
    creds = None

    # The file token.json stores the user's access and refresh tokens.
    token_path = 'token.json'

    # Check if token file exists
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    # If there are no (valid) credentials available, prompt the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://mail.google.com/'])
            creds = flow.run_local_server(port=8080)

        # Save the credentials for the next run
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def clean_gmail(query):
    # Initialize Gmail API
  
    # Define filter criteria
    # Replace these with your filter criteria

    count = 0
    while True:
    
        try:
            service = get_gmail_service()
            
    # List matching emails
            results = service.users().messages().list(userId='me', q=query).execute()
            messages = results.get('messages', [])
            message_ids = [message['id'] for message in messages]


            if not messages:
                print('No matching emails found.')
            else:
                print(f'Batch Cleaning up {len(messages)} matching emails...')

            # Delete multiple messages in a batch
            request_body = {
                "ids": message_ids
            }    
            count += 1

            for message in messages:
               
                service.users().messages().batchDelete(userId='me', body=request_body).execute()  
                print('Delete completed. Round : ',count)

            time.sleep(60) 

        except Exception as e:
            print(f'An error occurred: {str(e)}')

    

if __name__ == '__main__':
    query = 'category:promotions'
    clean_gmail(query)

   
    
