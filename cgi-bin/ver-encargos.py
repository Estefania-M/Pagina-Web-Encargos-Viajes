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
encargos = db.get5Encargos('0')
data = db.get5Encargos(id)
tabla = """
  <div class="info">
    <div class="container">
      <br>
      <h1 class="jumbotron-heading"><br>A continuación se muestran los encargos registrados:</h1>
    </div>

    <div class="container">
      <script src="datos.js"></script>
      <br>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Origen</th>
            <th scope="col">Destino</th>
            <th scope="col">Espacio</th>
            <th scope="col">Kilos</th>
            <th scope="col">Email</th>
            <th scope="col">Foto</th>
          </tr>
        </thead>
        <tbody>
        """
for p in data:
    ciudadO = db.getNCiudad(p[4])
    paisO = db.getNPais(ciudadO[0][1])
    ciudadD = db.getNCiudad(p[5])
    paisD = db.getNPais(ciudadD[0][1])
    kilos = db.getKilos(p[3])
    espacio = db.getEspacio(p[2])
    path = db.getPath(p[0])
    tabla+=f""" 
        <tr>
            <td><a href="../cgi-bin/informacion-encargo.py?id={p[0]}">
              <img class="boton" src="../img/boton_encargos.png" alt="botón viaje" width="25" height="25"></a>
              {paisO[0][0]}: {ciudadO[0][0]}
            </td>
            <td>{paisD[0][0]}: {ciudadD[0][0]}</td>
            <td>{espacio[0][0]}</td>
            <td>{kilos[0][0]}</td>
            <td>{p[6]}</td>
            <td> <img src=../media/{path[0][0]} width="120" height="120" /></td>
        </tr>
        """


tabla+="""
    </tbody>
    </table>
    <b>Para ver la información de cada viaje pulse en el ícono <img src="../img/boton_encargos.png" alt="botón viaje" width="25" height="25"> correspondiente.</b>
    """

filas = len(encargos)
i=1
botones=''
while filas>5:
  botones+="""<li class="page-item"><a class="page-link" href="../cgi-bin/ver-encargos.py?id="""+str(i)+"""">"""+str(i)+"""</a></li>"""
  i+=1
  filas-=5

tabla+= """
      <div aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li class="page-item">
            <a class="page-link" href="../cgi-bin/ver-encargos.py?id=1" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
              <span class="sr-only">Previous</span>
            </a>
          </li>
          """+botones+"""
          <li class="page-item"><a class="page-link" href="../cgi-bin/ver-encargos.py?id="""+str(i)+"""">"""+str(i)+"""</a></li>
          <li class="page-item">
            <a class="page-link" href="../cgi-bin/ver-encargos.py?id="""+str(i)+"""" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
              <span class="sr-only">Next</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
    </div>"""

with open('../templates/template.html','r', encoding="utf-8") as template:
    file = template.read()
    print(file.format('Ver Encargos','','','','','class="active"', tabla), file=utf8stdout)