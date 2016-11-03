
(function(cns, ccns) {

    cns.dashboard_namespace = cns.dashboard_namespace || {};
    let dns = cns.dashboard_namespace;

    dns.inputValidator = new ccns.CreateCalendarValidator();

    $('#calendar-insert-submit-button').click(function() {

        let calendarName = $('#calendar-name-input').val();
        if (!dns.inputValidator.validateName(calendarName)) {
            alert('Invalid input');
            return false;
        }

        return true;
    });

})(calendar_namespace, calendar_namespace.create_calendar_namespace);
