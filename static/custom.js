;

function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files;

    var output = [];

    for (var i = 0; i < files.length; i++) {
        console.log(files[i].name);
        FileUpload();
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


function FileUpload(file, url) {
    var formData = new FormData();
    formData.append('file', file);
    console.log(formData);
    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        dataType: 'json',
        success: function (data) {
            // メッセージ出したり、DOM構築したり。
        }
    });
}


$(function () {

    if (window.File && window.FileReader && window.FileList && window.Blob) {
        PageLoad();
    } else {
        alert('The File APIs are not fully supported in this browser.');
    }

});
