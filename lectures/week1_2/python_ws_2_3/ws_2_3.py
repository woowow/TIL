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
            self.print_success()
        else:
            self.print_fail()
    
    def current_status(self):
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")

    def print_success(self):
        print("좌석 예약이 완료되었습니다.")

    def print_fail(self):
        print("좌석 부족으로 인해 예약에 실패했습니다.")


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
theater2 = MovieTheater("CGV", 100)

# print(theater1)
# #print(theater2)

# theater1.reserve_seat()
# theater1.reserve_seat()
# theater1.reserve_seat()

# theater1.current_status()

vip1 = VIPMovieTheater("롯데시네마", 4, 3)
vip1.reserve_seat()
vip1.reserve_seat()
vip1.reserve_seat()
vip1.reserve_seat()
vip1.reserve_seat()