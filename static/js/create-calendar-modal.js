

(function(cns) {

    cns.create_calendar_namespace = cns.create_calendar_namespace || {};
    let ccns = cns.create_calendar_namespace;

    let nameErrorMessage = 'Not an acceptable calendar name';
    let repeatErrorMessage = 'Calendar already exists';

    ccns.checkCalendarName = function(name) {
        return /^[a-zA-Z\-0-9_]+$/.test(name);
    };


    ccns.calendarNameError = function(message) {
        $('#calendar-name-input-error').html(message);
    };


    ccns.removeErrors = function() {
        $('#calendar-name-input-error').html('');
    };


    ccns.validateCalendarName = function() {
        let calendarName = $('#calendar-name-input').val();
        if (!ccns.checkCalendarName(calendarName)) {
            ccns.calendarNameError(nameErrorMessage);
            return false;
        } else {
            ccns.removeErrors();
            return calendarName;
        }
    };


    $('#calendar-name-input').keyup(function() {
        ccns.validateCalendarName();
    });

    $('#create-calendar-button').click(function() {
        let calendarName = ccns.validateCalendarName();
        if (!calendarName) return;

        let request = {
            'calendarName': calendarName
        };

        $.post('/', request, function(resp) {
            if (resp == 'calendarexists') {
                ccns.calendarNameError(repeatErrorMessage);
            } else {
                window.location.replace(resp);
            }
        }).fail(function(err) {
            alert(err);
        });
    });

})(calendar_namespace);
