import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
from scipy import signal


img = cv2.imread("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003.png")

bilateral = cv2.bilateralFilter(img, 11, 75, 75)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, (5, 5), 7)
cv2.imshow("gauss", gauss)
cv2.waitKey(0)

wiener = signal.wiener(img, 5, 5)
cv2.imshow("wiener", wiener)
cv2.waitKey(0)

siralanmis = np.vstack((img, bilateral, gauss, wiener))
siralanmis2 = np.hstack((img, bilateral, gauss, wiener))
cv2.imshow("siralanmis", siralanmis)
cv2.imshow("siralanmis2", siralanmis2)
cv2.waitKey(0)

cv2.imwrite("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003_bilateral.png", bilateral)
cv2.imwrite("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003_gauss.png", gauss)
cv2.imwrite("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003_wiener3.png", wiener)
cv2.imwrite("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003_siralanmis.png", siralanmis)
cv2.imwrite("C:\\Users\\oguza\\Documents\GitHub\\basic_txt_codes\saglik\\0003_siralanmis2.png", siralanmis2)


cv2.destroyAllWindows()