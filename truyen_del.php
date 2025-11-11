<?php
include("connect.php");

$id = intval($_GET['id']); // idTruyen

// Xoá chương trước (tránh lỗi khoá ngoại)
mysqli_query($link, "DELETE FROM chuong WHERE idTruyen=" . $id);

// Xoá truyện
$sl = "DELETE FROM truyen WHERE idTruyen=" . $id;
if (mysqli_query($link, $sl))
    echo "OK";
else
    echo "Error";
?>
