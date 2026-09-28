(() => {
  const closeLabel = {
    it: "Chiudi",
    en: "Close",
    fr: "Fermer",
    de: "Schließen",
  };
  const lang = (document.documentElement.lang || "en").slice(0, 2);
  const label = closeLabel[lang] || closeLabel.en;

  const root = document.createElement("div");
  root.className = "lightbox";
  root.hidden = true;
  root.setAttribute("role", "dialog");
  root.setAttribute("aria-modal", "true");
  root.setAttribute("aria-label", label);
  root.innerHTML = `
    <button type="button" class="lightbox-close" aria-label="${label}">
      <span aria-hidden="true">×</span>
    </button>
    <img class="lightbox-img" alt="">
  `;
  document.body.appendChild(root);

  const img = root.querySelector(".lightbox-img");
  const closeBtn = root.querySelector(".lightbox-close");
  let lastFocus = null;

  function open(src, alt) {
    lastFocus = document.activeElement;
    img.src = src;
    img.alt = alt || "";
    root.hidden = false;
    document.body.classList.add("lightbox-open");
    closeBtn.focus();
  }

  function close() {
    if (root.hidden) return;
    root.hidden = true;
    img.removeAttribute("src");
    document.body.classList.remove("lightbox-open");
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  }

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a.shot-frame");
    if (!link) return;
    const href = link.getAttribute("href");
    if (!href) return;
    event.preventDefault();
    const thumb = link.querySelector("img");
    open(href, thumb ? thumb.getAttribute("alt") : "");
  });

  closeBtn.addEventListener("click", (event) => {
    event.stopPropagation();
    close();
  });

  root.addEventListener("click", (event) => {
    if (event.target === root) close();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") close();
  });
})();
