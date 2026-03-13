document.addEventListener('DOMContentLoaded', () => {
    const dot = document.querySelector('.cursor-dot');
    const outline = document.querySelector('.cursor-outline');
    
    let mouseX = 0;
    let mouseY = 0;
    let dotX = 0;
    let dotY = 0;
    let outlineX = 0;
    let outlineY = 0;

    // Smooth cursor movement
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    const trails = document.querySelectorAll('.cursor-trail');
    const trailPositions = Array.from({ length: trails.length }, () => ({ x: 0, y: 0 }));

    const animateCursor = () => {
        // Dot movement (faster)
        dotX += (mouseX - dotX) * 0.2;
        dotY += (mouseY - dotY) * 0.2;
        dot.style.left = `${dotX}px`;
        dot.style.top = `${dotY}px`;

        // Outline movement (radar)
        outlineX += (mouseX - outlineX) * 0.15;
        outlineY += (mouseY - outlineY) * 0.15;
        outline.style.left = `${outlineX}px`;
        outline.style.top = `${outlineY}px`;

        // Trail dots (sequential delay)
        trails.forEach((trail, index) => {
            const nextX = index === 0 ? dotX : trailPositions[index - 1].x;
            const nextY = index === 0 ? dotY : trailPositions[index - 1].y;
            
            trailPositions[index].x += (nextX - trailPositions[index].x) * (0.15 - index * 0.02);
            trailPositions[index].y += (nextY - trailPositions[index].y) * (0.15 - index * 0.02);
            
            trail.style.left = `${trailPositions[index].x}px`;
            trail.style.top = `${trailPositions[index].y}px`;
            trail.style.opacity = 0.4 - (index * 0.1);
            trail.style.transform = `translate(-50%, -50%) scale(${1 - index * 0.2})`;
        });

        requestAnimationFrame(animateCursor);
    };
    
    animateCursor();

    // Hover states for links and buttons
    const linkElements = document.querySelectorAll('a, button, .magnetic, .video-item');
    
    linkElements.forEach(link => {
        link.addEventListener('mouseenter', () => {
            dot.classList.add('active');
            outline.classList.add('active');
        });
        
        link.addEventListener('mouseleave', () => {
            dot.classList.remove('active');
            outline.classList.remove('active');
        });
    });

    // Viewfinder morphing for videos
    const videoCards = document.querySelectorAll('.video-item, .mini-reel-card');
    videoCards.forEach(card => {
        card.addEventListener('mouseenter', () => outline.classList.add('viewfinder'));
        card.addEventListener('mouseleave', () => outline.classList.remove('viewfinder'));
    });

    // Magnetic Effect Implementation
    const magneticElements = document.querySelectorAll('.magnetic');
    
    magneticElements.forEach(el => {
        el.addEventListener('mousemove', function(e) {
            const pos = this.getBoundingClientRect();
            const mouseX = e.clientX - pos.left;
            const mouseY = e.clientY - pos.top;
            
            const strength = this.getAttribute('data-strength') || 40;
            const moveX = (mouseX - pos.width / 2) / pos.width * strength;
            const moveY = (mouseY - pos.height / 2) / pos.height * strength;
            
            this.style.transform = `translate(${moveX}px, ${moveY}px)`;
        });
        
        el.addEventListener('mouseleave', function() {
            this.style.transform = 'translate(0px, 0px)';
        });
    });

    // Video Modal System
    const modal = document.getElementById('reelModal');
    const modalVideo = document.getElementById('reelVideo');
    const closeBtn = document.querySelector('.close-modal');
    const modalBg = document.querySelector('.modal-bg');

    const openModal = (src) => {
        if (!src) return;
        const source = modalVideo.querySelector('source');
        source.src = src;
        modalVideo.load();
        modal.style.display = 'flex';
        setTimeout(() => {
            modal.classList.add('is-open');
            modalVideo.play().catch(err => console.log("Auto-play blocked or error:", err));
        }, 10);
    };

    const closeModal = () => {
        modal.classList.remove('is-open');
        setTimeout(() => {
            modal.style.display = 'none';
            modalVideo.pause();
            modalVideo.currentTime = 0;
            const source = modalVideo.querySelector('source');
            source.src = "";
        }, 500);
    };

    videoCards.forEach(card => {
        card.addEventListener('click', () => {
            const videoSrc = card.getAttribute('data-video-src');
            openModal(videoSrc);
        });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (modalBg) modalBg.addEventListener('click', closeModal);

    // Reveal animations on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

    // Reveal page
    document.body.classList.remove('loading');
    document.body.classList.add('loaded');
});
