(function () {
  var isMac = /Mac|iPhone|iPad|iPod/i.test(navigator.userAgent);
  var hideClass = isMac ? "os-other" : "os-mac";

  // Apply immediately via stylesheet to avoid flash
  var style = document.createElement("style");
  style.textContent = "." + hideClass + " { display: none !important; }";
  document.head.appendChild(style);
})();
