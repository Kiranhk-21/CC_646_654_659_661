import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",database="user_management")
cursor = mydb.cursor()
    
def r_execute(str1):
        cursor.execute(str1)
        p= pd.DataFrame(cursor.fetchall(),columns=[i[0] for i in cursor.description])
        return p

def d_execute(str1):
        try :
            cursor.execute(str1)
            mydb.commit()
        except Exception as e:
            st.write(e)
        
def retrieve_id(l):
        cursor.execute(l)
        a = cursor.fetchall()
        b = [i[0] for i in a]
        print(b)
        return b
