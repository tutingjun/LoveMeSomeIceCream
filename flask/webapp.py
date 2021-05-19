import flask
from flask import render_template, request
from datasource import DataSource
import json
import sys

app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

search_option = ""
search_text = ""

@app.route('/')
def homePage():
    '''
    Simplest example: print something in the browser
    '''
    return render_template('index.html')

@app.route('/index')
def home():
    '''
    Simplest example: print something in the browser
    '''
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def searchResult():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    search_option = request.form["search_option"]
    search_text = request.form["search_text"]
    
    backend = DataSource()
    products_match = backend.match_product(search_text, search_option)
    result = []
    for img_key in products_match:
        result.append(backend.getProductSummary(img_key))
    return render_template('product_list.html', results=result)

@app.route('/results/rank', methods=['POST'])
def rankSearchResult():
    rank_option = request.form["rank"]

    backend = DataSource()
    products_match = backend.match_product(search_text, search_option)
    products_match = backend.rank_product(products_match, rank_option)
    print(products_match)
    result = []
    for img_key in products_match:
        result.append(backend.getProductSummary(img_key))
    return render_template('product_list.html', results=result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
