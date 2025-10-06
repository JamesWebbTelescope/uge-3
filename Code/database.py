import mysql.connector
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


class database_class():
    def __new__(db_a):
        #I am using the Singleton pattern to ensure that only one instance of the database_class exists.
        #That way, I avoid having multiple objects trying to access the same database
        if not hasattr(db_a, 'instance'): #If an instance of this class already exists
            db_a.instance = super(database_class, db_a).__new__(db_a)
        return db_a.instance #Return that instance
    
    def open_connection(self):
        #This is where I connect to the database
        self.connector = mysql.connector.connect( #Set the web address, user and password for connecting to the database
            host = "localhost",
            user = "root",
            password = "MYSQL1234.com"
        )
        self.connector.database = "cerealdatabase" #choose which database I want to connect to
    
    def get(self, criteria, value):
        #This function does two things depending on the arguments.
        #If no criteria are given, it just returns everything in the database.
        #If a filter criteria is given with no value, it returns "No criteria given"
        #If a criteria is given with values, it searches the database for all data points with that criteria and returns them.
        # Open a cursor.
        cursor = self.connector.cursor(dictionary=True) #Open a cursor
        if(criteria == 'None'): #If there are no criteria.
            cursor.execute("SELECT * FROM cerealdatabase.cereal;") #Set the command to just return everything in the database.
            if cursor.with_rows == True: #If I get a response 
                result = ( cursor.fetchall(), cursor.fetchwarnings() ) #Get the full response
            else:
                result = cursor.fetchwarnings() #Otherwise, just get the warnings, so I can figure out what went wrong.
        elif value > 0: #If we have a criteria and the value we're looking for is more than 0
            cursor.execute(F"SELECT * FROM cerealdatabase.cereal WHERE {criteria} = {value};") #Get all data points where the value matches.
            if cursor.with_rows == True:
                result = ( cursor.fetchall(), cursor.fetchwarnings() )
            else:
                result = cursor.fetchwarnings()
        else:
            result = "No criteria given"
        self.connector.commit() #Close the connection

        cursor.close() #Close the cursor

        return result

    def put(self, name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating):
        #This function is for adding new items to the database
        cursor = self.connector.cursor(dictionary=True) #Get a cursor
        if(name.find(",") > -1): #If the name contains "," the database can't handle it
            name_escape = name.replace(",", "/,") #So I replace it with /, so it ignores it
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name_escape}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')" #Design the command including all custom values
            cursor.execute(command) #Send the command to the database, so it can be executed
        if(name.find("'") > -1):
            name_escape = name.replace("'", "\"") #In the same fashion, I need to check for "'" and replace it with "\""
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name_escape}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')" #Design the command including all custom values
            cursor.execute(command) #Send the command to the database, so it can be executed
        else: #If the name doesn't have any special characters
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')" #Design the command including all custom values
            cursor.execute(command) #Send the command to the database, so it can be executed
        if cursor.with_rows == True: #Get the response from the database
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
        self.connector.commit() #Close the connection

        cursor.close() # Close cursor

        # Do something with result.
        print(result) #This probably needs to be replaced.

    def find(self, ID):
        #This function searches the database for products with the given ID
        cursor = self.connector.cursor(dictionary=True) #Get a cursor for the database
        command = f"SELECT * FROM cerealdatabase.cereal WHERE ID = {ID}" #Make the command including ID as a formatted string.
        cursor.execute(command) #Send the command to the database
        if cursor.with_rows == True: #If I actually get something back
            result = ( cursor.fetchall(), cursor.fetchwarnings() ) #Get the results including warnings
        else:
            result = cursor.fetchwarnings() #Get the warnings, so I can figure out what went wrong.
        self.connector.commit() #Close the connection
        cursor.close() #End the cursor
        return result #Returns a string either with the desired product or nothing
    
    def remove(self, ID):
        #This function removes products with the given ID from the database
        cursor = self.connector.cursor(dictionary=True) #Get a cursor
        command = f"DELETE FROM cerealdatabase.cereal WHERE ID = {ID}" #Set the command including custom ID
        cursor.execute(command) #Send the command to the database so it can be executed
        if cursor.with_rows == True: #Check whether I receive anything
            result = ( cursor.fetchall(), cursor.fetchwarnings() ) #If I received something, get it
        else:
            result = cursor.fetchwarnings() #Else, just get the warnings so I can figure out what went wrong
        self.connector.commit() #Close the connection
        cursor.close() #End the cursor
        return result #Return a string showing whether I managed to delete the product from the database or not.




# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
# To make the code easier to read, I have one resource per type of request.
class Startpage(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code
        return jsonify({'data': data}), 201

    
class Read(Resource):
    database = database_class() #Get an instance of the database
    def get(self):
        #This is where I handle the GET requests for the API
        self.database.open_connection() #Open a connection to the database
        criteria = request.args.get("criteria") #Check if there is a query including the criteria that I have to filter for
        if criteria == None: #If not
            result = self.database.get('None', 0) #Just get everything on the database
            return jsonify({'message': result}) #Update the webpage with the result
        else: #If there IS a criterion:
            values = request.args.get("values",-1,  type=int) #Get the value that I should filter for
            result = self.database.get(criteria, values) #Filter through the database for the 
            return jsonify({'message': result}) #Opdater hjemmesiden med resultatet
    
class Create(Resource):
    #Get an instance of the database class
    database = database_class()
    def post(self):
        #This function is for handling the POST requests for the API
        self.database.open_connection() #Open a connection to the database
        new_book = request.json #Get something from the HTTP request
        print(new_book) #print it out
        result = self.database.find(1) #Find the database item with ID = 1
        return jsonify({'message': result}) #Update the webpage with the result
    
class Delete(Resource):
    #This function handles the DELETE requests for the API
    database = database_class() #Get an instance of the database class
    def delete(self, id):
        self.database.open_connection() #Open a connection to the database
        result = self.database.find(id) #Check whether the item with the given id actually exists
        if len(result[0]) > 0: #If it does exist
            result = self.database.remove(id) #Remove it
            return jsonify({'result': result}) #Update the webpage with the result
        else:
            return jsonify({'message': 'The ID doesn\'t exist'}) #Update the webpage, saying that the ID doesn't exist

    

app = Flask(__name__)
# creating an API object
api = Api(app)


# adding the defined resources along with their corresponding urls
api.add_resource(Startpage, '/')
api.add_resource(Read, '/get/')
api.add_resource(Create, '/create/')
api.add_resource(Delete, '/delete/<int:id>')


# driver function
if __name__ == '__main__':

    app.run(debug = True)

