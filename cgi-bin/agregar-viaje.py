#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb
from codecs import utf_8_decode
from encodings import utf_8;
from db import DB
import sys
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'cc500241_u', 'lesPertjcu', 'cc500241_db')
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


with open('../templates/template.html','r', encoding="utf-8") as template:
    file = template.read()
    print(file.format('Agregar Viajes','','class="active"','','','',
    """
  <div class="info">
    <div class="container">
      <br>
      <h1 class="jumbotron-heading"><br>Rellene los datos para agregar un viaje:</h1>
    </div>

    <div class="container">
      <form id="formulario" action="save_viaje.py" method="POST" enctype="multipart/form-data">
        
        <div class="row">
          <div class="form-group col-lg-6">
            <label for="pais-origen">País de origen:</label>
            <select class="form-control" id="pais-origen" name="pais-origen" onchange="selectorPaisO()">
            """ + paises + """
            </select>
            <script>
                function selectorPaisO(){
                    let paisO= document.getElementById("pais-origen").value;
                    document.getElementById("ciudad-origen").value = (parseInt(paisO)+240).toString();
                }
            </script>
          </div>

          <div class="form-group col-lg-6">
            <label for="ciudad-origen">Ciudad de origen:</label>
            <select class="form-control" id="ciudad-origen" name="ciudad-origen" onchange="selectorCiudadO()">
            """ + ciudades + """
            </select>
            <script>
                function selectorCiudadO(){
                    let ciudadO = document.getElementById("ciudad-origen").value;
                    document.getElementById("pais-origen").value = (parseInt(ciudadO)-240).toString();
                }
            </script>
          </div>
        </div>
        <hr>

        <div class="row">
          <div class="form-group col-lg-6">
            <label for="pais-destino">País de destino:</label>
            <select class="form-control" id="pais-destino" name="pais-destino" onchange="selectorPaisD()">
            """ + paises + """
            </select>
            <script>
                function selectorPaisD(){
                    let paisD= document.getElementById("pais-destino").value;
                    document.getElementById("ciudad-destino").value = (parseInt(paisD)+240).toString();
                }
            </script>
          </div>

          <div class="form-group col-lg-6">
            <label for="ciudad-destino">Ciudad de destino:</label>
            <select class="form-control" id="ciudad-destino" name="ciudad-destino" onchange="selectorCiudadD()">
            """ + ciudades + """
            </select>
            <script>
                function selectorCiudadD(){
                    let ciudadD = document.getElementById("ciudad-destino").value;
                    document.getElementById("pais-destino").value = (parseInt(ciudadD)-240).toString();
                }
            </script>
          </div>
        </div>
        <hr>

        <div class="row">
          <div class="form-group col-lg-6">
            <label for="fecha-ida">Ingrese fecha de ida:</label>
            <input size="10" type="text" class="form-control" id="fecha-ida" placeholder="año-mes-día" name="fecha-ida">
          </div>

          <div class="form-group col-lg-6">
            <label for="fecha-regreso">Ingrese fecha de regreso:</label>
            <input size="10" type="text" class="form-control" id="fecha-regreso" placeholder="año-mes-día" name="fecha-regreso">
          </div>
        </div>
        <hr>

        <div class="row">
          <div class="form-group col-lg-6">
            <label for="espacio-disponible">Seleccione el espacio disponible:</label>
            <select class="form-control" id="espacio-disponible" name="espacio-disponible">
              <option value='0' selected>Seleccione ...</option>
              <option value='1'>10x10x10</option>
              <option value='2'>20x20x20</option>
              <option value='3'>30x30x30</option>
            </select>
          </div>

          <div class="form-group col-lg-6">
            <label for="kilos-disponibles">Seleccione los kilos disponible:</label>
            <select class="form-control" id="kilos-disponibles" name="kilos-disponibles">
              <option value='0' selected>Seleccione ...</option>
              <option value='1'>200 gr</option>
              <option value='2'>500 gr</option>
              <option value='3'>800 gr</option>
              <option value='4'>1 kg</option>
              <option value='5'>1.5 kg</option>
              <option value='6'>2 kg</option>
            </select>
          </div>
        </div>
        <hr>

        <div class="row">
          <div class="form-group col-lg-6">
            <label for="email">Ingrese su Email:</label>
            <input size="30" type="text" class="form-control" id="email"  placeholder="juanito@gmail.com" name="email">
          </div>

          <div class="form-group col-lg-6">
            <label for="celular">Ingrese su Celular:</label>
            <input size="15" type="text" class="form-control" id="celular" placeholder="e.g.: +569XXXXXXXX" name="celular">
          </div>
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Confirmar Viaje</button>
          <hr>
      </form>

    </div> 
  </div> 
    """))
