from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates a local webserver and automatically handles authentication
drive = GoogleDrive(gauth)

# Example: Upload a file
file1 = drive.CreateFile({'title': 'Hello.txt'}) 
file1.Upload()
print("File uploaded successfully.")
