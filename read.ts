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

function scroll_div(distance, times) {
    return new Promise((resolve) => {
        const scrollElement = document.querySelector('div[class^="index_scrollWindow"]');
        if (!scrollElement) {
            console.error("Element not found");
            resolve();
            return;
        }
        let iterations = 0;
        function scrollOnce() {
            scrollElement.scrollTop += distance;
            const scrollEvent = new Event('scroll');
            scrollElement.dispatchEvent(scrollEvent);
            iterations++;
            if (iterations < times) {
                setTimeout(scrollOnce, 200);
            } else {
                resolve();
            }
        }
        scrollOnce();
    });
}

async function my_scroll() {
    await scroll_div(4800, 20);
}
