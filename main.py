import cv2
import numpy as np
from numpy.lib.function_base import copy
from GreenEye import Eagle
# Подключение дополнительных модулей

cap = cv2.VideoCapture(r"road_Trim1.mp4")

if not cap.isOpened():
    print('не найдени файл')
    exit()

while cv2.waitKey(1) != 27:
    reading = val, img = cap.read()  # Чтение кадров
    if not val:  # Если кадры кончились
        print('Работа завершена')
        exit()
    try:
        Eagle(reading)  # Создаем класс Eagle
    except:
        pass
