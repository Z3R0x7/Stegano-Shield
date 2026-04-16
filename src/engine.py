import os
import zlib
import numpy as np
from PIL import Image
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

class SteganoShield:
    def __init__(self, password: str):
        # Professional Key Derivation (PBKDF2)
        salt = b'\\x00' * 16  # In production, use a unique salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.fernet = Fernet(key)

    def _prepare_data(self, data: str) -> str:
        # Encrypt and Compress
        encrypted = self.fernet.encrypt(data.encode())
        compressed = zlib.compress(encrypted)
        # Convert to binary
        return ''.join(format(b, '08b') for b in compressed) + '1111111111111110'

    def encode(self, img_path: str, message: str, output_path: str):
        img = Image.open(img_path).convert('RGB')
        pixels = np.array(img)
        
        binary_data = self._prepare_data(message)
        if len(binary_data) > pixels.size:
            raise ValueError("❌ Data too large for this image capacity.")

        # Flatten pixels and modify LSB
        flat_pixels = pixels.flatten()
        for i in range(len(binary_data)):
            flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_data[i])
            
        new_pixels = flat_pixels.reshape(pixels.shape)
        encoded_img = Image.fromarray(new_pixels.astype('uint8'))
        encoded_img.save(output_path)
        print(f"✅ Securely encoded to {output_path}")

    def decode(self, img_path: str) -> str:
        img = Image.open(img_path).convert('RGB')
        pixels = np.array(img).flatten()
        
        binary_data = ""
        for p in pixels:
            binary_data += str(p & 1)
            if binary_data.endswith('1111111111111110'):
                break
        
        binary_data = binary_data[:-16] # Remove delimiter
        byte_data = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))
        
        try:
            decrypted = self.fernet.decrypt(zlib.decompress(byte_data))
            return decrypted.decode()
        except Exception:
            return "❌ Decryption failed. Incorrect password or corrupted data."

if __name__ == "__main__":
    # Quick Test logic
    engine = SteganoShield("SpartanProtocol117")
    # engine.encode("assets/input.png", "Top Secret Intel", "assets/hidden.png")
