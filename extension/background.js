// // Create context menu item
// chrome.runtime.onInstalled.addListener(() => {
//   chrome.contextMenus.create({
//     id: "verify-text",
//     title: "Verify with VeriPy",
//     contexts: ["selection"]
//   });
// });

// // Handle context menu clicks
// chrome.contextMenus.onClicked.addListener((info, tab) => {
//   if (info.menuItemId === "verify-text") {
//     // Open popup with selected text
//     chrome.windows.create({
//       url: `index.html?text=${encodeURIComponent(info.selectionText)}`,
//       type: 'popup',
//       width: 400,
//       height: 600
//     });
//   }
// });

// Create context menu item
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "verify-text",
      title: "Verify with VeriPy",
      contexts: ["selection"]
    });
  });
  
  // Handle context menu clicks
  chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "verify-text") {
      // Open popup with selected text
      chrome.windows.create({
        url: `index.html?text=${encodeURIComponent(info.selectionText)}`,
        type: "popup",
        width: 400,
        height: 600
      });
    }
  });
