# SQL

MySQL virker mere tilgængeligt end PostgreSQL, pga. MySQL workbench.
https://www.mysql.com/
### Referencer
https://www.w3schools.com/mysql/default.asp

---
## Værktøjer

MySQL workbench
- Kort introduktion, bare så man kan få visuel adgang til sin database. Kan bruges til debugging. https://www.mysql.com/products/workbench/

MySQL Connector/NET
- Driver til kommunikation med MySQL fra .NET. https://dev.mysql.com/doc/connectors/en/connector-net.html

---
```C#
MySql.Data.MySqlClient.MySqlConnection conn;
string myConnectionString = "servel=server;uid=user;pwd=password;database=database";
try
{
	conn = MySql.Data.MySqlClient.MySqlConnection();
	conn.ConnectionString = myConnectionString;
	conn.Open();
	MySqlCommand cmd = new MySqlCommand();
	cmd.CommandText = "SELECT foo FROM bar";
	cmd.Connection = conn;
	MySqlDataReader reader = cmd.ExecuteReader();
	while (reader.Read())
	{
		Console.WriteLn(reader);
	}
	
}
catch (MySql.Data.MySqlClient.MySqlException ex)
{
	MessageBox.Shoq(ex.Message);
}
```