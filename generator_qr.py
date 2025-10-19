import qrcode

# Data for QR
data = "Product ID: 12345 | Name: Hamza Perfume | Price: 1200"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR Code
img.save("qr_code.png")

print("✅ QR code generated successfully! (qr_code.png)")
