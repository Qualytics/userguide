// Detect OS once
var osHideClass = /Mac|iPhone|iPad|iPod/i.test(navigator.userAgent) ? "os-other" : "os-mac";

// Inject persistent style rule
var osStyle = document.createElement("style");
osStyle.textContent = "." + osHideClass + " { display: none !important; }";
document.head.appendChild(osStyle);

// Re-apply on Material for MkDocs instant navigation
if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    document.querySelectorAll("." + osHideClass).forEach(function (el) {
      el.style.display = "none";
    });
  });
}
