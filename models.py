import psycopg2
import datetime 
import base64

class MyModel():
    def GetPicturs():
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="123",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="mydatabase")
            cursor = connection.cursor()

            postgreSQL_select_Query = "SELECT \
                                         pic \
                                         FROM public.pictures \
                                         order by date_time"

            #  ,date_time \


            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from table using cursor.fetchall")
            pictures_records = cursor.fetchall() 
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        
        return pictures_records

    def update(pic):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="123",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="mydatabase")
            cursor = connection.cursor()
            
            timenow = datetime.datetime.now()
            timestampStr = str(timenow.strftime('%Y-%m-%d'))
            sql_insert_query = " INSERT INTO pictures( pic, date_time)  VALUES (%s,%s) ;"

            pic= base64.encodebytes(pic).decode("utf-8")

            cursor.execute(sql_insert_query,(pic,timestampStr))
            connection.commit()
            print("Rocorde inserted")

        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")