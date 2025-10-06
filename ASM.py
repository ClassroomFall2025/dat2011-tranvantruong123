def nhap_ds_nv():
    print(">>> Chức năng: Nhập danh sách nhân viên và lưu file")

def doc_ds_nv():
    print(">>> Chức năng: Đọc danh sách nhân viên từ file và xuất ra màn hình")

def tim_nv_ma():
    print(">>> Chức năng: Tìm nhân viên theo mã")

def xoa_nv():
    print(">>> Chức năng: Xóa nhân viên theo mã")

def capnhat_nv():
    print(">>> Chức năng: Cập nhật thông tin nhân viên theo mã")

def tim_nv_luong():
    print(">>> Chức năng: Tìm nhân viên theo khoảng lương")

def sapxep_ten():
    print(">>> Chức năng: Sắp xếp nhân viên theo họ tên")

def sapxep_thunhap():
    print(">>> Chức năng: Sắp xếp nhân viên theo thu nhập")

def top5_nv():
    print(">>> Chức năng: Xuất 5 nhân viên có thu nhập cao nhất")

def menu():
    while True:
        print("===== Menu HỆ THỐNG QUẢN LÝ NHÂN SỰ - CÔNG TY RỒNG VIỆT =====:")
        print("nhập danh sách nhân viên")
        print("2 đọc thông tin nhân viên từ file")
        print("3 tính và hiển thị thông tin nhân viên theo mã")
        print("4 xóa nhân viên theo mã,cập nhật file dữ liệu")
        print("5cập nhật thông tin nhân viên theo mã và cập nhật file dữ liệu")
        print("6tìm các nhân viên có lương trong khoảng nhập từ bàn phím")
        print("7sắp xếp nhân viên theo họ và tên")
        print("8sắp xếp nhân viên theo lương")
        print("Xuất 5 thông tin nhân viên có lương cao nhất")
        print("0 thoát chương trình")
        chon = input("mời bạn chọn chức năng: ")
        if chon == '1':
            print(">>>> bạn đã chọn chức năng 1") 
        elif chon == '2':
            print(">>>> bạn đã chọn chức năng 2")
        elif chon == '3':
            print(">>>> bạn đã chọn chức năng 3")
        elif chon == '4':
            print(">>>> bạn đã chọn chức năng 4")
        elif chon == '5':
            print(">>>> bạn đã chọn chức năng 5")
        elif chon == '6':
            print(">>>> bạn đã chọn chức năng 6")
        elif chon == '7':
            print(">>>> bạn đã chọn chức năng 7")
        elif chon == '8':
            print(">>>> bạn đã chọn chức năng 8")
        elif chon == '9':
            print(">>>> bạn đã chọn chức năng 9")
        elif chon == '0':
            print(">>>> bạn đã thoát chương trình")
            break
      