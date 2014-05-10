
import os

from flask import request, render_template, send_from_directory

from dashboard import app


@app.route('/dashboard/<path:filename>')
def assets(filename):

    return send_from_directory(os.path.dirname(__file__), filename)


@app.route('/dashboard/<name>')
def dashboard(name):

    return render_template(name)


@app.route('/dashboard/severity')
def severity_widget():

    label = request.args.get('label', 'Alert Severity')

    return render_template('widgets/severity.html', label=label, query=request.query_string)


@app.route('/dashboard/status')
def status_widget():

    label = request.args.get('label', None)

    return render_template('widgets/status.html', label=label, query=request.query_string)


@app.route('/dashboard/details')
def details_widget():

    label = request.args.get('label', 'Alert Details')

    return render_template('widgets/details.html', label=label, query=request.query_string)
