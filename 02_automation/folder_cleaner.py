import os
import shutil

def organize_folder():
    extensions = {
        "Images": [".jpg", ".png", ".svg", ".gif"],
        "Docs": [".pdf", ".docx", ".txt"],
        "Code": [".py", ".html", ".css", ".js"]
    }

    for file in os.listdir("."):
        ext = os.path.splitext(file)[1].lower()
        for folder, ext_list in extensions.items():
            if ext in ext_list:
                os.makedirs(folder, exist_ok=True)
                shutil.move(file, os.path.join(folder, file))
                print(f"Verschoben: {file} -> {folder}")

if __name__ == "__main__":
    organize_folder()