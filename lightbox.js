(() => {
  const labels = { it: "Chiudi", en: "Close", fr: "Fermer", de: "Schließen" };
  const label = labels[(document.documentElement.lang || "en").slice(0, 2)] || "Close";

  const root = document.createElement("div");
  root.className = "lb";
  root.hidden = true;
  root.innerHTML =
    '<div class="lb-box">' +
    '<button type="button" class="lb-x" aria-label="' + label + '">×</button>' +
    '<img class="lb-img" alt="">' +
    "</div>";
  document.body.appendChild(root);

  const img = root.querySelector(".lb-img");
  const x = root.querySelector(".lb-x");

  function open(src, alt) {
    img.src = src;
    img.alt = alt || "";
    root.hidden = false;
  }

  function close() {
    root.hidden = true;
    img.removeAttribute("src");
  }

  document.addEventListener(
    "click",
    (e) => {
      const a = e.target.closest("a.shot-frame");
      if (!a) return;
      e.preventDefault();
      e.stopPropagation();
      const thumb = a.querySelector("img");
      open(a.getAttribute("href"), thumb && thumb.alt);
    },
    true
  );

  x.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    close();
  });

  root.addEventListener("click", (e) => {
    if (e.target === root) close();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });

  // Block touch-scroll from moving the page under the overlay
  root.addEventListener(
    "touchmove",
    (e) => {
      e.preventDefault();
    },
    { passive: false }
  );
})();
