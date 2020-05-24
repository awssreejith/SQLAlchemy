This is a sample menu driven program created to understand the usage of SQLAlchemy package
==========================================================================================
This program emphasize on Insert, Delete, Update DMLs and Create Table DDL.

The user interface is a shell menu using which the user can opt one among the following

                0) Display all weapons

                1) Display specific weapon according to ID

                2) Display All supported weapons type

                3) Insert a new weapon

                4) Delete a weapon

                5) Update a weapon

                6) Exit


The Database used is SQLite and uses SQLAlchemy ORM package.The below excerpts articulates the files included

sql.conf ==> This is the configuration file for database. The database types (Oracle,MSSQL,MySQL,PostGres and SQLite)can be defined
              here. Apart from that user can define the DB server, port, user name and password within this file. Currently the password 
              is stored in plain text format and SQLite is the only DB supported
