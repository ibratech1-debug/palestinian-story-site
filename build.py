"""
شغّل هذا الملف كل ما أضفت أو حذفت ملفات من مجلد pdfs:

    python build.py

بيقرأ كل ملفات PDF وبيكتب files.js تلقائياً.
اسم الملف بيصير اسم العرض (الشرطات والـ underscore بتتحول لمسافات).
مثال: تقرير_2025.pdf  ->  تقرير 2025
"""
import json
import os
import re

FOLDER = "pdfs"

files = sorted(
    f for f in os.listdir(FOLDER) if f.lower().endswith(".pdf")
)

items = [
    {"name": re.sub(r"[_-]+", " ", os.path.splitext(f)[0]).strip(), "file": f}
    for f in files
]

with open("files.js", "w", encoding="utf-8") as out:
    out.write("const FILES = " + json.dumps(items, ensure_ascii=False, indent=2) + ";\n")

print(f"تم: {len(items)} ملف")
