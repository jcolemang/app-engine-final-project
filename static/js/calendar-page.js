



(function (cns) {

    cns.calendar_page_namespace = cns.calendar_page_namespace || {};
    let ecns = cns.edit_cell_modal_namespace;
    let md = cns.markdown_namespace;

    // setting up the calendar page

    cns.getLocation = function() {
        return window.location.pathname;
    };


    cns.getUsername = function() {
        let loc = cns.getLocation();
        let username =  /\/calendar\/(.*?)\/.*/.exec(loc)[1];
        return username;
    };


    cns.getCalendarName = function() {
        let loc = cns.getLocation();
        let name = /\/calendar\/.*?\/(.*)/.exec(loc)[1];
        return name;
    };


    let converter = new Markdown.Converter();

    ecns.setCompleteHandler(function(id, newText) {
        $(id).find('.visible-text').html(converter.makeHtml(newText));
    });


    $('.calendar-cell').map(function() {
        let currCell = $(this);
        let markdownText = currCell.find('.hidden-markdown').html();
        let visibleHtml = converter.makeHtml(markdownText || '');
        currCell.find('.visible-text').html(visibleHtml);
    });


    $('.calendar-row-delete-button').click(function() {
        let rowKey = $(this).find('span.row-key').html();

        $.ajax({
            method: 'DELETE',
            url: window.location.pathname + '?rowKey=' + rowKey,
            success: function() {
                $('#' + rowKey).remove();
            },
            error: function() {

            }
        });
    });



})(calendar_namespace);
