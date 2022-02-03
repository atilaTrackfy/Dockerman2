from flask import Flask
app = Flask(__name__)
# creating route
@app.route("/")
def home():
    return "This is Home Page"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
