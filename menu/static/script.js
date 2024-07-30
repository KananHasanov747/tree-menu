document.addEventListener("DOMContentLoaded", () => {
  const treeMenu = document.querySelector(".tree-menu");

  function showActivePath(element) {
    let currentElement = element;

    while (currentElement) {
      if (currentElement.tagName === "UL") {
        currentElement.style.display = "block";
      }

      currentElement = currentElement.parentElement;
      if (currentElement && currentElement.tagName === "LI") {
        currentElement.style.display = "block";
      }
    }
  }

  function hideAllLists() {
    const lists = document.querySelectorAll(".tree-menu ul");
    lists.forEach((ul) => (ul.style.display = "none"));
  }

  function toggleList(event) {
    const button = event.currentTarget;
    const ul = button.nextElementSibling;
    if (ul) {
      ul.style.display = ul.style.display === "block" ? "none" : "block";
    }
  }

  function init() {
    hideAllLists();

    const activeItems = treeMenu.querySelectorAll(".dropdown.active");
    if (activeItems.length > 0) {
      activeItems.forEach((activeItem) => {
        let ul = activeItem.parentElement;
        while (ul && ul.tagName !== "UL") {
          ul = ul.parentElement;
        }
        if (ul) {
          showActivePath(ul);
        }
      });
    }

    const dropbtns = treeMenu.querySelectorAll(".dropbtn");
    dropbtns.forEach((button) => {
      button.addEventListener("click", toggleList);
    });
  }

  init();
});
