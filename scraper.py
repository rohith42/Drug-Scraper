from cgitb import text
from operator import index
from bs4 import BeautifulSoup
import requests, re
import string

printable = set(string.printable)
# Returns normalized string with non-ASCII characters removed
def normalize(s):
    return ''.join(filter(lambda x: x in printable, s))

# name, link, alt names (brand names and brand names of combination products), donts

"""
TEST URLS
Simvastatin: https://medlineplus.gov/druginfo/meds/a692030.html
Pyrethin... : https://medlineplus.gov/druginfo/meds/a601105.html
Chlorpheniramine: https://medlineplus.gov/druginfo/meds/a682543.html
"""


# Link
url = "https://medlineplus.gov/druginfo/meds/a682543.html"
page = requests.get(url)
doc = BeautifulSoup(page.text, 'html.parser')

# Name
name = doc.find(['h1']).string

# Do nots
sectionsWithDonts = doc.findAll(text=re.compile("Do not"))
donts = []
for section in sectionsWithDonts:
    match = re.search("Do not.*\.$", section)
    if match:
        sentence = match.group()
        # sentence will contain eveything until the end of the section,
        # so you need to stop at the end of the sentence (eos):
        eos = sentence.index('.')
        donts.append(sentence[:eos])


# ALTERNATE NAMES (BRAND NAMES AND COMBINATION)
altnames = []

# Alt Names 1 (Brand Names)
bn1 = doc.find(['div'], id='brand-name-1')
if bn1:
    bns = bn1.find_all(['li'])
    for item in bns:
        altnames.append(normalize(item.text))

# Alt Names 2 (Brand Names of Combination Products)
bn2 = doc.find(['div'], id='brand-name-2')
if bn2:
    bns = bn2.find_all(['li'])
    for item in bns:
        altnames.append(normalize(item.text))

print()
print(name)
print(url)
print()
print(altnames)
print()
print(donts)
print()
print()