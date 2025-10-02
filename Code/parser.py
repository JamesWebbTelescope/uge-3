import csv
import mysql.connector

class database_class:
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
        print(result)

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
        #print(result)


database = database_class()

database.open_connection()

with open('data/Cereal.csv', mode='r') as file:
    csvFile = csv.reader(file, delimiter=';')
    i = 0
    for lines in csvFile:
        i = i + 1
        cereal_data = []
        if not i > 2:
            continue
        cereal_data.append(lines)
        #print(cereal_data[0])    
        database.put(cereal_data[0][0], cereal_data[0][1], cereal_data[0][2], cereal_data[0][3], cereal_data[0][4], cereal_data[0][5], cereal_data[0][6], cereal_data[0][7], cereal_data[0][8], cereal_data[0][9], cereal_data[0][10], cereal_data[0][11], cereal_data[0][12], cereal_data[0][13], cereal_data[0][14], cereal_data[0][15])
