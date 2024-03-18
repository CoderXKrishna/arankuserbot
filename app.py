from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Joneswarrior. Bitch bakchodi nhi samajh me aaya kya. Sabki maa ki chut.'


if __name__ == "__main__":
    app.run()
