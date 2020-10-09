

#cac phuong thuc can thuc hien 
# insert tao moi ban ghi 
# update ban ghi trong db 
# read ban ghi 
# delete ban ghi 

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
server = 'localhost,1433' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' 
database = 'TestDB' 
username = 'sa' 
password = 'Vinhdongdo123@' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#execute the command 
tableName='TestDB.TestDB_Schema.Employees'

def insert_row(studentName,location):
    print("this is insert ban ghi")
    cursor.execute("""
    SET NOCOUNT ON;INSERT INTO TestDB.TestDB_Schema.Employees (Name,Location) 
    VALUES (?,?)""",
    studentName,location) 
    cnxn.commit()
    #row =cursor.fetchone()
    #while row: 
     #   print('id of student is: ' + str(row[0]))
     #   row = cursor.fetchone()

def update_row(id , studentName, location):
    print("this is update row") 


def read_row(id):
    row_data=" "
    print("this is read row: ",id)
    cursor.execute("SELECT * from TestDB.TestDB_Schema.Employees where id = ? ",id) 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        print(row[1])
        print(row[2])
        row_data=" ".join([str(data) for data in row])
        row = cursor.fetchone()
    print(row_data)
    return row_data


    


def delete_row(id):
    print("this is delete row ") 

def view_version():
    result =cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()
    return result
def execute():
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()
    print("select * from employees ")
    cursor.execute("SELECT * from TestDB_Schema.Employees ;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        print(row[1])
        row = cursor.fetchone()


    cursor.execute("""
    INSERT INTO TestDB_Schema.Employees (Name,Location) 
    VALUES (?,?)""",
    "lam","thanhhoa") 
    cnxn.commit()
    #row = cursor.fetchone()

    cursor.execute("SELECT * from TestDB_Schema.Employees ;") 
    row = cursor.fetchone() 
    while row: 
        print('Inserted Product key is ' + str(row[0]))
        row = cursor.fetchone()
    print("inser success ")
