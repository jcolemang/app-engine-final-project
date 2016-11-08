
(function(cns, cpn) {

    cpn.calendar_edit_toolbar_namespace = cpn.calendar_edit_toolbar_namespace || {};
    let cetn = cpn.calendar_edit_toolbar_namespace;

    // showing the populate dates modal
    $('#populate-dates-btn').click(function() {
        $('#populate-dates-modal').modal();
    });

    // showing and hiding the delete button column
    $('.delete-row-column').hide();
    $('#show-delete-col-btn').click(function() {
        $('.delete-row-column').toggle();
    });


})(calendar_namespace, calendar_namespace.calendar_page_namespace);
