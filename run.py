import os

scripts = {
    "1": ("Bilder optimieren", "01_media/optimize.py"),
    "2": ("Downloads aufräumen", "02_automation/cleanup.py")
}

print("--- Tool-Box ---")
for key, (name, _) in scripts.items():
    print(f"[{key}] {name}")

choice = input("Wähle ein Tool: ")
if choice in scripts:
    os.system(f"python {scripts[choice][1]}")