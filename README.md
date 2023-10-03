# Drug-Scraper

Scrapes drug information from medlineplus.gov using BeautifulSoup4 and stores important information in a PostgreSQL database. Uses Flask to deliver the JSON files as requested.

Stores the drug name, its link, its brand names, and important warnings (do nots).

<hr>

### Steps to run locally:

1. Clone this repository
```bash
git clone https://github.com/rohith42/Drug-Scraper.git
```

2. Create a conda environment
```bash
conda create -n drugScraper python=3.11 -y
conda activate drugScraper
```

3. Install the required packages
```bash
cd Drug-Scraper
pip install -r requirements.txt
```

4. Install PostgreSQL: https://www.postgresql.org/download/

5. Add a ```database.ini``` file with the right configurations to connect to your PostgreSQL database

6. Run the scraping script
```bash
python scraper.py
```

7. Run the application and visit the specified url
```bash
python main.py
```

<hr>

### File descriptions:

config.py contains the parser that reads a database.ini file and returns a dictionary containing the parameters to connect to the database.

drugDb.py contains DrugDb, the class that interfaces with the database.

getLinks.py is a script that gets the links for all the drugs on medlineplus.gov and writes it to links.txt.

main.py is the main Flask script to run the server. The home route delivers the html page found in templates/index.html.

scraper.py is the main webscraping script that gets all the drug information described above and inserts it into the database.

testDbAccess.py is to test the retrival of information from the database.
