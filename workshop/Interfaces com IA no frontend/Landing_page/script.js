// MENU MOBILE
const menuMobile = document.getElementById('menu-mobile');
const menu = document.querySelector('.menu');

menuMobile.addEventListener('click', () => {
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
});

// ROLAGEM SUAVE
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 60,
                behavior: 'smooth'
            });
        }
    });
});

// ANIMAÇÃO FADE-IN
const elements = document.querySelectorAll('section, .card');
const fadeInOnScroll = () => {
    elements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight - 50) {
            el.style.opacity = 1;
            el.style.transform = 'translateY(0)';
        }
    });
};
window.addEventListener('scroll', fadeInOnScroll);

// FORMULÁRIO
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();

    if (!nome || !email || !mensagem) {
        alert('Preencha todos os campos!');
        return;
    }

    alert('Mensagem enviada com sucesso!');
    this.reset();
});
