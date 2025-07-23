# 아래에 코드를 작성하시오.

class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name
    
    def reserve_seat(self):
        if self.total_seats - self.reserved_seats > 0:
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        else:
            print("좌석 부족으로 인해 예약에 실패했습니다.")
    
    def current_status(self):
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")


theater1 = MovieTheater("메가박스", 100)
theater2 = MovieTheater("CGV", 100)

print(theater1)
#print(theater2)

theater1.reserve_seat()
theater1.reserve_seat()
theater1.reserve_seat()

theater1.current_status()