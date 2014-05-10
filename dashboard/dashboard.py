
import logging

from flask import Flask

LOG = logging.getLogger(__name__)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", filename='/tmp/dashboard.log')

app = Flask(__name__)
app.config.from_object(__name__)

import views


def main():

    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()