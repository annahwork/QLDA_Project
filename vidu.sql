-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Aug 19, 2025
-- Phiên bản máy phục vụ: 10.1.37-MariaDB
-- Phiên bản PHP: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

 /*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `truyen_app`
--

DROP TABLE IF EXISTS `chuong`;
DROP TABLE IF EXISTS `truyen`;

-- --------------------------------------------------------
-- Bảng truyện
CREATE TABLE `truyen` (
  `idTruyen` int(11) NOT NULL AUTO_INCREMENT,
  `tenTruyen` varchar(255) NOT NULL,
  `tacGia` varchar(255) DEFAULT NULL,
  `theLoai` varchar(100) DEFAULT NULL,
  `moTa` text,
  `anhBia` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idTruyen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dữ liệu mẫu cho bảng truyen
INSERT INTO `truyen` (`tenTruyen`, `tacGia`, `theLoai`, `moTa`, `anhBia`) VALUES
('Dế Mèn Phiêu Lưu Ký', 'Tô Hoài', 'Thiếu nhi', 'Cuộc phiêu lưu của Dế Mèn qua nhiều miền đất mới.', 'demen.jpg'),
('Lão Hạc', 'Nam Cao', 'Văn học hiện thực', 'Câu chuyện cảm động về số phận người nông dân.', 'laohac.jpg');

-- --------------------------------------------------------
-- Bảng chương
CREATE TABLE `chuong` (
  `idChuong` int(11) NOT NULL AUTO_INCREMENT,
  `idTruyen` int(11) NOT NULL,
  `soChuong` int(11) NOT NULL,
  `tenChuong` varchar(255) DEFAULT NULL,
  `noiDung` text,
  PRIMARY KEY (`idChuong`),
  KEY `idTruyen` (`idTruyen`),
  CONSTRAINT `chuong_ibfk_1` FOREIGN KEY (`idTruyen`) REFERENCES `truyen` (`idTruyen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dữ liệu mẫu cho bảng chuong
INSERT INTO `chuong` (`idTruyen`, `soChuong`, `tenChuong`, `noiDung`) VALUES
(1, 1, 'Chương 1: Tuổi thơ Dế Mèn', 'Ngày xưa có một chú Dế Mèn...'),
(1, 2, 'Chương 2: Gặp gỡ Dế Choắt', 'Một hôm Dế Mèn gặp Dế Choắt gầy yếu...'),
(2, 1, 'Chương 1: Câu chuyện mở đầu', 'Lão Hạc kể chuyện với ông giáo...'),
(2, 2, 'Chương 2: Cái chết của Lão Hạc', 'Lão Hạc tìm đến cái chết để giữ phẩm giá...');

COMMIT;
