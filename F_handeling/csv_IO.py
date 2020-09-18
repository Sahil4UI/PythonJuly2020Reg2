import csv
'''
data = [
    {"name":"ram","id":101},
    {"name":"shyam","id":102},
    {"name":"radhey","id":103},
    {"name":"samay","id":104},
    {"name":"amar","id":105}
    ]

with open('data1.csv','w',newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow(item.values())
    
'''
with open('data.csv','r') as file:
    reader = csv.reader(file)
    for item in reader:
        print(item)
