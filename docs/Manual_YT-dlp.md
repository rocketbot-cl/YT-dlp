



# YT-dlp
  
Module to obtain videos, audio and subtitles from multiple compatible platforms with yt-dlp.  

*Read this in other languages: [English](Manual_YT-dlp.md), [Português](Manual_YT-dlp.pr.md), [Español](Manual_YT-dlp.es.md)*
  
![banner](imgs/Banner.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

Before using this module, you need to install two tools:

1. Install yt-dlp

    1.1 Download the yt-dlp.exe file from:

    https://github.com/yt-dlp/yt-dlp/releases/latest

    1.2 Create a folder and place the executable inside, for example:

        C:\yt-dlp\yt-dlp.exe

    1.3 Add this folder to your system's PATH environment variable:

    System → Environment Variables → Edit PATH → Add

        C:\yt-dlp

2. Install FFmpeg

    2.1 Go to:

    https://www.gyan.dev/ffmpeg/builds/

    and download the .zip file:

        ffmpeg-release-essentials.zip

    2.2 Extract it to a folder, for example: 

        C:\ffmpeg\ 

    2.3 Add to PATH: 

        C:\ffmpeg\bin



## Description of the commands

### Download Video
  
Download a video from a URL, allowing to define quality, proxy and output path.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Path of the folder where the video will be downloaded.|C:/Users/User/Videos|
|Quality|Specific quality of the video. Run the List Formats command to see the available qualities for a specific video. By default the best available quality will be downloaded.|best|
|yt-dlp Path|Optional. Path of the folder where yt-dlp is installed.|C:/Tools/yt-dlp.exe|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|

### Download Audio
  
Download audio from a video URL, and convert it to the desired format.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the audio to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Path of the folder where the audio will be downloaded.|C:/Users/User/Audios|
|Audio Format|Specific format of the audio. Run the List Formats command to see the available options for a specific audio. By default the best available quality will be downloaded.|mp3|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|

### Download Playlist
  
Download all videos from a playlist.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the playlist to download.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Path of the folder where the files will be downloaded.|C:/Users/User/Playlists|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|

### List Formats
  
List all available formats for a video.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|yt-dlp Path|Optional. Path of the folder where yt-dlp is installed.|C:/Tools/yt-dlp|
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
|Output path|Output path where subtitles will be downloaded.|C:/Users/User/Subtitulos|
|Output Format|Output format of the subtitles (e.g. srt, vtt, lrc, best, ass), by default is srt.|srt|
|Language|Language code (e.g. es, en, fr). Run the 'Available subtitles' command to see the available language codes for a video.|es|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|

### Download Automatic Subtitles
  
Download automatic subtitles in specific language.
|Parameters|Description|example|
| --- | --- | --- |
|URL|Full link of the video.|https://www.youtube.com/watch?v=PnMMBJiT338|
|Output path|Path where the file will be downloaded.|C:/Users/User/Subtitulos|
|Output Format|Output format of the subtitles (e.g. srt, vtt, lrc, best, ass), by default is vtt.|vtt|
|Language|Language code (e.g. es, en, fr). Run the 'Available subtitles' command to see the available language codes for a video.|es|
|Assign result to a Variable|Variable where True or False will be stored depending on the success of the command.|Variable|
