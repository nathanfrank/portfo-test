import os
from flask import send_from_directory
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    if f"{page_name}.html" == 'home.html':
        return render_template('index.html')
    else:
        return render_template(f"{page_name}.html")
    
# def write_to_file(data):
#     with open("database.txt", mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f"\nEmail: {email}, Subject: {subject}, Message: {message}")


def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        return csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou')
        except:
            return "Did not save to database, please try again."
    else:
        return 'Something went wrong!'
    

##Some updates to the file
    ##Testing branching & PR


