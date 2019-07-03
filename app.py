import hmac

from flask import Flask, request, jsonify
from git import Repo

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/mobile")
def mobile():
    return app.send_static_file("mobile.html")


@app.route("/github", methods=["POST"])
def github():
    signature = request.headers.get('X-Hub-Signature')
    sha, signature = signature.split('=')
    secret = str.encode("web")
    hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
    if hmac.compare_digest(hashhex, signature):
        repo = Repo("/usr/share/nginx/web")
        master = repo.heads.master
        curBranch = repo.head.reference
        if curBranch != master:
            repo.heads.master.checkout()
        repo.git.checkout('.')
        commit = request.json['after'][0:6]
        print('repository updated with commit {}'.format(commit))
        return jsonify({'msg': "success"}), 200
    else:
        return jsonify({'msg': "error"}), 200


if __name__ == "__main__":
    app.run(debug=False)
