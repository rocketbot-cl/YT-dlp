# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os
import glob
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'YT-dlp' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path = [cur_path] + sys.path
    
from yt_dlp import YoutubeDL
import os


global build_ydl_opts, simplify_formats

def build_ydl_opts(params):

    ydl_opts = {}

    output_path = params.get("output_path")
    if output_path:
        ydl_opts['outtmpl'] = output_path
    else:
        ydl_opts['outtmpl'] = '%(title)s.%(ext)s'

    if params.get("quality"):
        ydl_opts['format'] = params.get("quality")

    if params.get("proxy"):
        ydl_opts['proxy'] = params.get("proxy")

    return ydl_opts

def simplify_formats(info):
    formats = info.get("formats", [])

    video_heights = set()
    audio_exts = set()

    for f in formats:

        if f.get("ext") == "mhtml":
            continue

        vcodec = f.get("vcodec")
        acodec = f.get("acodec")
        height = f.get("height")
        ext = f.get("ext")

        if vcodec != "none" and height:
            video_heights.add(height)

        if vcodec == "none" and acodec != "none":
            audio_exts.add(ext)

    video_list = sorted(
        [f"{h}p" for h in video_heights]
    , key=lambda x: int(x.replace("p", "")))

    audio_list = sorted(list(audio_exts))

    return {
        "video_qualities": video_list,
        "audio_formats": audio_list
    }

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")


if module == "downloadVideo":

    try:
        quality = GetParams("quality") or "best" # 360, 360p, 720, 720p, best, worst
        output_path = GetParams("output_path")
        proxy = GetParams("proxy")
        url = GetParams("url")
        var = GetParams("var_")
        extra_data = GetParams("extra_data")

        if not output_path:
            output_path = "%(title)s.%(ext)s"

        quality = quality.lower().strip()

        if quality in ["best", "worst"]:
            format_selector = quality
        else:
            if quality.endswith("p"):
                quality = quality.replace("p", "")

            if not quality.isdigit():
                raise Exception("Quality invalid")

            format_selector = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"
        
        ffmpeg_path = base_path + 'modules' + os.sep + 'YT-dlp' + os.sep + 'bin' + os.sep

        ydl_opts = {
            "format": format_selector,
            "outtmpl": output_path,
            "merge_output_format": "mp4",
            "ffmpeg_location": ffmpeg_path,
            "no_warnings": True
        }

        if proxy:
            ydl_opts['proxy'] = proxy

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if extra_data:
            SetVar(extra_data, info)
        if var:
            SetVar(var, True)
    except Exception as e:
        PrintException()
        import traceback
        traceback.print_exc()
        SetVar(var, False)


if module == "downloadAudio":
    try:
        url = GetParams("url")
        audio_format = GetParams("audio_format") or "best" # mp3, m4a, webm, best
        var = GetParams("var_")
        extra_data = GetParams("extra_data")
        output_path = GetParams("output_path")

        if not output_path:
            output_path = "%(title)s.%(ext)s"
        
        ffmpeg_path = base_path + 'modules' + os.sep + 'YT-dlp' + os.sep + 'bin' + os.sep

        audio_format = audio_format.lower().strip()

        if audio_format == "best":
            ydl_opts = {
                "format": "bestaudio",
                "outtmpl": output_path,
                "ffmpeg_location": ffmpeg_path,
                "no_warnings": True
            }

        elif audio_format in ["mp3", "m4a", "webm"]:
            ydl_opts = {
                "format": "bestaudio",
                "outtmpl": output_path,
                "ffmpeg_location": ffmpeg_path,
                "no_warnings": True,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": audio_format,
                }]
            }

        else:
            raise Exception("Audio format invalid")
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if extra_data:
            SetVar(extra_data, info)
        if var:
            SetVar(var, True)

    except Exception as e:
        PrintException()
        SetVar(var, False)

if module == "downloadPlaylist":

    try:
        url = GetParams("url")
        var = GetParams("var_")
        extra_data = GetParams("extra_data")

        ydl_opts = {
            'outtmpl': GetParams("output_path") or '%(playlist)s/%(title)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if extra_data:
            SetVar(extra_data, info)
        if var:
            SetVar(var, True)

    except Exception as e:
        PrintException()
        SetVar(var, False)


if module == "getMetadata":

    try:
        url = GetParams("url")
        var = GetParams("var_")

        with YoutubeDL({'skip_download': True, "no_warnings": True, "quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        SetVar(var, info)

    except Exception as e:
        PrintException()
        SetVar(var, False)


if module == "listFormats":

    url = GetParams("url")
    var = GetParams("var_")

    try:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        clean_formats = simplify_formats(info)

        SetVar(var, clean_formats)


    except Exception as e:
        PrintException()
        SetVar(var, False)


if module == "getAvailableSubtitles":

    try:
        url = GetParams("url")
        var_ = GetParams("var_")
        proxy = GetParams("proxy")

        ydl_opts = {
            "skip_download": True,
            "quiet": True,
            "no_warnings": True,
        }

        if proxy:
            ydl_opts["proxy"] = proxy

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        result = {
            "manual_downloadable": [],
            "automatic_downloadable": []
        }

        # 🔹 Manual subtitles
        manual = info.get("subtitles") or {}
        for lang, tracks in manual.items():
            if tracks:
                # solo si tiene URL real
                valid = [t for t in tracks if t.get("url")]
                if valid:
                    result["manual_downloadable"].append(lang)

        # 🔹 Automatic subtitles
        auto = info.get("automatic_captions") or {}
        for lang, tracks in auto.items():
            if tracks:
                valid = [t for t in tracks if t.get("url")]
                if valid:
                    result["automatic_downloadable"].append(lang)

        SetVar(var_, result)

    except Exception as e:
        PrintException()
        SetVar(var_, {})


if module == "downloadSubtitles":

    try:
        url = GetParams("url")
        language = GetParams("language")
        var = GetParams("var_")
        output_path = GetParams("output_path")
        cookiefile = GetParams("cookiefile")
        subtitle_format = (GetParams("subtitle_format") or "srt").strip().lower()

        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, "%(title)s.%(ext)s")

        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'subtitleslangs': [language],
            'quiet': True,
            'no_warnings': True,
            'outtmpl': output_path
        }
        if cookiefile:
            ydl_opts["cookiefile"] = cookiefile
        if subtitle_format:
            ydl_opts["subtitlesformat"] = subtitle_format

        deno_exe = base_path + 'modules' + os.sep + 'YT-dlp' + os.sep + 'bin' + os.sep + 'deno' + os.sep + 'deno.exe'

        ydl_opts["js_runtimes"] = {
            "deno": {
                "path": deno_exe
            }
        } 

        ok = False
        last_err = None
        for attempt in range(1, 4):
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(url, download=True)
                ok = True
                break
            except Exception as e:
                last_err = e
                msg = str(e)
                if "HTTP Error 429" in msg:
                    from time import sleep
                    sleep(3 * attempt)
                    continue
                raise

        SetVar(var_, bool(ok))
        if not ok and last_err:
            safe = str(last_err).encode("utf-8", "backslashreplace").decode("utf-8")
            print("YT-DLP subtitles failed:", safe)

    except Exception as e:
        PrintException()


if module == "downloadAutoSubtitles":

    try:
        url = GetParams("url")
        language = (GetParams("language") or "en").strip()
        var_ = GetParams("var_")
        output_path = GetParams("output_path")
        proxy = GetParams("proxy")
        cookiefile = GetParams("cookiefile")
        subtitle_format = (GetParams("subtitle_format") or "srt").strip().lower()

        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, "%(title)s.%(ext)s")

        QUIET = False

        ydl_opts = {
            "skip_download": True,
            "writeautomaticsub": True,
            "writesubtitles": False,
            "subtitleslangs": [language],
            "subtitlesformat": subtitle_format,
            "outtmpl": output_path,
            "quiet": QUIET,
            "no_warnings": QUIET,
        }

        if cookiefile:
            ydl_opts["cookiefile"] = cookiefile

        deno_exe = base_path + 'modules' + os.sep + 'YT-dlp' + os.sep + 'bin' + os.sep + 'deno' + os.sep + 'deno.exe'

        ydl_opts["js_runtimes"] = {
            "deno": {
                "path": deno_exe
            }
        }        
        ok = False
        last_err = None
        for attempt in range(1, 4):
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(url, download=True)
                ok = True
                break
            except Exception as e:
                last_err = e
                msg = str(e)
                if "HTTP Error 429" in msg:
                    from time import sleep
                    sleep(3 * attempt)
                    continue
                raise

        SetVar(var_, bool(ok))
        if not ok and last_err:
            safe = str(last_err).encode("utf-8", "backslashreplace").decode("utf-8")
            print("YT-DLP subtitles failed:", safe)
    except Exception as e:
        PrintException()
