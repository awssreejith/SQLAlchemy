## This will populate the queries required.
## InputProvider --> QueryHelper --> SQLAlchemyAdapter --> DB
from app import InputProvider
class SQLQueryHelper(object):
    def __init__(self,SQLAlchemyAdapterHandle):
        self.SQLAlchemyAdapterHandle = SQLAlchemyAdapterHandle

    def displayAllWeaponType(self):
        '''
        query = f'SELECT * FROM Types'
        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(query)
        if (retVal < 0):
            print("\t\tFailed to gather information about weapons Types")
        else:
            for val in retMsg:
                print(f'\t\t{val}')
        '''
        table_type = self.SQLAlchemyAdapterHandle.getORMObject('Types')
        if table_type != None:
            sel = table_type.select()
            retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(sel)
            if (retVal < 0):
                print("\t\t[Error - Failed to gather information about weapons Types]")
            else:
                #print (retMsg.scalar())
                for val in retMsg:
                    print(f'\t\t{val}')

    def insertNewWeapon(self,weapon):
        queryGetType = f'SELECT Type_id as type from Types where Type_name=\'{weapon.TYPE}\''
        #query = f'INSERT INTO Weapons values({weapon.ID},{weapon.TYPE},{},{})'

        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(queryGetType)
        if (retVal < 0):
            print("\t\t[Error - Failed to gather information about Types]")
            print(retMsg)
        else:
            val = retMsg.fetchall() ## This returns an array of tuples [(id,type),(id,type)]
            if len(val)  <= 0:
                print("\t\t[MSG - Type not supported. Insertion failed]")
                return
            typeId = val[0][0]
            ## Now insert in to table
            ##First get the weapons table handle from ORM dictioary
            table_weapons = self.SQLAlchemyAdapterHandle.getORMObject('Weapons')
            if table_weapons == None:
                print("Error - Couldn't get Weapons table handle.Nothing to do")
                return
            
            ins = table_weapons.insert().values(Weapon_id = weapon.ID,Type = typeId,Manufacturer = weapon.MANUF,Country = weapon.COUNTRY)
        
            retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(ins)
            if (retVal < 0):
                print("\t\t[Error - Failed to insert new weapon]")
                print(retMsg)
            else:
                print("\t\t[Msg - Weapon inserted succesfully]")

        
    def displayAllWeapons(self):
        table_weapons = self.SQLAlchemyAdapterHandle.getORMObject('Weapons')
        sel = table_weapons.select()

        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(sel)
        if (retVal < 0):
            print("\t\t[Error - Failed to fetch weapons from DB]")
            print(retMsg)
        else:
            val = retMsg.fetchall()
            for element in val:
                print(element)

    def displaySpecificWeapons(self,weapon):
        table_weapons = self.SQLAlchemyAdapterHandle.getORMObject('Weapons')

        ##Ver Very important
        ## unlike insert statement, for select if we use where clause, then we need to give complete qualifier for the
        ##column. For example we have to give as 'table_weapons.columns.Weapon_id' as column name
        sel = table_weapons.select().where(table_weapons.columns.Weapon_id == weapon.ID)

        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(sel)
        if (retVal < 0):
            print("\t\t[Error - Failed to retrieve weapon details]")
            print(retMsg)
        else:
            val = retMsg.fetchall() ## This returns an array of tuples [(id,type),(id,type)]
            if len(val)  <= 0:
                print("\t\t[MSG - No rows returned]")
                return
            for ele in val:
                print(ele)   



    def deleteWeapon(self,weapon):
        table_weapons = self.SQLAlchemyAdapterHandle.getORMObject('Weapons')

        ##Very Very important
        ## unlike insert statement, for delete if we use where clause, then we need to give complete qualifier for the
        ##column. For example we have to give as 'table_weapons.columns.Weapon_id' as column name
        sel = table_weapons.select().where(table_weapons.columns.Weapon_id == weapon.ID)
        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(sel)
        if (retVal < 0):
            print("\t\t[Error - Failed to retrieve weapon details]")
            print(retMsg)
            return

        else:
            val = retMsg.fetchall() ## This returns an array of tuples [(id,type),(id,type)]
            if len(val)  <= 0:
                print("\t\t[MSG - No such weapon]")
                return

        ##If control reaches here, then we have a valid weapon with that ID. So lets delete it           

        deli = table_weapons.delete().where(table_weapons.columns.Weapon_id == weapon.ID)

        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(deli)
        if (retVal < 0):
            print("\t\t[Error - Failed to delete weapon]")
            print(retMsg)
        else:
            print("\t\t[MSG - Weapon deleted successfully]")



    def updateWeapon(self,weapon):
        ##first check the weapon is existing or not.
        table_weapons = self.SQLAlchemyAdapterHandle.getORMObject('Weapons')

        sel = table_weapons.select().where(table_weapons.columns.Weapon_id == weapon.ID)
        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(sel)
        if (retVal < 0):
            print("\t\t[Error - Failed to retrieve weapon details]")
            print(retMsg)
            return

        else:
            val = retMsg.fetchall() ## This returns an array of tuples [(id,type),(id,type)]
            if len(val)  <= 0:
                print("\t\t[MSG - No such weapon]")
                return

        ## NOTE - The update method never checks for the validity of an element. it simply inserts it.So we have to ensure that the TYPE is a valid one
        table_types = self.SQLAlchemyAdapterHandle.getORMObject('Types')
        selQuery = table_types.select().where(table_types.columns.Type_name == weapon.TYPE)
        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(selQuery)
        if (retVal < 0):
            print("\t\t[Error - Failed to retrieve type details]")
            print(retMsg)
            return

        else:
            val = retMsg.fetchall() ## This returns an array of tuples [(id,type),(id,type)]
            if len(val)  <= 0:
                print("\t\t[MSG - Invalid weapon type]")
                return
        ##If control reaches here, that means we have a valid weapon and type. Now update it
        ## Note: The update method takes dictionary as argument
        updateQuery = table_weapons.update().where(table_weapons.columns.Weapon_id == weapon.ID).values(
            {"Type":weapon.TYPE,"Manufacturer":weapon.MANUF,"Country":weapon.COUNTRY}
        )

        retVal,retMsg = self.SQLAlchemyAdapterHandle.execute(updateQuery)
        if (retVal < 0):
            print("\t\t[Error - Failed to update weapon]")
            print(retMsg)
        else:
            print("\t\t[MSG - Weapon updated successfully]")




 






