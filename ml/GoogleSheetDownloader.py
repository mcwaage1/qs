from __future__ import print_function

import os.path

import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = input("Copy the googlesheet ID (from the web address): ")
RANGE_NAME = input("Copy the spreadsheet name (from the bottom left of googlesheet): ")

def run(SPREADSHEET_ID=SPREADSHEET_ID, RANGE_NAME=RANGE_NAME):
        
    # https://stackoverflow.com/questions/11485271/google-oauth-2-authorization-error-redirect-uri-mismatch
    # Authentication
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('data/token.pickle'):
        with open('data/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('data/credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('data/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # build service
    print('Building service...')
    service = build('sheets', 'v4', credentials=creds)

    # Get Data from Google Sheet and Return a List
    def get_gsheet_data(SPREADSHEET_ID, RANGE_NAME):
          print("Getting spreadsheet...")
          sheet = service.spreadsheets()
          result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
          values = result.get('values', [])
          return values
    
    data_list = get_gsheet_data(SPREADSHEET_ID, RANGE_NAME)
    
    # create data and frame and use first row as header
    print('Making DataFrame from spreadsheet...')
    data = pd.DataFrame(data_list)
    new_header = data.iloc[0] # grab the first row for the header
    data = data[1:]           # take the data less the header row
    data.columns = new_header # set the header row as the df header
    
    print("DataFrame created...", "\n")
    print(data.head())

    # export to csv
    filename = input('The name of the file to be inserted into "data/<filename>.csv": ')
    data.to_csv(f"data/{filename}.csv", index=False)
    print(f'Exported "data/{filename}.csv"')

if __name__ == '__main__':
    run()