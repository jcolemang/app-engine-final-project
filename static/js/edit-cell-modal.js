

(function() {

    let convertText = md.markdownToHtml;

    let respondToInput = function() {
        let text = $('#markdown-input').val();
        $('#markdown-preview').html(convertText(text));
    };

    $('#markdown-input').keypress(respondToInput);
    $('#markdown-input').keydown(respondToInput);
    $('#markdown-input').keyup(respondToInput);

})();
