import sys
from os import system,name

class TableModel(object):
    ##for weapon table
    class weapon(object):
        def __init__(self):
            self.ID = ''
            self.TYPE = ''
            self.MANUF = ''
            self.COUNTRY = ''

    

class InputProvider(object):

    def __init__(self,SQLQueryHelperObj):
        self.funcTable = [self.displayAllWeapons,
        self.displaySpecificWeapons,
        self.displayAllWeaponType,
        self.insertNewWeapon,
        self.deleteWeapon,
        self.updateWeapon,
        self.exitMenu]

        ##SQLAlchemy Adapter object
        self.SQLQueryHelperObj = SQLQueryHelperObj

    def processInputLoop(self):

        mainChoice = False
        subChoice = False
        while mainChoice == False:
            if name == 'nt':
                system('cls')
            else:
                system('clear')
            print ('\n\n\t\tMenu')
            print ('\t\t====\n')

            print ('\t\t0) Display all weapons\n')
            print ('\t\t1) Display specific weapon according to ID\n')
            print ('\t\t2) Display All supported weapons type\n')
            print ('\t\t3) Insert a new weapon\n')
            print ('\t\t4) Delete a weapon\n')
            print ('\t\t5) Update a weapon\n')
            print ('\t\t6) Exit\n')
            subChoice = False
            while subChoice == False:
                choice = int(input('\n\t\tEnter your choice [0,1,2,3,4,5,6] => '))
                if choice >= 0 and choice <= 6:
                    subChoice = True
                else:
                    subChoice = False
            ######################################################################
            ## Actual processing starts here ####
            self.funcTable[choice]()
            ######################################################################
            goodChoice = False
            while goodChoice == False:
                yesOrNo = input('\n\t\tDo you want to continue[y/n] => ')
                if yesOrNo == 'Y' or yesOrNo == 'y' or yesOrNo == 'N' or yesOrNo == 'n':
                    goodChoice = True
                else:
                    goodChoice = False

            if yesOrNo == 'N' or yesOrNo == 'n':
                mainChoice = True
        print ('\n\n\t\tExiting the menu\n')
        
        

       

    def displayAllWeapons(self):
        self.SQLQueryHelperObj.displayAllWeapons()

    def displaySpecificWeapons(self):
        weapon = TableModel.weapon()
        self.populateWeaponDetails(weapon,False)
        self.SQLQueryHelperObj.displaySpecificWeapons(weapon)

        

    def displayAllWeaponType(self):
        self.SQLQueryHelperObj.displayAllWeaponType()

    def insertNewWeapon(self):
        weapon = TableModel.weapon()
        self.populateWeaponDetails(weapon)
        self.SQLQueryHelperObj.insertNewWeapon(weapon)  


    def deleteWeapon(self):
        weapon = TableModel.weapon()
        self.populateWeaponDetails(weapon,False)
        self.SQLQueryHelperObj.deleteWeapon(weapon)

    def updateWeapon(self):
        weapon = TableModel.weapon()
        self.populateWeaponDetails(weapon,True)
        self.SQLQueryHelperObj.updateWeapon(weapon)

    def exitMenu(self):
        print('Exiting the program')
        sys.exit()

    def populateWeaponDetails(self,weapon,all=True):
        weapon.ID      = input('\n\n\t\tEnter weapon ID          => ')
        if all == True:
            weapon.TYPE    = input('\t\tEnter weapon Type        => ')
            weapon.MANUF   = input('\t\tEnter manufacturer       => ')
            weapon.COUNTRY = input('\t\tEnter Country of origin  => ')
        return
