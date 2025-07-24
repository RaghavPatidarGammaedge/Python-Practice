# import csv
# with open("Book1.csv","r") as file: #with statement helps with autoclosing
#     data = csv.reader(file)
#     print(data)
#     print()
#     for singleRow in data:
#         print(singleRow)
#
import csv

d=[['honda','32','japanese'],['chevy','2','american']]
# with open('Book1.csv', 'w', newline='') as file2:
#     writer = csv.writer(file2)
#     writer.writerows(d)


with open("Book1.csv","a+",newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

    writer = csv.writer(csvfile)
    writer.writerows(d)




