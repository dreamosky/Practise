import cv2
img = cv2.imread("D:\Picture\zxp\DSC_3372a.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()