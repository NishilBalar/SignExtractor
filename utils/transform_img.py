import cv2
import numpy as np


def transform_image_for_cropping(img, pts):
    ## Assign point to right corner of image
    s = pts.sum(axis=1)
    tl = pts[np.argmin(s)]  # top-left point --> minimum sum
    br = pts[np.argmax(s)]  # bottom-right point --> maximum point

    diff = np.diff(pts, axis=1)  # for remaining two points
    tr = pts[np.argmin(diff)]  # top-right point  --> minimum difference
    bl = pts[np.argmax(diff)]  # bottom-left point --> max difference

    ##Compute Width of New Image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))  # choosing maximum of top and bottom width

    ##Compute Height of New Image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(
        int(heightA), int(heightB)
    )  # choosing maximum of rights side and left side width

    ##Create destination points for BIRD EYE VIEW
    dst = np.array(
        [[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]],
        dtype="float32",
    )

    # Apply Perspective Transformation
    M = cv2.getPerspectiveTransform(np.array([tl, tr, br, bl], dtype="float32"), dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))  # apply on input image

    return warped
