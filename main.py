import command as cm
print("\nLibrary Information System\n")
print("Add a Book(1)")
print("Delete a book(2)")
print("Check out a book from the system(3)")
print("Update a book(4)")
process=int(input("Which one you want to do?(1/2/3/4):"))
if process==1:
    BookName=input("Enter the Book's name:")
    BookType=input("Enter the Book's genre:")
    BookPage=input("Enter the Book's number of page:")
    BookName=str(BookName)
    BookType=str(BookType)
    BookPage=int(BookPage)
    cm.Book.insert(BookName.lower(),BookType.lower(),BookPage)
if process==2:
    BookId=input("Enter the Book's id:")
    BookId=int(BookId)
    cm.Book.delete(BookId)
if process==3:
    BookName=input("Enter the Book's name:")
    BookName=str(BookName)
    cm.Book.checkBook(BookName.lower())
if process==4:
    updated_book_id=int(input("Please enter the id of the book you want to update:"))
    Updated_BookName=input("Please enter the book's new name:")
    Updated_BookType=input("Please enter the book's new genre:")
    Updated_BookPage=int(input("Please enter the book's new number of page:"))
    cm.Book.Update(updated_book_id,Updated_BookName.lower(),Updated_BookType.lower(),Updated_BookPage)
    
