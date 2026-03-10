document.addEventListener('DOMContentLoaded', () => {
    // Initial Load Animation
    setTimeout(() => {
        document.body.classList.remove('loading');
        document.body.classList.add('loaded');
    }, 100);

    // --- Spotlight Background Glow ---
    const glowBg = document.querySelector('.glow-bg');
    
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    
    if (!isTouchDevice && glowBg) {
        
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            glowBg.style.setProperty('--gx', `${mouseX}px`);
            glowBg.style.setProperty('--gy', `${mouseY}px`);
        });

    } else if (glowBg) {
        glowBg.style.display = 'none';
    }

    // --- Magnetic Elements ---
    const magneticElements = document.querySelectorAll('.magnetic');
    if (!isTouchDevice) {
        magneticElements.forEach(el => {
            el.addEventListener('mousemove', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                const strength = el.getAttribute('data-strength') || 20;
                el.style.transform = `translate(${x / strength}px, ${y / strength}px)`;
            });

            el.addEventListener('mouseleave', () => {
                el.style.transform = `translate(0px, 0px)`;
                el.style.transition = 'transform 0.5s cubic-bezier(0.19, 1, 0.22, 1)';
            });
            
            el.addEventListener('mouseenter', () => {
                el.style.transition = 'none';
            });
        });
    }

    // --- Intersection Observer for Fade Up ---
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -5% 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach(element => {
        observer.observe(element);
    });

    // --- Flex Accordion Interaction ---
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            // Remove active from all
            accordionItems.forEach(el => el.classList.remove('active'));
            // Add active to hovered
            item.classList.add('active');
        });
        
        // Support for touch devices (only if it's NOT a video item to prevent intercepting clicks)
        if (!item.classList.contains('video-item')) {
            item.addEventListener('click', () => {
                accordionItems.forEach(el => el.classList.remove('active'));
                item.classList.add('active');
            });
        }
    });

    // --- Video Reel Modal Interaction ---
    const videoCards = document.querySelectorAll('.video-item');
    const reelModal = document.getElementById('reelModal');
    if (reelModal) {
        const reelVideo = document.getElementById('reelVideo');
        const closeModal = reelModal.querySelector('.close-modal');

        videoCards.forEach(card => {
            card.addEventListener('click', () => {
                const videoSrc = card.getAttribute('data-video-src');
                const posterStr = card.getAttribute('data-poster');
                
                reelVideo.src = videoSrc;
                reelVideo.poster = posterStr;
                reelVideo.load();
                
                reelModal.classList.add('is-open');
                reelVideo.play().catch(e => console.log("Auto-play prevented by browser."));
            });
        });

        const closeReel = () => {
            reelModal.classList.remove('is-open');
            reelVideo.pause();
            setTimeout(() => {
                reelVideo.src = "";
            }, 500);
        };

        closeModal.addEventListener('click', closeReel);
        
        reelModal.addEventListener('click', (e) => {
            if(e.target === reelModal || e.target.classList.contains('modal-bg')) {
                closeReel();
            }
        });
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && reelModal.classList.contains('is-open')) {
                closeReel();
            }
        });
    }


});
