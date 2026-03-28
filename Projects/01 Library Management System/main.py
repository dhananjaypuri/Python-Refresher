class Library:
    def __init__(self):
        self.books = dict();

    def add_books(self, book_id, name, author):
        if book_id in self.books:
            return f"Books id {book_id} already exists!!!!";
        else:
            self.books[book_id] = {"name": name, "author": author, "status": "available"};

            return f"Book {self.books[book_id]['name']} added successfully with id {book_id}";
    def search_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            return (
                f"Book ID: {book_id}, "
                f"Name: {book['name']}, "
                f"Author: {book['author']}, "
                f"Status: {book['status']}"
            );
        else:
            return f"Book is not available";

    def remove_book(self, book_id):
        if book_id in self.books:
            
            removed_bookid = self.books.pop(book_id);
            if removed_bookid:
                return f"Book with ID: {book_id} removed successfully !!!! ";
        else:
            return f"Book cannot be removed as its not available !!!!";

    def display_books(self):

        message = "";

        if len(self.books) > 0:
            
            message = message + f"Below {len(self.books)} Books are available .\n";
        
            for book in self.books.items():
                message = message + f"{book[0]} , Name: {book[1]['name']}\n";
            return message

        else:
            message = message + "No Books Available"
        
        return message;

    def issue_book(self, book_id):
        message = "";
        if book_id in self.books:

            status = self.books[book_id]['status'];
            if status == "available":
                self.books[book_id]['status'] = "issued";
                message = message + "Book Issued";
            else:
                message = message + "Book is already issued to someone else.";
        else:
            message = message + "Book is not available in library .";

        return message;

    def return_book(self, book_id):
        message = "";
        if book_id in self.books:

            status = self.books[book_id]['status'];
            if status == "issued":
                self.books[book_id]['status'] = "available";
                message = message + "Book Returned";
            else:
                message = message + "Book Already Available";

        else:
            message = message + "Book is not available in library .";

        return message;


bk = Library(); 

# print(bk.add_books(101, "Python", "ABC"));
# print(bk.add_books(102, "AI", "ML"));

# print(bk.search_book(101));
# print(bk.remove_book(101));
# print(bk.display_books());
# print(bk.add_books(101, "AI", "ML"));
# print(bk.display_books());
# print(bk.issue_book(102));
# print(bk.display_books());
# print(bk.return_book(102));
# print(bk.issue_book(102));

query = input('''Welcome to Library Management System
Select the option:

1 -> Display Books
2 -> Add Book
3 -> Search Book
4 -> Issue Book
5 -> Return Book
6 -> Remove Books
7 -> Eixt\n

Enter Option : ''');


while True:
    match query:
        case '1':
                print("Display Books\n");
                print(bk.display_books());
                print("=======================================");
                query = input("Select the option:");
        case '2':
                print("Add Book\n");

                try:
                    book_id = int(input("Enter the book ID: "));
                    name = input("Enter the name of the book : ");
                    author = input("Enter the author name : ");
                    print(bk.add_books(book_id, name, author));
                except Exception as e:
                     print(str(e));
                finally:
                    print("=======================================");
                    query = input("Select the option:");

        case '3':
                print("Search Book\n");
                
                try:
                    book_id = int(input("Enter the book ID: "));
                    print(bk.search_book(book_id));
                except Exception as e:
                     print(str(e));
                finally:
                    print("=======================================");
                    query = input("Select the option:");
         
        case '4':
                print("Issue Book\n");
                
                try:
                    book_id = int(input("Enter the book ID: "));
                    print(bk.issue_book(book_id));
                except Exception as e:
                     print(str(e));
                finally:
                    print("=======================================");
                    query = input("Select the option:");
        case '5':
                print("Return Book\n");
                
                try:
                    book_id = int(input("Enter the book ID: "));
                    print(bk.return_book(book_id));
                except Exception as e:
                     print(str(e));
                finally:
                    print("=======================================");
                    query = input("Select the option:");
        case '6':
                print("Remove Book\n");
                
                try:
                    book_id = int(input("Enter the book ID: "));
                    print(bk.remove_book(book_id));
                except Exception as e:
                     print(str(e));
                finally:
                    print("=======================================");
                    query = input("Select the option:");
        case '7':
                print("Bye Bye");
                break;
        case _:
                print("Invalid Options \nValid Options are : 1,2,3,4,5,6 and 7 .");
                query = input("Select the option:");