# Лабораторная работа №3

### Зависимости:
#### Python 3.x
#### OpenCV (cv2)
#### NumPy
#### scikit-image
#### Pillow (PIL)
#### Tkinter (обычно включен в Python)

### Функциональность
#### Адаптивный порог:

Эта функция применяет адаптивный порог к загруженному изображению.
Она вычисляет адаптивный порог с использованием фильтра Гаусса и отображает результат.
 
#### Обнаружение углов:

Эта функция обнаруживает углы на загруженном изображении с использованием метода обнаружения углов Харриса.
Обнаруженные углы выделены красным цветом.

#### Обнаружение линий:

Эта функция обнаруживает линии на загруженном изображении с использованием вероятностного преобразования Хафа.
Обнаруженные линии нарисованы синим цветом на изображении.

#### Перепад яркости:

Эта функция вычисляет градиент яркости на загруженном изображении с использованием оператора Собеля.
Градиентное изображение отображается.

#### Глобальный порог (Верхний):

Эта функция применяет глобальный порог к загруженному изображению.
Она использует метод Оцу и инвертирует пороговое изображение.
#### Глобальный порог (Нижний):

Эта функция применяет глобальный порог к загруженному изображению.
Она использует метод Оцу без инверсии.