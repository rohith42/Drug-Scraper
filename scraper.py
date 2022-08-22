from bs4 import BeautifulSoup
import requests, re
import string


printable = set(string.printable)
# Returns normalized string with non-ASCII characters removed
def normalize(s):
    return ''.join(filter(lambda x: x in printable, s))



print("\n\nLoading links...")

# Get all the links from the text file
links = set()
with open('links.txt') as f:
    for link in f.readlines():
        links.add(link[:-1])

print("Got links!\n\n")


count = 0
for link in links:
    if count >= 100:
        break
    
    # name, link, alt names (brand names and brand names of combination products), donts

    # Link
    url = link
    page = requests.get(url)
    doc = BeautifulSoup(page.text, 'html.parser')


    # Name
    name = doc.find(['h1']).string
    print("Processing: " + name + ", Link: " + link)


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
    print("Added " + str(len(donts)) + " do nots")
    

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
    print("Added " + str(len(altnames)) + " brand names\n")

    count += 1


print("====== DONE ======")

"""
TEST URLS
Simvastatin: https://medlineplus.gov/druginfo/meds/a692030.html
Pyrethin... : https://medlineplus.gov/druginfo/meds/a601105.html
Chlorpheniramine: https://medlineplus.gov/druginfo/meds/a682543.html
"""