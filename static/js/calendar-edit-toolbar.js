
(function(cns, cpn) {

    cpn.calendar_edit_toolbar_namespace = cpn.calendar_edit_toolbar_namespace || {};
    let cetn = cpn.calendar_edit_toolbar_namespace;

    $('#populate-dates-btn').click(function() {
        $('#populate-dates-modal').modal();
    });

})(calendar_namespace, calendar_namespace.calendar_page_namespace);
