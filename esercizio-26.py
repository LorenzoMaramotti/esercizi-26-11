lista_stipendi=[]
count = True
dipendenti = 0
ripetizioni = int(input("Quanti dipendenti ci sono nell'azienda?"))
somma = 0
while count == True:
    dipendenti += 1
    stipendio_persona=int(input("Stipendio dipendente"))
    lista_stipendi.append(stipendio_persona)

    if dipendenti == ripetizioni:
        tasto_exit = int(input("Per uscire premi -1"))
        if tasto_exit == -1:
            count = False
        else:
            pass
for i in lista_stipendi:
    somma += i
l = len(lista_stipendi)
print(lista_stipendi)
media_stipendi = somma/l
print(media_stipendi)