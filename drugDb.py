import psycopg2
from config import config

class DrugDb: 
    def __init__(self):
        self.conn = None
        self.cur = None

        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            self.conn = psycopg2.connect(**params)
            
            # create a cursor
            self.cur = self.conn.cursor()
            
            # confirm connection
            self.cur.execute('SELECT current_database()')
            db_name = self.cur.fetchone()[0]
            print("Successfully connected to " + db_name)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        self.cur.execute("CREATE TABLE IF NOT EXISTS drugs (id INTEGER PRIMARY KEY, name text, link text, altnames text, donts text)")
        self.conn.commit()
        self.id = 1
    

    def insert(self, name, link, altnames, donts):
        self.cur.execute("INSERT INTO drugs VALUES(%s,%s,%s,%s,%s)", (self.id, name, link, altnames, donts))
        self.conn.commit()
        self.id += 1
    

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