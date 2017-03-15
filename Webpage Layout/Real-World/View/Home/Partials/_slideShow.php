<?php
    $imagesLocation = "Media/Images/";
    $imagesPresent = glob($imagesLocation . '*.jpg');
    $sumOfImages = count($imagesPresent);

    if ($sumOfImages > 0) {
        ?>
<div id="carousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
        <?php
                        
            for ($i=0; $i<$sumOfImages; $i++) {
                if ($i == 0) {
                    echo "<li data-target='#carousel' data-slide-to='".$i."' class='active'></li>";
                } else {
                    echo "<li data-target='#carousel' data-slide-to='".$i."'></li>";
                }
            }
        ?>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
        <?php
            $count = 0;
            foreach ($imagesPresent as $image) {

                if ($count == 0) {
                    echo "<div class='item active'><img class='img-responsive' src='".$image."' /></div>";
                } else {
                    echo "<div class='item'><img class='img-responsive' src='".$image."' /></div>";
                }

                $count++;
            }

        ?>
    </div>

    <!-- Controls -->
    <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>
<?php
    } else {
        echo ("<div style='margin-top: -10px;'></div>");
    }
?>