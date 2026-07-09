document.addEventListener('DOMContentLoaded', () => {
    
    /* -------------------------------------
       1. Mobile Menu Toggle
    -------------------------------------- */
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuLinks = document.querySelectorAll('.mobile-link');
    let menuOpen = false;

    function toggleMenu() {
        menuOpen = !menuOpen;
        if (menuOpen) {
            mobileMenu.classList.remove('hidden');
            mobileMenu.classList.add('flex');
            document.body.style.overflow = 'hidden'; // Evita scroll do fundo
            menuBtn.innerHTML = '<i class="ph ph-x"></i>'; // Muda ícone para X
        } else {
            mobileMenu.classList.add('hidden');
            mobileMenu.classList.remove('flex');
            document.body.style.overflow = ''; // Restaura scroll
            menuBtn.innerHTML = '<i class="ph ph-list"></i>'; // Restaura hambúrguer
        }
    }

    if (menuBtn) {
        menuBtn.addEventListener('click', toggleMenu);
    }

    // Fecha o menu ao clicar em algum link
    menuLinks.forEach(link => {
        link.addEventListener('click', toggleMenu);
    });


    /* -------------------------------------
       2. Testimonial Slider (Mobile & Desktop)
    -------------------------------------- */
    const slider = document.getElementById('testimonial-slider');
    const dots = document.querySelectorAll('.slider-dot');
    const cards = document.querySelectorAll('.testimonial-card');

    if (slider && cards.length > 0) {
        // Função para calcular qual card está exatamente no centro
        const updateActiveCard = () => {
            const sliderCenter = slider.offsetWidth / 2;
            let closestCard = null;
            let closestDistance = Infinity;

            cards.forEach(card => {
                const cardCenter = card.offsetLeft + (card.offsetWidth / 2) - slider.scrollLeft;
                const distance = Math.abs(sliderCenter - cardCenter);
                if (distance < closestDistance) {
                    closestDistance = distance;
                    closestCard = card;
                }
            });

            cards.forEach((card, index) => {
                if (card === closestCard) {
                    card.classList.add('scale-100', 'z-10', 'shadow-card');
                    card.classList.remove('scale-75', 'z-0', 'shadow-none', 'opacity-50');
                    dots[index].classList.add('bg-mex-red', 'scale-125');
                    dots[index].classList.remove('bg-gray-300');
                } else {
                    card.classList.remove('scale-100', 'z-10', 'shadow-card');
                    card.classList.add('scale-75', 'z-0', 'shadow-none');
                    dots[index].classList.remove('bg-mex-red', 'scale-125');
                    dots[index].classList.add('bg-gray-300');
                }
            });
        };

        slider.addEventListener('scroll', updateActiveCard);
        window.addEventListener('resize', updateActiveCard);
        
        // Força a atualização inicial após o carregamento do layout
        setTimeout(updateActiveCard, 100);

        // Clicar nas bolinhas para rolar o slider até o card exato
        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => {
                cards[i].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            });
        });
    }

    /* -------------------------------------
       3. Smooth Scrolling (Fallback/Enhancement)
    -------------------------------------- */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

});
