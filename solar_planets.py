import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(
    img, 'Sun', (90,50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2, color=(0,0,255)
)

cv2.putText(
    img, 'Mercury', (123,254), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255)
)

cv2.putText(
    img, 'Venus', (195,170), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255)
)

cv2.putText(
    img, 'Earth', (293,265), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255)
)

cv2.putText(
    img, 'Mars', (388,255), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255)
)

cv2.putText(
    img, 'Jupiter', (540,385), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255)
)

cv2.putText(
    img, 'Saturn', (770,310), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.75, color=(255,255,255)
)

cv2.putText(
    img, 'Uranus', (970,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.65, color=(255,255,255)
)

cv2.putText(
    img, 'Neptune', (1120,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.55, color=(255,255,255)
)

cv2.imshow('output',img)

cv2.imwrite('solar-system.jpg',img)

cv2.waitKey(0)
