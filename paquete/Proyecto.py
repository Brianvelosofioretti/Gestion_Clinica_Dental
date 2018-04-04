
from paquete import servicios, Clientes
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        Gtk.Window.set_resizable(self, False)
        self.set_default_size(600, 400)
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50,margin_left=100,margin_right=100,margin_top=30)


        label1 = Gtk.Label()
        label1.set_markup("<i><b>Clinigalia</b></i>")

        caja.add(label1)
        boton1 = Gtk.Button("Consultar clientes")

        boton1.connect("clicked", self.on_boton_cliked, "clientes")

        caja.pack_start(boton1, False,True,0)
        boton2 = Gtk.Button("Servicios/Precios")
        boton2.connect("clicked", self.on_boton_cliked, "servicios")
        caja.add(boton2)

        boton3 = Gtk.Button("Salir")
        boton3.connect("clicked", self.on_boton_cliked, "salir")
        caja.add(boton3)

        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def on_boton_cliked(self, boton, pestaña):
        if pestaña == "clientes":
            fiestra = Clientes.FiestraPrincipal()
            fiestra.show_all()
            self.hide()
        elif pestaña == "servicios":
            fiestra = servicios.FiestraPrincipal()
            fiestra.show_all()
            self.hide()
        elif pestaña == "salir":
            Gtk.main_quit()







