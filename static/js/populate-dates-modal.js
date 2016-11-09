
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


    pdmn.validateDate = function(dateStr) {
        let parsedDate = /^(\d+)-(\d\d?)-(\d\d?)$/.exec(dateStr);

        console.log(dateStr);
        console.log(parsedDate);

        if (!parsedDate) {
            return false;
        }

        let month = +parsedDate[2];
        let day = +parsedDate[3];
        let year = +parsedDate[1];

        if (day < 1)
            return false;

        switch (month) {
        case 1:
            if (day > 31) return false;
            break;
        case 2:
            if (day > 28) return false;
            break;
        case 3:
            if (day > 31) return false;
            break;
        case 4:
            if (day > 30) return false;
            break;
        case 5:
            if (day > 31) return false;
            break;
        case 6:
            if (day > 30) return false;
            break;
        case 7:
            if (day > 31) return false;
            break;
        case 8:
            if (day > 31) return false;
            break;
        case 9:
            if (day > 30) return false;
            break;
        case 10:
            if (day > 31) return false;
            break;
        case 11:
            if (day > 30) return false;
            break;
        case 12:
            if (day > 31) return false;
            break;
        default:
            return false;
        }

        return true;
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
        if (!pdmn.validateDate(vacationStart)) return false;
        if (!pdmn.validateDate(vacationEnd)) return false;
        pdmn.addVacationRange(vacationStart, vacationEnd);
        pdmn.updateVacationRangeList();
        return true;
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
        let title = $('.page-title').html();
        $('.page-title').html('Please wait...');

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

        $('#populate-dates-modal').modal('hide');
        return true;
    });


})(calendar_namespace,
   calendar_namespace.calendar_page_namespace,
   calendar_namespace.calendar_page_namespace.calendar_edit_toolbar_namespace);
