function my_button() {
    var floatBtns = document.querySelectorAll('div[class^="index_floatBtn"]');
    if (floatBtns.length > 0) {
        floatBtns.forEach(button => {
            button.click();
        });
    } else {
        console.log('Float button is not found.');
    }
}

function my_span() {
    console.clear();
    var spans = document.querySelectorAll('span');
    function wordCount(str) {
        return str.trim().split(/\s+/).length;
    }
    spans.forEach(span => {
        if (wordCount(span.textContent) > 30) {
            console.log('%c' + span.textContent, 'font-size: large;');
        }
    });
    if (Array.from(spans).every(span => wordCount(span.textContent) <= 30)) {
        console.log('No spans with more than 30 words found.');
    }
}
