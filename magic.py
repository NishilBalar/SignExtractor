import color_adjust
import cv2
import crop_edge
import sign_extractor
import soften

source_image = cv2.imread("test.jpg")
img = 0

#First_stage: Cropping document part from an image
img = crop_edge.crop_img(source_image)
cv2.imwrite("s1-page_cropped.jpg", img)
print("- stage 1 completed - cropping is done")

#Second stage: Extract signatute from the document
img = sign_extractor.extract_sign(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.imwrite("s2-sign_extracted.jpg", img)
print("- stage 2 completed - signature extraction is done")

#Third Stage : Soften image (unsharping) 
soften.soften_mask(img)
cv2.imwrite("s3-soften_mask.jpg", img)
print("- stage 3 completed - softening (unsharpening mask) is done")

#Fourth Stage : adjusting image brightness and contrast
img = color_adjust.funcBrightContrast(img)
cv2.imwrite("s4-color_adjusted.jpg", img)
print("- stage 4 completed - colour adjustion is done")

cv2.imwrite("output.jpg", img)