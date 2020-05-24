## The create_engine will create the main connection engine for SQL alchemy
## The engine has connection pools and 'stuffs' to connect to different databse flavours
from sqlalchemy import create_engine

## The below Metadata class holds all the information about specific tables
## We require metadata for creating tables because this holds the metadata about the table object
from sqlalchemy import MetaData

## We need built in classes to represent tables, columns, varchars (strings), integers
## defining everything seperately just for apprehension
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

#sys module for exit
import sys
import os

##We have a foreign key dependency between Weapons table and type table
from sqlalchemy import ForeignKey

## sample documentation available at
## http://docs.sqlalchemy.org/en/latest/core/engines.html

## This is a dictionary which stores the table object. Whenever client wants to perform any
## table operation, ask for the respective table object and use it

class SQLAlchemyAdapter(object):
    def __init__(self,dbname,user,passwd,dbtype):
        ## for sqlite not user id password at this moment
        connectionString = ''
        self.ORMObjectMap = dict()
        if 'sqlite' in dbtype:
            connectionString = dbtype+dbname
            ## sqlite:///somedb.db
        else:
            print('This implementation supports only SQLite at this moment. Sorry')
            ##TODO - Implement support for other DB alsocreate_engine(engine_url)
            sys.exit(-3)


        ## Here we create an Engine with the connection string
        ## Note that this will NOT connect to DB yet
        self.connection = create_engine(connectionString)

        if self.connection == None:
            print('SQLAlchemy engine creation failed. Exiting!!')
            sys.exit(-4)
        print('SQLAlchemy engine creation Successful!!')

        ##############################################
        ## For this tutorial we create a DB fresh.
        ##############################################
        DBFileName = connectionString.split('/')
        os.system(f"rm -rf ./{DBFileName[len(DBFileName)-1]}")


    def initDB(self,supported_Types):
        '''This must be called if the data base is created afresh,after creating the SQLAlchemyAdapter object. Because we need to populate
        The table first and populate all the supported types. 
        NEVER CALL THIS IF THE DB IS ALREADY CREATED

        '''
    ## First create the Types table#
    #==============================#
        TableName = "Types"
    ## Create a Metadata for this table's creation
        metadata = MetaData()
    ## create a Table object for Types with our column requirement
        types = Table(TableName, metadata,
                      Column('Type_id', String, primary_key=True),
                      Column('Type_name', String,nullable=False),
                      )

    ##Create the actual table
        try:
            metadata.create_all(self.connection)
        except Exception as exc:
            print(exc)
            print("Types table creation failed. Exiting")
            sys.exit(-5)
        print("Types table creation Successful !!")
        self.ORMObjectMap['Types'] = types

    ## create a Table object for Weapons with our column requirement
        TableName = "Weapons"
        weapon = Table(TableName, metadata,
                      Column('Weapon_id', String, primary_key=True),
                      Column('Type', String,ForeignKey("Types.Type_id"),nullable=False),
                      Column('Manufacturer', String,nullable=False),
                      Column('Country', String,nullable=False)
                      )
        try:
            metadata.create_all(self.connection)
        except Exception as exc:
            print(exc)
            print("Weapons table creation failed. Exiting")
            sys.exit(-5)
        print("Weapons table creation Successful !!")
        self.ORMObjectMap['Weapons'] = weapon

        ## Dump all the supported types in to Types table
        query_insert = f'INSERT INTO Types VALUES ( '

        for val in supported_Types:
            keyList = list(val.keys())
            ## The above returns a dictionary of keys. So we need to convert it as list
            query_insert = f'INSERT INTO Types VALUES ( \'{keyList[0]}\',\'{val[keyList[0]]}\' )'
            retVal,retMsg = self.execute(query_insert)
            print (retMsg)

    def execute(self,query):
        '''
        We create connection only when we are executing a query.

        '''
        conn = self.connection.connect()
        retVal = 0
        result = None
        retMsg = '' ##Return message is only for any non zero return value. For successful execution, the actual data from DB is sent back
        if conn == None:
            retMsg = 'Failed to connect to DB'
            retVal = -1
        else:
            try:
                result = conn.execute(query)
            except Exception as ex:
                retMsg = ex
                retVal = -2

            if retVal == 0:
                #print("\t\tQuery executed succesfully")
                retMsg = result

        return retVal,retMsg


    def getORMObject(self,tableName):
        if tableName not in self.ORMObjectMap:
            return None
        return self.ORMObjectMap[tableName]
        


