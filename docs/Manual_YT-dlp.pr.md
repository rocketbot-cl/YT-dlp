



# YT-dlp
  
Módulo para obtener videos, audios y subtítulos desde múltiples plataformas compatibles con yt-dlp.  

*Read this in other languages: [English](Manual_YT-dlp.md), [Português](Manual_YT-dlp.pr.md), [Español](Manual_YT-dlp.es.md)*
  
![banner](imgs/Banner.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Baixar Vídeo
  
Baixe um vídeo de uma URL, permitindo definir qualidade, proxy e caminho de saída.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do vídeo para baixar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Modelo de saída|Modelo de saída do arquivo. Suporta variáveis internas do yt-dlp, para títolo e extensão usar %(title)s.%(ext)s.|C:/Videos/%(title)s.%(ext)s|
|Qualidade|Qualidade específica do vídeo. Execute o comando Listar Formatos para ver as qualidades disponíveis para um vídeo específico. Por padrão a melhor qualidade disponível será baixada.|best|
|Proxy|Proxy HTTP/HTTPS para download.|http://user:pass@127.0.0.1:8080|
|Atribuir resultado à variável|Variável onde True ou False serão armazenados dependendo do sucesso do comando.|Variable|
|Dados extras|Variável onde o JSON completo do vídeo baixado será armazenado.|Variable|

### Baixar Audio
  
Baixe um audio de uma URL, e converta para o formato desejado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do áudio para baixar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Modelo de saída|Modelo de saída do arquivo. Suporta variáveis internas do yt-dlp, para títolo e extensão usar %(title)s.%(ext)s.|C:/Audios/%(title)s.%(ext)s|
|Formato de Áudio|Formato específico do áudio. Execute o comando Listar Formatos para ver as opções disponíveis para um áudio específico. Por padrão a melhor qualidade disponível será baixada.|mp3|
|Atribuir resultado à variável|Variável onde True ou False serão armazenados dependendo do sucesso do comando.|Variable|
|Dados extras|Variável onde o JSON completo do áudio baixado será armazenado.|Variable|

### Baixar Playlist
  
Baixe todos os vídeos de uma playlist.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo da playlist para baixar.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Modelo de saída|Modelo de saída do arquivo. Suporta variáveis internas do yt-dlp, para títolo e extensão usar %(title)s.%(ext)s.|C:/Users/User/Playlists/%(playlist)s/%(title)s.%(ext)s|
|Atribuir resultado à variável|Variável onde True ou False serão armazenados dependendo do sucesso do comando.|Variable|
|Dados extras|Variável onde o JSON completo da playlist baixada será armazenado.|Variable|

### Listar Formatos
  
Liste todos os formatos disponíveis para um vídeo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Atribuir resultado à variável|Variável onde o resultado do comando será armazenado.|Variable|

### Obtener Metadados
  
Obtém metadados do vídeo sem baixá-lo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Atribuir resultado à variável|Variável onde o resultado do comando será armazenado.|Variable|

### Legendas disponíveis
  
Obtém lista de idiomas de legendas manuais e automáticas disponíveis.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Atribuir resultado à variável|Variável onde o resultado do comando será armazenado.|Variable|

### Baixar Legendas Manuais
  
Baixe legendas manuais em idioma especifico.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do vídeo.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Caminho de saída|Caminho onde os subtítulos serão salvos.|C:/Users/User/Subtitulos|
|Formato de saída|Formato de saída dos subtítulos (ex srt, vtt, lrc, best, ass), |srt|
|Arquivo de cookies|Caminho para o arquivo de cookies da página do vídeo, pode ser obtido com a extensão Get cookies txt https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Idioma|Código do idioma (ex es, en, fr). Execute o comando 'Legendas disponíveis' para ver os códigos de idiomas disponíveis para um vídeo.|es|
|Atribuir resultado à variável|Variável onde True ou False serão armazenados dependendo do sucesso do comando.|Variable|

### Baixar Legendas Automáticas
  
Baixe legendas automáticas em idioma especifico.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|Link completo do vídeo.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Caminho de saída|Caminho onde o arquivo será salvo.|C:/Users/User/Subtitulos|
|Formato de saída|Formato de saída dos subtítulos (ex srt, vtt, lrc, best, ass), |srt|
|Arquivo de cookies|Caminho para o arquivo de cookies da página do vídeo, pode ser obtido com a extensão Get cookies txt https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Idioma|Código do idioma (ex es, en, fr). Execute o comando 'Legendas disponíveis' para ver os códigos de idiomas disponíveis para um vídeo.|es|
|Atribuir resultado à variável|Variável onde True ou False serão armazenados dependendo do sucesso do comando.|Variable|
