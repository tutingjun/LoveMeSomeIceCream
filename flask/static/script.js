/* sets different search area divs for different search conditions */
function changeSearchArea(name) {
  clearAll();
  if (name === "brand") {
    document.getElementById("brand-search").style.display = "flex";
  }
  else if (name === "name") {
    document.getElementById("site-search").style.display = "flex";
    document.getElementById("site-search-text").placeholder='Enter product name, eg. Salted Caramel Core';
    document.getElementById("nameHelpTab").textContent="Name: could be the displayed product name or its full name(ie. subhead, see subhead info in product detail page)";
  }
  else if (name === "ingredients") {
    document.getElementById("site-search").style.display = "flex";
    document.getElementById("site-search-text").placeholder='Enter an ingredient, eg. chocolate';
  }
  else if (name === "advance"){
    document.getElementById("advance-search").style.display = "block";
  }
}


/* initiates the search area by clearing all divs that correspond to other search conditions */
function clearAll(){
    var seachDropDown = document.getElementById("brand-search");
    var searchBar = document.getElementById("site-search");
    var advanceSearch = document.getElementById("advance-search");

    seachDropDown.style.display = "none";
    searchBar.style.display = "none";
    advanceSearch.style.display = "none";
}
