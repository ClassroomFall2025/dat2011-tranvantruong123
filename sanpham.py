class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia
    # def doc_giam_gia(self):
    #     return self.__giam_gia
    # def phi_giam_gia(self, giam_gia_moi):
    #     self.__giam_gia=giam_gia_moi
    def nhap_thong_tin(self):
        self.ten_san_pham = input("tên sản phẩm")
        self.gia = float(input('GIÁ'))
        self.giam_gia = float(input("giảm giá:"))
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def xuat_thong_tin(self):
        print(f"sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá hết {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")
    def _str_(self):
        return(f"sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá hết {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")


