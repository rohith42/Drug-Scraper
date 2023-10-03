from drugDb import DrugDb

"""
This script is to test the get methods of DrugDB.
"""

db = DrugDb()

allNames = db.getNames()
# print(allNames)

testDrug = db.getDrug('Simvastatin')
for item in testDrug.items():
    print(item)