#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

db = DB('localhost', 'cc500241_u', 'lesPertjcu', 'cc500241_db')
args = cgi.FieldStorage()
id = args.getvalue('id')
data = db.get1Viaje(int(id))
ciudadO = db.getNCiudad(data[0][1])
paisO = db.getNPais(ciudadO[0][1])
ciudadD = db.getNCiudad(data[0][2])
paisD = db.getNPais(ciudadD[0][1])
kilos = db.getKilos(data[0][5])
espacio = db.getEspacio(data[0][6])
info = """
  <div class="info">
    <div class="container">
      <br>
      <h1 class="jumbotron-heading"><br>Información del Viaje:</h1>
    </div>
    <div class="container">
      <div class="info-viaje">
        <h4 class="title-section"> Origen</h4>
        <p><b> País: </b>"""+paisO[0][0]+""".<br><b>Ciudad: </b>"""+ciudadO[0][0]+""". </p> 
        <hr>
        <h4 class="title-section"> Destino</h4>
        <p><b> País: </b>"""+paisD[0][0]+""".<br><b>Ciudad: </b>"""+ciudadD[0][0]+""". </p> 
        <hr>
        <h4 class="title-section"> Fechas</h4>
        <p><b> De Ida: </b>"""+str(data[0][3])[:10]+"""<br><b>De Regreso: </b>"""+str(data[0][4])[:10]+""" </p> 
        <hr>
        <h4 class="title-section"> Información del encargo</h4>
        <p><b> Espacio Disponible: </b>"""+espacio[0][0]+"""<br><b>Kilos Disponibles: </b>"""+kilos[0][0]+"""</p> 
        <hr>
        <h4 class="title-section"> Información del pasajero</h4>
        <p><b> Email: </b>"""+data[0][7]+"""<br><b>Teléfono Móvil (Celular): </b>"""+data[0][8]+"""</p> 
        <hr>
      </div>
      <a class="btn btn-info" href="../cgi-bin/ver-viajes.py?id=1">Volver a Viajes</a>
      <br><br>

    </div> 
  </div>
        """

with open('../templates/template.html','r', encoding="utf-8") as template:
    file = template.read()
    print(file.format('Información Viaje','','','','class="active"','', info), file=utf8stdout)