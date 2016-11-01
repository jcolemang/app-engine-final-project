


(function(cns) {

    cns.edit_cell_modal_namespace = cns.edit_cell_modal_namespace || {};
    let ecns = cns.edit_cell_modal_namespace;
    let md = cns.markdown_namespace;

    let converter = md.converter;

    ecns.getText = function() {
        return $('#markdown-input').val();
    };

    ecns.respondToInput = function() {
        let text = ecns.getText();
        $('#markdown-preview').html(converter.makeHtml(text));
    };

    ecns.getUrlSafeKey = function() {
        let modal = $('#edit-cell-modal');
        let url_safe_key_input = modal.find('#clicked-modal-key');
        return url_safe_key_input.val();
    };

    ecns.setUrlSafeKey = function(key) {
        let modal = $('#edit-cell-modal');
        let url_safe_key_input = modal.find('#clicked-modal-key');
        url_safe_key_input.val(key);
    };

    ecns.openModal = function(cellKey) {
        ecns.setUrlSafeKey(cellKey);
        $('#edit-cell-modal').modal();
    };

    ecns.closeModal = function(cell_key) {
        $('#edit-cell-modal').modal('toggle');
    };

    ecns.completeHandler = function() { };

    ecns.setCompleteHandler = function(f) {
        ecns.completeHandler = f;
    };

    ecns.submitChanges = function(newText, url_safe_key) {
        $.ajax({
            method: 'PUT',
            data: {
                'text': newText,
                'url_safe_key': url_safe_key
            },
            success: ecns.closeModal,
            error: function(jqXHR, textStatus, errorThrown) {

            },
            complete: ecns.completeHandler
        });
    };

    // setting up the automatic updates
    $('#markdown-input').keyup(ecns.respondToInput);

    // open the modal when a key is pressed
    $('.calendar-cell').click(function() {
        let url_safe_key = $(this).attr('id');
        ecns.openModal(url_safe_key);
    });

    // submit the data when the button is pressed
    $('#edit-modal-submit-button').click(function() {
        let urlSafeKey = ecns.getUrlSafeKey();
        let text = ecns.getText();
        ecns.submitChanges(text, urlSafeKey);
    });


})(calendar_namespace);
