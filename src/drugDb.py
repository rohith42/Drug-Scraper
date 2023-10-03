import psycopg2
from config import config

class DrugDb: 
    """
    Class connects to drugdb postgresql database server.
    Can only insert values once (that's why self.id=1).
    Insert values using scraper.py if that script has not
    already been executed on this computer.
    Primarily to interface with the database;
    use methods getNames() and getDrug(name).
    """
    
    
    def __init__(self):
        self.conn = None
        self.cur = None

        try:
            print("\n\nConnecting to database...")

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
        listOfTuples = self.cur.fetchall()
        normalized = []
        for t in listOfTuples:
            normalized.append(t[0])
        return normalized
    

    def getDrug(self, name):
        self.cur.execute("SELECT * FROM drugs WHERE name=%s",(name,))
        d = self.cur.fetchall()[0]
        name, link, altnames, donts = d[1], d[2], d[3], d[4]
        # Have to split the brand names and donts because they'll
        # be stored as one long concatennated string in db
        return ({
            'name' : name,
            'link' : link,
            'brands' : altnames.split('$'),
            'do nots' : donts.split('$')
        })


    def view(self):
        self.cur.execute("SELECT * FROM drugs")
        return self.cur.fetchall()


    
    def __del__(self):
        self.conn.close()