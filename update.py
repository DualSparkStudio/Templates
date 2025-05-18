import os
import re

TEMPLATES_DIR = "D:/work/templates"

REPLACEMENT_HTML = '''<p class="mb-0 fs--1 text-700">&copy; This template is made with&nbsp;<svg class="bi bi-suit-heart-fill" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1z"></path></svg>&nbsp;by&nbsp;<a class="text-700" href="https://www.dualsparkstudio.com/" target="_blank">DualSpark Studio</a></p>'''

def replace_in_html_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(subdir, file)
                print(f"🔍 Checking: {file_path}")
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Look for the target text
                if re.search(r'<p[^>]*?(copyright|©).*?</p>', content, re.IGNORECASE | re.DOTALL):
                    print("   ✅ Match found! Replacing...")
                    new_content = re.sub(
                        r'<p[^>]*?(copyright|©).*?</p>',
                        REPLACEMENT_HTML,
                        content,
                        flags=re.IGNORECASE | re.DOTALL
                    )
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                else:
                    print("   ❌ No matching copyright line.")

replace_in_html_files(TEMPLATES_DIR)
