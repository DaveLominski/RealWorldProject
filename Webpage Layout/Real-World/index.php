<?php
    include_once($_SERVER['DOCUMENT_ROOT']."/Control/MainController.php");
    $controller = new MainController();
    $controller -> invoke();
?>