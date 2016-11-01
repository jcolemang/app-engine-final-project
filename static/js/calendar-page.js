



(function (cns) {

    let ecns = cns.edit_cell_modal_namespace;
    let md = cns.markdown_namespace;

    // setting up the calendar page

    let converter = md.converter;

    ecns.setCompleteHandler(function(id, newText) {
        console.log(id);
        console.log($(id));
        $(id).html(converter.makeHtml(newText));
    });

    $('.calendar-cell').map(function() {
        console.log($(this).html());
        $(this).html(converter.makeHtml($(this).html()));
    });

})(calendar_namespace);
