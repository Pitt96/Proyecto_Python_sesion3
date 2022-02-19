import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic,QtWidgets
import Funciones as operaciones
class Ejercicio01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("proyecto01.ui",self)
        self.initUi()
    
    def initUi(self):
        self.twgtabla.setColumnWidth(0,180)
        self.twgtabla.setColumnWidth(1,100)
        self.twgtabla.setColumnWidth(2,95)
        self.twgtabla.setColumnWidth(3,95)
        self.twgtabla.setColumnWidth(4,100)
        self.twgtabla.setColumnWidth(5,159)
        self.bnuevo.clicked.connect(self.limpiar)
        self.bagregar.clicked.connect(self.agregar)
        #self.bmodificar.clicked.connect(self.modificar)
        #self.bguardarcambios.clicked.connect(self.cambios)
        self.bsalir.clicked.connect(self.salir)
        self.cbcantidad.activated.connect(self.seleccion)
        self.cbcantidad.addItem("Escoge...")
        for i in range(100):
            self.cbcantidad.addItem(str(i+1))

    def limpiar(self):
        self.tcliente.setText("")
        self.cbcantidad.setCurrentIndex(0)
        self.lblprecio.setText("")
        self.lbltotal.setText("")
        self.lbligb.setText("")
        self.lblpagototal.setText("")
        self.tcliente.setFocus()

    def seleccion(self):
        #cantidad=int(self.cbcantidad.currentText())
        cantidad=int(self.cbcantidad.itemText(self.cbcantidad.currentIndex()))
        precio=operaciones.obtenerPrecio(cantidad)
        total=operaciones.obtenerTotal(cantidad,precio)
        igv=operaciones.obtenerIGV(total)
        pagoTotal=float(operaciones.obtenerPagoTotal(total,igv))
        self.lblprecio.setText(str(precio))
        self.lbltotal.setText(str(total))
        self.lbligb.setText(str(igv))
        self.lblpagototal.setText(str(pagoTotal))

    def agregar(self):
        cliente=self.tcliente.text()
        cantidad=int(self.cbcantidad.itemText(self.cbcantidad.currentIndex()))
        precio=float(self.lblprecio.text())
        cantidad=int(self.cbcantidad.currentText())
        total=float(self.lbltotal.text())
        igv=float(self.lbligb.text())
        pago=float(self.lblpagototal.text())
        operaciones.ingresodatos(cliente,cantidad,precio,total,igv,pago)
        datos=[{"CLIENTE":operaciones.listadatos[0],
        "CANTIDAD":operaciones.listadatos[1],
        "PRECIO":operaciones.listadatos[2],
        "TOTAL":operaciones.listadatos[3],
        "IGV":operaciones.listadatos[4],
        "PAGO TOTAL":operaciones.listadatos[5]}]

        indicefila=self.twgtabla.rowCount()
        self.twgtabla.insertRow(indicefila)
        for d in datos:
            self.twgtabla.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(d["CLIENTE"])))
            self.twgtabla.setItem(indicefila,1,QtWidgets.QTableWidgetItem(str(d["CANTIDAD"])))
            self.twgtabla.setItem(indicefila,2,QtWidgets.QTableWidgetItem(str(d["PRECIO"])))
            self.twgtabla.setItem(indicefila,3,QtWidgets.QTableWidgetItem(str(d["TOTAL"])))
            self.twgtabla.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(d["IGV"])))
            self.twgtabla.setItem(indicefila,5,QtWidgets.QTableWidgetItem(str(d["PAGO TOTAL"])))
            indicefila+=1
        operaciones.listadatos.clear()
    
    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_1=Ejercicio01()
    ventana_1.show()
    sys.exit(app.exec())