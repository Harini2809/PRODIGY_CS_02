from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new(img.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple([(p ^ key) for p in pixel])
            encrypted_img.putpixel((x, y), encrypted_pixel)

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    decrypted_img = Image.new(encrypted_img.mode, (width, height))

    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple([(p ^ key) for p in encrypted_pixel])
            decrypted_img.putpixel((x, y), decrypted_pixel)

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    while True:
        image_path = input("Enter the path to the image: ")
        key = int(input("Enter the encryption/decryption key: "))

        encrypt_or_decrypt = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()

        if encrypt_or_decrypt == 'e':
            encrypt_image(image_path, key)
        elif encrypt_or_decrypt == 'd':
            encrypted_image_path = input("Enter the path to the encrypted image: ")
            decrypt_image(encrypted_image_path, key)
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        
        another = input("Do you want to continue? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
