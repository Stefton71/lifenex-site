(function () {
  var root = document.getElementById("lightbox");
  if (!root) return;

  var img = root.querySelector(".lightbox-img");
  var closeBtn = root.querySelector(".lightbox-close");
  var lastFocus = null;

  // Force overlay styles so a stale cached CSS cannot dump the image under the footer.
  root.style.cssText = [
    "position:fixed",
    "inset:0",
    "z-index:10000",
    "display:none",
    "align-items:center",
    "justify-content:center",
    "padding:1.25rem",
    "margin:0",
    "background:rgba(12,10,24,0.82)",
    "backdrop-filter:blur(8px)",
    "-webkit-backdrop-filter:blur(8px)",
    "box-sizing:border-box"
  ].join(";");

  function openLightbox(src, alt) {
    if (!src || !img) return;
    lastFocus = document.activeElement;
    img.src = src;
    img.alt = alt || "";
    root.classList.add("is-open");
    root.style.display = "flex";
    root.setAttribute("aria-hidden", "false");
    document.body.classList.add("lightbox-open");
    document.body.style.overflow = "hidden";
    if (closeBtn) closeBtn.focus();
  }

  function closeLightbox() {
    root.classList.remove("is-open");
    root.style.display = "none";
    root.setAttribute("aria-hidden", "true");
    document.body.classList.remove("lightbox-open");
    document.body.style.overflow = "";
    if (img) {
      img.removeAttribute("src");
      img.alt = "";
    }
    if (lastFocus && typeof lastFocus.focus === "function") {
      lastFocus.focus();
    }
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest("a.shot-frame");
    if (!link) return;
    var href = link.getAttribute("href");
    if (!href) return;
    event.preventDefault();
    var shotImg = link.querySelector("img");
    openLightbox(href, shotImg ? shotImg.getAttribute("alt") : "");
  });

  root.addEventListener("click", function (event) {
    if (event.target === root) closeLightbox();
  });

  if (closeBtn) {
    closeBtn.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      closeLightbox();
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && root.classList.contains("is-open")) {
      closeLightbox();
    }
  });
})();
