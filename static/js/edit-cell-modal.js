


(function(cns) {

    cns.edit_cell_modal_namespace = cns.edit_cell_modal_namespace || {};
    let ecns = cns.edit_cell_modal_namespace;
    let md = cns.markdown_namespace;

    let converter = md.converter;


    ecns.setCurrentCell = function(currentCell) {
        ecns.currentCell = currentCell;
    };


    ecns.getCurrentCell = function() {
        return ecns.currentCell;
    };


    ecns.resetCurrentCell = function() {
        ecns.currentCell = undefined;
    };


    ecns.getText = function() {
        return $('#markdown-input').val();
    };


    ecns.resetEdits = function() {
        let oldMarkdown = ecns.getCurrentCell().find('.hidden-markdown').html();
        ecns.getCurrentCell().find('.hidden-markdown-edits').html(oldMarkdown);
        ecns.setText(oldMarkdown);
        ecns.respondToInput();
    };


    ecns.setText = function(text) {
        $('#markdown-input').val(text);
    };


    ecns.saveEdits = function(text) {
        ecns.getCurrentCell().find('.hidden-markdown-edits').html(text);
    };


    ecns.respondToInput = function() {
        let text = ecns.getText();
        ecns.saveEdits(text);
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


    ecns.openModal = function(cellKey, markdownText) {
        ecns.setUrlSafeKey(cellKey);
        let modal = $('#edit-cell-modal');
        $('#markdown-input').val(markdownText);
        $('#edit-cell-modal').modal();
        $('#markdown-input').focus();
    };


    ecns.closeModal = function(cell_key) {
        ecns.resetCurrentCell();
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
            complete: function() {
                ecns.completeHandler('#' + url_safe_key, newText);
            }
        });
    };

    // setting up the automatic updates
    $('#markdown-input').keyup(ecns.respondToInput);

    // open the modal when a key is pressed
    $('.calendar-cell').click(function() {
        let url_safe_key = $(this).attr('id');
        let clickedCell = $(this);
        let markdownText = clickedCell.find('.hidden-markdown-edits').html();
        ecns.setCurrentCell(clickedCell);
        ecns.setText(markdownText);
        ecns.openModal(url_safe_key, markdownText);
        ecns.respondToInput();
    });

    // submit the data when the button is pressed
    $('#edit-modal-submit-button').click(function() {
        let urlSafeKey = ecns.getUrlSafeKey();
        let text = ecns.getText();
        ecns.getCurrentCell().find('.hidden-markdown').html(text);
        ecns.getCurrentCell().find('.hidden-markdown-edits').html(text);
        ecns.submitChanges(text, urlSafeKey);
    });

    $('#reset-input-button').click(function() {
        ecns.resetEdits();
    });


})(calendar_namespace);
