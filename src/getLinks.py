from bs4 import BeautifulSoup
import requests

"""
Scraps all the links to all the drugs from medlineplus.gov
and writes them to links.txt to be parsed and iterated over in
scraper.py. This scraper is needed because of the way 
medlineplus.gov is structured.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
baseurl = "https://medlineplus.gov/druginfo"
# Links are stored as set because same link may appear multiple
# times in medlineplud.gov
links = set()

print("\n\n")
for l in letters:
    print("Now processing: " + l)

    url = "https://medlineplus.gov/druginfo/drug_" + l + "a.html"
    page = requests.get(url)
    doc = BeautifulSoup(page.text, 'html.parser')

    atags = doc.find(['ul'], id='index').find_all(['a'])
    for a in atags:
        ext = a['href']
        # Append \n at the end here for when writing to .txt file
        link = baseurl + ext[1:] + "\n"
        links.add(link)
    
    print("Links found: " + str(len(atags)) + "\n")


print("\n\nWriting links to text file...\n")
with open('links.txt', 'w') as f:
    f.writelines(links)

print("DONE")