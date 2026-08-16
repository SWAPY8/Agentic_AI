# Create a Library Management System using Class and Object in Python. 
# What to Do 1. Create a class named Book.  
# 2. Create a constructor __init__() to initialize:  o Book name  o Book ID  o Author name  o Availability status  
# 3. Create a display_book() method to display book details.  
# 4. Create a issue_book() method:  o Check whether the book is available.  o If available, issue the book and change its status.  o If already issued, display an appropriate message.
# 5. Create a return_book() method:  o Return the issued book.  o Change its availability status back to available.  
# 6. Create a check_availability() method to display whether the book is available or issued. 


class Book:
    BOOK_STORE = ["To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Moby-Dick",
    "Wuthering Heights",
    "The Picture of Dorian Gray",
    "Crime and Punishment",
    "Jane Eyre",

    # Fantasy & Sci-Fi
    "The Hobbit",
    "Dune",
    "The Fellowship of the Ring",
    "Harry Potter and the Philosopher's Stone",
    "Neuromancer",
    "The Hitchhiker's Guide to the Galaxy",
    "A Game of Thrones",
    "Fahrenheit 451",
    "The Left Hand of Darkness",
    "The Name of the Wind",

    # Thriller, Mystery & Horror
    "The Da Vinci Code",
    "Gone Girl",
    "The Girl with the Dragon Tattoo",
    "And Then There Were None",
    "The Silence of the Lambs",
    "Dracula",
    "The Shining",
    "Frankenstein",
    "Rebecca",
    "Big Little Lies",

    # Contemporary Fiction & Drama
    "The Kite Runner",
    "Life of Pi",
    "Normal People",
    "Where the Crawdads Sing",
    "The Book Thief",
    "The Alchemist",
    "Little Fires Everywhere",
    "The Midnight Library",
    "A Thousand Splendid Suns",
    "All the Light We Cannot See",

    # Thought-Provoking Non-Fiction
    "Sapiens: A Brief History of Humankind",
    "Atomic Habits",
    "Thinking, Fast and Slow",
    "Educated",
    "The Immortal Life of Henrietta Lacks",
    "Quiet: The Power of Introverts",
    "Becoming",
    "Outliers: The Story of Success",
    "The Power of Habit",
    "A Short History of Nearly Everything"]
    
    def __init__ (self, Book_Name, Book_ID, Author_Name, Availability_Status ):
        self.Book_Name = Book_Name
        self.Book_ID = Book_ID
        self.Author_Name = Author_Name
        self.Availability_Status = Availability_Status
        
    def show_option(self):
        print("Enter 1 for Display Book Shell.")
        print("Enter 2 for Issue Book .")
        print("Enter 3 for Return Book .")
        print("Enter 4 for Check Book Availability.")
        print("Enter 5 for Exit.")
        
    def display_book(self):
        pass
        