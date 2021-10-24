const apiURL = "https://speechmote-329915.ue.r.appspot.com/test/";
const proxyURL = "http://localhost:8010/proxy";

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
    var chunks = [];
    mediaRecorder.mimeType = 'audio/wav'; // check this line for audio/wav
    mediaRecorder.ondataavailable = function (blob) {
        chunks.push(blob);
        console.log(chunks.length);
        var urlblob = URL.createObjectURL(blob);
        var a = document.createElement('a');
        document.body.appendChild(a);
        a.style = 'display: none';
        a.href = urlblob;
        a.download = 'send.wav';
        a.click();
        console.log("wav saved to local file");

    };
    mediaRecorder.start(1000);
    chrome.commands.onCommand.addListener( async function (command) {
        if (command === "stop") {
            mediaRecorder.stop();
            console.log("data available after MediaRecorder.stop() called.");
            console.log("recorder stopped");
        }
    });
    
}
function onMediaError(e) {
    console.error('media error', e);
}

async function record(info,tab) {
    if (info.menuItemId == "") {
        console.log("yay!");
    }
    console.log("Record button clicked!"); //do a sound or something here 
    console.log(info.frameId);
    //text = await testapi()
    text = await testapi();

    chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs) {
        url = tabs[0].url;
        emoteType = matchURL(url);
        console.log(emoteType);
        //navigator.getUserMedia(mediaConstraints, onMediaSuccess, onMediaError); //record audio
        //make api call here
        //call printText() with the returned text
        printText(text, tab, info);
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

function printText(text, tab, info) {
    chrome.tabs.executeScript(tab.id, {
        frameId: info.frameId || 0,
        matchAboutBlank: true,
        code: `document.execCommand('insertText', false, ${JSON.stringify(text)})`,
    });
}
async function testapi() {
    var test = await fetch(proxyURL + "/kekwyepme").then(response => response.text());
    // await fetch(proxyURL)
    // .then(test = data=>{return data.text()})
    // .then(res=>{console.log(res)})
    // .then(error=>console.log(error));
    // console.log("test's value is: ", test);
    return test;
}
async function formapi() {
    files = files
    formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append("file"+i, files[i]);
    }
    return await fetch(proxyURL, {
        method: 'POST',
        body: formData
    }).then(response => response.text());
}
