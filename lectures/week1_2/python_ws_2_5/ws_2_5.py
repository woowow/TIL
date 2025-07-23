# 아래에 코드를 작성하시오.

class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def reserve_seat(self):
        if self.total_seats > self.reserved_seats:
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        else:
            print("좌석 예약에 실패했습니다.")

class MovieTheater(Theater):

    total_movies = 0

    def __init__(self, name, total_seats, total_movies):
        super().__init__(name, total_seats)
        self.total_movies = total_movies
    
    def add_movie(cls):
        cls.total_movies += 0
    
    def description(self):
        print(f"영화관 이름: {self.name}")
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")
        print(f"총 영화 수: {self.total_movies}")

mt1 = MovieTheater("메가박스", 100, 1)
mt1.reserve_seat()
mt1.reserve_seat()
mt1.description()