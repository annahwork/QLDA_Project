from ketnoi.ketnoi_mysql import connect_mysql
from mysql.connector import Error


def update_danhmuc(madm, tendm, mota):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        data = (tendm, mota, madm)

        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Đã cập nhật danh mục có ID = {madm}")
        else:
            print(f"Không tìm thấy danh mục có ID = {madm}")

    except Error as e:
        print(f"Lỗi khi cập nhật danh mục: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()