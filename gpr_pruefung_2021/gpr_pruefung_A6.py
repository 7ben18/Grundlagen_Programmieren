def collect_data_sales(file_name, customer_nr: int):
    with open(file_name) as file:

        # Kopfzeile einlesen
        head = file.readline()
        new_head = head.split("\\t")[:-1]

        # Datensatz einlesen
        rows = file.readlines()
        new_rows = [x.split("\\t")[:-1] for x in rows]

        #print(rows)
        #print(new_rows)

        # Kopfzeile analysieren
        index_kunde = 0
        index_artikel = 0
        index_anzahl = 0

        for index, col in enumerate(new_head):
            if "Kunde" == col:
                index_kunde = index
                #print(index_kunde)
            elif "Artikel" == col:
                index_artikel = index
                #print(index_artikel)
            elif "Anzahl" == col:
                index_anzahl = index
                #print(index_anzahl)

    # Datensatz analysieren
    output = {}
    for auftrag in new_rows:
        if int(auftrag[index_kunde]) == customer_nr:
            if auftrag[index_artikel] not in output:
                output[auftrag[index_artikel]] = int(auftrag[index_anzahl])
            else:
                output[auftrag[index_artikel]] += int(auftrag[index_anzahl])
    return output

#print(collect_data_sales("gpr_pruefung_A6_datei", 12345))

def print_sales_data(data):
    print("Artikel -> Anzahl")
    for key, value in data.items():
        print(str(key) + " -> " + str(value))

def articles(file_name, customer_no):
    data = collect_data_sales(file_name, customer_no)
    print_sales_data(data)

articles("gpr_pruefung_A6_datei", 12345)



# Merci Haris fuer dini hilf!