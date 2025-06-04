chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status !== 'complete' || !tab.url.startsWith("http")) return;

  const url = new URL(tab.url);

  const payload = {
    title: tab.title,
    url: tab.url,
    hostname: url.hostname,
    path: url.pathname,
    query: url.search,
    tabId: tab.id,
    windowId: tab.windowId,
    favIconUrl: tab.favIconUrl || null
  };

  console.log("Crumb: Sending payload", payload);

  fetch("http://localhost:3555", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  }).catch(err => {
    console.error("Crumb: Failed to reach server", err);
  });
});