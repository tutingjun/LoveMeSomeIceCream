// for index.html
// use different divs for different search options
function changeSearchArea(name) {
  clearAll();
  if (name === "brand") {
    document.getElementById("brand-search").style.display = "flex";
  }
  else if (name === "name") {
    document.getElementById("site-search").style.display = "flex";
    document.getElementById("site-search-text").placeholder='Enter product name';
  }
  else if (name === "ingredients") {
    document.getElementById("site-search").style.display = "flex";
    document.getElementById("site-search-text").placeholder='Enter an ingredient';
  }
  else if (name === "advance"){
    document.getElementById("advance-search").style.display = "block";
  }
}

function clearAll(){
    var seachDropDown = document.getElementById("brand-search");
    var searchBar = document.getElementById("site-search");
    var advanceSearch = document.getElementById("advance-search");

    seachDropDown.style.display = "none";
    searchBar.style.display = "none";
    advanceSearch.style.display = "none";
}
