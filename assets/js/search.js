(function () {
  "use strict";

  var input = document.getElementById("search-input");
  var resultsList = document.getElementById("search-results");
  var status = document.getElementById("search-status");
  if (!input || !resultsList) return;

  var documents = [];
  var index = null;

  status.textContent = "Loading search index…";

  fetch("/search.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      documents = data;
      index = lunr(function () {
        this.ref("url");
        this.field("title", { boost: 10 });
        this.field("speaker", { boost: 5 });
        this.field("tags", { boost: 5 });
        this.field("content");

        documents.forEach(function (doc) {
          this.add(doc);
        }, this);
      });
      status.textContent = "";
      input.disabled = false;
    })
    .catch(function () {
      status.textContent = "Could not load the search index.";
    });

  function render(matches) {
    resultsList.innerHTML = "";
    if (!matches.length) {
      status.textContent = "No talks found.";
      return;
    }
    status.textContent = matches.length + " result(s)";
    matches.forEach(function (match) {
      var doc = documents.find(function (d) {
        return d.url === match.ref;
      });
      if (!doc) return;
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = doc.url;
      a.textContent = doc.title;
      li.appendChild(a);
      if (doc.month || doc.speaker) {
        var meta = document.createElement("span");
        meta.textContent =
          " — " + [doc.month, doc.speaker].filter(Boolean).join(" · ");
        li.appendChild(meta);
      }
      resultsList.appendChild(li);
    });
  }

  input.addEventListener("input", function () {
    var query = input.value.trim();
    if (!index || query.length < 2) {
      resultsList.innerHTML = "";
      status.textContent = "";
      return;
    }
    var matches;
    try {
      matches = index.search(
        query
          .split(/\s+/)
          .map(function (term) {
            return term + "*";
          })
          .join(" ")
      );
    } catch (e) {
      matches = [];
    }
    render(matches.slice(0, 25));
  });
})();
