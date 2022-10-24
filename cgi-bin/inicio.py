#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb
from codecs import utf_8_decode
from encodings import utf_8;
import sys
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

with open('../templates/template.html','r', encoding="utf-8") as template:
    file = template.read()
    print(file.format('Planifica tus viajes y encargos', 'class="active"','','','','',
    """
    <section class="jumbotron text-center">
        <div class="container">
            <br><br><br><br>
            <h1 class="jumbotron-heading"> <br><b>☼ PLANIFICA AQUÍ TUS <a href="../cgi-bin/agregar-viaje.py">VIAJES</a> Y <a href="../cgi-bin/agregar-encargo.py">ENCARGOS</a> ☼</b><br> <br></h1>
        </div>
    </section>
    """))
