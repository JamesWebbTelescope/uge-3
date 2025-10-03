<h1>Cereal REST API</h1>
A simple REST API for a list of cereal products.

<h1>Description</h1>
Ths project is a simple locally based API for cereal products. It relies on a simple MySQL Database to manage a list of cereal products and nutritional values.
It allows for four different types of operations: GET, POST, PUT and delete

<h1>Getting started</h1>
<h2>Dependencies</h2>

Flask

Flask-restful

csv

mysql

Windows 11 Pro.

<h2>Installing</h2>

Open Windows Powershell and run the following command ```pip install flask-restful```

<h1>How/where to download your program</h1>
The code for the program can be found in the \Code-folder.
<h1>Any modifications needed to be made to files/folders</h1>
None
<h1>Executing program</h1>
Open the parser.py - file in VS Code. Run it with the Python debugger and wait for it to finish.
Once that is done, open the database.py file and run it.
<h1>How to run the program</h1>

When you run it, the database.py - file will give you a local web address in the VS Code terminal. Copy it into your preferred browser and go to it.
When you get there, you will see the message "Hello world"
Once there, you can add /get/ to the web address to test the GET request handling.
In the Postman app, you can send POST and DELETE commands to test their handling.

<h1>Step-by-step bullets</h1>

<h1>code blocks for commands</h1>
Sending GET commands ´´´/get´´´
Sending GET commands with criteria and values ´´´/get?criteria=string&values=value´´´

<h1>Help</h1>
To send POST and DELETE requests to the webpage, you need the Postman app for sending them: https://www.postman.com/downloads/

<h1>Any advise for common problems or issues.</h1>
I am using ID as primary keys for the database. So right now, the parser.py - file doesn't actually work, since it tries to add data points with ID's that already exist.

<h1>command to run if program contains helper info</h1>

<h1>Authors</h1>
Contributors names and contact info

Vitor From
Viktor.From@specialisterne.dk

<h1>Version History</h1>
0.2
Various bug fixes and optimizations
See commit change or See release history
0.1
Initial Release
License
This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

Acknowledgments
Inspiration, code snippets, etc. * awesome-readme * PurpleBooth * dbader * zenorocha * fvcproductions
