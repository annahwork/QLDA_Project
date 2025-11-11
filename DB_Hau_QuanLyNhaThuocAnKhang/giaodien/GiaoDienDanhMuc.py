# Tệp: giaodien/GiaoDienDanhMuc.py
import tkinter as tk
from tkinter import ttk, messagebox

# Import các hàm xử lý từ thư mục 'common' và 'ketnoidb'
# Đảm bảo các đường dẫn import này khớp với cấu trúc dự án của bạn
try:
    from ketnoidb.ketnoi_mysql import connect_mysql
    from common.get_all_danhmuc import get_all_danhmuc
    from common.insert_danhmuc import insert_danhmuc
    from common.update_danhmuc import update_danhmuc
    from common.delete_danhmuc import delete_danhmuc
except ImportError:
    # Xử lý nếu chạy file trực tiếp mà không qua cấu trúc gói
    print("Không thể import từ common/ketnoidb, thử import thư mục cha...")
    import sys
    import os

    # Thêm thư mục gốc của dự án (DB_Lê Thị Mỹ Hậu) vào Python Path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from ketnoi.ketnoi_mysql import connect_mysql
    from common.get_all_danhmuc import get_all_danhmuc
    from common.insertdanhmuc import insert_danhmuc
    from common.update_danhmuc import update_danhmuc
    from common.delete_danhmuc import delete_danhmuc


# --- CÁC HÀM XỬ LÝ GIAO DIỆN ---

def load_data():
    """Tải dữ liệu từ CSDL lên Treeview"""
    # Xóa tất cả dữ liệu cũ trên cây
    for row in tree.get_children():
        tree.delete(row)

    # Lấy dữ liệu mới từ CSDL (gọi hàm từ common)
    danh_sach = get_all_danhmuc()
    if danh_sach:
        for item in danh_sach:
            # Chèn dữ liệu vào cây
            # Chú ý: Đảm bảo get_all_danhmuc trả về danh sách các dictionary
            # (Hàm get_all_danhmuc của bạn đang trả về dictionary, nên đã đúng)
            tree.insert("", "end", values=(item['madm'], item['tendm'], item['mota']))


def them_danh_muc():
    """Hàm wrapper cho nút Thêm"""
    tendm = entry_ten.get()
    mota = entry_mota.get()

    if not tendm:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập Tên danh mục!")
        return

    try:
        # Gọi hàm insert từ 'common'
        insert_danhmuc(tendm, mota)
        messagebox.showinfo("Thành công", "Đã thêm danh mục thành công!")
        load_data()  # Tải lại bảng
        xoa_du_lieu_entry()  # Xóa trắng ô nhập liệu
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm: {e}")


def sua_danh_muc():
    """Hàm wrapper cho nút Sửa"""
    selected = tree.focus()  # Lấy dòng đang chọn
    if not selected:
        messagebox.showwarning("Thông báo", "Vui lòng chọn một dòng để sửa!")
        return

    try:
        # Lấy ID từ dòng đang chọn
        values = tree.item(selected, 'values')
        madm = values[0]

        # Lấy dữ liệu mới từ ô text
        tendm = entry_ten.get()
        mota = entry_mota.get()

        if not tendm:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập Tên danh mục!")
            return

        # Gọi hàm update từ 'common'
        update_danhmuc(madm, tendm, mota)
        messagebox.showinfo("Thành công", "Đã cập nhật danh mục thành công!")
        load_data()  # Tải lại bảng
        xoa_du_lieu_entry()  # Xóa trắng ô nhập liệu
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")


def xoa_danh_muc():
    """Hàm wrapper cho nút Xóa (Đã sửa lỗi)"""
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Thông báo", "Vui lòng chọn một dòng để xóa!")
        return

    try:
        values = tree.item(selected, 'values')
        madm = values[0]  # Lấy Mã DM từ cột đầu tiên

        # Hiển thị hộp thoại xác nhận CÓ/KHÔNG
        if messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc muốn xóa danh mục [ID: {madm}, Tên: {values[1]}] không?"):
            # Gọi hàm delete từ 'common'
            delete_danhmuc(madm)

            messagebox.showinfo("Thành công", "Đã xóa danh mục thành công!")
            load_data()  # Tải lại bảng
            xoa_du_lieu_entry()  # Xóa trắng ô nhập liệu
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")


def xoa_du_lieu_entry():
    """Xóa trắng 2 ô nhập liệu"""
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)


def on_select(event):
    """Hàm được gọi khi bấm vào một dòng trên bảng"""
    selected = tree.focus()
    if not selected:
        return

    # Lấy dữ liệu từ dòng đó
    values = tree.item(selected, 'values')

    # Xóa dữ liệu cũ trong 2 ô
    xoa_du_lieu_entry()

    # Chèn dữ liệu mới vào 2 ô
    entry_ten.insert(0, values[1])  # Cột Tên DM
    entry_mota.insert(0, values[2])  # Cột Mô tả


# --- CÀI ĐẶT GIAO DIỆN CHÍNH (UI) ---

root = tk.Tk()
root.title("Quản lý danh mục sản phẩm")
root.geometry("700x400")
root.resizable(False, False)

# Frame nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# Frame nút bấm
frame_btn = tk.Frame(root)
frame_btn.pack(fill="x", padx=10, pady=5)

# Gán các hàm wrapper cho từng nút
btn_them = tk.Button(frame_btn, text="Thêm", width=12, command=them_danh_muc)
btn_them.pack(side="left", padx=5)

btn_sua = tk.Button(frame_btn, text="Sửa", width=12, command=sua_danh_muc)
btn_sua.pack(side="left", padx=5)

btn_xoa = tk.Button(frame_btn, text="Xóa", width=12, command=xoa_danh_muc)
btn_xoa.pack(side="left", padx=5)

btn_hienthi = tk.Button(frame_btn, text="Làm mới", width=12, command=xoa_du_lieu_entry)
btn_hienthi.pack(side="left", padx=5)

# Frame bảng (Treeview)
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("madm", "tendm", "mota")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên danh mục")
tree.heading("mota", text="Mô tả")

tree.column("madm", width=70, anchor=tk.CENTER)
tree.column("tendm", width=200)
tree.column("mota", width=350)

tree.pack(fill="both", expand=True)

# Gắn sự kiện khi chọn 1 dòng
tree.bind("<<TreeviewSelect>>", on_select)

# --- CHẠY ỨNG DỤNG ---

# Tải dữ liệu ban đầu khi mở app
load_data()

# Giữ cho cửa sổ luôn hiển thị
root.mainloop()