from flask import Flask, request

app = Flask(__name__)

@app.route('/post_energy_info', methods=['POST'])
def receive_energy_info():
    request_data = request.get_json()
    print(request_data)
    return 200


if __name__ == '__main__':
    app.run()
