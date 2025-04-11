import os
import time
import pickle
import mimetypes
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_FILE = 'token.pickle'
LOCAL_DIRECTORY = 'path/to/your/folder'

def authenticate_google_drive():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file(service, file_path, folder_id=None):
    file_name = os.path.basename(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File {file_name} uploaded to Google Drive with ID: {file['id']}")

def sync_local_to_drive():
    service = authenticate_google_drive()
    for filename in os.listdir(LOCAL_DIRECTORY):
        local_file_path = os.path.join(LOCAL_DIRECTORY, filename)
        if os.path.isfile(local_file_path):
            upload_file(service, local_file_path)

class FileHandler(FileSystemEventHandler):
    def __init__(self, service):
        self.service = service
    
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified or added: {event.src_path}")
        upload_file(self.service, event.src_path)

def start_file_watcher():
    service = authenticate_google_drive()
    event_handler = FileHandler(service)
    observer = Observer()
    observer.schedule(event_handler, LOCAL_DIRECTORY, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    sync_local_to_drive()
    print("Watching folder for changes...")
    start_file_watcher()
