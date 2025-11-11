from common.insert_danhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")

    insert_danhmuc(ten, mota)

    con = input("TIẾP TỤC Y, THOÁT THÌ NHẤN BẤT KỲ: ")
    if con != 'Y':
        break