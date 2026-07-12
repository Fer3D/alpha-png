from PIL import Image
import os
import glob

carpeta = os.path.dirname(os.path.abspath(__file__))

pngs = glob.glob(os.path.join(carpeta, "*.png"))

if not pngs:
    print("No se encontraron archivos PNG en esta carpeta.")
else:
    print(f"Se encontraron {len(pngs)} archivos PNG.\n")

    for archivo in pngs:
        nombre = os.path.basename(archivo)

        try:
            img = Image.open(archivo)

            if "A" not in img.getbands():
                print(f"[NO] {nombre} -> No tiene canal alfa.")
            else:
                alpha = img.getchannel("A")
                minimo, maximo = alpha.getextrema()

                if minimo < 255:
                    print(f"[SI] {nombre} -> Usa transparencia.")
                else:
                    print(f"[NO] {nombre} -> Tiene canal alfa, pero todos los píxeles son opacos.")

        except Exception as e:
            print(f"[ERROR] {nombre}: {e}")

print("\nProceso terminado.")
input("Pulsa ENTER para cerrar...")