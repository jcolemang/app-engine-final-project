
(function() {

    $('#delete-calendar-button').click(function() {

        let calendarName = $('#modal-hidden-calendar-name').html();
        $('#' + calendarName).remove();

        $.ajax({
            method: 'DELETE',
            url: window.location.pathname + '?calendarName=' + calendarName,
            success: function() {
                $('#' + calendarName).remove();
            },
            error: function() {

            }
        });
    });


})();
