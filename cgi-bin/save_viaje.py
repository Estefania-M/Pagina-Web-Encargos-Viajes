#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import os
import sys
import re
from datetime import datetime

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

db = DB('localhost', 'cc500241_u', 'lesPertjcu', 'cc500241_db')
form = cgi.FieldStorage()

pais_origen = form.getvalue('pais-origen')
ciudad_origen = form.getvalue('ciudad-origen')
pais_destino = form.getvalue('pais-destino')
ciudad_destino = form.getvalue('ciudad-destino')
fecha_ida = form.getvalue('fecha-ida')
fecha_regreso = form.getvalue('fecha-regreso')
kilos = form.getvalue('kilos-disponibles')
espacio = form.getvalue('espacio-disponible')
email = form.getvalue('email')
celular = form.getvalue('celular')


data1 = db.get_pais()
data2 = db.get_ciudad()

paises = ''
paises += "<option value='0' selected>Seleccione ...</option>"
for p in data1:
    paises+=f"""
        <option value={p[0]}>{p[1]}</option>
        """

ciudades = ''
ciudades += "<option value='0' selected>Seleccione ...</option>"
for p in data2:
    ciudades+=f"""
        <option value={p[0]}>{p[1]}</option>
        """


# Validar campos
errores = ''

largo_FI = len(fecha_ida)
largo_FR = len(fecha_regreso)
largo_email = len(email)
largo_celular = len(celular)

if (pais_origen == '0'):
    errores += '<p>Debe ingresar un pais de origen</p>'

if (ciudad_origen == '0'):
    errores += '<p>Debe ingresar una ciudad de origen</p>'

if (pais_destino == '0'):
    errores += '<p>Debe ingresar un pais de destino</p>'
elif (pais_origen == pais_destino):
    errores += '<p>Debe ingresar un pais de destino diferente al de origen</p>'

if (ciudad_destino == '0'):
    errores += '<p>Debe ingresar una ciudad de destino</p>'

regex_fecha = "^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
if (largo_FI == 0):
    errores += '<p>Debe ingresar una fecha de ida</p>'
elif (not re.match(regex_fecha, fecha_ida)):
    errores += '<p>Formato de fecha de ida incorrecta</p>'
    
if (largo_FR == 0):
    errores += '<p>Debe ingresar una fecha de regreso</p>'
elif (not re.match(regex_fecha, fecha_regreso)):
    errores += '<p>Formato de fecha de regreso incorrecta</p>'
elif(fecha_ida>fecha_regreso):
    errores += '<p>Fecha de regreso debe ser posterior a la fecha de ida</p>'


if (kilos == '0'):
    errores += '<p>Debe ingresar una cantidad de kilos disponibles</p>'

if (espacio == '0'):
    errores += '<p>Debe ingresar una cantidad de espacio disponible</p>'


regex_email = "^\\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
if (largo_email == 0):
    errores += '<p>Debe ingresar un email</p>'
elif(not re.match(regex_email, email)):
    errores += '<p>Dirección de email inválido</p>'

regex_celular =  "^(\+\d{1,3}( )?)?((\(\d{1,3}\))|\d{1,3})[- .]?\d{3,4}[- .]?\d{4}$"
if (largo_celular>=1 and (not re.match(regex_celular, celular))):
    errores += '<p>Número de celular incorrecto</p>'


if errores == '':
    data = (int(ciudad_origen), int(ciudad_destino), fecha_ida, fecha_regreso, int(kilos), int(espacio), email, celular)
    db.save_viaje(data)
    mensaje = '''
        <section class="jumbotron text-center">
            <div class="container">
                <br><br>
                <h2 class="jumbotron-heading bg-success text-center text-uppercase text-white">
                    <br><b>¡Su viaje fue añadido con éxito!</b><br><br>
                </h2>
                <br><br><br>
                <h1 class="jumbotron-heading"> <br><b>☼ PLANIFICA AQUÍ TUS <a href="../cgi-bin/agregar-viaje.py">VIAJES</a> Y <a href="../cgi-bin/agregar-encargo.py">ENCARGOS</a> ☼</b><br> <br></h1>
            </div>
        </section>
    '''
    with open('../templates/template.html','r', encoding="utf-8") as template:
        file = template.read()
        print(file.format('Añadido con éxito','class="active"','','','','', mensaje), file=utf8stdout)

else:
    with open('../templates/agregar-viaje.html','r', encoding="utf-8") as template:
        file = template.read()
        print(file.format('Error validación datos', errores, paises, ciudades, paises, ciudades), file=utf8stdout)

