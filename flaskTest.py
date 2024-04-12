import json
import requests
from flask import Flask, render_template, request, jsonify
from access_token import MpesaAccessToken, LipanaMpesaPpassword

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', message="Mpesa Integration test")

@app.route('/access')
def access():
    return render_template('access.html', message=MpesaAccessToken.validated_mpesa_access_token)

@app.route('/stkpush', methods=['POST'])
def stkpush():
    name = request.form['name']
    phn = int(request.form['phone'])
    countryCode = '254'
    phone = countryCode + str(phn)

    print(f'Name: {name}, Phone number: {phone}')
    
    data = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": int(phone),
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": int(phone),
        "CallBackURL": "https://project.my-market.co.ke/Callback_main/callbackurl_prjct.php",
        "AccountReference": "KENNETH",
        "TransactionDesc": "Testing stk push"
    }
    response = lipa_na_mpesa_online(data)
    return render_template('stkpush.html', message = response)

def lipa_na_mpesa_online(data):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    res = requests.post(api_url, json=data, headers=headers).json()
    print(json.dumps(res, indent= 4))
    try:
        return res["ResponseDescription"]
    except:
        return res["errorMessage"]

if __name__ == '__main__':
    app.run(debug=True)
