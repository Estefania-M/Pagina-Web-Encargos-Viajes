# Pagina-Web-Tarea-2
Repositorio de una página web para agregar viajes y/o encargos para el curso de Desarrollo de Aplicaciones Web de la Universidad de Chile.

En la página de inicio de la carperta cgi-bin se muestra el menú principal del sistema que tiene las opciones “Agregar Viaje”, “Agregar Encargo”,
“Ver Viajes” y “Ver Encargos”.

● “Agregar Viaje”: solicita datos del viaje, pero ahora al presionar el botón “Grabar Viaje” hace submit al CGI que valida los datos en el lado servidor e inserta el registro en la tabla “viaje” de la base de datos. Si todo salió bien, se devuelve a la página del menú principal del sistema, mostrando un mensaje que
informa que se agregó exitosamente el viaje.

● “Agregar Encargo”: solicita datos del encargo, pero ahora al presionar el botón “Grabar Encargo” debe hacer submit al CGI que valida los datos en
el lado del servidor e inserta el registro en la tabla “encargo”. Las
fotografías se almacenan en el directorio media del servidor web y en la base de
datos quedará almacenada la ruta a ese archivo. Si todo salió bien, se devuelve a la
página del menú principal del sistema, mostrando un mensaje que informa que se
agregó exitosamente el encargo.

● Listado de Viajes: muestra los datos de los viajes guardados, pero
considera grupos de 5 elementos, si hay más de 5 se muestran por página
permitiendo avanzar y retroceder según corresponda. Si se hace click sobre un viaje se
debe mostrar la información del viaje.

● Listado de Encargos: muestra los datos de los encargos guardados, pero
considera grupos de 5 elementos, si hay más de 5 se muestran por página
permitiendo avanzar y retroceder según corresponda. Si se hace click sobre un encargo
se debe mostrar la información de ese encargo.

● Ver Viaje: se obtienen los datos del viaje correspondiente desde la base de datos y despliega la información.

● Ver Encargo: se obtienen los datos del encargo correspondiente desde la base de datos y despliega la información.
