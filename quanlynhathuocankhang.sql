-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 03:08 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `quanlynhathuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `madm` int(11) NOT NULL,
  `tendm` varchar(100) NOT NULL,
  `mota` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`madm`, `tendm`, `mota`) VALUES
(1, 'Điện thoại', 'Các loại điện thoại thông minh từ nhiều hãng khác nhau'),
(2, 'Laptop', 'Máy tính xách tay phục vụ học tập và làm việc'),
(3, 'Máy tính bảng', 'Tablet nhỏ gọn, tiện lợi cho giải trí và công việc'),
(4, 'Phụ kiện', 'Phụ kiện công nghệ như tai nghe, sạc, cáp, chuột, bàn phím'),
(6, 'quần áo', 'hot123');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `masp` int(11) NOT NULL,
  `tensp` varchar(255) NOT NULL,
  `giaban` decimal(10,2) NOT NULL,
  `giacu` decimal(10,2) DEFAULT NULL,
  `giamgia` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT 0,
  `hinhanh` varchar(255) DEFAULT NULL,
  `madm` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`masp`, `tensp`, `giaban`, `giacu`, `giamgia`, `soluong`, `hinhanh`, `madm`) VALUES
(1, 'iPhone 15 Pro Max', 33990000.00, 36990000.00, 8, 20, 'iphone15promax.jpg', 1),
(2, 'Samsung Galaxy S24 Ultra', 29990000.00, 33990000.00, 12, 15, 's24ultra.jpg', 1),
(3, 'Xiaomi Redmi Note 13', 6490000.00, 6990000.00, 7, 40, 'redmi13.jpg', 1),
(4, 'MacBook Air M2 2023', 28990000.00, 30990000.00, 6, 10, 'macbookairm2.jpg', 2),
(5, 'ASUS TUF Gaming F15', 24990000.00, 27990000.00, 11, 8, 'asustuf15.jpg', 2),
(6, 'Dell XPS 13 Plus', 34990000.00, 36990000.00, 5, 5, 'dellxps13.jpg', 2),
(7, 'iPad Air 5', 15990000.00, 17990000.00, 11, 12, 'ipadair5.jpg', 3),
(8, 'Samsung Galaxy Tab S9', 18990000.00, 20990000.00, 10, 9, 'tabs9.jpg', 3),
(9, 'Tai nghe AirPods Pro 2', 5990000.00, 6490000.00, 8, 50, 'airpodspro2.jpg', 4),
(10, 'Chuột Logitech MX Master 3S', 2490000.00, 2690000.00, 7, 30, 'mxmaster3s.jpg', 4),
(11, 'Bàn phím Keychron K6', 2290000.00, 2490000.00, 8, 25, 'keychronk6.jpg', 4);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`madm`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`masp`),
  ADD KEY `madm` (`madm`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `madm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `masp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`madm`) REFERENCES `danhmuc` (`madm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
