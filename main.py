import cv2
from flask import Flask,render_template,request,redirect

app=Flask(__name__)


@app.route ("/")
def start():
    return "start"
@app.route("/check",methods=["GET","POST"])
def check():
    if request.method=="POST":
        file = request.files['image']
        file.save('image.jpg')

        image = cv2.imread("image.jpg", 1)
        face_cascade = cv2.CascadeClassifier('faces.xml')
        faces = face_cascade.detectMultiScale(image, 1.1, 4)
        for (x, y, w, h) in faces:
            print("this is mister ramadan ")
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 4)
        new_image=cv2.imwrite('human_faces.jpeg', image)
        return redirect("/image")
    return render_template("check.html")


@app.route("/image")
def image():
    return render_template("image.html")



if __name__=="__main__":
    app.run(debug=True)