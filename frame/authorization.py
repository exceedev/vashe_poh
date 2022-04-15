from crypt import methods
from flask import Flask, render_template, redirect, request, jsonify


app = Flask(__name__)

client = app.test_client()


request_json = {
    'objects': [
        {
            'id': 0,
            'title': 'text in title 0',
            'body': 'text in body 0'
        },
        {
            'id': 1,
            'title': 'text in title 1',
            'body': 'text in body 1'
        },
        {
            'id': 2,
            'title': 'text in title 2',
            'body': 'text in body 2'
        }
    ],
    'count': 3,
    'info': 'text info. Description.'
}


@app.route("/")
def index():
    return "<h1>Hello matherFucka!</h1>"


@app.route("/<path:anytext>")
def dublecator(anytext):
    return f"<h1>Ты вводишь какую то дичь. Где ты блеать видел такой сука путь? {anytext}. Я ТЕБЯ СПРАШИВАЮ! ГДЕ??!?!?!?</h1>"


@app.route("/auth", methods=['GET'])
def auth_get():
    return jsonify(request_json)


@app.route("/auth", methods=['POST'])
def auth_post():
    req = request.json
    request_json['objects'].append(req)

    print(req)
    return jsonify(request_json)


@app.route("/info")
def info():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)
