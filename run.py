from flask import Flask, request, redirect, render_template
import twilio.twiml

app = Flask(__name__)
wd = []
i = 0

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
    i = i+1
    if i >= len(wd):
        i = 0
    if len(wd) == 0:
        curr = "empty"
    else:
        curr = wd[i]
    return render_template('index.html',word=curr);
if __name__ == "__main__":
    app.run(debug=True)
