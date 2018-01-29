import gi
import sqlite3 as dbapi

import Clientes

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(600, 400)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        caja1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=160)
        etiqueta1 = Gtk.Label("Nombre", margin_right=180)
        etiqueta2 = Gtk.Label("Apellidos")
        caja1.add(etiqueta1)
        caja1.add(etiqueta2)
        caja.add(caja1)

        caja2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada1 = Gtk.Entry(margin_left=100, margin_right=20)

        entrada2 = Gtk.Entry(margin_left=40)

        caja2.add(entrada1)
        caja2.add(entrada2)

        caja.add(caja2)

        caja3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=170)
        etiqueta1 = Gtk.Label("Dni", margin_right=195)
        etiqueta2 = Gtk.Label("Dirección")
        caja3.add(etiqueta1)
        caja3.add(etiqueta2)
        caja.add(caja3)

        caja4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada3 = Gtk.Entry(margin_left=100, margin_right=20)


        entrada4 = Gtk.Entry(margin_left=40)

        caja4.add(entrada3)
        caja4.add(entrada4)

        caja.add(caja4)

        #

        caja5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=160)
        etiqueta1 = Gtk.Label("Teléfono", margin_right=150)
        etiqueta2 = Gtk.Label("Fecha de nacimiento")
        caja5.add(etiqueta1)
        caja5.add(etiqueta2)

        caja.add(caja5)

        caja6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada5 = Gtk.Entry(margin_left=100, margin_right=20)


        entrada6 = Gtk.Entry(margin_left=40)


        caja6.add(entrada5)

        caja6.add(entrada6)

        caja.add(caja6)

        caja7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=50, margin_left=225)

        boton1 = Gtk.Button("Enviar", margin_right=20)

        boton1.connect("clicked", self.on_boton_Clicked, entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, "Enviar")  # enviamos todos los datos

        #recordar enviar datos en la misma posicion que en la funcion


        boton2 = Gtk.Button("Volver")

        boton2.connect("clicked", self.on_boton_Clicked, entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, "Volver")

        caja7.add(boton1)
        caja7.add(boton2)

        caja.add(caja7)

        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def on_boton_Clicked(self, boton,entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, opcion):  # recibimos datos en la posicion exacta que los enviamos
        # para recoger el texto debemos usar el get text con la llamada de una funcion como el boton click
        dato1 = entrada1.get_text()
        dato2 = entrada2.get_text()
        dato3 = entrada3.get_text()
        dato4 = entrada4.get_text()
        dato5 = entrada5.get_text()
        dato6 = entrada6.get_text()


        if opcion == "Enviar":
            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()
            cursor.execute("insert into clientes values("+"'" + dato1 + "'"+","+ "'" + dato2 + "'"+","+ "'" + dato3 +
                           "'"+","+ "'" + dato4 + "'"+","+ dato5+","+ "'" + dato6 +"'"+")")
            bbdd.commit()
            bbdd.close()

            messagedialog = Gtk.MessageDialog(parent=self,
                                              flags=Gtk.DialogFlags.MODAL,
                                              type=Gtk.MessageType.WARNING,
                                              buttons=Gtk.ButtonsType.CLOSE,
                                              message_format="Datos guardados")
            messagedialog.show()

            messagedialog.connect("response", lambda *a: messagedialog.destroy())#cierra la ventana emergente

        elif opcion == "Volver":
            Clientes.FiestraPrincipal()#llama a la ventana principal

            self.hide()


