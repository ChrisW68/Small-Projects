import cv2

#Load a image and have a variable name "img"
img=cv2.imread("galaxy.jpg",0)

#print(type(img))
#print(img)
print(img.shape)
#print(img.ndim)

#Resize the image t be half the original size
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#Show a image on the screen based on resized_image variable
cv2.imshow("Galaxy",resized_image)
#Image window is shown until button is pushed to
cv2.imwrite("Resize_Galaxy.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
