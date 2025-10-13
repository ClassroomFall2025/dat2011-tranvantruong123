class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def chu_vi(self):
        return self.dai + self.rong * 2
    def dien_tich(self):
        return self.dai * self.rong
    def xuat(self):
        print(f"chiều dài:(self.dai):")
        print(f"Chiều rộng: {self.rong}")
        print(f"Diện tích: {self.get_dien_tich()}")
        print(f"Chu vi: {self.get_chu_vi()}")

class Vuong(ChuNhat):
    def __init__(self, canh):
        self.canh=canh
        super().__init__(self.canh, self.canh)

    def xuat(self):
        print(f"cạnh hình vuông:{self.dai}")
        print(f"chu vi hình vuômg:{self.chu_vi()}")
        print(f"diện tích hình vuông:{self.dien_tich()}")
