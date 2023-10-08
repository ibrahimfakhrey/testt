import cv2
image_name=input("write the image name")
image = cv2.imread(image_name, 1)
face_cascade = cv2.CascadeClassifier('faces.xml')



def find_mistre_ramadan(image):
  faces = face_cascade.detectMultiScale(image, 1.1, 4)
  for (x, y, w, h) in faces:
    if x ==806 and y==162 and w==185 and h==185:
      print("this is mister ramadan ")
      cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)
      return True
    else:
      return False


if find_mistre_ramadan(image):
  print("this is the secret")
else:
  print("i didnot find mister ramadan ")


# cv2.imwrite('human_faces.jpeg', image)


