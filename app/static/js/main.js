document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menu-button');
    const menuContainer = document.getElementById('menu-container');
    const pages = ['Travel', 'Food', 'Drinks', 'Activities', 'Room Arrangements'];

    menuButton.addEventListener('click', function() {
        menuContainer.classList.toggle('menu-open');
        updateMenu();
    });

    function updateMenu() {
        menuContainer.innerHTML = ''; // Clear previous menu items

        pages.forEach(page => {
            const link = document.createElement('a');
            link.href = `/${page.toLowerCase().replace(' ', '_')}`;
            link.textContent = page;
            menuContainer.appendChild(link);
        });
    }
});