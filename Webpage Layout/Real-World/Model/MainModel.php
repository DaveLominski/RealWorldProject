<?php 
    include_once($_SERVER["DOCUMENT_ROOT"]."/Model/DBModel.php");

    class MainModel {
        
        public function __construct(){
            // Temp hard coded values for demo
            $this->database = new DBModel();
            $this->conn = $this->database->connectDb();
        }
        
        public function getQuestions(){
            $result = mysqli_query($this->conn, "SELECT * FROM Questions");
            $rows = array();
            
            while($row = mysqli_fetch_assoc($result)) {
                array_push($rows, $row);
            }
            return $rows;
        }
    }
?>