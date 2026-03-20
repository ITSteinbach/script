import os

def find_todos():
    print("Offene Aufgaben im Code:\n")
    for file in os.listdir("."):
        if file.endswith(".py") and file != "run.py":
            with open(file, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if "TODO:" in line:
                        print(f"[{file} Line {i}]: {line.strip()}")

if __name__ == "__main__":
    find_todos()