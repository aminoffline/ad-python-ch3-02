#email : expression@string.string
#password : string+numbers
import mysql.connector
config = {
    'user':'Amin',
    'password':'Adv@ncePyth0n',
    'host':'localhost'
    'database':'second_assignment'
}
T_NAME = 'ep'
db = mysql.connector.connect(**config)
cursor = db.cursor()
"""
NOW ASSUME WE HAVE DATABASE WITH TABLE WITH CHARACTERIZATION WE NEED TO INSERT OUR  INPUT DATA
"""

email , password = input('please: enter your eamil: ') , input("type your password")