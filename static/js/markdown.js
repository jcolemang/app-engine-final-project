

var md = md || {};

md.escapeString = function(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
};

md.markdownToHtml = function(text) {

    let htmlString = md.escapeString(text);
    let replacements = {};
    replacements['^#\\s+(.*)'] = ['<h1>$1<h1>', ''];
    replacements['^##\\s+(.*)'] = ['<h2>$1<h2>', ''];
    replacements['^###\\s+(.*)'] = ['<h3>$1<h3>', ''];
    replacements['^####\\s+(.*)'] = ['<h4>$1<h4>', ''];
    replacements['^#####\\s+(.*)'] = ['<h5>$1<h5>', ''];
    replacements['(.*?)\\*(.*?)\\*(.*)'] = ['$1<b>$2<b>$3', 'g'];
    replacements['(.*?)_(.*?)_(.*)'] = ['$1<i>$2<i>$3', 'g'];

    for (let re in replacements) {
        htmlString = htmlString.replace(new RegExp(re, replacements[re][1]), replacements[re][0]);
    }

    return htmlString;
};
