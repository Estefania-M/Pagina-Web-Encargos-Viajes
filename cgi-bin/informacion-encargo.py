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
data = db.get1Encargo(int(id))
ciudadO = db.getNCiudad(data[0][4])
paisO = db.getNPais(ciudadO[0][1])
ciudadD = db.getNCiudad(data[0][5])
paisD = db.getNPais(ciudadD[0][1])
kilos = db.getKilos(data[0][3])
espacio = db.getEspacio(data[0][2])
path = db.getPath(data[0][0])
tamaño = len(path)
imagenes = ''
script = ''
if(tamaño>1):
  imagenes += """<img id="2" class="zoom" src="../media/"""+path[1][0]+"""" alt="2" width="640" height="480"><br><br>"""
  script += """<script>
              var modal = document.getElementById("Modal");
              var img = document.getElementById("2");
              var modalImg = document.getElementById("imagenes");
              img.onclick = function(){
                  modal.style.display = "block";
                  modalImg.src = this.src;
                  }
              var span = document.getElementsByClassName("close")[0];
              span.onclick = function() { 
                  modal.style.display = "none";
              }</script>"""
if(tamaño==3):
  imagenes += """<img id="3" class="zoom" src="../media/"""+path[2][0]+"""" alt="3" width="640" height="480"><br><br>"""
  script += """<script>
              var modal = document.getElementById("Modal");
              var img = document.getElementById("3");
              var modalImg = document.getElementById("imagenes");
              img.onclick = function(){
                  modal.style.display = "block";
                  modalImg.src = this.src;
                  }
              var span = document.getElementsByClassName("close")[0];
              span.onclick = function() { 
                  modal.style.display = "none";
              }</script>"""

info = """
  <div id="Modal" class="modal">
    <span class="close">&times;</span>
    <img src="#" class="modal-content" id="imagenes" alt="imagen de encargo">
  </div>

  <div class="info">
    <div class="container">
      <br>
      <h1 class="jumbotron-heading"><br>Información del Encargo:</h1>
    </div>
    <div class="container">
      <div class="info-encargo">
        <h4 class="title-section"> Origen</h4>
        <p><b> País: </b>"""+paisO[0][0]+""".<br><b>Ciudad: </b>"""+ciudadO[0][0]+""". </p> 
        <hr>
        <h4 class="title-section"> Destino</h4>
        <p><b> País: </b>"""+paisD[0][0]+""".<br><b>Ciudad: </b>"""+ciudadD[0][0]+""". </p> 
        <hr>
        <h4 class="title-section"> Información del encargo</h4>
        <p><b> Descripción: </b>"""+data[0][1]+"""<br>
        <b> Espacio a Solicitar: </b>"""+espacio[0][0]+"""<br><b>Kilos a Solicitar: </b>"""+kilos[0][0]+"""</p> 
        <hr>
        <h4 class="title-section"> Información del solicitante</h4>
        <p><b> Email: </b>"""+data[0][6]+"""<br><b>Teléfono Móvil (Celular): </b>"""+data[0][7]+"""</p> 
        <hr>
        <h4 class="title-section"> Imágenes del Encargo</h4>
        <img id="1" class="zoom" src="../media/"""+path[0][0]+"""" alt="1" width="640" height="480"><br><br>
        """+imagenes+""" 
        <script>
              var modal = document.getElementById("Modal");
              var img = document.getElementById("1");
              var modalImg = document.getElementById("imagenes");
              img.onclick = function(){
                  modal.style.display = "block";
                  modalImg.src = this.src;
                  }
              var span = document.getElementsByClassName("close")[0];
              span.onclick = function() { 
                  modal.style.display = "none";
                  }
        </script>
        """+script+"""
        <hr>
      </div>
      <a class="btn btn-info" href="../cgi-bin/ver-encargos.py?id=1">Volver a Encargos</a>
      <br><br>

    </div> 
  </div>
        """

with open('../templates/template.html','r', encoding="utf-8") as template:
    file = template.read()
    print(file.format('Información Viaje','','','','','class="active"', info), file=utf8stdout)