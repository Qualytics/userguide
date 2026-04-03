function initCardFilters() {
  document.querySelectorAll(".md-typeset .grid.cards").forEach(function (grid) {
    // Skip if already has a filter
    if (grid.previousElementSibling && grid.previousElementSibling.classList.contains("card-filter-wrapper")) return;

    var ul = grid.querySelector("ul");
    if (!ul) return;

    var wrapper = document.createElement("div");
    wrapper.className = "card-filter-wrapper";

    // Search icon (SVG magnifying glass)
    var icon = document.createElement("span");
    icon.className = "card-filter-icon";
    icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" /></svg>';

    var input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Search";
    input.className = "card-filter";

    wrapper.appendChild(icon);
    wrapper.appendChild(input);
    grid.parentNode.insertBefore(wrapper, grid);

    // Extract clean words from each card once
    var cards = [];
    ul.querySelectorAll("li").forEach(function (card) {
      var text = card.textContent.toLowerCase().replace(/[^\w\s]/g, " ");
      var words = text.split(/\s+/).filter(function (w) { return w.length > 0; });
      cards.push({ el: card, text: text, words: words });
    });

    input.addEventListener("input", function () {
      var query = this.value.toLowerCase().trim();
      if (query === "") {
        cards.forEach(function (c) { c.el.style.display = ""; });
        return;
      }

      var terms = query.split(/\s+/);

      cards.forEach(function (c) {
        var match = terms.every(function (term) {
          // Direct substring match
          if (c.text.indexOf(term) !== -1) return true;

          // Fuzzy: for terms >= 3 chars, allow Levenshtein distance of 1
          if (term.length >= 3) {
            return c.words.some(function (word) {
              if (Math.abs(word.length - term.length) > 1) return false;
              return levenshtein(term, word) <= 1;
            });
          }

          return false;
        });
        c.el.style.display = match ? "" : "none";
      });
    });
  });
}

function levenshtein(a, b) {
  var m = a.length, n = b.length;
  if (m === 0) return n;
  if (n === 0) return m;

  var prev = [], curr = [];
  for (var j = 0; j <= n; j++) prev[j] = j;

  for (var i = 1; i <= m; i++) {
    curr[0] = i;
    for (var j = 1; j <= n; j++) {
      if (a[i - 1] === b[j - 1]) {
        curr[j] = prev[j - 1];
      } else {
        curr[j] = 1 + Math.min(prev[j], curr[j - 1], prev[j - 1]);
      }
    }
    var tmp = prev;
    prev = curr;
    curr = tmp;
  }
  return prev[n];
}

// Run on initial load
document.addEventListener("DOMContentLoaded", initCardFilters);

// Re-run on Material for MkDocs instant navigation
if (typeof document$ !== "undefined") {
  document$.subscribe(initCardFilters);
}
