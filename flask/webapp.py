import flask
from flask import render_template, request
from datasource import DataSource
import sys

app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# store the search keywords and field as global vars
# this is to retain the same list of search result when the user ranks the products
search_option = "" # column to search in
search_text = "" # keyword for search

@app.route('/')
def homePage():
    '''
    Default direct to the index
    '''
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def searchResult():
    '''
    Direct the page to the list of products,
    based on the form results, search_option and
    search_text, from index.html.
    '''
    # global keyword used here to declare that we are changing the global vars
    global search_option
    global search_text
    search_option = request.form["search_option"]
    search_text = request.form["search_text"]
    
    backend = DataSource()
    products_match = backend.match_product(search_text, search_option)
    result = []
    for img_key in products_match:
        result.append(backend.getProductSummary(img_key))
    return render_template('product_list.html', results=result)

@app.route('/rank', methods=['POST'])
def rankSearchResult():
    '''
    Rank the search results with respect to the user's choice in the drop down bar
    '''
    rank_option = request.form["rank"]

    backend = DataSource()
    products_match = backend.match_product(search_text, search_option)
    products_match = backend.rank_product(products_match, rank_option)
    print(products_match)
    result = []
    for img_key in products_match:
        result.append(backend.getProductSummary(img_key))
    return render_template('product_list.html', results=result)

@app.route('/results/<name>')
def getProduct(name):
    '''
    This method retrieve all product info and review info of the product chosen by the user. (the product chosen is based on the click action the user performed on the previous product_list.html page)
    '''
    backend = DataSource()
    product_info = backend.getProductInfo(name)
    review_info = backend.getProductReviewInfo(name)
    return render_template('sample_result_page.html', product=product_info, reviews=review_info)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
