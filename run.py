from flask import Flask, request, redirect, render_template
import twilio.twiml

app = Flask(__name__)
wd = "Empty"

@app.route("/words", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    wd = body

    resp = twilio.twiml.Response()
    resp.message(body)
    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def ind():
    
    return render_template('index.html',word=wd);
if __name__ == "__main__":
    app.run(debug=True)
