import pymysql.cursors

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="34.bjkberat",
    database="library"
)

mycursor=mydb.cursor()




class Book:
    def __init__(self,BookName,BookType,BookPage,BookId,Updated_BookName,Updated_BookType,Updated_BookPage):
        self.BookName=BookName
        self.BookType=BookType
        self.BookPage=BookPage
        self.BookId=BookId
        

    def insert(BookName,BookType,BookPage):
        kontrol=0
        sql6="SELECT BookType FROM books where BookName=%s"
        mycursor.execute(sql6,BookName)
        data4=mycursor.fetchall()
        if not data4:
            sql="INSERT INTO books(BookName,BookType,BookPage) VALUE(%s,%s,%s)"
            values=(BookName,BookType,BookPage)
            mycursor.execute(sql,values)
            
            try:
                mydb.commit()
                print(f"A book named {BookName} was added!")
            except pymysql.connect.Error as err:
                print("Error code:",err)
                
            finally:
                mydb.close()
                print("Database closed!")
        else:
            print("This book already exist!")
            mydb.close()
            print("Database closed!")

            
    def checkBook(BookName):
        sql2="SELECT idbooks FROM books WHERE BookName=%s"
        try:
            mycursor.execute(sql2,BookName)
            data2=mycursor.fetchall()
            if not data2:
                print("This book doesn't exist")
            else:
                for i in data2:
                    for k in i:
                        print(f"The book found ,book's id:{k}")
            mydb.commit()
        except pymysql.connect.Error as err:
            print("Error code:",err)
        finally:
            mydb.close()
            
    def delete(BookId):
        sql5="SELECT idbooks FROM books where idbooks=%s"
        mycursor.execute(sql5,BookId)
        check=mycursor.fetchall()
        if not check:
            print(f"The book with this id:{BookId} already deleted!")
        else:
            sql3="DELETE FROM books where idbooks=%s"
            try:
                value3=BookId
                mycursor.execute(sql3,value3)
                sql4="SELECT idbooks FROM books where idbooks=%s"
                mycursor.execute(sql4,BookId)
                data3=mycursor.fetchall()
                
                if not data3:
                    print(f"The book with id:{BookId} deleted!")
                else:
                    print("The book could not be deleted because something went wrong!")
                mydb.commit()
                
            except pymysql.connect.Error as err:
                print("Error code:",err)
            finally:
                mydb.close()
    def Update(BookId,Updated_BookName,Updated_BookType,Updated_BookPage):
        sql7="UPDATE books SET BookName=%s WHERE idbooks=%s"
        value7=(Updated_BookName,BookId)
        mycursor.execute(sql7,value7)
        sql8="UPDATE books SET BookType=%s WHERE idbooks=%s"
        value8=(Updated_BookType,BookId)
        mycursor.execute(sql8,value8)
        sql9="UPDATE books SET BookPage=%s WHERE idbooks=%s"
        value9=(Updated_BookPage,BookId)
        mycursor.execute(sql9,value9)
        try:
            mydb.commit()
        except pymysql.connect.Error as err:
            print("Error code:",err)
        finally:
            print(f"The book with id:{BookId} was updated ,book's new name:{Updated_BookName},book's new genre:{Updated_BookType},book's new number of page:{Updated_BookPage}")
            print("Database closed!")
            mydb.close()
