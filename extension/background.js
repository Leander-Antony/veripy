chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "log-selected-text",
      title: "Log Selected Text",
      contexts: ["selection"]
    });
  });
  
  chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "log-selected-text") {
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
          console.log("Selected text:", window.getSelection().toString());
        }
      });
    }
  });
  