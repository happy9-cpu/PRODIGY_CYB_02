from PIL import Image

# Encrypt image by modifying RGB values using a key
def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    encrypted = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # Apply encryption logic
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted.putpixel((x, y), (r, g, b))

    encrypted.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


# Decrypt image by reversing RGB value shift
def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    decrypted = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # Apply decryption logic
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted.putpixel((x, y), (r, g, b))

    decrypted.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# Main program loop
def main():
    print("===== Image Encryption Tool =====")
    choice = input("Do you want to Encrypt (E) or Decrypt (D)? ").upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Enter E or D.")
        return

    image_path = input("Enter the path to the image (e.g. test.jpg): ")
    try:
        key = int(input("Enter the key (a number between 1 and 255): "))
        if not (1 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter a number between 1 and 255.")
        return

    if choice == 'E':
        output_path = "encrypted_image.png"
        encrypt_image(image_path, key, output_path)
    else:
        output_path = "decrypted_image.png"
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
