//Background Code for Speechmote
function record(info,tab) {
    console.log("Record button clicked!"); //do a sound or something here 
    console.log(info.frameId);
    
    // chrome.tabs.create({  
    //   url: "http://www.google.com/search?q=" + info.selectionText
    // });
  }
  chrome.contextMenus.create({
    title: "Record Audio", 
    contexts:["editable"], 
    onclick: record
  });