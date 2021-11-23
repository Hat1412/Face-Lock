from tkinter import *
import cv2, face_recognition

root = Tk()
passw = StringVar()
cam = cv2.VideoCapture(0)
universal_font = ("Times New Roman", 40)

BG = "#B5E61D"
FG = "#B97A57"
EC = "#22B14C"
root.config(bg = BG)


def cls(fr):
    for widgets in fr.winfo_children():
        widgets.destroy()

def lck():
    _, frame = cam.read()

    cv2.imwrite("tmp.png", frame)
    known_image = face_recognition.load_image_file("File path to your face picture")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    unknown_image = face_recognition.load_image_file("tmp.png")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    cam.release()

    try:
        return results
    except IndexError:
        cam.release()
        return False

def chk(tmp):
    if passw.get() ==  "My_Secret":
        entry = lck()

        if entry:
            root.unbind("<Return>")
            print("Access Granted")


Entry(root, textvariable = passw, font = universal_font, show = "*", bg = FG).pack()

root.bind("<Return>", chk)
root.mainloop()
