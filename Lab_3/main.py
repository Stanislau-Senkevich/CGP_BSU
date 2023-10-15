import numpy as np
import cv2 as cv
from tkinter import ttk
from tkinter import *
from scipy import ndimage as ndi
from skimage.feature import peak_local_max, canny, corner_peaks, corner_harris
from PIL import ImageTk, Image
from skimage.transform import probabilistic_hough_line


class MainSolution:
    def __init__(self, file):
        self.image = cv.imread(file)
        self.back = None

    def filter(self):
        self.back = cv.cvtColor(cv.pyrMeanShiftFiltering(
            self.image, 15, 50), cv.COLOR_BGR2GRAY)
        img = Image.fromarray(self.back)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def adaptive_threshold(self):
        thresh2 = cv.adaptiveThreshold(self.back, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        img = Image.fromarray(thresh2)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def corner_detection(self):
        corners = corner_peaks(corner_harris(self.back), min_distance=5)
        result = np.zeros_like(self.image)
        result[corners[:, 0], corners[:, 1]] = [255, 0, 0]
        img = Image.fromarray(result)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def line_detection(self):
        edges = canny(self.back)
        lines = probabilistic_hough_line(edges, threshold=15, line_length=3, line_gap=2)
        result = np.zeros_like(self.image)
        for p0, p1 in lines:
            cv.line(result, p0, p1, [255, 0, 0], 1)
        img = Image.fromarray(result)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def brightness_gradient(self):
        gradient_x = cv.Sobel(self.back, cv.CV_64F, 1, 0, ksize=3)
        gradient_y = cv.Sobel(self.back, cv.CV_64F, 0, 1, ksize=3)
        gradient = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
        gradient = (gradient * 255).astype(np.uint8)

        img = Image.fromarray(gradient)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def global_threshold_upper(self):
        ret, thresh1 = cv.threshold(self.back, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        img = Image.fromarray(thresh1)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def global_threshold_lower(self):
        ret, thresh1 = cv.threshold(self.back, 0, 255, cv.THRESH_TOZERO | cv.THRESH_OTSU)
        img = Image.fromarray(thresh1)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)


if __name__ == "__main__":
    root = Tk()
    ms = MainSolution("img/bright.png")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"1400x900")
    ms.filter()

    lbl_text1 = ttk.Label(text=(" " * 8) + "Адаптивная\nпороговая обработка")
    lbl_text1.place(x=30, y=20)
    img1 = ms.adaptive_threshold()
    lbl1 = ttk.Label(image=img1)
    lbl1.place(x=30, y=90, width=300, height=300)

    lbl_text2 = ttk.Label(text="Обнаружение углов")
    lbl_text2.place(x=385, y=50)
    img2 = ms.corner_detection()
    lbl2 = ttk.Label(image=img2)
    lbl2.place(x=370, y=90, width=300, height=300)

    lbl_text3 = ttk.Label(text="Обнаружение линий")
    lbl_text3.place(x=725, y=50)
    img3 = ms.line_detection()
    lbl3 = ttk.Label(image=img3)
    lbl3.place(x=710, y=90, width=300, height=300)

    lbl_text4 = ttk.Label(text="Перепад яркости")
    lbl_text4.place(x=1065, y=50)
    img4 = ms.brightness_gradient()
    lbl4 = ttk.Label(image=img4)
    lbl4.place(x=1050, y=90, width=300, height=300)

    lbl_text5 = ttk.Label(text="Глобальная пороговая обработка\n\t(Верхний порог)")
    lbl_text5.place(x=100, y=430)
    img5 = ms.global_threshold_upper()
    lbl5 = ttk.Label(image=img5)
    lbl5.place(x=210, y=500, width=300, height=300)

    lbl_text6 = ttk.Label(text="Глобальная пороговая обработка\n\t(Нижний порог)")
    lbl_text6.place(x=810, y=430)
    img6 = ms.global_threshold_lower()
    lbl6 = ttk.Label(image=img6)
    lbl6.place(x=900, y=500, width=300, height=300)

    root.mainloop()