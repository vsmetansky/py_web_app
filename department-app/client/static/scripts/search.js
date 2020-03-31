const NAV = document.getElementById('nav-container');
const MENU = NAV.innerHTML;

const SEARCH_BAR = `
<div class="search-bar">
    <input id="search-field" type="search">
    <button class="nav-button right" autofocus onclick="closeSearchBar()">Close</button>
</div>`;

function showSearchBar() {
    NAV.innerHTML = SEARCH_BAR;
    document.getElementById('search-field').focus()
}

function closeSearchBar() {
    NAV.innerHTML = MENU;
}

function search() {
    i
}