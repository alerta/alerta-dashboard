
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

import views


def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
