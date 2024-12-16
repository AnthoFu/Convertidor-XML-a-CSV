import xml.etree.ElementTree as ET
import csv
import glob
import os

def xml_to_csv(xml_file, csv_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Abrimos el archivo csv y con el mode "w" de escritura
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Escribimos el encabezado
        header = []
        for child in root[0]:  # Esto es para archivos que se piensen que es una estructura sencilla
            header.append(child.tag)
        writer.writerow(header)

        # Escribimos los datos en cada casilla
        for elem in root:
            row = []
            for child in elem:
                row.append(child.text)
            writer.writerow(row)

# Utilizamos la libreria "glob" para poder buscar todos los archivos .xml en la carpeta actual
xml_files = glob.glob('*.xml')  # Esto obtiene todos los archivos con extensión .xml

# Iteramos sobre cada archivo XML y los convertimos a CSV
for xml_file in xml_files:
    csv_file = xml_file.replace('.xml', '') + '.csv'  # Eliminar la extensión .xml y agregar .csv
    xml_to_csv(xml_file, csv_file)
    
    #OPCIONAL (Eliminamos el archivo XML despues de hacer la conversion)
    os.remove(xml_file)  # Esto elimina el archivo XML