def delta(a,b,c):
    valore_delta=(b**2)-(4*a*c)
    return valore_delta

def fuoco(a,b,c):
    valore_delta = delta(a,b,c)
    x_fuoco=(-b)/(2*a)
    y_fuoco=(1-valore_delta)/(4*a)
    return x_fuoco, y_fuoco

def vertice(a,b,c):
    valore_delta = delta(a,b,c)
    x_vertice=(-b)/(2*a)
    y_vertice=-(valore_delta)/(4*a)
    return x_vertice, y_vertice

a=int(input("Inserisci il valore del parametro a: "))
b=int(input("Inserisci il valore del parametro b: "))
c=int(input("Inserisci il valore del parametro c: "))

coordinate_vertice=vertice(a,b,c)
coordinate_fuoco=fuoco(a,b,c)

print("Le coordinate del vertice sono" , coordinate_vertice, "Le coordinate del fuoco sono" , coordinate_fuoco)