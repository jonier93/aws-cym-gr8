from flask import Flask

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend", static_url_path="") 

from routes.route import *

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "8080"
    app.run(host, port, debug=True)