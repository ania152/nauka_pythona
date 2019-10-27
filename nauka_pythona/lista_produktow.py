import pprint, csv

def zapisz_koszyk(owoce):
    with open ('koszyk.csv', mode='w') as csv_file:
        fieldnames = ['nazwa', 'cena', 'vat', 'jednostka', 'ilosc']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in range (len(owoce)):
            writer.writerow(owoce[i])



def main():
    koszyk = [
        {'nazwa': 'jablko', 'cena': '2', 'vat': '23.0', 'jednostka': 'kg', 'ilosc': '2'},
        {'nazwa': 'gruszka', 'cena': '3', 'vat': '23.0', 'jednostka': 'kg','ilosc': '3'},
        {'nazwa': 'banan', 'cena': '4', 'vat': '23.0', 'jednostka': 'kg','ilosc': '4'}
    ]
    pprint.pprint(koszyk)
    zapisz_koszyk(koszyk)



if __name__== "__main__":
    main()

#produkt = {'nazwa': 'jablko', 'cena': '2', 'vat': '23.0', 'jednostka': 'kg'}
