function setAllCheckboxes(text, source) {

    var divs = document.querySelectorAll('div[id="' + text + '"]');

    for (i = 0; i < divs.length; i++) {
        var checkboxes = divs[i].querySelectorAll('input[type="checkbox"]');
        if (checkboxes[0] != source)
            checkboxes[0].checked = source.checked;
    }

}

