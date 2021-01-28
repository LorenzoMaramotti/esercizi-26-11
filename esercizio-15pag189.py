nazioni=['Belgio' , 'Francia' , 'Germania' , 'Grecia' , 'Italia' , 'Paesi Bassi' , 'Polonia' ,  'Portogallo' , 'Regno Unito']
capitali=['Bruxelles' , 'Parigi' , 'Berlino' , 'Atene' , 'Roma' , 'Amsterdam' , 'Varsavia' , 'Lisbona' , 'Londra']

while True:
    scelta_stato=input("Scegli uno stato per saperne la capitale.\nRicordati di inserire la maiuscola: ")
    if scelta_stato in nazioni:
        i = nazioni.index(scelta_stato)
        print("La capitale dello stato" , scelta_stato , "è" , capitali[i])
    else:
        scelta=int(input("Questa capitale non è nel nostro database \nPer inserirne una nuova premi 1 \nPer uscire premi 0: "))
        while True:
            if scelta==1:
                break
            elif scelta==0:
                print("Grazie e arriverderci")
                break
            else:
                print("Per favore seleziona un carattere tra 1 e 0")
                break