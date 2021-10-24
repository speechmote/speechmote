function onClick() {
    console.log("running runner");  

    navigator.mediaDevices.getUserMedia({audio: true, video: false}, () => {chrome.extension.sendMessage({greeting: "kekw"}, function(response) {
        console.log(response.farewell);
    })});

    chrome.extension.onMessage.addListener(
        function(request, sender, sendResponse) {
            if (request.greeting === "kekw") {
                sendResponse({farewell: "lul"});
                console.log("in listener");
            }
            return true;
        }
    );
}

 var elem = document.getElementById("changeColor");
 elem.onclick = onClick;