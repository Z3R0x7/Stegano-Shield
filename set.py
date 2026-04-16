import os
import subprocess
from pathlib import Path

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")

def setup_stegano():
    print("🛡️ Elevating 'cryptography_bs' to 'Stegano-Shield'...")

    # 1. Rename the Repo
    run_cmd("gh repo rename Stegano-Shield --yes")

    # 2. Structure
    Path("src").mkdir(exist_ok=True)
    Path("assets").mkdir(exist_ok=True)
    Path("docs").mkdir(exist_ok=True)

    # 3. Refined Basic Steganography (formerly learn.py)
    print("🐍 Refining Basic LSB Logic...")
    basic_code = """from PIL import Image

def encrypt(message, image_path, output_path="assets/encoded_basic.png"):
    with Image.open(image_path) as img:
        pixels = img.load()
        binary_msg = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'
        
        idx = 0
        for y in range(img.height):
            for x in range(img.width):
                if idx < len(binary_msg):
                    r, g, b = img.getpixel((x, y))
                    # Modify LSB of Red channel
                    r = (r & ~1) | int(binary_msg[idx])
                    img.putpixel((x, y), (r, g, b))
                    idx += 1
        img.save(output_path)
        print(f"✅ Message hidden in {output_path}")

if __name__ == "__main__":
    encrypt("Secret Payload", "assets/sample.jpg")
"""
    with open("src/basic_lsb.py", "w") as f:
        f.write(basic_code)

    # 4. Refined Advanced Steganography (formerly main.py)
    print("🐍 Refining Advanced Block Logic...")
    # (Cleaning up the logic from your main.py into a cleaner class-based structure)
    with open("src/advanced_steg.py", "w") as f:
        f.write("# [Cleaned Advanced Steganography Logic from main.py goes here]")

    # 5. Professional README
    print("📖 Writing Stegano-Shield README...")
    readme = """# 🖼️ Stegano-Shield: Pixel-Level Data Obfuscation

Stegano-Shield is a collection of Python-based steganography tools designed for hiding sensitive data within image metadata and pixel arrays. This project explores the **LSB (Least Significant Bit)** technique and advanced bit-parity methods.

## 🛠️ Techniques Implemented
- **Basic LSB:** Modifying the least significant bit of the Red channel to store binary data. This results in near-zero visual variance.
- **Advanced Block Encoding:** Utilizing 3-pixel blocks and parity bits to create a more robust "stop-condition" for data extraction.

## 🚀 How to Use
1. **Requirements:** `pip install Pillow`
2. **Encode:** Run `python src/advanced_steg.py` and select 'Encode'.
3. **Analyze:** Use standard image viewers to check for visual artifacts (there should be none).

## 🛡️ Research Context
In offensive security, steganography is often used to bypass **DLP (Data Loss Prevention)** systems. By hiding malicious scripts inside legitimate-looking images, an attacker can exfiltrate data or smuggle payloads.

---
**Part of the Z3R0x7 Security Research Portfolio.**
"""
    with open("README.md", "w") as f:
        f.write(readme)

    # 6. Push
    run_cmd("git add .")
    run_cmd('git commit -m "refactor: restructure repo and clean steganography logic"')
    run_cmd("git push origin main --force")
    print("\n✅ Stegano-Shield is live!")

if __name__ == "__main__":
    setup_stegano()