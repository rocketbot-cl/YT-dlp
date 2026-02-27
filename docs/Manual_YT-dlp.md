



# YT-dlp
  
Module to obtain videos, audio and subtitles from multiple compatible platforms with yt-dlp.  

*Read this in other languages: [English](Manual_YT-dlp.md), [Português](Manual_YT-dlp.pr.md), [Español](Manual_YT-dlp.es.md)*
  
![banner](imgs/Banner.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Download Video
  
Download a video from a URL, allowing to define quality, proxy and output path.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output template|Output template of the file. Supports yt-dlp internal variables, for title and extension use %(title)s.%(ext)s.|C:/Videos/%(title)s.%(ext)s|
|Quality|Specific quality of the video. Run the List Formats command to see the available qualities for a specific video. By default the best available quality will be downloaded.|best|
|Proxy|HTTP/HTTPS proxy for download.|http://user:pass@127.0.0.1:8080|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|
|Extra data|Variable where the complete JSON of the downloaded video will be stored.|Variable|

### Download Audio
  
Download audio from a video URL, and convert it to the desired format.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the audio to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output template|Output template of the file. Supports yt-dlp internal variables, for title and extension use %(title)s.%(ext)s.|C:/Audios/%(title)s.%(ext)s|
|Audio Format|Specific format of the audio. Run the List Formats command to see the available options for a specific audio. By default the best available quality will be downloaded.|mp3|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|
|Extra data|Variable where the complete JSON of the downloaded audio will be stored.|Variable|

### Download Playlist
  
Download all videos from a playlist.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the playlist to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output template|Output template of the file. Supports yt-dlp internal variables, for title and extension use %(title)s.%(ext)s.|C:/Users/User/Playlists/%(playlist)s/%(title)s.%(ext)s|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|
|Extra data|Variable where the complete JSON of the downloaded playlist will be stored.|Variable|

### List Formats
  
List all available formats for a video.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Assign result to a Variable|Variable where the result of the command will be stored.|Variable|

### Get Metadata
  
Get metadata of a video without downloading it.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Assign result to a Variable|Variable where the result of the command will be stored.|Variable|

### Available subtitles
  
Get list of available manual and automatic subtitles languages.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Assign result to a Variable|Variable where the result of the command will be stored.|Variable|

### Download Manual Subtitles
  
Download manual subtitles in specific language.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Output path where subtitles will be saved.|C:/Users/User/Subtitulos|
|Output Format|Output format of the subtitles (e.g. srt, vtt, lrc, best, ass), by default is srt.|srt|
|Cookies file|Path to the cookies file of the video page, it can be obtained with the Get cookies txt extension https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Language|Language code (e.g. es, en, fr). Run the 'Available subtitles' command to see the available language codes for a video.|es|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|

### Download Automatic Subtitles
  
Download automatic subtitles in specific language.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Path where the file will be saved.|C:/Users/User/Subtitulos|
|Output Format|Output format of the subtitles (e.g. srt, vtt, lrc, best, ass), by default is srt.|srt|
|Cookies file|Path to the cookies file of the video page, it can be obtained with the Get cookies txt extension https//goo.su/Grmma|C:/Subtitulos/cookies.txt|
|Language|Language code (e.g. es, en, fr). Run the 'Available subtitles' command to see the available language codes for a video.|es|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|
