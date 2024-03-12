web Application : http://51.20.10.115:5000/

Regex Web Application Documentation:
Overview
This web application allows users to input a test string, a regular expression pattern, and an email address. 
It then performs regex matching on the test string using the provided pattern and validates the entered email address using a regex pattern.
Code Explanation
app.py
index route ("/"): Renders the index.html template, which contains a form for entering the test string, regex pattern, and email address.
results route ("/results"): Handles the form submission, performs regex matching on the test string, validates the email address, and renders the results.html template.
validate_email_page route ("/validate-email"): Renders the validate_email.html template, which contains a form for entering an email address to validate.
validate_email route ("/validate-email", methods=["POST"]): Handles the email validation form submission and renders the validate_email_result.html template.
Static files: Static files such as CSS stylesheets are served from the "static" directory.
HTML Templates
index.html: Form for entering input data.
results.html: Displays matched strings, email validation result, and input text.
validate_email.html: Form for entering an email address to validate.
validate_email_result.html: Displays the result of email validation.
CSS Styles
styles.css: Contains CSS styles for styling HTML elements.
Conclusion
This document provides a comprehensive guide for creating a web application for regex operations using Flask. 
Users can input a test string, a regex pattern, and an email address to perform regex matching and email validation.
