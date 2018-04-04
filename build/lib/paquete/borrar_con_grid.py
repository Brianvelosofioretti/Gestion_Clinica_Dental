import gi
import sqlite3 as dbapi
from paquete import Clientes

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="elimina cliente")
        self.set_default_size(400,300)

        grid = Gtk.Grid()

        etiqueta = Gtk.Label("Inserta el dni del cliente a eliminar", margin_top=50,margin_left=110)

        entrada = Gtk.Entry()

        caja=Gtk.Box(margin_top=30,margin_left=120)
        caja.add(entrada)

        botonEliminar = Gtk.Button("Eliminar",margin_right=20)

        botonEliminar.connect("clicked", self.on_click, entrada, "eliminar")

        botonVolver = Gtk.Button("Volver")
        botonVolver.connect("clicked", self.on_click, entrada, "volver")

        caja1=Gtk.Box(margin_left=120, margin_top=30)
        caja1.add(botonEliminar)
        caja1.add(botonVolver)


        grid.add(etiqueta)
        grid.attach(caja, 0, 1, 1, 1)#con atach asignamos las posicion en el grid
        grid.attach(caja1, 0, 2, 1, 1)
        #grid.attach(caja2, 1, 2, 1, 1)

        #grid.attach_next_to(caja2,caja1 ,Gtk.PositionType.LEFT,1, 2)#pon el boton volver al lado de boton eliminar

        self.add(grid)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def on_click(self, boton, entrada, etiqueta):
            dni = entrada.get_text()

            if etiqueta == "eliminar":
                bbdd = dbapi.connect("Clinica.dat")
                cursor = bbdd.cursor()
                cursor.execute("delete from clientes where dni=" + "'" + dni+"'")
                bbdd.commit()
                bbdd.close()
                print("Cliente eliminado correctamente")

            elif etiqueta == "volver":
                fiestra = Clientes.FiestraPrincipal()
                fiestra.show_all()
                self.hide()

