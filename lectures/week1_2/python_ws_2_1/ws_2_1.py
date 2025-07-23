# 아래에 코드를 작성하시오.

class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name

theater1 = MovieTheater("메가박스", 100)
theater2 = MovieTheater("CGV", 100)
print(theater1)
print(theater2)