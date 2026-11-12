// Beloved Meadow — small helpers. Nothing here stores or sends anything.
(function () {
  // Print buttons
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-print]");
    if (b) { e.preventDefault(); window.print(); }
  });
  // Open grown-up notes so they appear on paper, then restore.
  var opened = [];
  window.addEventListener("beforeprint", function () {
    document.querySelectorAll("details").forEach(function (d) {
      if (!d.open) { d.open = true; opened.push(d); }
    });
  });
  window.addEventListener("afterprint", function () {
    opened.forEach(function (d) { d.open = false; });
    opened = [];
  });
})();
