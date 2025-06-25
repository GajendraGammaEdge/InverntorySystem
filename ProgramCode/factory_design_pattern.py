from abc import  ABC , abstractmethod
class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectange(Shapes):
    def area(self,l,b):
       # l=int(input())
       # b=int(input())
       print('Area of the Rectangle',l*b)

class Circle(Shapes):
    def area(self,r):
        # r = int(input())
        print("Area of cicle", 2*3.14*r*r)

class ShapesFactory:
    def get_area(self,area_type):
        if area_type is None:
            return  None
        area_type =area_type.lower()

        if area_type == 'rectangle':
            return Rectange()
        if area_type == 'circle':
            return Circle()

        else:
            return f'The Unknown shape {area_type}'


if __name__ == '__main__':
    fac = ShapesFactory()

    sh1 = fac.get_area("rectangle")
    sh1.area(4,5)

    sh2  =fac.get_area("circle")
    sh2.area(7)
