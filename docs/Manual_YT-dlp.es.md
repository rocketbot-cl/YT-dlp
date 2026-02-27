



# YT-dlp
  
Módulo para obtener videos, audios y subtítulos desde múltiples plataformas compatibles con yt-dlp.  

*Read this in other languages: [English](Manual_YT-dlp.md), [Português](Manual_YT-dlp.pr.md), [Español](Manual_YT-dlp.es.md)*
  
![banner](imgs/Banner.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Descargar Video
  
Descarga un video desde una URL, permitiendo definir calidad, proxy y ruta de salida.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video a descargar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Plantilla de salida|Ruta, nombre del archivo a guardar. Soporta variables internas de yt-dlp, para titulo original y extension usar %(title)s.%(ext)s.|C:/Videos/%(title)s.%(ext)s|
|Calidad|Calidad específica del video. Ejecutar el comando Listar Formatos para ver las calidades disponibles para un video específico. Por default se descargará la mejor calidad disponible.|best|
|Proxy|Proxy HTTP/HTTPS para la descarga.|http://user:pass@127.0.0.1:8080|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|
|Extra data|Variable donde se almacenará el JSON completo del video descargado.|Variable|

### Descargar Audio
  
Descarga el audio de un video desde una URL, y lo convierte al formato deseado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del audio a descargar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Plantilla de salida|Ruta, nombre del archivo a guardar. Soporta variables internas de yt-dlp, para titulo original y extension usar %(title)s.%(ext)s.|C:/Audios/%(title)s.%(ext)s|
|Formato de Audio|Formato específico del audio. Ejecutar el comando Listar Formatos para ver las opciones disponibles para un audio específico. Por default se descargará la mejor calidad disponible.|mp3|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|
|Extra data|Variable donde se almacenará el JSON completo del audio descargado.|Variable|

### Descargar Playlist
  
Descarga todos los videos de una playlist.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo de la playlist descargar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Plantilla de salida|Ruta, nombre del archivo a guardar. Soporta variables internas de yt-dlp, para titulo original y extension usar %(title)s.%(ext)s.|C:/Users/User/Playlists/%(playlist)s/%(title)s.%(ext)s|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|
|Extra data|Variable donde se almacenará el JSON completo de la playlist descargada.|Variable|

### Listar Formatos
  
Lista todos los formatos disponibles para un video.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Obtener Metadata
  
Obtiene metadata del video sin descargarlo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Subtitulos disponibles
  
Obtiene lista de idiomas de subtítulos manuales y automáticos disponibles.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Descargar Subtítulos Manuales
  
Descarga subtítulos manuales en idioma específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta donde se guardarán los subtítulos.|C:/Users/User/Subtitulos|
|Formato de salida|Formato en el que se descargarán los subtítulos (ej srt, vtt, lrc, best, ass), por default es srt.|srt|
|Archivo de Cookies|Ruta al archivo de cookies de la página del video, se puede obtener con la extensión Get cookies txt https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Idioma|Código del idioma (ej es, en, fr). Ejecutar el comando 'Subtítulos disponibles' para ver los códigos de idiomas disponibles para un video.|es|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|

### Descargar Subtítulos Automáticos
  
Descarga subtítulos automáticos en idioma específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|Enlace completo del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta donde se alojará el archivo.|C:/Users/User/Subtitulos|
|Formato de salida|Formato en el que se descargarán los subtítulos (ej srt, vtt, lrc, best, ass), por default es srt.|srt|
|Archivo de Cookies|Ruta al archivo de cookies de la página del video, se puede obtener con la extensión Get cookies txt https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Idioma|Código del idioma (ej es, en, fr). Ejecutar el comando 'Subtítulos disponibles' para ver los códigos de idiomas disponibles para un video.|es|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|
