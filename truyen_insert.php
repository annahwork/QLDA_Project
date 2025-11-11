<?php
include("connect.php");

if (isset($_POST['insert'])) {
    $tenTruyen = mysqli_real_escape_string($link, $_POST['tenTruyen']);
    $tacGia    = mysqli_real_escape_string($link, $_POST['tacGia']);
    $theLoai   = mysqli_real_escape_string($link, $_POST['theLoai']);
    $moTa      = mysqli_real_escape_string($link, $_POST['moTa']);
    $anhBia    = mysqli_real_escape_string($link, $_POST['anhBia']);

    $sl = "INSERT INTO truyen (tenTruyen, tacGia, theLoai, moTa, anhBia) 
           VALUES ('$tenTruyen', '$tacGia', '$theLoai', '$moTa', '$anhBia')";

    if (mysqli_query($link, $sl))
        echo "OK";
    else
        echo "Error: " . mysqli_error($link);
}
?>
