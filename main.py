import cv2,pytesseract

#if os.path.exists("")

image = cv2.imread('img/doc01.png')

print(image.shape)
# cv2.imshow('Original', image)
# #image [linha , colunas, pixels]

# image[:,:,0] = 0
# cv2.imshow('Zeros', image)

# cv2.waitKey(0)


texto = pytesseract.image_to_string(image)

print(texto)


