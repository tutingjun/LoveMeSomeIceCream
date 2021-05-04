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


    def connect(self):
        '''
        Establishes a connection to the database with the following credentials:
            user - username, which is also the name of the database
            password - the password for this database on perlman

        Returns: a database connection.

        Note: exits if a connection cannot be established.
        '''
        try:
            connection = psycopg2.connect(database="tut", user="tut", password="farm498lamp")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
     
        
    def match_product(self, connection, keyword, match_column):
        '''
        Retrieve the image keys of all products that contain the input keyword in the specified column of that product
        
        Parameters: 
            connection - the connection to the database
            keyword - string of user input
            match_column - the name of the column in which keyword should be searched, a string
        
        Returns:
            a list of image keys of all products whose match_column contains keyword. Empty list if there is no match.
        '''
        if (match_column == "ingredients"):
            keyword = keyword.upper()
        try:
            cursor = connection.cursor();
            if (match_column != "name"):
                query = "SELECT image_key FROM products WHERE " + str(match_column) + " LIKE '%" + str(keyword) + "%'"
                cursor.execute(query)
                return list(sum(cursor.fetchall(), ()))
            elif (match_column == "name"):
                return self.match_name(connection, keyword)
            else:
                print("Invalid match_column")
                return []
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return []
    
    
    def match_name(self, connection, keyword):
        '''
        Retrieve the image keys of all products that contain the input keyword in the name or subhead of that product

        Parameters:
            connection - the connection to the database
            keyword - string of user input

        Returns:
            a list of image keys of all products whose product name or subhead contains keyword. Empty list if there is no match.
        '''
        try:
            cursor = connection.cursor();
            query  = "SELECT image_key FROM products WHERE product_name "+ " LIKE '%"+str(keyword).capitalize() +"%'" + "OR subhead " + "LIKE '%"+str(keyword).capitalize() + "%'"
            cursor.execute(query)
            out = list(sum(cursor.fetchall(), ()))
            return out
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return []
   
   
    def advance_match(self, connection, brand, product_name, upper_rating, lower_rating, ingredients, review_text):
        '''
        Call the two helper function advance_products_match and advance_reviews_match and merge the two lists into one without dulipcate image_key
        
        Parameters: 
            connection - the connection to the database
            brand - user input brand name string
            product_name - user input product name string
            upper_rating - upper bound on the user's input range of rating, integer
            lower_rating - lower bound on the user's input range of rating, integer
            ingredients - user input ingredient names string
            review_text - user input review segment string 
                
        Returns:
            a list of image keys of all products that match the input condition. Empty list if there is no match.
        '''
        products_match = self.advance_products_match(connection, brand, product_name, upper_rating, lower_rating, ingredients)
        reviews_match = self.advance_reviews_match(connection, review_text)

        advance_match = list(set(products_match).intersection(reviews_match))
        return advance_match


    def advance_products_match(self, connection, brand, product_name, upper_rating, lower_rating, ingredients):
        '''
        Retrieve the image keys of all products that match the input conditions specified by the parameters(excluding the condition on reviews)
        
        Parameters: 
            connection - the connection to the database
            brand - user input brand name string
            product_name - user input product name string
            upper_rating - upper bound on the user's input range of rating, integer
            lower_rating - lower bound on the user's input range of rating, integer
            ingredients - user input ingredient names string
        
        Returns:
            a list of image keys of all products that match the input condition. Empty list if there is no match.            
        '''
        try:
            cursor = connection.cursor();

            query_products  = "SELECT image_key FROM products WHERE brand " + " LIKE '%" + str(brand) + "%' AND product_name " + "LIKE '%" + str(product_name).capitalize()+ "%' OR subhead " + "LIKE '%"+str(product_name).capitalize() + "%' AND rating BETWEEN " + str(upper_rating) + " AND " + str(lower_rating) + " AND ingredients " + "LIKE '%" + str(ingredients).upper() + "%'"

            cursor.execute(query_products)
            return list(sum(cursor.fetchall(), ()))
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return []


    def advance_reviews_match(self, connection, review_text):
        '''
        Retrieve the image keys of all products whose review contains review_text

        Parameters:
            connection - the connection to the database
            brand - user input brand name string
            review_text - user input review segment string 
                
        Returns: 
            a list of image keys of all products whose review contains review_text. Empty list if there is no match.
        '''
        try:
            cursor = connection.cursor();
            query_reviews = "SELECT image_key FROM reviews WHERE review_text " + "LIKE '%" + str(review_text) + "%'"
            cursor.execute(query_reviews)
            return list(sum(cursor.fetchall(), ()))
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return []


    def rank_product(self, connection, product_list, rank_column):
        '''
        Rank the input products with respect to the input column

        Parameters:
            connection - the connection to the database.
            prodcut_list - list of all product image_key given by the search page
            rank_column - name of the column used to rank the product_list
        
        Returns:
            a list of ranked products image_key with respect to the input column
        '''
        pass


    def getProductSummary(self, connection, image_key):
        '''
        Retrieve the product's name, brand name, image,
        and rating as a dictionary, for display on the
        list of results page
        
        Parameters:
            connection - the connection to the database
            image_key - the image key (got from the user's click) that serves as a unique ID for the product, a string

        Returns:
            a dictionary (column name : value pairs) for the product with the specified image key. Column names contain the product's name, brand name, image, and rating
        '''
        pass
    
    
    def getProductDetail(self, connection, image_key):
        '''
        Call the two helper function getProductInfo and getProductReviewInfo and merge the two dictionaries returned into one

        Parameters: 
            connection - the connection to the database
            image_key - the image key (got from the user's click) that serves as the unique ID for the product, a string
            
        Returns: 
            a dictionary (column name : value) that contains all the info we need to make the product detail html page
        '''
        pass


    def getProductInfo(self, connection, image_key):
        '''
        Retrieve the product's name, image, brand, subhead, description, ingredients for display on the product section of the product detail page 
        
        Parameters: 
            connection - the connection to the database
            image_key - the image key (got from the user's click) that serves as the unique ID for the product, a string
            
        Returns: 
            a dictionary (column name : value) that contains all the info about the product for the product section on the product detail page
        '''
        pass


    def getProductReviewInfo(self, connection, image_key):
        '''
        Retrieve the star, text and author infomation from the product's reviews for display on the review section of the product detail page

        Parameters:
            connection - the connection to the database
            image_key - the image key (got from the user's click) that serves as the unique ID for the product, a string
        
        Returns: 
            a dictionary (column name : value) that contains all the review related info we need to make the review section of the product detail html page
        '''
        pass
    

    
    
    



if __name__ == '__main__': 
    # your code to test your function implementations goes here.
    test = DataSource()
    connection = test.connect()

    #match
    products_ingredient_match = test.match_product(connection, "chocolate", "ingredients")
    products_name_match = test.match_product(connection, "Salted", "name")
    products_advance_match = test.advance_match(connection, "bj", "Salted Caramel Core", 3, 4, "cream", "good")
    
    #print
    print("products_ingredient_match\n")
    for item in products_ingredient_match:
        print(item)
    
    print("products_name_match\n")
    for item in products_name_match:
        print(item)
    
    print("products_advance_match\n")
    for item in products_advance_match:
        print(item)
