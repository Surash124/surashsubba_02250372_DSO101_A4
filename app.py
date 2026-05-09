from logging.config import listen

from flask import Flask        # import Flask library
app = Flask(__name__)          # create the app

@app.route('/')                # when someone visits "/"
def home():
    return "Hello DevOps!"     # return this text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # start the server
                                        #listen to ALL incoming connections
                                        # on port 5000