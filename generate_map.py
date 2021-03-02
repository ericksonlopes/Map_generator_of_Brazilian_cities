import folium
import csv

with open('BRAZIL_CITIES.csv', encoding='utf-8', newline='') as csvfile:
    head = [[index, value] for index, value in enumerate(csvfile.readline().split(';'))]

    reader_file = csv.reader(csvfile, delimiter=';')
    for row in reader_file:
        print(row[0], row[1])

    print(head)

# map = folium.Map(location=[-23.715357, -46.85055197])
# map.save('Location.html')
