<?php
if (isset($_GET['id'])) {
    include("connect.php");

    $id = intval($_GET['id']); // tránh SQL Injection
    $sl = "SELECT * FROM truyen WHERE idTruyen = " . $id;
    $kq = mysqli_query($link, $sl);

    if ($kq && mysqli_num_rows($kq) > 0) {
        $arr = mysqli_fetch_assoc($kq);
        echo json_encode($arr, JSON_UNESCAPED_UNICODE);
    } else {
        echo json_encode(["error" => "Không tìm thấy truyện"], JSON_UNESCAPED_UNICODE);
    }
}
?>
