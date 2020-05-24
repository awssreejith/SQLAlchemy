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
              

weapons.db ==> This is the database file for SQLite.The actual data will be persisted in this

AppMain.py ==> Main entry point of this application

SQLAlchemyAdapter.py ==> This is the adapter class used to link the actual SQLAlchemy ORM classes and user model class.The table objects are composed within this class and the client use this adapter for communicating with the SQLAlchemy engine.

InputProvider.py ==> This class is responsible to provide the user with the Menu option and fetch the input. This is the view class

SQLQueryHelper.py ==> This is a bridge between the view class(InputProvider.py) and the Model class (SQLAlchemyAdapter.py)

Usage:
======

During initialization two tables will be created. They are 'Weapons' and 'Types' table. The 'Types' table will be populated with all the
supported types(ROCKET,MORTAR,RIFLE & TANK) and weapons tables will be populated without any element. The user can use the Menu option to populate the weapons as well as perform other operations mentioned in the menu

