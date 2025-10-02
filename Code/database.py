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
    
    def get(self):

        # Instantiate connector.
        # Set database.

        # Open a cursor.
        cursor = self.connector.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cerealdatabase.cereal;")
        if cursor.with_rows == True:
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
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
        cursor = self.connector.cursor(dictionary=True)
        command = f"SELECT * FROM cerealdatabase.cereal WHERE ID = {ID}"
        cursor.execute(command)
        if cursor.with_rows == True:
            result = ( cursor.fetchall(), cursor.fetchwarnings() )
        else:
            result = cursor.fetchwarnings()
        self.connector.commit()
        cursor.close()
        return result



# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):

    def get(self, num):

        return jsonify({'square': num**2})
    
class Read(Resource):
    type = "None"
    database = database_class()
    def get(self, id):
        self.database.open_connection()
        if id == 0:
            return jsonify({'message': self.database.get()})
        else:
            return jsonify({'message': self.database.find(id)})
    
class Create(Resource):
    database = database_class()
    def post(self):
        self.database.open_connection()
        new_book = request.json
        print(new_book)
        result = self.database.find(1)
        return jsonify({'message': result})
    

app = Flask(__name__)
# creating an API object
api = Api(app)


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Read, '/get/<int:id>')
api.add_resource(Create, '/create/')


# driver function
if __name__ == '__main__':

    app.run(debug = True)

