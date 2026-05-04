import platform
import os
import getpass # Yangi kutubxona qo'shdik

def noutbuk_malumoti():
    print("--- HP Noutbuk Tizim Malumotlari ---")
    print(f"Operatsion tizim: {platform.system()} {platform.release()}")
    print(f"Protsessor: {platform.processor()}")
    print(f"Mashina turi: {platform.machine()}")
    
    # os.getlogin() o'rniga mana buni ishlatamiz:
    foydalanuvchi = getpass.getuser()
    print(f"Foydalanuvchi: {foydalanuvchi}")
    print("-" * 35)

if __name__ == "__main__":
    noutbuk_malumoti()