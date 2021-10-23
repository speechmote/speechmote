var MediaStreamRecorder = require('msr');

var mediaConstraints = {
    audio: true
};

chrome.contextMenus.create({
    title: "Record Audio", 
    contexts:["editable"], 
    onclick: record,
    id: "speechmote"
});

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
    fetch('https://speechmote-329915.ue.r.appspot.com/').then(response => {
            console.log(response.json());
    });

    text = ":pepega: :kekw:";

    chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs) {
        url = tabs[0].url;
        emoteType = matchURL(url);
        console.log(emoteType);
        //navigator.getUserMedia(mediaConstraints, onMediaSuccess, onMediaError); //record audio
        //make api call here
        //call printText() with the returned text
    });
}

function matchURL(url) {
    if (url.includes("discord")) {
        //pass discord parameter to api call (emotes should have colons)
        return "discord";
    } else if (url.includes("twitch")) {
        //pass twitch parameter to api call (emotes should be plain)
        return "twitch";
    }
}

function printText(text) {
    chrome.tabs.executeScript(tab.id, {
        frameId: info.frameId || 0,
        matchAboutBlank: true,
        code: `document.execCommand('insertText', false, ${JSON.stringify(text)})`,
    });
}
