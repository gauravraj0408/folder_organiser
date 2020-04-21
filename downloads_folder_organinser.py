# Author : Gaurav Raj
# Website : http://gauravraj.gq/
# Please give a credit if you use it or modify it
# Thank You...
# Credit : JanB0 
# profile : https://github.com/JanB0/

# imports:
import os
import shutil
print("""
\t╔══════════════════════════════════════╗
\t║     Folders Organiser Started !!!    ║
\t╚══════════════════════════════════════╝
""")
def create_folders(directories, directory_path):
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(directory_path + '/' + key)
    if "OTHER" not in os.listdir(directory_path):
        os.mkdir(directory_path + '/' + "OTHER")

def organize_folders(directories, directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break

def organize_remaining_files(directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)

def organize_remaining_folders(directories, directory_path):
    list_dir = os.listdir(directory_path)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = directory_path + '/' + folder
            dest_path = os.path.join(directory_path, "Folders", folder)
            shutil.move(src_path, dest_path)
try:
    if __name__ == '__main__':
        directory_path = "C:/Users/gaura/Downloads"
        directories = {
            "HTML": (".html5", ".html", ".htm", ".xhtml"),
            "Images": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                       "svg",
                       ".heif", ".psd"),
            "Videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                       ".mng",
                       ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
            "Documents": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                          ".ods",
                          ".odt", ".pdf", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                          ".rvg", ".rtf", ".txt", ".in", ".out", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                          "pptx"),
            "Compressed": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                         ".dmg", ".rar", ".xar", ".zip"),
            "Audio": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                      ".mp3",
                      ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
            "Python": ".py",
            "Programs": ".exe",
            "Others": "",
            "Folders": ""
        }
        print(" Creating Folders...\n")
        try:
            if os.path.exists():
                pass
            else:
                create_folders(directories, directory_path)
        except Exception as err2:
            print(" Some Folders Exists Already...")
        # create_folders(directories, directory_path)
        print("\n Folders Successfully Created...\n\n Organising Folders...\n")
        organize_folders(directories, directory_path)
        print(" Folders organised Successfully...\n\n Organising Remaining Folders...\n")
        organize_remaining_files(directory_path)
        print(" Moving Folders inside Created \"Folders...\" \n")
        organize_remaining_folders(directories, directory_path)
        print(" Folders organising Successful...\n")
except Exception as error:
    print(error, "Exiting Program...")
print("""
\t╔══════════════════════════════════════╗
\t║   Folders Organising Completed !!!   ║
\t╚══════════════════════════════════════╝
""")
