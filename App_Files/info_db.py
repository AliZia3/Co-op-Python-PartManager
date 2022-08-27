import sqlite3


class Database:

    # Initializing Database
    def __init__(self, db):
        # Sets up connection to database
        self.con = sqlite3.connect(db)

        # Used to execute queries
        self.cur = self.con.cursor()

        # Creates table with 5 coloumns if it doesn't exist
        self.cur.execute('''CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, 
        retailer text, price text)''')

        # Saves changes
        self.con.commit()

    # CRUD Operations
    def fetch(self):
        self.cur.execute('SELECT * FROM parts')
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.con.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,)) # Need trailing comma since its a tuple
        self.con.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute('UPDATE parts SET part=?, customer=?, retailer=?, price=? WHERE id=?',
                         (part, customer, retailer, price, id))
        self.con.commit()

    def delete(self):
        self.cur.execute("DELETE FROM parts")
        self.con.commit()

    # Destructor is called when all references to the object have been deleted
    def __del__(self):
        # Closes the connection
        self.con.close()

