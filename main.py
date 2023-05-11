from flask import Flask, Response, request
from flask_cors import CORS
import requests


MSERVER_URL = 'http://192.168.100.142:999'
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.get("/status")
def mserver_get_status():
    res = requests.get(MSERVER_URL + '/status')

    return Response(
        res.content,
        status=res.status_code,
        headers={
            'Content-Type': 'text/xml'
        }
    )


@app.post("/xml")
def mserver_post_xml():
    res = requests.post(MSERVER_URL + '/xml', data=request.data, headers={
        'Stw-Application': request.headers.get('Stw-Application'),
        'Stw-Authorization': request.headers.get('Stw-Authorization'),
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',

    })

    return Response(
        res.content,
        status=res.status_code,
        headers={
            'Content-Type': 'text/xml'
        }
    )


if __name__ == '__main__':
    app.run(debug=True, port=8888)