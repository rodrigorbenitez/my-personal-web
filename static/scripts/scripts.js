document.addEventListener('DOMContentLoaded', () => {

    // Start by loading first page.
    load_page('home');

    // Set links up to load new pages.
    document.querySelectorAll('.nav-link').forEach(link => {
        link.onclick = () => {
            load_page(link.dataset.page);
            return false;
        };
    });
});
