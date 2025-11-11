import mysql.connector
from mysql.connector import Error
def connect_mysql():
    """ Kết nối đến MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Đã sửa lại mật khẩu rỗng
            database='quanlynhathuocankhang' # Đã sửa lại đúng tên database
        )

        if connection.is_connected():
            print('Kết nối MySQL thành công!')
            return connection

    except Error as e:
        print(f"Lỗi khi kết nối MySQL: {e}")
        return None