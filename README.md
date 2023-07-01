# Tp-api
##INTRODUCCIÓN

Para el trabajo tomamos la idea de un sistema de gestión de alumnos de la materia, que disponibiliza métodos para la consulta y carga del estado de los mismos en cuanto a su rendimiento académico, medidas de descriptivas del rendimiento de los mismos y consultas más generales como la obtención de alumnos por legajo, apellido, borrado o carga.
Se desarrolló en Python con el módulo flask, en entornos físicos corriendo tanto sobre Windows 10 y Linux (Pop!_OS). Se testeo el correcto funcionamiento de tanto servidor como cliente en ambos SO.
También se usaron distintas consolas como el command prompt de windows y bash en su versión para Windows y Linux.
##DESCRIPCIÓN DEL ENTORNO DE TRABAJO DEL SERVIDOR
Para el servidor se eligió su programación en Python utilizando el módulo Flask, por experiencia previa con ese módulo, y la posibilidad de proveer una interfaz web para consumir la API además del cliente en Python. Por complicaciones se desistió de implementar el acceso mediante el browser pero se mantuvo algunas características para soportarlo a futuro.  
##DESCRIPCIÓN DEL ENTORNO DE TRABAJO DEL DEL CLIENTE

El cliente se trata de un programa de consola en Python que consume la API mediante la elección de opciones de un menú para facilitar su uso. 
Nos propusimos ofuscar las request solo dejando visible al usuario sus salidas o la entrada de los valores necesarios para realizar una consulta como el apellido, legajo o comisión a buscar.
También se considera que el cliente puede correr desde la misma PC como desde otra en la misma red local por lo que admite establecer ambas conexiones con facilidad.

##DESCRIPCIÓN DE LA BASE DE DATOS ELEGIDA
La base elegida es una recreación del listado de alumnos de la TUIA que cursan la materia Redes de Datos.


