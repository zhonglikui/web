from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("home.html")


@app.route("/webscan_360_cn.html")
def webscan_360_cn():
    return app.send_static_file("webscan_360_cn.html")


if __name__ == "__main__":
    app.run(debug=False)
