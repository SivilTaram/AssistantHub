import requests
from flask import Flask
from flask import abort, redirect, url_for, request, render_template
import json

Client_Id = "e0508786-b2e7-4d01-8509-473d3a8954ee"
Client_Secret = "cbX2NHhNTlUJtUZIA_fNcpu4D0wYOmg-FpvvoRiq1r7_MWSum46KIbKmi8iUHY0JzzRO3qJBY2GVfLKX"

Token_Url = "https://oauth.cnblogs.com/connect/token"
Callback_Url = "https://oauth.cnblogs.com/auth/callback"
Access_Token = ""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("ranking.html")


def fetch_access_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    token_param = {
        "client_id": Client_Id,
        "client_secret": Client_Secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(Token_Url, data=token_param, headers=headers)
    content = response.content.decode('utf8')
    obj = json.loads(content)
    access_token = obj['access_token']
    return access_token


def get_edu_comments(access_token):
    url = "https://api.cnblogs.com/api/users"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': "Bearer "+access_token
    }
    response = requests.get(url=url, headers=headers)
    content = response.content.decode('utf8')
    print(content)


if __name__ == '__main__':
    #access_token = fetch_access_token()
    #get_edu_comments(access_token)
    app.run(debug=True)