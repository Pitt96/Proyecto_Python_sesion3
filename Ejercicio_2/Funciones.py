import array as ary
listadatos=[]
def ingresodatos(xcodigo,xnombre,xcategoria,xocupacion,xsueldo,xdescuento1,xdescuento2,xbonificacion1,xbonificacion2):
    listadatos.extend([xcodigo,xnombre,xcategoria,xocupacion,xsueldo,xdescuento1,xdescuento2,xbonificacion1,xbonificacion2])

def categoriaSueldo(categoria):
    if categoria == "A":
        ocupacion="Analista"
        sueldo=2500
        d1=porcentaje(sueldo,0.12)
        d2=porcentaje(sueldo,0.1)
        b1=porcentaje(sueldo,0.14)
        b2=porcentaje(sueldo,0.16)
        sd=suma(d1,d2)
        sb=suma(b1,b2)
        t=sueldo-sd+sb
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(sd),str(sb),str(round(t,2))]
    elif categoria == "B":
        ocupacion="Programador"
        sueldo=1500
        d1=porcentaje(sueldo,0.1)
        d2=porcentaje(sueldo,0.08)
        b1=porcentaje(sueldo,0.12)
        b2=porcentaje(sueldo,0.14)
        sd=suma(d1,d2)
        sb=suma(b1,b2)
        t=sueldo-sd+sb
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(sd),str(sb),str(round(t,2))]
    elif categoria == "C":
        ocupacion="Asistente"
        sueldo=1000
        d1=porcentaje(sueldo,0.08)
        d2=porcentaje(sueldo,0.06)
        b1=porcentaje(sueldo,0.10)
        b2=porcentaje(sueldo,0.12)
        sd=suma(d1,d2)
        sb=suma(b1,b2)
        t=sueldo-sd+sb
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(sd),str(sb),str(round(t,2))]
    elif categoria == "D":
        ocupacion="Tecnico"
        sueldo=700
        d1=porcentaje(sueldo,0.06)
        d2=porcentaje(sueldo,0.04)
        b1=porcentaje(sueldo,0.08)
        b2=porcentaje(sueldo,0.10)
        sd=suma(d1,d2)
        sb=suma(b1,b2)
        t=sueldo-sd+sb
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(sd),str(sb),str(round(t,2))]
    elif categoria == "E":
        ocupacion="Operador"
        sueldo=500
        d1=porcentaje(sueldo,0.04)
        d2=porcentaje(sueldo,0.02)
        b1=porcentaje(sueldo,0.06)
        b2=porcentaje(sueldo,0.08)
        sd=suma(d1,d2)
        sb=suma(b1,b2)
        t=sueldo-sd+sb
        s=[ocupacion,str(sueldo),str(d1),str(d2),str(round(b1,2)),str(b2),str(sd),str(sb),str(round(t,2))]
    return s

def porcentaje(s,por):
    return s*por
    
def suma(a,y):
    return a+y