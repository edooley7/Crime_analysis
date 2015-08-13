from flask import Flask
app = flask.Flask(__name__)

@app.route("/")
def viz_page():
    with open("error.html", 'r') as viz_file:
        return viz_file.read()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
