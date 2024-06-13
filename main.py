"""
Projekt 3 

Autor - Ondřej Charvát
Email: ondrej.charvat05@gmai.com

"""

import requests
from bs4 import BeautifulSoup
import csv
import argparse

default_url = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
default_output_file = 'output.csv'

def remove_after_last_slash(url):
    return url[:url.rfind('/')]

def krok1(url, output_file):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        
        data = []  # List to store all rows of data

        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                cell1 = cells.pop(0)
                cell2 = cells.pop(0)
                links = cell1.find_all("a") 
                if len(links) >= 1:
                    link1 = links.pop(0)
                    href = link1.get("href")
                    url2 = remove_after_last_slash(url) + "/" + href

                    row_data = [cell1.get_text(strip=True), cell2.get_text(strip=True)]
                    krok2(url2, data, row_data)
        
        # Write data to CSV file
        with open(output_file, 'w', newline='', encoding='cp1250') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)
    else:
        print("Chyba při získavání dat")

def krok2(url, excel_rows, row_data):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        hlavicky = []

        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 9:
                cell1 = cells.pop(3)
                cell2 = cells.pop(3)
                platne_hlasy = cells.pop(5)
                row_data.extend([cell1.get_text(strip=True), cell2.get_text(strip=True), platne_hlasy.get_text(strip=True)])
            elif len(cells) == 5:
                nazev_strany = cells.pop(1).get_text(strip=True)
                celkem_hlas = cells.pop(1).get_text(strip=True)
                row_data.append(celkem_hlas)
                hlavicky.append(nazev_strany)
        if len(excel_rows) == 0:
            hlavicky = ['code', 'location', 'registered', 'envelopes', 'valid'] + hlavicky
            excel_rows.append(hlavicky)
        excel_rows.append(row_data)
    else:
        print("Chyba při získavání dat")

def main(url, output_file):
    krok1(url, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web scraping script')
    parser.add_argument('url', type=str, nargs='?', default=default_url, help='URL of the website to scrape')
    parser.add_argument('output_file', type=str, nargs='?', default=default_output_file, help='Name of the output file')
    args = parser.parse_args()
    
    main(args.url, args.output_file)
