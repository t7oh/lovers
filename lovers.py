
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type
import random
import os
from datetime import datetime

# عرض صورة الجمجمة
print("\033[91m")
print(r'''
               ██████████
           ████▒▒▒▒▒▒▒▒████
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
       ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒██
      ██▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒██
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██
       ██▒▒███████████████▒▒██
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
           ████▒▒▒▒▒▒▒▒████
               ██████████
''')
print("\033[0m")

# عرض الاسم تحت الجمجمة باللون الأحمر وبخط كبير
print("""
\033[91m
I   L O V E
D A N A ,
R U B Y ,
R E E M A
\033[0m
""")

def analyze_number(phone):
    try:
        parsed = phonenumbers.parse(phone)
    except phonenumbers.NumberParseException:
        print("❌ رقم غير صالح")
        return

    if not phonenumbers.is_valid_number(parsed):
        print("❌ رقم غير صحيح أو غير مدعوم")
        return

    info = {
        "رقم الهاتف": phone,
        "الدولة": geocoder.description_for_number(parsed, "ar"),
        "شركة الاتصال": carrier.name_for_number(parsed, "ar"),
        "نوع الرقم": number_type(parsed),
        "التوقيت": timezone.time_zones_for_number(parsed)
    }

    fake_emails = [
        "userx91@protonmail.com",
        "ksa_user92@mail.ru",
        "fahad1995@gmail.com",
        "leaked.acc@tuta.io"
    ]
    leaks = [
        "https://darkbin.io/lookup?id=" + phone[-4:],
        "https://leakbase.pw/user?q=" + phone,
        "https://datadump.cx/dark?id=" + phone[-5:]
    ]

    print("\n📄 المعلومات:")
    for k, v in info.items():
        print(f"- {k}: {v}")

    print("\n📧 الإيميلات المسربة المحتملة:")
    for email in random.sample(fake_emails, 2):
        print(f"- {email}")

    print("\n🌐 روابط OSINT مزعومة:")
    for l in leaks:
        print(f"- {l}")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/{phone.strip('+')}_{ts}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("📄 تقرير رقم الهاتف\n\n")
        for k, v in info.items():
            f.write(f"- {k}: {v}\n")
        f.write("\n📧 الإيميلات:\n")
        for email in fake_emails:
            f.write(f"- {email}\n")
        f.write("\n🌐 روابط OSINT:\n")
        for l in leaks:
            f.write(f"- {l}\n")

    print(f"\n✅ تم حفظ التقرير في: {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("📌 الاستخدام: python3 dragon_hunter.py +9665XXXXXXX")
    else:
        analyze_number(sys.argv[1])
