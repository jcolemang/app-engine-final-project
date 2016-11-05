
(function(cns, cpn) {

    cpn.calendar_edit_toolbar_namespace = cpn.calendar_edit_toolbar_namespace || {};
    let cetn = cpn.calendar_edit_toolbar_namespace;


    cetn.validateNumDays = function(val) {
        return /^\s*[0-9]+\s*$/.test(val) && +val > 0;
    };

    cetn.checkNumDaysInput = function() {

        let numDays = $('#num-days-input').val();
        let isValid = cetn.validateNumDays(numDays);

        if (!isValid) {
            $('#num-days-input-group').addClass('has-error');
            return false;
        }

        $('#num-days-input-group').removeClass('has-error');
        return true;
    };


    // external input bindings

    $('#populate-dates-btn').click(function() {
        $('#populate-dates-modal').modal();
    });


    // modal input bindings

    $('#num-days-input').change(cetn.checkNumDaysInput);
    $('#num-days-input').keyup(cetn.checkNumDaysInput);


    $('#populate-dates-modal-cancel-button').click(function() {
        $('#populate-dates-modal').modal('toggle');
    });


    $('#populate-dates-modal-submit-button').click(function() {
        let isValid = true;
        isValid = isValid && cetn.checkNumDaysInput();
    });



})(calendar_namespace, calendar_namespace.calendar_page_namespace);
