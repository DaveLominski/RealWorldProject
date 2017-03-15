<!DOCTYPE HTML>
<html>
    <head>
        <?php 
            // Declares all the pages meta tags and CSS Scripts (TOO BE BUNDLED).
            require_once($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_meta.php");
        ?>
    </head>
    <body>

        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-4 col-md-3 menuContainer">
                    <?php
                        // Declares the main navigation of the webpage.
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_nav.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_updates.php");
                    ?>
                </div>
                <div class="col-sm-8 col-md-9 mainContainer">
                    <?php
                        // Email Form and Slideshow.
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_emailForm.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_createQuestion.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_slideShow.php");
                    
                        // Page Template Documents.
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Templates/game.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Templates/download.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Templates/questions.php");
                        //include($_SERVER['DOCUMENT_ROOT']."/View/Templates/generate.php");
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Templates/about.php");

                        // Declares the footer of the page.
                        include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_footer.php");
                    ?>
                </div>
            </div>
        </div>
        <?php
            // Delcares all the pages scripts (TO BE BUNDLED).
            include($_SERVER['DOCUMENT_ROOT']."/View/Home/Partials/_scripts.php");
        ?>
    </body>
</html>