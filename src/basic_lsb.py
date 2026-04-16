from PIL import Image

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
