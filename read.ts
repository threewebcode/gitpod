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
