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
