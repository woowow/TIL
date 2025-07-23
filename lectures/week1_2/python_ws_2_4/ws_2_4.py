# 아래에 코드를 작성하시오.
# 아래에 코드를 작성하시오.

class MovieTheater:

    total_movies = 0

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.total_movies

    def reserve_seat(self):
        if self.total_seats - self.reserved_seats > 0:
            self.reserved_seats += 1
            self.print_success()
        else:
            self.print_fail()
    
    def current_status(self):
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")

    def print_success(self):
        print("좌석 예약이 성공적으로 완료되었습니다.")

    def print_fail(self):
        print("좌석 부족으로 인해 예약에 실패했습니다.")
    
    def add_movie(cls):
        cls.total_movies += 1
        print("영화가 성공적으로 추가되었습니다.")
    
    def description(self):
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")
        
    def print_movies(cls):
        print(f"총 영화 수: {cls.total_movies}")

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats
        self.reserved_vip_seat = 0
    
    def reserve_vip_seat(self):
        if self.vip_seats - self.reserved_vip_seat > 0:
            self.reserved_vip_seat += 1
            self.reserved_seats += 1
            self.print_success()
        else:
            self.print_fail()
    
    def reserve_seat(self):
        vip_seats_count = self.vip_seats - self.reserved_vip_seat

        if vip_seats_count > 0:
            self.reserve_vip_seat()
        elif self.total_seats - self.reserved_seats > 0:
            self.reserved_seats += 1
            super().print_success()
        else:
            super().reserve_seat()
    
    def print_success(self):
        print("VIP 좌석 예약이 완료되었습니다.")
    
    def print_fail(self):
        print("예약 가능한 VIP 좌석이 없습니다.")    

theater1 = MovieTheater("메가박스", 100)
theater2 = MovieTheater("CGV", 150)

# print(theater1)
# #print(theater2)

theater1.reserve_seat()
theater1.reserve_seat()
theater2.reserve_seat()
theater1.add_movie()
theater1.add_movie()

theater1.current_status()
theater2.current_status()

theater1.print_movies()
theater1.description()

# vip1 = VIPMovieTheater("롯데시네마", 4, 3)
# vip1.reserve_seat()
# vip1.reserve_seat()
# vip1.reserve_seat()
# vip1.reserve_seat()
# vip1.reserve_seat()