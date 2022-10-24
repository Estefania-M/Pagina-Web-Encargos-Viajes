--INSERTAR UN ENCARGO (llaves foráneas: espacio, kilos, origen, destino)
INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador) VALUES (?,?,?,?,?,?,?)
--INSERTAR foto de un encargo (llave foránea: encargo_id)
INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) VALUES (?,?,?)

--INSERTAR UN VIAJE (llaves foráneas: origen, destino, kilos_disponible, espacio_disponible)
INSERT INTO  viaje (origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero) VALUES (?,?,?,?,?,?,?,?)

--OBTENER TODOS LOS VIAJES
SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero FROM viaje

--OBTENER LOS PRIMEROS 5 VIAJES
SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero FROM viaje ORDER BY id ASC LIMIT 5

--OBTENER LA SEGUNDA PÁGINA DE 5 VIAJES
SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero FROM viaje ORDER BY id ASC LIMIT 4, 5

--OBTENER INFORMACION DE 1 VIAJE
SELECT id, origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero FROM viaje WHERE id=?

--OBTENER TODOS LOS ENCARGOS
SELECT id, descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador FROM encargo

--OBTENER INFORMACION DE UN ENCARGO
SELECT id, descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador FROM encargo WHERE id=?
--OBTENER fotos de un encargo
SELECT id, ruta_archivo, nombre_archivo FROM foto WHERE encargo_id=?

--OBTENER LOS PRIMEROS 5 ENCARGOS
SELECT id, descripcion, espacio, kilos, origen, destino, imagen, email_encargador, celular_encargador FROM encargo ORDER BY id ASC LIMIT 5

--OBTENER LA SEGUNDA PAGINA DE 5 ENCARGOS
SELECT id, descripcion, espacio, kilos, origen, destino, imagen, email_encargador, celular_encargador FROM encargo ORDER BY id ASC LIMIT 4, 5
