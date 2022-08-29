from google.auth.transport.requests import Request, service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './credentials/keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SPREADSHEET_ID = '1ilwVZ0nwA4yuE7s0gJ67x3xUcyI-PxNBSrFLnpMeHzk'

SHEET_ID = '1913774483'



service = build('sheets', 'v4', credentials=credentials)
sheetService = service.spreadsheets()


def getLastId():

    request = sheetService.get(spreadsheetId=SPREADSHEET_ID).execute()

    totalRows = request.get('sheets', [])[0].get('properties').get('gridProperties').get('rowCount', [])
    

    lastId = totalRows - 2


    return lastId


def getTotalRows():

    request = sheetService.get(spreadsheetId=SPREADSHEET_ID).execute()

    totalRows = request.get('sheets', [])[0].get('properties').get('gridProperties').get('rowCount', [])
    
    return totalRows


def appendCells(animeData):

    lastId = getLastId()

    #List who contains dictionaries
    # with the data of each row
    rowsList = []

    valuesList = []

    for anime in animeData:

        lastId = lastId + 1

        valuesList = [
            {"userEnteredValue": {"numberValue": lastId }},
            {"userEnteredValue": {"stringValue" : anime.get("tittle")}},
            {"userEnteredValue": {"stringValue": anime.get("hash")}},
            {"userEnteredValue": {"stringValue": anime.get("chapter")}},
            {"userEnteredValue": {"stringValue": anime.get("kitsu_id")}}
        ]

        rowsList.append({"values": valuesList})

    
    rowsBody = {
        "appendCells" : {
            "sheetId" : SHEET_ID,
            "rows" : rowsList,
            "fields": "*"
            }    
    }

    batchRequest = {"requests": [rowsBody]}

    request = sheetService.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=batchRequest).execute()

    return request


def getRange(range: str):

    rangeData = sheetService.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()


    return rangeData.get('values')

