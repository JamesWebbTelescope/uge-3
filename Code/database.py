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

    def find(self):
        cursor = self.connector.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cerealdatabase.cereal WHERE ï»¿name='100% Bran'")
        result = (cursor.fetchall(), cursor.fetchwarnings())

        print(result)

database = database_class()

database.open_connection()

database.get()




