# 🖼️ Stegano-Shield: Pixel-Level Data Obfuscation

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
