from ketnoi.ketnoi_mysql import connect_mysql
from mysql.connector import Error


def delete_danhmuc(madm):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()

        # Xóa sản phẩm trước (do có khóa ngoại)
        cursor.execute("DELETE FROM sanpham WHERE madm = %s", (madm,))

        # Sau đó mới xóa danh mục
        cursor.execute("DELETE FROM danhmuc WHERE madm = %s", (madm,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Đã xóa danh mục có ID = {madm} và các sản phẩm liên quan.")
        else:
            print(f"Không tìm thấy danh mục có ID = {madm}")

    except Error as e:
        print(f"Lỗi khi xóa danh mục: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
