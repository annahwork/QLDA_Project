<?php
include("connect.php");

if (isset($_GET['id'])) {
    // Lấy 1 truyện theo id
    $sl = "SELECT * FROM truyen WHERE idTruyen=" . intval($_GET['id']);
    $kq = mysqli_query($link, $sl);
    $arr = mysqli_fetch_assoc($kq);
    echo json_encode($arr, JSON_UNESCAPED_UNICODE);
} else {
    // Lấy danh sách tất cả truyện
    $sl = "SELECT * FROM truyen";
    $kq = mysqli_query($link, $sl);
    $arr = [];
    while ($d = mysqli_fetch_assoc($kq)) {
        $arr[] = $d;
    }
    echo json_encode($arr, JSON_UNESCAPED_UNICODE);
}
?>
