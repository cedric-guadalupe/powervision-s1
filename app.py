from flask import Flask, jsonify

app = Flask(__name__)

# @app.route('/', methods=['POST', "GET"])
# @app.route('/app/api/phoneValidationLogin', methods=['POST'])
@app.route('/', defaults={'path': ''}, methods=['POST', "GET"])
@app.route('/<path:path>', methods=['POST', "GET"])
def get_data(path):
    response = {
        "code": 0,
        "data": {
            "expire": "2055-12-31T23:59:59Z",
            "token": "abcdef123456",
            "user": {
                "addtime": "2023-05-01T12:34:56Z",
                "birthday": "1990-01-01",
                "city": "Paris",
                "country": "France",
                "headImage": "https://example.com/images/user.jpg",
                "id": 12345,
                "ipCity": "Paris",
                "nickname": "JohnDoe",
                "sex": "Male",
                "signature": "Carpe Diem",
                "storeToken": "store_token_example",
                "storeUid": "store_uid_example",
                "userId": "user12345",
                "useremail": "john.doe@example.com",
                "username": "John Doe",
                "userphone": "+33123456789"
            }
        },
        "msg": "Success"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
