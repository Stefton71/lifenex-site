(function () {
  var root = document.getElementById("lightbox");
  if (!root) return;

  var img = root.querySelector(".lightbox-img");
  var closeBtn = root.querySelector(".lightbox-close");
  var lastFocus = null;

  function openLightbox(src, alt) {
    if (!src || !img) return;
    lastFocus = document.activeElement;
    img.src = src;
    img.alt = alt || "";
    root.classList.add("is-open");
    root.setAttribute("aria-hidden", "false");
    document.body.classList.add("lightbox-open");
    if (closeBtn) closeBtn.focus();
  }

  function closeLightbox() {
    root.classList.remove("is-open");
    root.setAttribute("aria-hidden", "true");
    document.body.classList.remove("lightbox-open");
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
      closeLightbox();
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && root.classList.contains("is-open")) {
      closeLightbox();
    }
  });
})();
