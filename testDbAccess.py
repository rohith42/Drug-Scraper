from drugDb import DrugDb

db = DrugDb()

allNames = db.getNames()
# print(allNames)

testDrug = db.getDrug('Simvastatin')
for item in testDrug.items():
    print(item)