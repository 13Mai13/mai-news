# HOWTOs

This is a page with all the manual processes I needed to do to acomplish this project. 

## How to configure a gmail oauth

1. Go to Google Cloud Console → APIs & Services -> Create a new project

2. Click Enable APIs and Services -> Search for and enable “Gmail API”

3. Go to Credentials → “Create Credentials” → OAuth client ID -> Choose “Desktop app”

Download the resulting credentials.json

Save credentials.json in your project folder. Under `/secrets` -> the projet is configured not to commit that part. Once the credentrials are there, a `token.json` file would be generated. You may need to move it to store it under `secrets`.
