var MediaStreamRecorder = require('msr');

var mediaConstraints = {
    audio: true
};

function onMediaSuccess(stream) {
    var mediaRecorder = new MediaStreamRecorder(stream);
    mediaRecorder.mimeType = 'audio/wav'; // check this line for audio/wav
    mediaRecorder.ondataavailable = function (blob) {
        // POST/PUT "Blob" using FormData/XHR2
        var blobURL = URL.createObjectURL(blob);
        document.write('<a href="' + blobURL + '">' + blobURL + '</a>');
        chrome.tabs.create({
            url: blobURL
          });
    };
    mediaRecorder.start(3000);
}
function onMediaError(e) {
    console.error('media error', e);
}
function record(info,tab) {
    if (info.menuItemId == "") {
        console.log("yay!");
    }
    console.log("Record button clicked!"); //do a sound or something here 
    console.log(info.frameId);
    navigator.getUserMedia(mediaConstraints, onMediaSuccess, onMediaError);
}

chrome.contextMenus.create({
    title: "Record Audio", 
    contexts:["editable"], 
    onclick: record,
    id: "speechmote"
});