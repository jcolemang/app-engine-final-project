
(function(cns, cpn, cetn) {

    // setting up the new namespace
    cetn.populate_dates_modal_namespace = cetn.populate_dates_modal_namespace || {};
    let pdmn = cetn.populate_dates_modal_namespace;


    // modal specific functions

    let vacationPairs = [];

    pdmn.addVacationRange = function(newStart, newEnd) {
        vacationPairs.push([newStart, newEnd]);
    };


    pdmn.removeVacationRange = function() {

    };


    pdmn.populateDates = function() {
        // pass
    };


    pdmn.updateVacationRangeList = function() {

        let htmlResult = '';
        vacationPairs.map(function(pair) {
            let vacationStart = pair[0];
            let vacationEnd = pair[1];
            return '<li>' + vacationStart + ' -- ' + vacationEnd + '</li>';
        }).forEach(function(text) {
            htmlResult += text;
        });

        $('#vacation-range-list').html(htmlResult);
    };


    pdmn.validateNumDays = function(val) {
        return /^\s*[0-9]+\s*$/.test(val) && +val > 0;
    };


    pdmn.checkNumDaysInput = function() {

        let numDays = $('#num-days-input').val();
        let isValid = pdmn.validateNumDays(numDays);

        if (!isValid) {
            $('#num-days-input-group').addClass('has-error');
            return false;
        }

        $('#num-days-input-group').removeClass('has-error');
        return numDays;
    };



    // modal input bindings



    $('#num-days-input').change(pdmn.checkNumDaysInput);


    $('#num-days-input').keyup(pdmn.checkNumDaysInput);


    $('#add-vacation-range-button').click(function() {
        let vacationStart = $('#vacation-days-input-start').val();
        let vacationEnd = $('#vacation-days-input-end').val();
        pdmn.addVacationRange(vacationStart, vacationEnd);
        pdmn.updateVacationRangeList();
    });


    $('#populate-dates-modal-cancel-button').click(function() {
        $('#populate-dates-modal').modal('toggle');
    });


    $('#populate-dates-modal-submit-button').click(function() {
        let isValid = true;
        let numDays = pdmn.checkNumDaysInput();
        isValid = isValid && numDays;

        if (!isValid) {
            return false;
        }

        let startDate = $('#start-date-input').val();

        $.ajax({
            url: '/generate-calendar',
            method: 'POST',
            data: {
                'calendarName': cns.getCalendarName(),
                'username': cns.getUsername(),
                'numDays': numDays,
                'startDate': startDate,
                'vacationRanges': JSON.stringify(vacationPairs)
            },

            success: function(resp) {
                location.reload();
            },

            error: function() {

            }
        });

        return true;
    });


})(calendar_namespace,
   calendar_namespace.calendar_page_namespace,
   calendar_namespace.calendar_page_namespace.calendar_edit_toolbar_namespace);
