from flask import Flask        # import Flask library
app = Flask(__name__)          # create the app

@app.route('/')                # when someone visits "/"
def home():
    return "Hello DevOps!"     # return this text

if __name__ == '__main__':
    app.run()                  # start the server