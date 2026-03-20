import os
from PIL import Image

def resize_images(target_width=1200):
    for file in os.listdir("."):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(file)
            # Proportionale Skalierung berechnen
            w_percent = (target_width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            img = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
            img.save(f"resized_{file}")
            print(f"Optimiert: {file}")

if __name__ == "__main__":
    resize_images()