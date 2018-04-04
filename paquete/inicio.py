import gi
import sqlite3 as dbapi
from paquete import Proyecto

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Clinigalia')
        Gtk.Window.set_resizable(self, False)
        # Un contenedor que superpone widgets uno encima del otro
        self.overlay = Gtk.Overlay()
        self.add(self.overlay)
        self.background = Gtk.Image.new_from_file('clinica.jpg')
        self.overlay.add(self.background)
        self.grid = Gtk.Grid()
        self.overlay.add_overlay(self.grid)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_top=70,margin_left=130)

        nomeEmp = Gtk.Label()
        nomeEmp.set_markup("<i><b>Usuario</b></i>")
        entrada = Gtk.Entry(margin_top=10)

        caja.add(nomeEmp)
        caja.add(entrada)

        caja2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_left=130,margin_top=65)

        contra = Gtk.Label()
        contra.set_markup("<i><b>Contraseña</b></i>")
        entrada2 = Gtk.Entry(margin_top=10)
        entrada2.set_visibility(False)  # ocultar campos

        caja2.add(contra)
        caja2.add(entrada2)

        caja3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_left=170,margin_top=65,margin_right=40)

        login = Gtk.Button("Login")

        # en el boton logueo enviamos las variables
        login.connect("clicked", self.on_boton_Clicked, entrada, entrada2)
        login.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('green'))

        # conectando evento clicked al boton debemos pasar los dos get text

        caja3.add(login)

        self.grid.add(caja)

        self.grid.attach(caja2, 0, 1, 1, 1)#tras el primer elemento

        self.grid.attach(caja3, 0, 2, 1, 1)#tras el segundo elemento

        self.set_position(Gtk.WindowPosition.CENTER)  # centrar ventana
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()



    def on_boton_Clicked(self, boton, entrada, entrada2):
            # pasamos get tex en la funcion del click
            usuario = entrada.get_text()
            contraseña = entrada2.get_text()
            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()
            try:
                validar = cursor.execute(
                "select usuario from inicio where usuario =""'" + usuario + "'" + "and contraseña=""'" + contraseña + "'")


                consultaUser = (str(validar.fetchone()[0]))  # sacamos la tupla del fetchone y lo pasamos a string para poder comparar


                if consultaUser == usuario:
                 print("Conectado")
                 fiestra = Proyecto.FiestraPrincipal()
                 fiestra.show_all()
                 self.hide()



                #podemos llamar a otra ventana importando la ventana que queremos y llamando a la clase que contiene la vista
                #Clientes.FiestraPrincipal()  # llama a la ventana principal


            except :
                print("error usuario o contraseña")


#indicamos la main
if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()
    Gtk.main_quit()

