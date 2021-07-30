import hashlib, os, binascii, pyodbc
# ------------------------------------------------------------------------------------------#
# Hash Salt Process
# ------------------------------------------------------------------------------------------#
def zest_key():
    """ Lets generate a salt """
    zest = binascii.hexlify(os.urandom(16)).decode()
    return zest
      
def hash_key(salt, key):
    """ Lets create a hash with some zest! """
    key = hashlib.pbkdf2_hmac('sha512', key.encode('utf-8'), salt.encode(), 100000)    
    return infix_salt(salt.encode(), binascii.hexlify(key)) 
 
def infix_salt(root, key):
    """ This splits the hash in half and inserts the salt in the middle """        
    prfx = key[ :int(len(key) / 2)]
    sffx = key[int(len(key) / 2): ]    
    return (prfx + root + sffx).decode('ascii')
# ------------------------------------------------------------------------------------------#
# Unsalt Process
# ------------------------------------------------------------------------------------------#
def unfix_salt(stored):
    """ Lets extract a salted hash from the stored password """    
    return stored[64:96]

def check_key(stored_password, attempt):
    """ Lets validate the attempt """    
    salt = unfix_salt(stored_password)   
    attempt = hashlib.pbkdf2_hmac('sha512', attempt.encode('utf-8'), salt.encode(), 100000)
    attempt = infix_salt(salt.encode(), binascii.hexlify(attempt))    
    return stored_password == attempt
# ------------------------------------------------------------------------------------------#
# Establish Communications with DB
# ------------------------------------------------------------------------------------------#
def establish_accesscomm():
    """ Establish communication to accessdb """
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Daddy\Desktop\acctmgmt.accdb;')        
    return connection
# ------------------------------------------------------------------------------------------#
# Read/Write DB Records
# ------------------------------------------------------------------------------------------#
def accesscomm_record(connection, username, hash):
    """ Pass communication, record changes to db, commit and verify records, close connection """
    cursor = connection.cursor()
    rstinc = 'ALTER TABLE USERS ALTER COLUMN ID COUNTER(1,1)'
    deltabl = 'Delete * From USERS'
    acdbq = 'INSERT INTO USERS (Username, Digest) VALUES (?,?)'
    cursor.execute(deltabl)
    cursor.execute(rstinc)
    cursor.execute(acdbq, (username,hash))    
    cursor.execute('select * from users')
    for row in cursor.fetchall():
        print(row)
    cursor.commit()
    cursor.close()
    connection.close()
 
def accesscomm_withdraw(connection, username, attempt):
    cursor = connection.cursor()
    #acdb = 'INSERT INTO USERS (Username, Digest) VALUES (?,?)'
    #cursor.execute(acdb, (username,hash))    
    cursor.execute('select * from users')
    for item in cursor.fetchall():
        if item.Username == username:  
            print("Username identified!")
            if check_key(item.Digest, attempt):
                print("Passwords appear to match!")
            else:
                print("Passwords do not match, try again...")
        else:
            print("Username unidentified...")
    #cursor.commit()
    cursor.close()
    connection.close()
# ------------------------------------------------------------------------------------------#
# Input/Output users credentials, validations
# ------------------------------------------------------------------------------------------#
# Hash/Salt and add record to DB
# accesscomm_record(establish_accesscomm(),"Username123",hash_key(zest_key(), 'Password45'))
 
# Check if username, password is valid
# accesscomm_withdraw(establish_accesscomm(), "Username123", "Password45") #True
# accesscomm_withdraw(establish_accesscomm(), "Username54", "Password45")  #Flase
