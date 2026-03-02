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
import os, shutil, subprocess, json

base_path = tmp_global_obj["basepath"]

def _find_yt_dlp(custom_path: str = None) -> str:
    """
    Busca yt-dlp:
    - si custom_path viene: usa ese
    - si no: busca yt-dlp en PATH
    """
    if custom_path and custom_path.strip():
        p = custom_path.strip().strip('"')
        if os.path.isfile(p):
            return p
        if p.lower() in ["yt-dlp", "yt-dlp.exe"]:
            return "yt-dlp"
        raise Exception(f"yt-dlp no encontrado en ruta indicada: {p}")

    exe = shutil.which("yt-dlp") or shutil.which("yt-dlp.exe")
    if exe:
        return exe
    raise Exception("yt-dlp no esta instalado o no está en el PATH. Instalalo o indica yt_dlp_path.")

def _run(cmd_list, timeout=None):
    """
    Ejecuta comando y retorna (ok, stdout, stderr, returncode)
    Captura bytes y decodifica manualmente para evitar UnicodeDecodeError (charmap).
    """
    p = subprocess.run(
        cmd_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout
    )

    out = (p.stdout or b"").decode("utf-8", errors="replace")
    err = (p.stderr or b"").decode("utf-8", errors="replace")

    ok = (p.returncode == 0)
    return ok, out, err, p.returncode

def _outtmpl_folder_only(output_folder: str, template: str):
    """
    Si output_folder viene vacío, usa Descargas.
    template debe ser algo tipo "%(title)s.%(ext)s" o "%(playlist_title)s/%(title)s.%(ext)s"
    """
    if not output_folder:
        output_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return os.path.join(output_folder, template)

def simplify_formats(info_json):
    formats = info_json.get("formats") or []

    heights = set()
    audio_exts = set()

    for f in formats:
        vcodec = (f.get("vcodec") or "").lower()
        acodec = (f.get("acodec") or "").lower()
        ext = (f.get("ext") or "").lower()
        height = f.get("height")

        has_video = vcodec and vcodec != "none"
        has_audio = acodec and acodec != "none"

        if (not has_video) and has_audio:
            if ext:
                audio_exts.add(ext)

        if has_video and isinstance(height, int) and height > 0:
            heights.add(height)

    video_qualities = [f"{h}p" for h in sorted(heights)]
    audio_formats = sorted(audio_exts)

    return {
        "video_qualities": video_qualities,
        "audio_formats": audio_formats
    }

module = GetParams("module")

if module == "downloadVideo":
    var_ = GetParams("var_")
    url = GetParams("url")
    output_folder = GetParams("output_path")
    quality = (GetParams("quality") or "best").strip().lower()
    yt_dlp_path = GetParams("yt_dlp_path")

    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)
        outtmpl = _outtmpl_folder_only(output_folder, "%(title)s.%(ext)s")
        if quality in ["best", "worst"]:
            fmt = quality
        else:
            if quality.endswith("p"):
                quality = quality[:-1]
            if not quality.isdigit():
                raise Exception("Quality inválida. Usa best/worst o 360/720/1080 o 360p/720p/1080p")
            fmt = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"
        cmd = [ytdlp, "-f", fmt, "-o", outtmpl, "--no-abort-on-error"]
        cmd.append(url)
        ok, out, err, rc = _run(cmd)
        SetVar(var_, ok)

        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")

    except Exception as e:
        PrintException()
        SetVar(var_, False)

if module == "downloadAudio":
    var_ = GetParams("var_")
    try:
        url = GetParams("url")
        output_folder = GetParams("output_path")
        audio_format = (GetParams("audio_format") or "m4a").strip().lower()
        yt_dlp_path = GetParams("yt_dlp_path")

        ytdlp = _find_yt_dlp(yt_dlp_path)
        outtmpl = _outtmpl_folder_only(output_folder, "%(title)s.%(ext)s")

        cmd = [ytdlp, "-x", "--audio-format", audio_format, "-o", outtmpl, "--no-abort-on-error"]
        cmd.append(url)
        ok, out, err, rc = _run(cmd)

        SetVar(var_, ok)

        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")

    except Exception:
        PrintException()
        SetVar(var_, False)

if module == "downloadPlaylist":
    var_ = GetParams("var_")
    url = GetParams("url")
    output_folder = GetParams("output_path")
    yt_dlp_path = GetParams("yt_dlp_path")
    limit_str = GetParams("limit")
    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)

        outtmpl = _outtmpl_folder_only(output_folder, "%(playlist_title)s/%(title)s.%(ext)s")

        cmd = [ytdlp, "-o", outtmpl, "--yes-playlist", "--no-abort-on-error"]

        if limit_str and str(limit_str).strip().isdigit():
            cmd += ["--playlist-end", str(int(limit_str))]

        cmd.append(url)

        ok, out, err, rc = _run(cmd)
        if var_:
            SetVar(var_, ok)
        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")

    except Exception:
        PrintException()
        if var_:
            SetVar(var_, False)

if module == "listFormats":
    var_ = GetParams("var_")
    url = GetParams("url")
    yt_dlp_path = GetParams("yt_dlp_path")
    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)

        cmd = [ytdlp, "--no-warnings", "-J", url]

        ok, out, err, rc = _run(cmd)
        info = json.loads(out) if ok else {}
        simplified = simplify_formats(info)
        if var_:
            SetVar(var_, json.dumps(simplified, ensure_ascii=False))

        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")

    except Exception:
        PrintException()
        if var_:
            SetVar(var_, False)

if module == "getMetadataJson":
    var_ = GetParams("var_")
    json_var = GetParams("json_var")
    url = GetParams("url")
    yt_dlp_path = GetParams("yt_dlp_path")

    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)
        cmd = [ytdlp, "-J", "--no-warnings", url]

        ok, out, err, rc = _run(cmd, timeout=120)
        if ok:
            SetVar(json_var, out)
        else:
            SetVar(json_var, err)
        SetVar(var_, ok)
        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")
    except Exception:
        PrintException()
        SetVar(var_, False)

elif module == "getAvailableSubtitles":
    var_ = GetParams("var_")
    url = GetParams("url")
    yt_dlp_path = GetParams("yt_dlp_path")

    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)
        cmd = [ytdlp, "--no-warnings", "-J", url]
        ok, out, err, rc = _run(cmd, timeout=120)

        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")

        info = json.loads(out)
        
        manual = sorted((info.get("subtitles") or {}).keys())
        automatic = sorted((info.get("automatic_captions") or {}).keys())

        result = {
            "manual": manual,
            "automatic": automatic
            }
        
        if var_:
            SetVar(var_, json.dumps(result, ensure_ascii=False))

    except Exception:
        PrintException()
        if var_:
            SetVar(var_, False)

if module == "downloadSubtitles":
    var_ = GetParams("var_")
    output_var = GetParams("output_var")
    url = GetParams("url")
    language = (GetParams("language") or "en").strip()
    output_folder = GetParams("output_path")
    subtitle_format = (GetParams("subtitle_format") or "srt").strip().lower()
    yt_dlp_path = GetParams("yt_dlp_path")

    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)
        outtmpl = _outtmpl_folder_only(output_folder, "%(title)s.%(ext)s")
        cmd = [
            ytdlp,
            "--skip-download",
            "--write-subs",
            "--sub-langs", language,
            "--sub-format", subtitle_format,
            "-o", outtmpl,
            "--no-abort-on-error",
            "--sleep-subtitles", "60"
        ]

        cmd.append(url)
        ok, out, err, rc = _run(cmd)

        SetVar(var_, ok)

        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")
    except Exception:
        PrintException()
        SetVar(var_, False)

if module == "downloadAutoSubtitles":
    var_ = GetParams("var_")
    url = GetParams("url")
    language = (GetParams("language") or "en").strip()
    output_folder = GetParams("output_path")
    subtitle_format = (GetParams("subtitle_format") or "vtt").strip().lower()
    yt_dlp_path = GetParams("yt_dlp_path")
    try:
        ytdlp = _find_yt_dlp(yt_dlp_path)
        outtmpl = _outtmpl_folder_only(output_folder, "%(title)s.%(ext)s")
        cmd = [
            ytdlp,
            "--skip-download",
            "--write-auto-subs",
            "--sub-langs", language,
            "--sub-format", subtitle_format,
            "-o", outtmpl,
            "--no-abort-on-error",
            "--sleep-subtitles", "60"
        ]

        cmd.append(url)
        ok, out, err, rc = _run(cmd)
        SetVar(var_, ok)
        if not ok:
            raise Exception(err.strip() or f"yt-dlp failed (rc={rc})")
    except Exception:
        PrintException()
        SetVar(var_, False)