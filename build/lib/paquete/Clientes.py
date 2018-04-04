import gi,re,time
import sqlite3 as dbapi
from paquete import Proyecto
from paquete import informes
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk

#dialog
class DialogExample(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Warning", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label("¿Estas seguro de que quieres eliminar a este cliente?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()



#main class
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clientes")
        Gtk.Window.set_resizable(self, False)
        self.set_default_size(900, 650)
        self.bbdd = dbapi.connect("Clinica.dat")
        self.cursor = self.bbdd.cursor()
        self.dato1=""
        self.dato2=""
        self.dato3=""
        self.dato4=""
        self.dato5=""
        self.dato6=""

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)


        modelo = Gtk.ListStore(str, str, str, str, int, str)#modelo de datos

        self.cursor.execute("select * from clientes")

        for x in self.cursor.fetchall():#muestra datos de las columnas
            modelo.append([x[0], x[1], x[2], x[3], x[4], x[5]])#añade al modelo los datos de los clientes
        vista = Gtk.TreeView(model=modelo, margin_top=10)
        columnas = ["Nombre", "Apellido", "Dni", "Direccion", "Telefono", "FechaNacimiento"]
        for i in range(len(columnas)):#durante la longitud de la lista crea las columnas
            #espacion entre celdas
            celda = Gtk.CellRendererText(xpad=30)
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)

        #establecemos barra lateral de scroll
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy( Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(vista)#añadimos barra lateral al treview
        scrolled_window.set_min_content_height(250)#establecemos ventana para el treeview

        caja.add(scrolled_window)

                ###################################Vista de cliente#################################################
        caja4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_left=150)

        caja5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=160)
        etiqueta1 = Gtk.Label(margin_right=180)
        etiqueta1.set_markup("<i><b>Nombre</b></i>")
        etiqueta2 = Gtk.Label()
        etiqueta2.set_markup("<i><b>Apellido</b></i>")
        caja5.add(etiqueta1)
        caja5.add(etiqueta2)
        caja4.add(caja5)

        caja6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada1 = Gtk.Entry(margin_left=100, margin_right=20)

        entrada2 = Gtk.Entry(margin_left=40)

        caja6.add(entrada1)
        caja6.add(entrada2)

        caja4.add(caja6)

        caja7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=170)
        etiqueta3 = Gtk.Label(margin_right=195)
        etiqueta3.set_markup("<i><b>Dni</b></i>")
        etiqueta4 = Gtk.Label()
        etiqueta4.set_markup("<i><b>Dirección</b></i>")
        caja7.add(etiqueta3)
        caja7.add(etiqueta4)
        caja4.add(caja7)

        caja8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada3 = Gtk.Entry(margin_left=100, margin_right=20)

        entrada4 = Gtk.Entry(margin_left=40)

        caja8.add(entrada3)
        caja8.add(entrada4)

        caja4.add(caja8)



        caja9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_left=160)
        etiqueta5 = Gtk.Label(margin_right=150)
        etiqueta5.set_markup("<i><b>Teléfono</b></i>")
        etiqueta6 = Gtk.Label()
        etiqueta6.set_markup("<i><b>Fecha de nacimiento</b></i>")


        caja9.add(etiqueta5)
        caja9.add(etiqueta6)

        caja4.add(caja9)

        caja10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20)

        entrada5 = Gtk.Entry(margin_left=100, margin_right=20)

        entrada6 = Gtk.Entry(margin_left=40)

        caja10.add(entrada5)

        caja10.add(entrada6)

        caja4.add(caja10)


        caja11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin_top=50, margin_left=225)

        boton1 = Gtk.Button("Enviar", margin_right=20)
        boton1.modify_fg(Gtk.StateFlags.NORMAL,Gdk.color_parse('green'))


        boton1.connect("clicked", self.on_boton_Clicked, entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, "Enviar")  # enviamos todos los datos

        #recordar enviar datos en la misma posicion que en la funcion


        boton2 = Gtk.Button("Volver")
        boton2.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('blue'))

        boton2.connect("clicked", self.on_boton_Clicked, entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, "Volver")


        botonInforme = Gtk.Button("Informe",margin_left=270)
        botonInforme.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('orange'))

        botonInforme.connect("clicked", self.on_boton_Clicked,entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, "informe")

        caja11.add(boton1)
        caja11.add(boton2)
        caja11.add(botonInforme)

        caja4.add(caja11)

                ####################################borrado de cliente######################################

        grid = Gtk.Grid(margin_left=270)

        etiqueta = Gtk.Label( margin_top=50, margin_left=110)
        etiqueta.set_markup("<i><b>Inserta el dni del cliente a eliminar</b></i>")

        entrada = Gtk.Entry()

        caja12 = Gtk.Box(margin_top=30, margin_left=120)
        caja12.add(entrada)

        botonEliminar = Gtk.Button("Eliminar")
        botonEliminar.modify_fg(Gtk.StateFlags.NORMAL,Gdk.color_parse('red'))
        botonVolver = Gtk.Button("Volver")
        botonVolver.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('blue'))


        botonVolver.connect("clicked", self.on_click, entrada, "volver")

        botonEliminar.connect("clicked", self.on_click,entrada,"eliminar")


        caja13 = Gtk.Box(margin_left=130, margin_top=30,spacing=10)
        caja13.add(botonEliminar)
        caja13.add(botonVolver)


        grid.add(etiqueta)
        grid.attach(caja12, 0, 1, 1, 1)  # con atach asignamos las posicion en el grid
        grid.attach(caja13, 0, 2, 1, 1)



        caja_stack = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # switcher
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        stack.add_titled(caja4, "inserta", "Insertar Cliente")

        stack.add_titled(grid, "check", "Borrar cliente")

        stack_switcher = Gtk.StackSwitcher(margin_left=350)
        stack_switcher.set_stack(stack)
        caja_stack.pack_start(stack_switcher, True, True, 0)
        caja_stack.pack_start(stack, True, True, 0)

        caja.add(caja_stack)


        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()


    def match_Nombre_apellido(self,entryNom, entryApe):
        cadena = entryNom
        cadena2 = entryApe
        pattern = re.compile('[A-Za-z]+')

        if pattern.match(cadena) == None or pattern.match(cadena2) == None :

            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Nombre o apellido incorrecto")
            dialog.format_secondary_text(
                "No estan permitidos numeros")
            dialog.run()
            dialog.destroy()
            #forzamos error para que no inserte en la base de datos
            self.dato5 = ""
        



    def match_dni(self, entryDni):
        cadena = entryDni
        pattern = re.compile('[0-9]{8}[A-ZÑ]')

        if pattern.match(cadena) == None:

            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Formato dni incorrecto")
            dialog.format_secondary_text(
                "Dni debe ser ej: 17690989L ")
            dialog.run()
            dialog.destroy()
            self.dato5 = ""




    def match_address(self, entryAddress):
        cadena = entryAddress
        #nombre de calle con número exterior y un número interior opcional
        pattern = re.compile('[a-zA-Z1-9À-ÖØ-öø-ÿ]+\.?(( |\-)[a-zA-Z1-9À-ÖØ-öø-ÿ]+\.?)* (((#|[nN][oO]\.?) ?)?\d{1,4}(( ?[a-zA-Z0-9\-]+)+)?)')

        if pattern.match(cadena) == None:

            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Direccion incorrecta")
            dialog.format_secondary_text(
                "Formato direccion numero")
            dialog.run()
            dialog.destroy()
            self.dato5=""




    def match_phone(self, entryPhone):
        cadena = entryPhone
        pattern = re.compile('^[679][0-9]{8}')

        if pattern.match(cadena) == None:

            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Telefono incorrecto")
            dialog.format_secondary_text(
                "El telefono debe empezar por 6|7|9 y debe contener 9 digitos")
            dialog.run()
            dialog.destroy()
            self.dato5=""



    def match_birthdate(self, entryPhone):
        cadena = entryPhone
        pattern = re.compile('^([0][1-9]|[12][0-9]|3[01])(/)([0][1-9]|[1][0-2])(/)(\d{4})$')

        lista=cadena.split('/')

        if pattern.match(cadena) == None or int(lista[2]) <= 1898 or int(lista[2]) > int(time.strftime('%Y')):#año obtenido por el sistema
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK, "Edad incorrecta")
            dialog.format_secondary_text(
                "El formato fecha debe ser dd/mm/yy")
            dialog.run()
            dialog.destroy()
            self.dato5=""





    def on_boton_Clicked(self, boton,entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, opcion):  # recibimos datos en la posicion exacta que los enviamos
        # para recoger el texto debemos usar el get text con la llamada de una funcion como el boton click
      try:
         self.dato1 = entrada1.get_text()
         self.dato2 = entrada2.get_text()
         self.dato3 = entrada3.get_text()
         self.dato4 = entrada4.get_text()
         self.dato5 = entrada5.get_text()
         self.dato6 = entrada6.get_text()


         if opcion == "Enviar":
             # check fields

            self.match_phone(self.dato5)

            self.match_Nombre_apellido(self.dato1,self.dato2)

            self.match_dni(self.dato3)

            self.match_address(self.dato4)

            self.match_birthdate(self.dato6)


             # otra forma cursor.execute("insert into clientes VALUES('%s', '%s', '%s', '%s' , '%s')" %(dato1, dato2,dato3,dato4,dato5,dato6))

            self.cursor.execute("insert into clientes values("+"'" + self.dato1 + "'"+","+ "'" + self.dato2 + "'"+","+ "'" + self.dato3 +
                           "'"+","+ "'" + self.dato4 + "'"+","+ self.dato5+","+ "'" + self.dato6 +"'"+")")


            self.bbdd.commit()
            self.bbdd.close()
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Datos guardados correctamente")
            dialog.run()
            dialog.destroy()

         #actualizamos la vista
            self.destroy()
            FiestraPrincipal()

         elif opcion == "Volver":
            fiestra = Proyecto.FiestraPrincipal()
            fiestra.show_all()
            self.hide()

         elif opcion == "informe":
            informes.generaClientes()
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Informe Generado")
            dialog.run()
            dialog.destroy()

      except dbapi.IntegrityError:
          dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "DNI Duplicado")
          dialog.format_secondary_text("Ya existe una persona con ese Dni")
          dialog.run()
          dialog.destroy()


    def on_click(self, boton, entrada, etiqueta):
        if etiqueta == "eliminar":

            dni = entrada.get_text()

            pattern = re.compile('[0-9]{8}[A-ZÑ]')

            #check dni
            if pattern.match(dni) == None:

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Formato dni incorrecto")
                dialog.format_secondary_text("Dni debe ser ej: 17690989L ")
                dialog.run()
                dialog.destroy()

            else:
                dialog = DialogExample(self)
                response = dialog.run()

                if response == Gtk.ResponseType.OK:
                    self.cursor.execute("delete from clientes where dni=" + "'" + dni + "'")
                    self.bbdd.commit()
                    self.bbdd.close()
                    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente eliminado")
                    dialog.run()
                    dialog.destroy()
                    self.destroy()
                    FiestraPrincipal()

                elif response == Gtk.ResponseType.CANCEL:
                    dialog.destroy()




        elif etiqueta == "volver":
            fiestra = Proyecto.FiestraPrincipal()
            fiestra.show_all()
            self.hide()


