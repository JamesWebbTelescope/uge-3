# SQL

MySQL virker mere tilgængeligt end PostgreSQL, pga. MySQL workbench.
https://www.mysql.com/
### Referencer
https://www.w3schools.com/mysql/default.asp

---
## Værktøjer

MySQL workbench
- Kort introduktion, bare så man kan få visuel adgang til sin database. Kan bruges til debugging. https://www.mysql.com/products/workbench/

MySQL Connector/Python
- Driver til kommunikation med MySQL fra Python. https://dev.mysql.com/doc/connector-python/en/

---
## Kode eksempler

1. MySQL Connector/Python minimalt eksempel.

```python
import mysql.connector

# Instantiate connector.
connector = mysql.connector.connect(
	host = "host",
	user = "user",
	password = "password"
)

# Set database.
connector.database = "db_name"
        
# Open a cursor.
cursor = self.connection.cursor(dictionary=True)
cursor.execute("query_string")
if cursor.with_rows == True:
	result = ( cursor.fetchall(), cursor.fetchwarnings() )
else:
	result = cursor.fetchwarnings()
self.connection.commit()

# Close cursor
cursor.close()

# Do something with result.
print(result)
``` 
^mysql-connector-python




