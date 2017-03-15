<?php
    include_once($_SERVER["DOCUMENT_ROOT"]."/Model/MainModel.php");

    class MainController {
        // Set main model in which to invoke
        public $model;
        public $questionData;
        
        public function __construct()
        {
            //Define new models here
            $model = new MainModel();
            $questionData = $model->getQuestions();
            $_REQUEST['result'] = $questionData;
        }
        
        public function invoke()
        {
            // Set models and display views on conditions.
            include($_SERVER['DOCUMENT_ROOT']."/View/Home/_Layout.php");
        }
    }
?>