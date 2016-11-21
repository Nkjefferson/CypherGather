from flask import Flask, request, redirect, render_template
from collections import deque
import twilio.twiml
import random

app = Flask(__name__)
wd = deque()
dic = []
used = []
with open('static/list.txt', 'r') as f:
    dic = [line.strip() for line in f]
i = 0
random.seed()

@app.route("/words", methods=['GET', 'POST'])
def hello_monkey():
    global wd
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    resp = twilio.twiml.Response()
    if not(" " in body) and body not in blacklist and body not in used:
        wd.append(body.title())
        resp.message(body)

    if body in used:
        resp.message(body,"has already been submitted")
    elif body in blacklist:
        resp.message(body,"is a word the preformers would rather not use")
    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def ind():
    global wd
    global i
    global dic
    global used
    i = i+1
    if i >= len(wd):
        i = 0
    if len(wd) == 0:
        curr = dic[random.randint(0,len(dic))].title()
    else:
        curr = wd.popleft()
    used.append(curr)
    return render_template('index.html',word=curr);
if __name__ == "__main__":
    app.run(debug=True)
