from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex_pattern = request.form["regex"]
    matches = re.findall(regex_pattern, test_string)
    email = request.form["email"]
    email_valid = re.match(r"[^@]+@[^@]+\.[^@]+",email) is not None
    return render_template("results.html", test_string=test_string, matches=matches, email=email, email_valid=email_valid)

@app.route("/validate-email")
def validate_email_page():
    return render_template("validate_email.html")

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    valid = re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
    return render_template("validate_email_result.html", valid=valid)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
