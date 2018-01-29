import gi
import sqlite3 as dbapi
import Proyecto
import insertarClientes
import borrar_con_grid
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clientes")
        self.set_default_size(400, 400)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)

        try:#nos conectamos a la base de datos
            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()

        except dbapi.OperationalError as e:
            print("problema " + str(e))
        modelo = Gtk.ListStore(str, str, str, str, int, str)#modelo de datos
        columnas = ["Nombre", "Apellido", "Dni", "Direccion", "Telefono", "FechaNacimiento"]

        vista = Gtk.TreeView(model=modelo,margin_top=20)
        for x in cursor.execute("select * from clientes"):#muestra datos de las columnas
            modelo.append([x[0], x[1], x[2], x[3], x[4], x[5]])#añade al modelo los datos de los clientes
        for i in range(len(columnas)):#durante la longitud de la lista crea las columnas
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)
        #establecemos barra lateral de scroll
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy( Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(vista)#añadimos barra lateral al treview
        scrolled_window.set_min_content_height(250)#establecemos ventana para el treeview

        caja.add(scrolled_window)



#caja botones
        caja2 = Gtk.Box(spacing=70,margin_top=20,margin_left=100,margin_right=10)
        boton = Gtk.Button("Insertar cliente")
        boton.connect("clicked", self.on_boton_Clicked, "Insertar")#enviamos ls operaciones a la funcion
        caja2.add(boton)
        boton = Gtk.Button("Borrar cliente")
        boton.connect("clicked", self.on_boton_Clicked, "Borrar")
        caja2.add(boton)
        caja.add(caja2)
#caja boton volver
        caja3=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,margin_left=215,margin_top=5)
        boton=Gtk.Button("Volver")
        boton.connect("clicked", self.on_boton_Clicked, "Volver")
        caja3.add(boton)
        caja.add(caja3)


        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def on_boton_Clicked(self, boton, operacion):
        try:
            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()
        except dbapi.OperationalError as e:
            print("problema " + str(e))  # visualizar error

        if operacion == "Insertar":
            fiestra =insertarClientes.FiestraPrincipal()
            fiestra.show_all()
            self.hide()
        elif operacion == "Borrar":
            borrar_con_grid.GridWindow()

            self.hide()

        elif operacion == "Volver":
            fiestra = Proyecto.FiestraPrincipal()
            fiestra.show_all()
            self.hide()



