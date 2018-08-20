from flask import Flask

app = Flask("flask-tutorial")

@app.route("/")
def hello_world():
	return "Hello World! <strong>I am learning Flask</strong>", 200

app.run(debug=True, use_reloader=True)

# @app.route("/<name>")
# def index(name):
#     # if name.lower() == "educat":
#     #     return "Olá {}".format(name), 200
#     # else:
#     #     return "Not Found", 404
#     return "Olá {}".format(name)

# app.run(debug=True, use_reloader=True)