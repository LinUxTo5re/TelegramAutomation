import easyocr

# Define the path to your image
image_path = 'photo_2023-09-10_21-36-37.jpg'  # Replace with the path to your image

# Create an OCR reader
reader = easyocr.Reader(['en'])  # Specify the language(s) you want to use

# Extract text from the image
result = reader.readtext(image_path)

# Print or process the extracted text
for detection in result:
    print(detection[1])
