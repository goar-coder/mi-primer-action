import sys
import platform
from datetime import datetime

def main():
    print("¡Hola desde GitHub Actions! 🚀")
    print(f"Versión de Python: {sys.version}")
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Fecha y hora de ejecución: {datetime.now()}")

if __name__ == "__main__":
    main()
