import flask
from flask import render_template, request
from datasource import *
import json
import sys

app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homePage():
    '''
    Simplest example: print something in the browser
    '''
    return render_template('index.html')

@app.route('/results', methods=['POST', 'GET'])
def searchResult():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    if request.method == 'POST':
        result = request.form

        # Here is where you would call one or more database methods with the form data.
    return render_template('product_list.html', results=result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)