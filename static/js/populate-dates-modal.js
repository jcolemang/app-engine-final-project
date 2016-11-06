
(function(cns, cpn, cetn) {

    // setting up the new namespace
    cetn.populate_dates_modal_namespace = cetn.populate_dates_modal_namespace || {};
    let pdmn = cetn.populate_dates_modal_namespace;


    // modal specific functions

    let vacationPairs = [];

    pdmn.addVacationRange = function(newStart, newEnd) {
        vacationPairs.push([newStart, newEnd]);
        console.log(vacationPairs);
    };


    pdmn.removeVacationRange = function() {

    };


    pdmn.populateDates = function() {
        // pass
    };


    pdmn.updateVacationRangeList = function() {

        let htmlResult = '';
        vacationPairs.map(function(pair) {
            let vacationStart = pair[0];
            let vacationEnd = pair[1];
            return '<li>' + vacationStart + ' -- ' + vacationEnd + '</li>';
        }).forEach(function(text) {
            htmlResult += text;
        });

        $('#vacation-range-list').html(htmlResult);
    };


    // event listeners

    $('#add-vacation-range-button').click(function() {
        let vacationStart = $('#vacation-days-input-start').val();
        let vacationEnd = $('#vacation-days-input-end').val();
        pdmn.addVacationRange(vacationStart, vacationEnd);
        pdmn.updateVacationRangeList();
    });

})(calendar_namespace,
   calendar_namespace.calendar_page_namespace,
   calendar_namespace.calendar_page_namespace.calendar_edit_toolbar_namespace);
