<?php
    class DBModel {
        public function __construct(){
            $this->host = "localhost";
            $this->user = "root";
            $this->pass = "test";
            $this->database = "Real-World";
        }
        
        public function connectDb(){
            $mySqli = mysqli_connect($this->host, $this->user, $this->pass, $this->database);
            if (!$mySqli) {
                die("CONNECTION ERROR");
            }
            return $mySqli;
        }
    }
?>