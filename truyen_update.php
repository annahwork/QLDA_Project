<?php
include("connect.php");

if (isset($_POST['id'])) {
    $id       = intval($_POST['id']); // idTruyen
    $tenTruyen = mysqli_real_escape_string($link, $_POST['tenTruyen']);
    $tacGia    = mysqli_real_escape_string($link, $_POST['tacGia']);
    $theLoai   = mysqli_real_escape_string($link, $_POST['theLoai']);
    $moTa      = mysqli_real_escape_string($link, $_POST['moTa']);
    $anhBia    = mysqli_real_escape_string($link, $_POST['anhBia']);

    $sl = "UPDATE truyen 
           SET tenTruyen='$tenTruyen', tacGia='$tacGia', theLoai='$theLoai', moTa='$moTa', anhBia='$anhBia'
           WHERE idTruyen=$id";

    if (mysqli_query($link, $sl))
        echo "OK";
    else
        echo "Error: " . mysqli_error($link);
}
?>
