def kirish_tekshiruvi(foydalanuvchi, daraja):
    """Foydalanuvchi huquqini tekshiruvchi funksiya"""
    if daraja == "admin":
        return f"Salom {foydalanuvchi}, tizimga to'liq kirish ruxsat etildi! 🔓"
    elif daraja == "user":
        return f"Salom {foydalanuvchi}, sizda faqat o'qish huquqi bor. 📖"
    else:
        return "Kirish taqiqlandi! 🚫"

# Foydalanuvchidan ma'lumot olamiz
ism = input("Ismingizni kiriting: ")
rol = input("Rolingizni kiriting (admin/user): ").lower()

# Funksiyani chaqiramiz va natijani chiqaramiz
print(kirish_tekshiruvi(ism, rol))
