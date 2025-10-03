import mysql.connector
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


class database_class():
    def __new__(db_a):
        if not hasattr(db_a, 'instance'):
            db_a.instance = super(database_class, db_a).__new__(db_a)
        return db_a.instance
    
    def open_connection(self):
        self.connector = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "MYSQL1234.com"
        )
        self.connector.database = "cereal_database"
    
    def get(self, criteria, value):

        # Instantiate connector.
        # Set database.

        # Open a cursor.
        cursor = self.connector.cursor(dictionary=True)
        if(criteria == 'None'):
            cursor.execute("SELECT * FROM cerealdatabase.cereal;")
            if cursor.with_rows == True:
                result = ( cursor.fetchall(), cursor.fetchwarnings() )
            else:
                result = cursor.fetchwarnings()
        elif value > 0:
            cursor.execute(F"SELECT * FROM cerealdatabase.cereal WHERE {criteria} = {value};")
            if cursor.with_rows == True:
                result = ( cursor.fetchall(), cursor.fetchwarnings() )
            else:
                result = cursor.fetchwarnings()
        else:
            result = "No criteria given"
        self.connector.commit()

        # Close cursor
        cursor.close()

        # Do something with result.
        return result

    def put(self, name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating):
        cursor = self.connector.cursor(dictionary=True)
        if(name.find(",") > -1):
            name_escape = name.replace(",", "/,")
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name_escape}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')"
            #print(command)
            cursor.execute(command)
        if(name.find("'") > -1):
            name_escape = name.replace("'", "\"")
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name_escape}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')"
            #print(command)
            cursor.execute(command)
        else:
            command = f"INSERT INTO cerealdatabase.cereal VALUES ('{name}', '{mfr}', '{type}', {calories}, {protein}, {fat}, {sodium}, '{fiber}', {carbo}, {sugars}, {potass}, {vitamins}, {shelf}, {weight}, {cups}, '{rating}')"
            #print(command)
            cursor.execute(command)
        #cursor.execute("INSERT INTO cerealdatabase.cereal VALUES ('{name}', 'N', 'C', 70, 4.0, 1.0, 130, '10', 5, 6, 280, 25, 3, '1', '0.33', '68.402.973')")
        if cursor.with_rows == True:
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
        self.connector.commit()

        # Close cursor
        cursor.close()

        # Do something with result.
        print(result)

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
            result = ( cursor.fetchall(), cursor.fetchwarnings() ) #
        else:
            result = cursor.fetchwarnings()
        self.connector.commit()
        cursor.close()
        return result




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
    type = "None"
    database = database_class()
    def get(self):
        self.database.open_connection()
        criteria = request.args.get("criteria")
        if criteria == None:
            result = self.database.get('None', 0)
            return jsonify({'message': result})
        else:
            values = request.args.get("values",-1,  type=int)
            result = self.database.get(criteria, values)
            return jsonify({'message': result})
        #return jsonify({'message': self.database.find(id)})
    
class Create(Resource):
    database = database_class()
    def post(self):
        self.database.open_connection()
        new_book = request.json
        print(new_book)
        result = self.database.find(1)
        return jsonify({'message': result})
    
class Delete(Resource):
    database = database_class()
    def delete(self, id):
        self.database.open_connection()
        result = self.database.find(id)
        if len(result[0]) > 0:
            result = self.database.remove(id)
            return jsonify({'result': result})
        else:
            return jsonify({'message': 'The ID doesn\'t exist'})

    

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

