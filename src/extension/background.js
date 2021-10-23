// //Background Code for Speechmote
// function record(info,tab) {
//     console.log("Record button clicked!"); //do a sound or something here 
//     console.log(info.frameId);
//     text = ":pepega: :kekw:";

//     url = chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
//         let url = tabs[0].url;
//         console.log(url);
//     }); 
    
//     chrome.tabs.executeScript(tab.id, {
//         frameId: info.frameId || 0,
//         matchAboutBlank: true,
//         code: `document.execCommand('insertText', false, ${JSON.stringify(text)})`,
//       });
//   }
//   chrome.contextMenus.create({
//     title: "Record Audio", 
//     contexts:["editable"], 
//     onclick: record
//   });