lista_veicoli_transitati = []
numero_giorni = 0
ripetizioni = 0
tasto_exit = 0
somma = 0
while True:
    numero_giorni += 1
    ripetizioni += 1
    print("Veicoli entrati il giorno", numero_giorni ,": ")
    veicoli_transitati = int(input())
    lista_veicoli_transitati.append(veicoli_transitati)

    if tasto_exit == veicoli_transitati:
        break

for i in lista_veicoli_transitati:
    somma += i
print("sono transitati" , somma , "veicoli in" , numero_giorni , "giorni")