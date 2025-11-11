from common.update_danhmuc import update_danhmuc

while True:
    madm = input("Nhập vào mã danh mục: ")
    tendm = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")

    update_danhmuc(madm, tendm, mota)

    con = input("TIẾP TỤC Y, THOÁT THÌ NHẤN BẤT KỲ: ")
    if con != 'Y':
        break