class Road:
    def __init__(self, _length, _width):
        self._length = float(_length)
        self._width = float(_width)

    def raschet(self, weight=25, thickness=5):
        raschet_ = self._length * self._width * weight * thickness
        return print(f"Масса асфальта для покрытия всего дорожного полотна:"
                     f" {round(raschet_ / 1000, 1)} т.")


try:
    a = Road(float(input("Введите длину в м.: ")), float(input("Введите ширину в м.: ")))
    a.raschet()
except:
    print("Введите числа")
