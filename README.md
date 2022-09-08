# Drug-Scraper

Uses BeautifulSoup4 to scrape drug information from medlineplus.gov and stores that information in a postgresql database. Uses Flask to deliver the JSON files as requested.

Stores the drug name, its link, its brand names, and important warnings (do nots).

config.py contains the parser that reads a database.ini file and returns a dictionary containing the parameters to connect to the database.

drugDb.py contains DrugDb, the class that interfaces with the database.

getLinks.py is a script that gets the links for all the drugs on medlineplus.gov and writes it to links.txt.

main.py is the main Flask script to run the server. The home route delivers the html page found in templates/index.html.

scraper.py is the main webscraping script that gets all the drug information described above and inserts it into the database.

testDbAccess.py is to test the retrival of information from the database.
