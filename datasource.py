import psycopg2

class DataSource:
    '''
    DataSource executes all of the queries on the database.
    It also formats the data to send back to the frontend, typically in a list
    or some other collection or object.
    '''

    def __init__(self):
        '''
        Note: if you choose to implement the constructor, this does *not* count as one of your implemented methods.
        '''

    def keyword_search(connection):
        try:
            cursor = connection.cursor()
            query = "SELECT product_name FROM products"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
    
def connect():
    try:
        connection = psycopg2.connect(database="tut", user="tut", password="farm498lamp")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

if __name__ == '__main__':
    # your code to test your function implementations goes here.
    test = DataSource()
    connection = connect()
    results = test.keyword_search(connection)
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)
    connection.close()
