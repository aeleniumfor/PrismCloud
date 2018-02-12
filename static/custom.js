;

function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files;

    var output = [];


    for (var i = 0; i < files.length; i++) {
        document.getElementById('output').innerHTML += files[i].name + '(' + files[i].size + ') '
            + files[i].lastModifiedDate.toLocaleDateString() + files[i].lastModifiedDate.toLocaleTimeString() + ' - ' + files[i].type + '<br/>';
    }
}

function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy';
}

function PageLoad(evt) {
    var dropFrame = document.getElementById('DropFrame');
    dropFrame.addEventListener('dragover', handleDragOver, false);
    dropFrame.addEventListener('drop', handleFileSelect, false);
}

window.onload = function () {
    PageLoad();
};

