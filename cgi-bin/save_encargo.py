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

descripcion = form.getvalue('descripcion')
kilos = form.getvalue('kilos-solicitados')
espacio = form.getvalue('espacio-solicitado')
pais_origen = form.getvalue('pais-origen')
ciudad_origen = form.getvalue('ciudad-origen')
pais_destino = form.getvalue('pais-destino')
ciudad_destino = form.getvalue('ciudad-destino')
foto1 = form['foto-encargo-1']
foto2 = form['foto-encargo-2']
foto3 = form['foto-encargo-3']
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

largo_descripcion = len(descripcion)
largo_email = len(email)
largo_celular = len(celular)
tipos_soportados = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
MAX_FILE_SIZE= 350000
size = 0

if (largo_descripcion == 0):
    errores += '<p>Debe ingresar una descripcion</p>'
elif(largo_descripcion>250):
    errores += '<p>Descripcion muy larga</p>'

if (espacio == '0'):
    errores += '<p>Debe ingresar una cantidad de espacio a solicitar</p>'

if (kilos == '0'):
    errores += '<p>Debe ingresar una cantidad de kilos a solicitar</p>'

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

if(not foto1.filename):
    errores += '<p>Debe subir como mínimo 1 imagen de su encargo en la primera casilla</p>'
elif(foto1.type not in tipos_soportados):
    errores += '<p>Debe subir la 1ra imagen con formato válido (jpeg, jpg, png o webp)</p>'
else:
    size += os.fstat(foto1.file.fileno()).st_size
if(foto2.filename):
    tipo_foto2 = foto2.type
    size += os.fstat(foto2.file.fileno()).st_size
    if(tipo_foto2 not in tipos_soportados):
        errores += '<p>Debe subir la 2da imagen con formato válido (jpeg, jpg, png, o webp)</p>'
if(foto3.filename):
    tipo_foto3 = foto3.type
    size += os.fstat(foto3.file.fileno()).st_size
    if(tipo_foto3 not in tipos_soportados):
        errores += '<p>Debe subir la 3ra imagen con formato válido (jpeg, jpg, png o webp)</p>'
if(size>MAX_FILE_SIZE):
    errores += '<p>El peso total de los archivos es muy grande, pruebe subiendo archivos de menor tamaño</p>'

regex_email = "^\\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
if (largo_email == 0):
    errores += '<p>Debe ingresar un email</p>'
elif(not re.match(regex_email, email)):
    errores += '<p>Dirección de email inválido</p>'

regex_celular =  "^(\+\d{1,3}( )?)?((\(\d{1,3}\))|\d{1,3})[- .]?\d{3,4}[- .]?\d{4}$"
if (largo_celular>=1 and (not re.match(regex_celular, celular))):
    errores += '<p>Número de celular incorrecto</p>'


if errores == '':
    data = (descripcion, int(espacio), int(kilos), int(ciudad_origen), int(ciudad_destino), email, celular, foto1)
    if(foto2.filename):
        data = (descripcion, int(espacio), int(kilos), int(ciudad_origen), int(ciudad_destino), email, celular, foto1, foto2)
    if(foto3.filename):
        data = (descripcion, int(espacio), int(kilos), int(ciudad_origen), int(ciudad_destino), email, celular, foto1, foto2, foto3)
    db.save_encargo(data)
    mensaje = '''
        <section class="jumbotron text-center">
            <div class="container">
                <br><br>
                <h2 class="jumbotron-heading bg-success text-center text-uppercase text-white">
                    <br><b>¡Su encargo fue añadido con éxito!</b><br><br>
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
    with open('../templates/agregar-encargo.html','r', encoding="utf-8") as template:
        file = template.read()
        print(file.format('Error validación datos', errores, paises, ciudades, paises, ciudades), file=utf8stdout)

