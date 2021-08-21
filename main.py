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
def check_then_Insert(Table_name,keys,values):
    email , password = values[0], values[1]
    email_temp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(email_temp, email):
        if re.findall("\d", password) and re.findall(r'[A-Za-z]', password):
            Insert_Table(Table_name, keys, values)
            print("Data Inserted Successfully")
        else:
            print("Error: Password must be an Expression (string+numbers) ")
    else:
        print(
            "Error: email format is wrong please enter correct Format like below \n info@maktabkhooneh.org \n expression@string.string ")

email , password = input('please: enter your email: ') , input("type your password: ")
key = ['email','password']
values = [email,password]
A = check_then_Insert(T_NAME,key,values)
