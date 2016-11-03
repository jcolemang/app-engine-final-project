



(function (cns) {

    let ecns = cns.edit_cell_modal_namespace;
    let md = cns.markdown_namespace;

    // setting up the calendar page

    let converter = md.converter;

    ecns.setCompleteHandler(function(id, newText) {
        $(id).html(converter.makeHtml(newText));
    });

    $('.calendar-cell').map(function() {
        let currCell = $(this);
        let markdownText = currCell.find('.hidden-markdown').html();
        let visibleHtml = converter.makeHtml(markdownText);
        currCell.find('.visible-text').html(visibleHtml);
    });

})(calendar_namespace);
