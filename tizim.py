import platform
import os

def noutbuk_malumoti():
    print("--- HP Noutbuk Tizim Malumotlari ---")
    print(f"Operatsion tizim: {platform.system()} {platform.release()}")
    print(f"Protsessor: {platform.processor()}")
    print(f"Mashina turi: {platform.machine()}")
    print(f"Foydalanuvchi: {os.getlogin()}")
    print("-" * 35)

if __name__ == "__main__":
    noutbuk_malumoti()