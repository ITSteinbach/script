import os
import subprocess
import sys

def get_scripts():
    script_list = []
    # Gehe durch alle Unterordner (außer versteckte wie .git)
    for root, dirs, files in os.walk("."):
        if ".git" in root or root == ".":
            continue
        
        for file in files:
            if file.endswith(".py") and file != "run.py":
                full_path = os.path.join(root, file)
                script_list.append((file, full_path))
    return sorted(script_list)

def main():
    scripts = get_scripts()
    
    if not scripts:
        print("Keine Skripte in den Unterordnern gefunden.")
        return

    print(f"\n{'='*30}")
    print("      DEVELOPER TOOLBOX")
    print(f"{'='*30}\n")
    
    for i, (name, path) in enumerate(scripts, 1):
        # Zeige den Namen und den Ordner zur Orientierung
        folder = os.path.dirname(path).replace(".\\", "").replace("./", "")
        print(f"[{i}] {name}  ({folder})")

    print("\n[q] Beenden")
    
    choice = input("\nWelches Tool möchtest du starten? ")
    
    if choice.lower() == 'q':
        sys.exit()
        
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(scripts):
            script_path = scripts[idx][1]
            print(f"\nStarte: {scripts[idx][0]}...\n")
            subprocess.run([sys.executable, script_path])
        else:
            print("Ungültige Auswahl.")
    except ValueError:
        print("Bitte eine Zahl eingeben.")

if __name__ == "__main__":
    main()