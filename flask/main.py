from flask import Flask, redirect, request, jsonify
import requests
import pymysql

# client_id = ""
# client_secret = ""

db = pymysql.connect(host="15.165.161.62", user='seulbee',
                     password='dltmfql', db='sb_flask', charset='utf-8')
cursor = db.cursor()
sql = "select * from accounts"

cursor.execute(sql)

cursor.fetchall()

db.commit()
db.close()


app = Flask(__name__)


@app.route('/naver-login')
def naverLogin():
    global client_id
    redirect_uri = "http://localhost:5001/naver-login-callback"
    url = f"https://nid.naver.com/oauth2.0/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    return redirect(url)


@app.route('/naver-login-callback')
def naverLoginCallback():
    global client_id, client_secret
    params = request.args.to_dict()
    code = params.get("code")
    redirect_uri = "http://localhost:5001/naver-login-callback"

    token_request = requests.get(
        f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={code}")
    token_json = token_request.json()
    print(token_json)
    access_token = token_json.get("access_token")

    profile_request = requests.get(
        "https://openapi.naver.com/v1/nid/me", headers={"Authorization": f"Bearer {access_token}"},)
    profile_data = profile_request.json()

    print(profile_data)
    return "Done"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
