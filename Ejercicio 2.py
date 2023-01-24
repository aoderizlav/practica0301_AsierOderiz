import csv

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F", "8": "P", "9": "D",
            "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V", "18": "H",
            "19": "L", "20": "C", "21": "K", "22": "E"}


def check_DGT(ruta):
    with open(ruta, encoding="utf-8") as csvfile:
        lista = []
        correcion = []
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for datos in reader:
            lista.append(datos)
            nombre = check_username(datos[0])
            DNI = check_nif(datos[1])
            correcion.append([nombre, DNI])

    with open("C:/Users/HP/Desktop/Pycharm/practica0301_AsierOderiz/50.csv", 'w', encoding='utf-8',
              newline='') as csvfille:
        writer = csv.writer(csvfille, delimiter=',', dialect=csv.excel)
        for check in correcion:
            writer.writerow(check)


def check_username(user_name):
    return user_name.title()


def check_nif(user_nif):
    if user_nif == "DNI":
        return user_nif
    else:
        DNI = str(user_nif)
        numero = DNI[0:8]
        check = int(numero) % 23
        numero_corregido = nif_dict[str(check)]
    return numero + numero_corregido


check_DGT("C:/Users/HP/Desktop/Pycharm/practica0301_AsierOderiz/50.csv")
