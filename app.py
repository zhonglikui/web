from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("home.html")


@app.route("/github", methods=["POST", "GET"])
def github():
    return app.send_static_file("home.html")
    # signature = request.headers.get('X-Hub-Signature')
    # sha, signature = signature.split('=')
    # secret = str.encode(app.config.get('GITHUB_SECRET'))
    # hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
    # if hmac.compare_digest(hashhex, signature):
    #     repo = Repo(app.config.get('REPO_PATH'))
    #     origin = repo.remotes.origin
    #     origin.pull('--rebase')
    #     commit = request.json['after'][0:6]
    #     print('Repository updated with commit {}'.format(commit))
    # return jsonify({}), 200


if __name__ == "__main__":
    app.config['GITHUB_SECRET'] = "web"
    app.config['REPO_PATH'] = "/usr/share/nginx/web"
    app.run(debug=False)
