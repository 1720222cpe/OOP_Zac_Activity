import csv 

filenames = ['name', 'age', 'country_code2', 'country_code3']

rows = [
    {'name': 'Zac',
    'age': 21,
    'country_code2' : 'PH',
    'country_code3' : 'PHL'},
     {'name': 'Zyrus',
    'age': 23,
    'country_code2' : 'PH',
    'country_code3' : 'PHL'},
     {'name': 'Dan',
    'age': 11,
    'country_code2' : 'PH',
    'country_code3' : 'PHL'},
]

with open('countries.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.Dictwriter(f, filenames=filenames)
    writer.writeheader()
    writer.writerows(rows)