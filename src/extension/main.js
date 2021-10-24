var MediaStreamRecorder = require('msr');

var mediaConstraints = {
    audio: true
};

function onMediaSuccess(stream) {
    var options = {mimeType: 'audio/webm'};
    var mediaRecorder = new MediaRecorder(stream, options);
    var chunks = [];
    mediaRecorder.ondataavailable = function (blob) {
        chunks.push(blob.data);
        console.log(chunks.length);
        /*var urlblob = URL.createObjectURL(blob);
        var a = document.createElement('a');
        document.body.appendChild(a);
        a.style = 'display: none';
        a.href = urlblob;
        a.download = 'send.wav';
        a.click();
        console.log("wav saved to local file");*/

    };
    mediaRecorder.start(1000);
    chrome.commands.onCommand.addListener( async function (command) {
        if (command === "stop") {
            mediaRecorder.stop();
            download();
            console.log("data available after MediaRecorder.stop() called.");
            console.log("recorder stopped");
        }
    });
    function download() {
        var globalBlob = new Blob(chunks, {
            type: 'audio/webm'
        });
        var url = URL.createObjectURL(globalBlob);
        console.log(globalBlob);
        chrome.tabs.create({ url: url });
        /*var a = document.createElement('a');
        document.body.appendChild(a);
        a.style = 'display: none';
        a.href = url;
        a.download = 'test.webm';
        a.click();
        window.URL.revokeObjectURL(url);*/
    }
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
