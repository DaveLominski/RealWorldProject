<section id="questions">
    <h2>Questions</h2>
    
    <select class="col-xs-12 margin-bottom-15">
        <option name="default" disabled selected='selected'>Please select a question...</option>
        <?php 
            for ($i=0; $i<count($_REQUEST['result']); $i++) {
                echo ("<option>".($_REQUEST['result'][$i]['question'])."</option>");
            }
        ?>
    </select>
    
    <div id="pie-chart-display" style="width:100%; height:auto;"></div>
    
    <button class="btn btn-main btn-block" data-toggle="modal" data-target="#createForm">
        Create a question
    </button>
</section>