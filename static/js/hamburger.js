document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.getElementById('navbar-default');
    const hamburger = document.getElementById('hamburger');

    function openNavBar() {
        const hidden = navbar.classList.toggle('hidden');
        if (hidden) {
            console.log('Desativado');
        }
        else {
            console.log('Ativado');
        }
    }

    hamburger.addEventListener('click', openNavBar);
});
