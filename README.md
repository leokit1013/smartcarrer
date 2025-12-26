## This app will build resume with side by side options.
 
Integrate streamlit-webrtc for live recording.


Auto-fill these text areas with transcriptions.

## Steps to run and create env in python:
python server.py
streamlit run login.py
OR
python run_app.py

create virtual env in python:
python -m venv .venv
OR
python -m venv myenv

# Activate it (choose your operating system)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
OR
.\venv\Scripts\activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1



## Steps:
Go to GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)

# Click Generate new token.
Scope: repo (for private repos), or just public_repo if your repo is public.
Set expiration (optional).

Copy the token (you’ll use this instead of your password).

Clone a repo using HTTPS
git clone https://github.com/username/repo_name.git


When it asks for username → enter your GitHub username.

When it asks for password → paste the personal access token.

Pull/Push with token
git pull origin main
git push origin main

Use username as your GitHub username and token as password

## See python db
### Go to the path where .db file is present and open cmd
python db - sqlite3:
 
sqlite3 users.db

sqlite> .tables

users  logs  sessions

sqlite> .schema users

sqlite> .headers on

sqlite> .mode column

sqlite> SELECT * FROM users LIMIT 5;

sqlite> ALTER TABLE users ADD COLUMN plan TEXT DEFAULT 'free';

sqlite> .quit

## Resolve google auth eror:
### Add in oauth consent screen -> Clients -> Authorized redirect URIs
https://smartcarrer.in
https://smartcarrer.in/component/streamlit_oauth.authorize_button/index.html

## For Render 
### start command
gunicorn server:app --bind 0.0.0.0:$PORT

## For gcp
###
default port is 8080

# Concept of Switch pages
## Inside pages folder if you want to switch use 
st.switch_pages("pages/filename.py")

## Switching from outside to pages folder
from streamlit_extras.switch_page_button import switch_page
switch_page("Home")