from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello matherFucka!</h1>"


@app.route("/<path:anytext>")
def dublecator(anytext):
    return f"<h1>Ты вводишь какую то дичь. Где ты блеать видел такой сука путь? {anytext}. Я ТЕБЯ СПРАШИВАЮ! ГДЕ??!?!?!?</h1>"


@app.route("/auth", methods=['POST', ])
def auth():
    return "\n".join(request.__dict__) + f"\n\n{request.__dict__}"


@app.route("/info")
def info():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)
