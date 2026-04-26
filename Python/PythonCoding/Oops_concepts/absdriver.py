

from Oops_concepts.rectangle import Rectangle
from Oops_concepts.square import Square

sqobj = Square(10)

print(f'Area : {sqobj.calculate_area()} \t Perimeter: {sqobj.calculate_perimeter()}')

rect_obj = Rectangle(l=10, b=5)
print(f'Area : {rect_obj.calculate_area()} \t Perimeter: {rect_obj.calculate_perimeter()}')