;

function getCSRF() {
    return $('[name = csrfmiddlewaretoken]').val();
}