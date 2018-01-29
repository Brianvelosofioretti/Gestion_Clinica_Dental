import gi
import sqlite3 as dbapi
import Proyecto
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Servicios")
        self.set_default_size(400, 400)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        try:#nos conectamos a la base de datos
            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()

        except dbapi.OperationalError as e:
            print("problema " + str(e))

        modelo = Gtk.ListStore(str, str)#modelo de datos
        columnas = ["Servicio", "Precio"]

        vista = Gtk.TreeView(model=modelo,margin_top=10)#añadimos el model de datos al treeview
        for x in cursor.execute("select * from servicios"):#muestra datos de las columnas
            modelo.append([x[0], x[1]])#añade al modelo los datos de los clientes
        for i in range(len(columnas)):#durante la longitud de la lista crea las columnas
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)#mostramos por cada columna las celdas y en cada celsa su informacion
            vista.append_column(columna)
#scroll
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(
            Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(vista)
        scrolled_window.set_min_content_height(300)

        caja.add(scrolled_window)



#caja boton volver
        caja3=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,margin_left=160,margin_top=30)
        boton=Gtk.Button("Volver")
        boton.connect("clicked", self.on_boton_Clicked, "Volver")
        caja3.add(boton)
        caja.add(caja3)

        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def on_boton_Clicked(self, boton, operacion):

        if operacion == "Volver":

            fiestra = Proyecto.FiestraPrincipal()
            fiestra.show_all()
            self.hide()
