import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic,QtWidgets
import Funciones as operaciones
class Ejercicio02(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Proyecto2.ui",self)
        self.initUi()
    
    def initUi(self):
        self.twgdatos.setColumnWidth(0,150)
        self.twgdatos.setColumnWidth(1,180)
        self.twgdatos.setColumnWidth(2,100)
        self.twgdatos.setColumnWidth(3,150)
        self.twgdatos.setColumnWidth(4,128)
        self.twgdatos.setColumnWidth(5,130)
        self.twgdatos.setColumnWidth(6,130)
        self.twgdatos.setColumnWidth(7,128)
        self.twgdatos.setColumnWidth(8,158)
        self.bnuevo.clicked.connect(self.limpiar)
        self.bagregar.clicked.connect(self.agregar)
        self.bsalir.clicked.connect(self.salir)
        self.cbcategoria.activated.connect(self.seleccion)
        

    def limpiar(self):
        self.txtcodigo.setText("")
        self.txtnombre.setText("")
        self.cbcategoria.setCurrentIndex(0)
        self.txtocupacion.setText("")
        self.txtsueldo.setText("")
        self.txtdescuento1.setText("")
        self.txtdescuento2.setText("")
        self.txtbonificacion1.setText("")
        self.txtbonificacion2.setText("")
        self.txtsumaDescuento.setText("")
        self.txtsumaBonificacion.setText("")
        self.txtsueldoTotal.setText("")
        self.txtcodigo.setFocus()

    def seleccion(self):

        cta=self.cbcategoria.currentText()
        if(cta=="<..CATEGORIA..>"):
            aux="error"
            datosCategoria=[aux,aux,aux,aux,aux,aux,aux,aux,aux]
        else:
            datosCategoria=operaciones.categoriaSueldo(cta)
        ocupacion=datosCategoria[0]
        sueldo=datosCategoria[1]
        descuento1=datosCategoria[2]
        descuento2=datosCategoria[3]
        bonificacion1=datosCategoria[4]
        bonificacion2=datosCategoria[5]
        sDescuento=datosCategoria[6]
        sBonificacion=datosCategoria[7]
        pagoTotal=datosCategoria[8]
        
        self.txtocupacion.setText(ocupacion)
        self.txtsueldo.setText(sueldo)
        self.txtdescuento1.setText(descuento1)
        self.txtdescuento2.setText(descuento2)
        self.txtbonificacion1.setText(bonificacion1)
        self.txtbonificacion2.setText(bonificacion2)
        self.txtsumaDescuento.setText(sDescuento)
        self.txtsumaBonificacion.setText(sBonificacion)
        self.txtsueldoTotal.setText(pagoTotal)

        
        

    def agregar(self):
        codigo=self.txtcodigo.text()
        nombres=self.txtnombre.text()
        categoria=self.cbcategoria.currentText()
        if(categoria=="<..CATEGORIA..>"):
            aux="error"
            datosCategoria=[aux,aux,aux,aux,aux,aux,aux,aux,aux]
        else:
            datosCategoria=operaciones.categoriaSueldo(categoria)
        ocupacion=datosCategoria[0]
        sueldo=datosCategoria[1]
        descuento1=datosCategoria[2]
        descuento2=datosCategoria[3]
        bonificacion1=datosCategoria[4]
        bonificacion2=datosCategoria[5]
        #sDescuento=datosCategoria[6]
        #sBonificacion=datosCategoria[7]
        #pagoTotal=datosCategoria[8]
        
        operaciones.ingresodatos(codigo,nombres,categoria,ocupacion,sueldo,descuento1,descuento2,bonificacion1,bonificacion2)
        datos=[{"CODIGO":operaciones.listadatos[0],
        "NOMBRES":operaciones.listadatos[1],
        "CATEGORIA":operaciones.listadatos[2],
        "OCUPACION":operaciones.listadatos[3],
        "SUELDO":operaciones.listadatos[4],
        "DESCUENTO1":operaciones.listadatos[5],
        "DESCUENTO2":operaciones.listadatos[6],
        "BONIFICACION1":operaciones.listadatos[7],
        "BONIFICACION2":operaciones.listadatos[8]}]

        indicefila=self.twgdatos.rowCount()
        self.twgdatos.insertRow(indicefila)
        for d in datos:
            self.twgdatos.setItem(indicefila,0,QtWidgets.QTableWidgetItem(d["CODIGO"]))
            self.twgdatos.setItem(indicefila,1,QtWidgets.QTableWidgetItem(d["NOMBRES"]))
            self.twgdatos.setItem(indicefila,2,QtWidgets.QTableWidgetItem(d["CATEGORIA"]))
            self.twgdatos.setItem(indicefila,3,QtWidgets.QTableWidgetItem(d["OCUPACION"]))
            self.twgdatos.setItem(indicefila,4,QtWidgets.QTableWidgetItem(d["SUELDO"]))
            self.twgdatos.setItem(indicefila,5,QtWidgets.QTableWidgetItem(d["DESCUENTO1"]))
            self.twgdatos.setItem(indicefila,6,QtWidgets.QTableWidgetItem(d["DESCUENTO2"]))
            self.twgdatos.setItem(indicefila,7,QtWidgets.QTableWidgetItem(d["BONIFICACION1"]))
            self.twgdatos.setItem(indicefila,8,QtWidgets.QTableWidgetItem(d["BONIFICACION2"]))
            indicefila+=1
        operaciones.listadatos.clear()
    
    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_2=Ejercicio02()
    ventana_2.show()
    sys.exit(app.exec())