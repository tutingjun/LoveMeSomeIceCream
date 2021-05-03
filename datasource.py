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
        try:
            connection = psycopg2.connect(database="tut", user="tut", password="farm498lamp")
        except Exception as e:
            print("Connection error: ", e)
            exit()

    def keyword_search(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT product_name FROM products"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
    
    def close_connection(self):
        self.connection.close()

if __name__ == '__main__': 
    # your code to test your function implementations goes here.
    test = DataSource()
    results = test.keyword_search()
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)
    test.close_connection()
