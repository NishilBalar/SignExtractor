#unsharping an image

import cv2

def soften_mask(image):

    # perform GaussianBlur filter to use it in unsharpening mask
    gaussian_3 = cv2.GaussianBlur(image, (9, 9), 10.0)
    # calculates the weighted sum of two arrays (source image and GaussianBlur filter) to perform unsharpening mask
    soften_image = cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
    # return unsharpened image
    return soften_image