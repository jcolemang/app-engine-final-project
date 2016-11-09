
(function() {

    $('.date-cell.calendar-clickable').click(function() {
        let rowKey = $(this).find('.date-cell-row-key').html();
        $('#edit-row-date-modal-row-key').html(rowKey);
    });

    $('#edit-row-date-modal-submit-button').click(function() {


        let rowKey = $('#edit-row-date-modal-row-key').html();
        let date = $('#edit-row-date-date-input').val();
        let parsedDate = /^(\d+)-(\d\d?)-(\d\d?)$/.exec(date);
        if (!parsedDate)
            return false;

        $.ajax({
            method: 'PUT',
            data: {
                'rowKey': rowKey,
                'date': date
            },
            success: function(resp) {
                window.location.reload();
            },
            error: function(jqXHR, textStatus, errorThrown) {

            }
        });

        return true;
    });

})();
