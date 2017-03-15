<!-- Email Form Modal -->
<div class="modal fade" id="createForm" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-body">
                <button type="button" class="btn btn-help btn-close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">X</span>
                </button>
                <form class="emailForm">
                    <h4>Create a Question</h4>
                    <input type="text" class="form-control font-secondary" placeholder="Question" />
                    
                    <input type="text" class="option form-control font-secondary" placeholder="Option 1" maxlength="255" />
                    
                    <div class="row question-attributes">
                        <div class="dropdown col-xs-4">
                            <select class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
                                <option><a href="#">Local</a></option>
                                <option><a href="#">Neighbours</a></option>
                            </select>
                        </div>

                        <div class="dropdown col-xs-4">
                            <select class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
                                <option><a href="#">Financial</a></option>
                                <option><a href="#">Population</a></option>
                                <option><a href="#">Happiness</a></option>
                                <option><a href="#">Hunger</a></option>
                            </select>
                        </div>
                        <div class="col-xs-4">
                            <input type="text" class="form-control font-secondary" placeholder="Effect Damage (%)" maxlength="3" />
                        </div>
                    </div>
                    
                    <input type="text" class="option form-control font-secondary" placeholder="Option 2" maxlength="255" />
                    
                    <div class="row question-attributes">
                        <div class="dropdown col-xs-4">
                            <select class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
                                <option><a href="#">Local</a></option>
                                <option><a href="#">Neighbours</a></option>
                            </select>
                        </div>

                        <div class="dropdown col-xs-4">
                            <select class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
                                <option><a href="#">Financial</a></option>
                                <option><a href="#">Population</a></option>
                                <option><a href="#">Happiness</a></option>
                                <option><a href="#">Hunger</a></option>
                            </select>
                        </div>
                        <div class="col-xs-4">
                            <input type="text" class="form-control font-secondary" placeholder="Effect Damage (%)" maxlength="3" />
                        </div>
                    </div>
                    
                    
                    <button type="submit" class="btn btn-second-main btn-block">
                        <span class="glyphicon glyphicon-send"></span>
                        <span aria-hidden="SUBMIT">SUBMIT</span>
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>