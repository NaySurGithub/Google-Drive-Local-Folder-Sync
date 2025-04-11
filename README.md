#Google Drive Local Folder Sync

This Python script automatically syncs a local folder with Google Drive. It monitors the folder for any new or modified files and uploads them to Google Drive.

Features:
- Automatic Upload: Any new or modified files in the local folder are automatically uploaded to Google Drive.
- Real-Time Monitoring: The script uses the `watchdog` library to monitor changes in the local folder and triggers uploads accordingly.
- OAuth2 Authentication: Uses OAuth2 for authentication with Google Drive API, ensuring secure access.

Requirements:
- Python 3.x
- Required libraries:
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
  - `watchdog`

Setup:
1. Install required libraries:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client watchdog
   
Setup

Step 1: Google Drive API Setup

1. Go to the Google Developer Console.


2. Create a new project.


3. Enable the Google Drive API for your project.


4. Create OAuth 2.0 credentials:

Download the credentials.json file and place it in the same directory as your script.



5. When you run the script for the first time, it will prompt you to authorize access. Once authorized, the script will store the authentication token in token.pickle for future use.



Step 2: Modify Local Directory Path

Modify the LOCAL_DIRECTORY variable in the script to point to the local folder you want to sync with Google Drive.


Step 3: Run the Script

To run the script, simply execute it using Python:

python sync_to_drive.py

The script will upload all files in the specified local directory to Google Drive. Additionally, it will continuously monitor the directory for changes and upload new or modified files automatically.

Functions

authenticate_google_drive(): Authenticates the user and returns a Google Drive service object.

upload_file(service, file_path, folder_id=None): Uploads a file to Google Drive.

sync_local_to_drive(): Syncs the local directory with Google Drive by uploading all files.

start_file_watcher(): Starts the file watcher to monitor the directory for changes and upload files when modifications occur.

FileHandler class: Handles file system events (additions/changes) and triggers file uploads.


Troubleshooting

Authentication issues: Ensure that credentials.json is correctly placed in the script directory and that the OAuth flow completes successfully.

Permissions issues: Make sure your Google Drive API credentials have the correct permissions to upload files.


License

This project is licensed under the MIT License - see the LICENSE file for details
