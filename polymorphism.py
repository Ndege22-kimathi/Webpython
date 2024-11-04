#Same methods, different implementations- poly and morph


class Rectangle:
    def shape(self):
        print("Drawing a Rectangle")


class Parallelogram:
    def shape(self):
        print("Drawing a Parallelogram")

class Rhombus:
    def shape(self):
        print("Drawing a Rhombus")


r = Rectangle()
r.shape()

p = Parallelogram()
p.shape()

rhom = Rhombus()
rhom.shape()