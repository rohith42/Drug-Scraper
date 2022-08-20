from cgitb import text
from bs4 import BeautifulSoup
import requests, re

url = "https://medlineplus.gov/druginfo/meds/a692030.html"
page = requests.get(url)
doc = BeautifulSoup(page.text, 'html.parser')

title = doc.findAll(['h1'])[0].string
how = doc.find_all(['div'], id='how')
sectionsWithDonts = doc.findAll(text=re.compile("Do not|do not"))
donts = []
for section in sectionsWithDonts:
    match = re.search("Do not.*\.$", section)
    if match:
        donts.append(match.group())
print(donts)