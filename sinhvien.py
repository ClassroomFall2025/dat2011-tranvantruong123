class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_mon):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.__diem = diem_mon

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self.__diem}")
    
class SinhVienXLDL:
    def __init__(self, ma_sv, ho_ten, diem_mon,lap_trinh):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.__diem = diem_mon
        self.lap_trinh = lap_trinh

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self.__diem}, Lập trình: {self.lap_trinh}")
SV1 = SinhVienXLDL("PS44496","Văn Trương",7,"Python")
SV1.xuat_thong_tin_sv()

# class SinhVien:

#     def __init__(self, ten_sv, namsinh_sv, diem_mon):
#         self.ten_sinh_vien = ten_sv
#         self.nam_sinh = namsinh_sv
#         self.diem = diem_mon

#     def xuat_thong_tin_sv(self):
#         print(f"Sinh viên {self.ten_sinh_vien}, sinh năm {self.nam_sinh}, có điểm môn {self.diem}")
#     def __str__(self):
#         return f"sinh viên (self .ten_sinh_vien), sinh viên 


# class sinhvienXLDL:
#     def __init__(self, ten_sv, namsinh_sv, diem_mon,lap_trinh):
#         SinhVien.__init__(self,ten_sv,namsinh_sv,diem_mon)
#         self.lap_trinh = lap_trinh

#     def xuat_thong_tin_sv(self):
#         print(f"{SinhVien.xuat_thong_tin_sv(self)} và học lập trình {self.lap_trinh}")
        

# sv1 = sinhvienXLDL("hiền",2006,8,"python")
# sv1.xuat_thong_tin_sv()

class SinhVienXLDL(SinhVien):
    def init_(self, ma_sv, ho_ten, diem_mon,lap_trinh):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self. diem = diem_mon
        self.lap_trinh = lap_trinh

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self. diem}, Lập trình: {self.lap_trinh}")
SV1= SinhVienXLDL("PS45187","Sabini Cavini Sabyn ",10,"Python")
SV1.xuat_thong_tin_sv()

## lớp con kế thừa
class SinhVienUDPM(SinhVien):
    def _init_(self, ma_sv, ho_ten, diem_mon, lap_trinh, mang):
        super() .__init__(ma_sv, ho_ten, diem_mon)
        self.lap_trinh = lap_trinh
        self.mang = mang

    def xuat_thong_tin_sv(self):
        super().xuat_thong_tin_sv()
        print(f"Lap trinh: {self.lap_trinh}, Mang: {self.mang}")