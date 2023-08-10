import cv2

#Reading the image file
image=cv2.imread("madara2.jpg",cv2.IMREAD_UNCHANGED)

new_scale=int(input("Enter the factor by which you want to inc/dec the image"))

#new-width and height to change the dimensions
new_width=int(image.shape[1]*new_scale/100)
new_height=int(image.shape[0]*new_scale/100)

result=cv2.resize(image,(new_width,new_height))#resize function to resize the image with new dimensions
cv2.imwrite('newmadara.jpg',result)#creating a new image file
cv2.waitKey(0)