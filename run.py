from flask import Flask, request, redirect, render_template
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)

    resp = twilio.twiml.Response()
    resp.message(body)
    return render_template('index.html', word = body)

if __name__ == "__main__":
    app.run(debug=True)
