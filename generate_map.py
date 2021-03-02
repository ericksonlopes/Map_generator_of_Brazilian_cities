import folium
import csv

cidade = input('Digite uma cidade:')
uf = input('Informe o UF: ')

with open('BRAZIL_CITIES.csv', encoding='utf-8', newline='') as csvfile:
    # print([[index, value] for index, value in enumerate(csvfile.readline().split(';'))])

    # le o arquivo, especificando o limite
    reader_file = csv.reader(csvfile, delimiter=';')
    # por cada linha do arquivo
    for row in reader_file:
        # Se a cidade for igual ao item da coluna 0
        if cidade.lower() == row[0].lower() and uf == row[1]:
            print(row[0], row[1], row[23], row[24])
            # Busca a Localização
            map_loc = folium.Map(location=[row[24], row[23]])
            # Cria o arquivo HTML com o mapa
            map_loc.save(f'{row[0]}_{row[1]}.html')

