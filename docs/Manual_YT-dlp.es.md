



# YT-dlp
  
Módulo para obtener videos, audios y subtítulos desde múltiples plataformas compatibles con yt-dlp.  

*Read this in other languages: [English](Manual_YT-dlp.md), [Português](Manual_YT-dlp.pr.md), [Español](Manual_YT-dlp.es.md)*
  
![banner](imgs/Banner.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Antes de usar este módulo, es necesario instalar dos herramientas:

1. Instalar yt-dlp

    1.1 Descargar el archivo yt-dlp.exe desde:
https://github.com/yt-dlp/yt-dlp/releases/latest

    1.2 Crear una carpeta y colocar el ejecutable dentro, por ejemplo:

        C:\yt-dlp\yt-dlp.exe

    1.3 Añadir esta carpeta a la ruta del sistema:

    Sistema → Variables de entorno → Variables del sistema → Editar PATH → Añadir

        C:\yt-dlp

2. Instalar FFmpeg

    2.1 Ir a la pagina:
https://www.gyan.dev/ffmpeg/builds/

    y descargar el .zip:

        ffmpeg-release-essentials.zip

    2.2 Extraer en una carpeta, por ejemplo:

        C:\ffmpeg\

    2.3 Añadir al PATH:

        C:\ffmpeg\bin

## ID de video YouTube

El ID del video de YouTube es una cadena de 11 caracteres (letras, números, - o _), por ejemplo:

    PnMMBJiT338

### Formatos de URL donde aparece el ID:

1. URL estándar (la más común)

    Aquí viene después de v=

        
        https://www.youtube.com/watch?v=PnMMBJiT338

    ID:

        PnMMBJiT338
        
2. URL corta (youtu.be)

        https://youtu.be/PnMMBJiT338

    ID:

        PnMMBJiT338

3. URL con playlist

        https://www.youtube.com/watch?v=PnMMBJiT338&list=RD...

    ID:

        PnMMBJiT338

    La playlist es otro parámetro (list=).
4. URL embed o shorts

        https://www.youtube.com/embed/PnMMBJiT338
        https://www.youtube.com/shorts/PnMMBJiT338

    ID:

        PnMMBJiT338


## Descripción de los comandos

### Descargar Video
  
Descarga un video, permitiendo definir la calidad deseada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video a descargar, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta de la carpeta donde se descargará el video.|C:/Users/User/Videos|
|Ruta a yt-dlp|Opcional. Ruta al ejecutable yt-dlp, para los casos en los que de error por no encontrarlo.|C:/Tools/yt-dlp.exe|
|Calidad|Calidad específica del video. Ejecutar el comando Listar Formatos para ver las calidades disponibles para un video específico. Por default se descargará la mejor calidad disponible.|best|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|

### Descargar Audio
  
Descarga el audio de un video desde una URL, y lo convierte al formato deseado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del audio a descargar, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta hacia la carpeta donde se descargará el audio.|C:/Users/User/Audios|
|Formato de Audio|Formato específico del audio. Ejecutar el comando Listar Formatos para ver las opciones disponibles para un audio específico. Por default se descargará la mejor calidad disponible.|mp3|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|

### Descargar Playlist
  
Descarga todos los videos de una playlist.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo de la playlist descargar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de descarga|Ruta hacia la carpeta donde se descargarán los archivos.|C:/Users/User/Playlists|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|

### Listar Formatos
  
Lista todos los formatos disponibles para un video.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta a yt-dlp|Opcional. Ruta de la carpeta donde se encuentra yt-dlp.|C:/Tools/yt-dlp|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Obtener Metadata
  
Obtiene metadata del video sin descargarlo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Subtitulos disponibles
  
Obtiene lista de idiomas de subtítulos manuales y automáticos disponibles.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Asignar resultado a Variable|Variable donde se almacenará el resultado del comando.|Variable|

### Descargar Subtítulos Manuales
  
Descarga subtítulos manuales en idioma específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta haciala carpeta donde se descargarán los subtítulos.|C:/Users/User/Subtitulos|
|Formato de salida|Formato en el que se descargarán los subtítulos (ej srt, vtt, lrc, best, ass), por default es srt.|srt|
|Idioma|Código del idioma (ej es, en, fr). Ejecutar el comando 'Subtítulos disponibles' para ver los códigos de idiomas disponibles para un video.|es|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|

### Descargar Subtítulos Automáticos
  
Descarga subtítulos automáticos en idioma específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL o ID|Enlace completo del video, o el ID del video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Ruta de salida|Ruta hacia la carpeta donde se descargará el archivo.|C:/Users/User/Subtitulos|
|Formato de salida|Formato en el que se descargarán los subtítulos (ej srt, vtt, lrc, best, ass), por default es vtt.|vtt|
|Idioma|Código del idioma (ej es, en, fr). Ejecutar el comando 'Subtítulos disponibles' para ver los códigos de idiomas disponibles para un video.|es|
|Asignar resultado a Variable|Variable donde se almacenará True o False dependiendo del éxito del comando.|Variable|
