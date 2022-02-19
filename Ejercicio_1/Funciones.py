listadatos=[]
def ingresodatos(vcliente,ccantidad,vprecio,vtotal,vigv,vpagototal):
    listadatos.extend([vcliente,ccantidad,vprecio,vtotal,vigv,vpagototal])


def obtenerPrecio(cantidad):
    precio=0
    if cantidad >0 and cantidad<5:
        precio=300.0
    elif cantidad >=5 and cantidad<=10:
        precio=250.0
    elif cantidad >=10:
        precio=200.0
    return precio

def obtenerTotal(cantidad,precio):
    total=cantidad*precio
    return total

def obtenerIGV(total):
    igv=total*0.18
    return igv

def obtenerPagoTotal(pago,igv):
    pagoT=pago+igv
    return pagoT