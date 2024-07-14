import cv2 as cv
import numpy as np
from tkinter import *

def process_image(image, lower_range, upper_range):
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_img, lower_range, upper_range)
    color_image = cv.bitwise_and(image, image, mask=mask)
    return color_image

def show_image(image, window_name='Image'):
    cv.imshow(window_name, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def click_action1():
    img = cv.imread('C:/Projekty/Color_Detection/data/zachod.jpg')
    lower_range = (0, 50, 50)
    upper_range = (10, 255, 255)
    color_image = process_image(img, lower_range, upper_range)
    show_image(color_image, 'Color Image')

def click_action2():
    cap = cv.VideoCapture(0)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        color_image = process_image(frame, lower_blue, upper_blue)
        cv.imshow('frame', frame)
        cv.imshow('Color Detection', color_image)
        if cv.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    cv.destroyAllWindows()

root = Tk()
root.title("Color Detection Choice")
root.geometry('600x400+20+20')
click_button1 = Button(root, text="Zdjęcie", width=8, command=click_action1)
click_button1.pack(pady=10)
click_button2 = Button(root, text="Kamera", width=8, command=click_action2)
click_button2.pack(pady=10)
root.mainloop()
