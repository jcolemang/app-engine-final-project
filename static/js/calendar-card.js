
(function() {

    $('.delete-calendar-button').click(function() {
        let calendarName = $(this).find('.hidden-calendar-name').html();
        $('#modal-hidden-calendar-name').html(calendarName);
    });

})();
