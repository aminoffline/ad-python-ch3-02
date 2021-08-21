#email : expression@string.string
#password : string+numbers
import mysql.connector , re
config = {
    'user':'Amin',
    'password':'Adv@ncePyth0n',
    'host':'localhost',
    'database':'second_assignment'
}
T_NAME = 'ep'
db = mysql.connector.connect(**config)
cursor = db.cursor()
def Insert_Table(Table_name,keys,values):
    key = str(keys)
    key = key.replace("[", "")
    key = key.replace("]", "")
    key = key.replace("'","")
    key = key.replace('"','')
    val = str(values)
    val = val.replace("[", "")
    val = val.replace("]", "")
    sql = f"INSERT INTO {Table_name} ({key}) VALUES ({val})"
    cursor.execute(sql)
    db.commit()
"""
NOW ASSUME WE HAVE DATABASE WITH TABLE WITH CHARACTERIZATION WE NEED TO INSERT OUR  INPUT DATA
"""
email_temp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Z|a-z]{2,}\b'
password_temp = r'\w+'

email , password = input('please: enter your email: ') , input("type your password: ")
key = ['email','password']
values = [email,password]
if re.fullmatch(email_temp, email):
    if re.fullmatch(password_temp,password) and re.match(r'[A-Za-z]',password):
        if re.match('\d',password):
            Insert_Table(T_NAME,key,values)
            print("Data Inserted Successfully")
        else:
            print("Password must have Number")
    else:
        print("Password must be an Expression (string+numbers) ")
else:
    print("email format is wrong please enter correct Format like below \n info@maktabkhooneh.org expression@string.string ")



