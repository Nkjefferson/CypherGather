from flask import Flask, request, redirect, render_template
import twilio.twiml
import random

app = Flask(__name__)
wd = []
dic = []
with open('static/list.txt', 'r') as f:
    dic = [line.strip() for line in f]
i = 0
random.seed()

@app.route("/words", methods=['GET', 'POST'])
def hello_monkey():
    global wd
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    wd.append(body)

    resp = twilio.twiml.Response()
    resp.message(body)
    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def ind():
    global wd
    global i
    global dic
    i = i+1
    if i >= len(wd):
        i = 0
    if len(wd) == 0:
        curr = dic[random.randint(0,len(dic))].title()
    else:
        curr = wd.pop()
    return render_template('index.html',word=curr);
if __name__ == "__main__":
    app.run(debug=True)
