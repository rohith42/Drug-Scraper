import psycopg2

class DrugDb: 
    def __init__(self, db):
        self.conn = psycopg2.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS drugs (id INTEGER PRIMARY KEY, name text, link text, altnames text, donts text)")
        self.conn.commit()
    
    def insert(self, name, link, altnames, donts):
        self.cur.execute("INSERT INTO drugs VALUES (NULL,?,?,?,?)", (name, link, altnames, donts))
        self.conn.commit()
    
    def getNames(self):
        self.cur.execute("SELECT name FROM drugs")
        return self.cur.fetchall()
    
    def getDrug(self, name):
        self.cur.execute("SELECT * FROM drugs WHERE name=?",(name))
        return self.cur.fetchall()

    def view(self):
        self.cur.execute("SELECT * FROM drugs")
        return self.cur.fetchall()
    
    def __del__(self):
        self.conn.close()