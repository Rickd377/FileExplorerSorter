import os, shutil

path = "C:/Users/rick-/Desktop/Downloads - sorted/"
downloads = "C:/Users/rick-/Downloads/"

folder_names = [
  'Documents',
  'PDFs',
  'Images',
  'Installers',
  'Audios',
  'Videos',
  'Code',
  'Archives',
  'Fonts',
  'Others'
]

document_ext = [
    "docx", "docm", "doc", "dotx", "dotm", "dot", "xps", "rtf", "txt", "odt",
    "xlsx", "xlsm", "xlsb", "xls", "csv", "xltx", "xltm", "xlt", "prn", "dif", "slk", "xlam", "xla", "ods",
    "pptx", "pptm", "potx", "potm", "thmx", "ppsx", "ppsm", "ppam", "odp"
    "odg", "odf", "sxw", "sxc", "sxi", "log", "wps", "wpd", "pages",
    "eml", "msg", "oft", "ics", "vcf", "epub", "mobi", "azw", "azw3",
    "dat", "key", "keynote", "numbers", "one", "note", "notebook", "section",
    "asc", "imp", "gdoc", "gsheet", "gslides"
]

pdf_ext = ["pdf"]

image_ext = [
    "jif", "arw", "nrw", "k25", "dib", "heif", "heic", "jp2", "jk2", "jpf", "jpx", "jpm", "mj2", "svgz",
    "apng", "png", "avif", "gif", "jpg", "jpeg", "jpe", "jfif", "pjpeg", "pjp", "webp", "bmp", 
    "ico", "cur", "tif", "tiff", "raw", "ai", "xcf",
    "cr2", "nef", "orf", "sr2", "crw", "dng", "raf", "rw2", "mrw", "x3f", "pef", "srw",
    "psd", "ind", "indd", "indt", "eps", "svg",
    "pcx", "tga", "exif", "fpx", "lcd", "ani", "cdp", "drw", "psp", "pdn"
]

installer_ext = [
  "exe", "msi", "msix", "msp", "msu", "app", "pkg", "dmg", "deb", "rpm",
  "appx", "appxbundle", "bat", "cmd", "inf", "iss", "action", "air", "crx",
  "xpi", "jar", "apk", "aab", "vbs", "msc", "ws", "wsf", "cab", "update"
]

audio_ext = [
    "mp3", "wav", "wma", "ogg", "m4a", "flac", "alac", "aiff", "aif",
    "pcm", "aac", "wv", "tta", "m3u", "m3u8", "pls", "wpl",
    "mid", "midi", "kar", "amr", "awb", "dvf", "msv", "vox",
    "au", "snd", "cda", "ac3", "dss", "m4p", "gsm", "ra", "rm", "adt",
    "adts", "aob", "ape", "mka", "m3a", "mp2", "mpga", "oga", "mogg", "opus",
    "spx", "3ga", "aa", "aa3", "aax", "aac3"
]

video_ext = [
    "mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "m4v", "mpeg", "mpg",
    "mxf", "vob", "3gp", "3g2", "mts", "m2ts", "ts", "qt", "asf", "rm", "rmvb",
    "swf", "f4v", "dv", "wtv", "amv", "vr", "360", "braw", "r3d",
    "divx", "xvid", "ogv", "mjpeg", "mpv", "m2v", "svi", "mpe", "m1v", "m4p", "prproj", "aep", "drp", "dav", "rec"
]

code_ext = [
    "html", "htm", "xhtml", "css", "scss", "sass", "less", "js", "jsx", "ts", "tsx",
    "php", "asp", "aspx", "jsp", "cshtml", "razor",
    "py", "java", "c", "cpp", "cs", "h", "hpp", "rs", "go", "rb", "pl", "swift",
    "kt", "kts", "dart", "lua", "r", "m", "mm", "scala", "groovy",
    "ps1", "sh", "bash", "zsh", "fish", "tcl", "perl",
    "xml", "json", "yaml", "yml", "ini", "conf", "config", "toml",
    "sql", "db", "dbf", "mdb", "accdb", "md", "markdown", "rst", "asciidoc", "tex",
    "sln", "csproj", "vbproj", "vcxproj", "proj", "gradle", "pom", "ipynb", "rmd",
    "vim", "gitignore", "dockerignore", "env", "editorconfig"
]

archive_ext = [
  "zip", "rar", "7z", "gz", "tar", "iso", "bz2", "xz", "tgz"
]

font_ext = [
  "ttf", "otf", "woff", "woff2", "eot"
]

def createFolders():
  for i in range(len(folder_names)):
    os.makedirs(path + folder_names[i], exist_ok=True)

def getUniqueFileName(folder_path, base_name, ext, counter):
    if base_name.endswith('s'):
        base_name = base_name[:-1]
    new_name = f"{base_name.lower()}_{counter:03d}.{ext}"
    return new_name

def moveFiles():
  files = os.listdir(downloads)
  folder_counts = {folder: 1 for folder in folder_names}

  for file in files:
    if os.path.isdir(downloads + file):
      continue

    file_ext = os.path.splitext(file)[1][1:].lower()
    
    try:
      dest_folder = ""
      if file_ext in document_ext:
        dest_folder = "Documents"
      elif file_ext in pdf_ext:
        dest_folder = "PDFs"
      elif file_ext in image_ext:
        dest_folder = "Images"
      elif file_ext in installer_ext:
        dest_folder = "Installers"
      elif file_ext in audio_ext:
        dest_folder = "Audios"
      elif file_ext in video_ext:
        dest_folder = "Videos"
      elif file_ext in code_ext:
        dest_folder = "Code"
      elif file_ext in archive_ext:
        dest_folder = "Archives"
      elif file_ext in font_ext:
        dest_folder = "Fonts"
      else:
        dest_folder = "Others"

      dest_path = path + dest_folder
      new_name = getUniqueFileName(dest_path, dest_folder, file_ext, folder_counts[dest_folder])
      shutil.move(downloads + file, os.path.join(dest_path, new_name))
      print(f"Moved: {file} >> {new_name}")
      folder_counts[dest_folder] += 1

    except PermissionError:
      print(f"Permision denied: Could not move {file}")
    except FileExistsError:
      print(f"File already exists: {file}")
    except Exception as e:
      print(f"Error moving {file}: {str(e)}")

if __name__ == "__main__":
  createFolders()
  moveFiles()