from app import InputProvider
from app import SQLAlchemyAdapter
from app import SQLQueryHelper

import sys

## We create the list of supported types during DB initialization
supported_Types = (
    {'type_1' : 'RIFLE' } ,
    {'type_2' : 'TANK'  } ,
    {'type_3' : 'ROCKET'} ,
    {'type_4' : 'MORTAR'} 
)



def getConfigVals():
    ##Get the configuration from sql.conf file
    dbname = ''
    user = ''
    passwd = ''
    dbtype = ''
    try:
        confFile = open('sql.conf','r')
    except Exception as e:
        print (e)
        sys.exit(-1)

    for line in confFile:
        line = line.rstrip().lstrip()
        if len(line) and line[0] != '#':
            token = line.split('=')
            if len(token) > 1:
                if (token[0] == 'DB_NAME'):
                    dbname = token[1]
                elif (token[0] == 'USER'):
                    user = token[1]
                elif (token[0] == 'PASSWORD'):
                    passwd = token[1]
                elif (token[0] == 'DB_TYPE'):
                    dbtype = token[1]     
                else:
                    pass ## TODO Don't let any invalid entry  
    return dbname,user,passwd,dbtype

if __name__=="__main__":

    dbname,user,passwd,dbtype = getConfigVals()
    if (dbname != '' and user != '' and passwd != '' and dbtype != ''):
        sqlObj    = SQLAlchemyAdapter.SQLAlchemyAdapter(dbname,user,passwd,dbtype)
        ##Initialize DB with supported types
        sqlObj.initDB(supported_Types)
        SQLQueryHelperObj = SQLQueryHelper.SQLQueryHelper(sqlObj)
        IProvider = InputProvider.InputProvider(SQLQueryHelperObj)
        IProvider.processInputLoop()
    else:
        print('DBname or User or Password cannot be empty in sql.conf file\n')
        print('Program exiting')
        sys.exit(-2) ## even without exit(),  program will exit :-D