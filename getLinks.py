from bs4 import BeautifulSoup
import requests

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
baseurl = "https://medlineplus.gov/druginfo"
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
        link = baseurl + ext[1:] + "\n"
        links.add(link)
    
    print("Links found: " + str(len(atags)) + "\n")


print("\n\nWriting links to text file...\n")
with open('links.txt', 'w') as f:
    f.writelines(links)

print("DONE")