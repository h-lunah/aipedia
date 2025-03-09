const currentUrl = window.location.pathname;

function edit() {
  const article = document.querySelector(".entry-content");
  const editButton = document.querySelector(".edit-button");

  if (article.getAttribute("contenteditable") === "false") {
    article.setAttribute("contenteditable", "true");
    editButton.textContent = "Save";
    article.focus();
  } else {
    article.setAttribute("contenteditable", "false");
    editButton.textContent = "Edit";
  }
}

function search() {
  const searchTerm = window.prompt("Enter a topic to search for.");

  if (searchTerm) {
    window.location.href = `/wiki/${searchTerm}`;
  }
}

function back() {
  if (document.referrer === "" || currentUrl === "/wiki/Main_Page") {
    window.location.href = "/wiki/Main_Page";
  } else {
    history.back();
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.querySelector(".model-dropdown");
  selectElement.value =
    localStorage.getItem("selectedModel") || "gemini-2.0-flash";

  selectElement.addEventListener("change", async function (event) {
    event.preventDefault(); // Prevents any default form submission behavior

    const selectedValue = selectElement.value;

    const response = await fetch("/api/select-model", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ value: selectedValue }),
    });

    if (!response.ok) {
      throw new Error(
        `Request to set model failed with status code ${response.status}`,
      );
    }

    localStorage.setItem("selectedModel", selectedValue);
    location.reload();
  });
});

if (currentUrl === "/wiki/Main_Page") {
  const backButton = document.querySelector(".back-button");
  const editButton = document.querySelector(".edit-button");
  const homeButton = document.querySelector(".home-button");

  if (backButton) {
    backButton.remove();
  }

  if (editButton) {
    editButton.remove();
  }

  if (homeButton) {
    homeButton.style.fontWeight = 600;
  }
} else {
  const searchButton = document.querySelector(".search-button");

  if (searchButton) {
    searchButton.remove();
  }
}

const wikiPath = currentUrl.split("/")[2];

const normalizedUrl = decodeURIComponent(
  `/wiki/${wikiPath.charAt(0).toUpperCase()}${wikiPath.slice(1)}`,
).replace(/ /g, "_");

history.pushState({}, "", normalizedUrl);
