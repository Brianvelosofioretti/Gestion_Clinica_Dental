
from reportlab.graphics.shapes import Image,Drawing

import gi
import sqlite3 as dbapi
gi.require_version('Gtk', '3.0')
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors



def generaClientes():
        """Xeramos o informe dos Clientes usando as librerias de reportlab

           Crease unha lista 'paxina' a que lle engadiremos os elementos seguintes:

           imaxe2 -- engadimos unha imaxe cos parametros(desplazamentoX,desplazamentoY,ancho,alto)

           debuxo2 -- indicaremos a posicion na que situaremos a imaxe cos parametros (ancho,alto)

           debuxo2.add(imaxe2) -- engade a imaxe ao noso debuxo

           paxina.append(debuxo2) -- engade o debuxo a nosa paxina
           -------------------------------------------------------------------------------------------
           A continuación crearemos a conexion a nosa base de datos:

           bbdd = dbapi.connect("Clinica.dat") -- conecta a base de datos "Clinica.dat"

           cursor = bbdd.cursor() -- creamos un cursor para executar ordes sobre as taboas
           -------------------------------------------------------------------------------------------
           Pasamos a xerar a tabla no noso informe:

           columnas -- Creamos as columnas da nosa taboa

           cursor.execute -- executa a operacion sql deseada

           taboa -- creamos unha taboa a que lle pasamos as columnas e o resultado da nosa consulta

           taboa.setStyle -- define o estilo da nosa taboa

           paxina.append(taboa) -- engade a taboa a nosa paxina
           --------------------------------------------------------------------------------------------
           Por ultimo xeramos o documento pdf para iso debemos realizar o seguinte:

           *SimpleDocTemplate -- ao que lle pasamos(nome do pdf a xerar,formato da paxina,e borde)

           *debemos pasarlle unha referencia

            doc.build(paxina) -- Xera o informe coa configuracion anterior

        """
        try:
            paxina = []

            imaxe2 = Image(80, 50, 280, 150, "logo.png")  # x lateral y horizontal ancho y alto
            debuxo2 = Drawing(300, 200)
            debuxo2.add(imaxe2)
            paxina.append(debuxo2)  # añadimos dibujo a la lista

            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()

            columnas = [["Nombre", "Apellido", "Dni", "Direccion", "Telefono", "FechaNacimiento"]]

            cursor.execute("select * from clientes")
            taboa = Table(columnas + cursor.fetchall())  # recupera los datos
            #parametros style de x a x y de y a y
            taboa.setStyle(
                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                 ("BACKGROUND", (0, 0), (-1, -1), colors.lightcyan), ("BACKGROUND", (0, 0), (5, 0), colors.lightgreen)])

            paxina.append(taboa)

            doc = SimpleDocTemplate("informeClientes.pdf", pagesize=A4, showBoundary=1)  # boundary linea a4
            doc.build(paxina)


        except dbapi.OperationalError as e:
            print("problema " + str(e))


def generaServicios():
        """Xeramos o informe dos Servizos usando as librerias de reportlab

            Crease unha lista 'paxina' a que lle engadiremos os elementos seguintes:

            imaxe -- engadimos unha imaxe cos parametros(desplazamentoX,desplazamentoY,ancho,alto)

            debuxo -- indicaremos a posicion na que situaremos a imaxe cos parametros (ancho,alto)

            debuxo.add(imaxe) -- engade a imaxe ao noso debuxo

            paxina.append(debuxo) -- engade o debuxo a nosa paxina
            -------------------------------------------------------------------------------------------
            A continuación crearemos a conexion a nosa base de datos:

            bbdd = dbapi.connect("Clinica.dat") -- conecta a base de datos "Clinica.dat"

            cursor = bbdd.cursor() -- creamos un cursor para executar ordes sobre as taboas
            -------------------------------------------------------------------------------------------
            Pasamos a xerar a tabla no noso informe:

            columnas -- Creamos as columnas da nosa taboa

            cursor.execute -- executa a operacion sql deseada

            taboa -- creamos unha taboa a que lle pasamos as columnas e o resultado da nosa consulta

            taboa.setStyle -- define o estilo da nosa taboa

            paxina.append(taboa) -- engade a taboa a nosa paxina
            --------------------------------------------------------------------------------------------
            Por ultimo xeramos o documento pdf para iso debemos realizar o seguinte:

            *SimpleDocTemplate -- ao que lle pasamos(nome do pdf a xerar,formato da paxina,e borde)

            *debemos pasarlle unha referencia

             doc.build(paxina) -- Xera o informe coa configuracion anterior

         """
        try:
            paxina = []

            imaxe = Image(80, 50, 280, 150, "logo.png")  # x lateral y horizontal ancho y alto
            debuxo = Drawing(300, 200)
            debuxo.add(imaxe)
            paxina.append(debuxo)  # añadimos dibujo a la lista

            bbdd = dbapi.connect("Clinica.dat")
            cursor = bbdd.cursor()

            columnas = [["Servicio", "Precio"]]

            cursor.execute("select * from servicios")
            taboa = Table(columnas + cursor.fetchall())  # recupera los datos

            taboa.setStyle(
                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                 ("BACKGROUND", (0, 0), (-1, -1), colors.lightcyan), ("BACKGROUND", (0, 0), (5, 0), colors.lightgreen),
                 ])

            paxina.append(taboa)

            doc = SimpleDocTemplate("informeServicio.pdf", pagesize=A4, showBoundary=1)  # boundary linea a4
            doc.build(paxina)


        except dbapi.OperationalError as e:
            print("problema " + str(e))
