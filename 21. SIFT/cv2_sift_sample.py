# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np

img = cv2.imread('chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# surf = cv2.SURF(400)
# surf = cv2.xfeatures2d.
# sift = cv2.SIFT()
# kp = sift.detect(gray, None)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

# img = cv2.drawKeypoints(gray, kp)

cv2.imwrite('sift_keypoints.jpg', img)

cv2.drawKeypoints(
    gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints.jpg', img)
