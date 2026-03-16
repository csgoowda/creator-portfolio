document.addEventListener('DOMContentLoaded', () => {
    // 1. Reveal Strategy: Immediate body reveal, then staggered content
    const revealPage = () => {
        document.body.classList.remove('loading');
        document.body.classList.add('loaded');
    };
    revealPage();

    // 2. Cinematic Interaction Engine (Scroll Reveals)
    const initScrollReveals = () => {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        const revealElements = document.querySelectorAll('.reveal, .stagger-reveal, .fade-up');
        revealElements.forEach(el => revealObserver.observe(el));

        // --- FALLBACK: Force reveal if observer fails to trigger (e.g. hash links or load errors) ---
        setTimeout(() => {
            revealElements.forEach(el => {
                if (!el.classList.contains('active')) {
                    el.classList.add('active');
                }
            });
        }, 1500);
    };

    // 3. Fluid Cursor & Interactive Highlights
    // 3. Ultra-Reliable High-Tech Cursor
    const initCursor = () => {
        const dot = document.querySelector('.cursor-dot');
        const outline = document.querySelector('.cursor-outline');
        const trails = document.querySelectorAll('.cursor-trail');
        
        if (!dot && !outline) return;

        let mouseX = -100, mouseY = -100;
        let dotX = -100, dotY = -100;
        let outlineX = -100, outlineY = -100;
        let isFirstMove = true;

        const trailPositions = Array.from({ length: trails.length || 0 }, () => ({ x: -100, y: -100 }));

        // Ripple Effect on Click
        window.addEventListener('mousedown', (e) => {
            const ripple = document.createElement('div');
            ripple.className = 'cursor-ripple';
            ripple.style.left = `${e.clientX}px`;
            ripple.style.top = `${e.clientY}px`;
            document.body.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });

        // Mouse Move Listener
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;

            if (isFirstMove) {
                dotX = mouseX;
                dotY = mouseY;
                outlineX = mouseX;
                outlineY = mouseY;
                trailPositions.forEach(p => { p.x = mouseX; p.y = mouseY; });
                isFirstMove = false;
                
                // Show cursor
                if (dot) dot.style.opacity = "1";
                if (outline) outline.style.opacity = "1";
                trails.forEach(t => t.style.opacity = "0.3");
            }
        }, { passive: true });

        // Initial CSS hide
        if (dot) dot.style.opacity = "0";
        if (outline) outline.style.opacity = "0";
        trails.forEach(t => t.style.opacity = "0");

        // Animation Loop
        const render = () => {
            if (!isFirstMove) {
                dotX += (mouseX - dotX) * 0.35;
                dotY += (mouseY - dotY) * 0.35;
                outlineX += (mouseX - outlineX) * 0.18;
                outlineY += (mouseY - outlineY) * 0.18;

                if (dot) dot.style.transform = `translate(${dotX}px, ${dotY}px) translate(-50%, -50%)`;
                if (outline) outline.style.transform = `translate(${outlineX}px, ${outlineY}px) translate(-50%, -50%)`;

                trails.forEach((trail, index) => {
                    const targetX = index === 0 ? dotX : trailPositions[index - 1].x;
                    const targetY = index === 0 ? dotY : trailPositions[index - 1].y;

                    trailPositions[index].x += (targetX - trailPositions[index].x) * 0.25;
                    trailPositions[index].y += (targetY - trailPositions[index].y) * 0.25;

                    trail.style.transform = `translate(${trailPositions[index].x}px, ${trailPositions[index].y}px) translate(-50%, -50%) scale(${1 - index * 0.15})`;
                });
            }
            requestAnimationFrame(render);
        };
        render();

        // Hover States
        const interactables = 'a, button, .magnetic, .video-item, .command-card, .accordion-item';
        document.querySelectorAll(interactables).forEach(el => {
            el.addEventListener('mouseenter', () => {
                outline?.classList.add('active');
                dot?.classList.add('active');
            });
            el.addEventListener('mouseleave', () => {
                outline?.classList.remove('active');
                dot?.classList.remove('active');
            });
        });
    };

    // Add Keyframes via JS for dynamic pulse
    const style = document.createElement('style');
    style.textContent = `
        @keyframes crossHairPulse {
            0%, 100% { transform: translate(-50%, -50%) scale(1); }
            50% { transform: translate(-50%, -50%) scale(1.1); filter: brightness(1.5); }
        }
    `;
    document.head.appendChild(style);

    // 4. Magnetic Effects
    const initMagnetic = () => {
        document.querySelectorAll('.magnetic').forEach(el => {
            el.addEventListener('mousemove', function (e) {
                const pos = this.getBoundingClientRect();
                const x = e.clientX - pos.left;
                const y = e.clientY - pos.top;
                const strength = this.getAttribute('data-strength') || 40;
                const moveX = (x - pos.width / 2) / pos.width * strength;
                const moveY = (y - pos.height / 2) / pos.height * strength;
                this.style.transform = `translate(${moveX}px, ${moveY}px)`;
            });
            el.addEventListener('mouseleave', function () {
                this.style.transform = 'translate(0px, 0px)';
            });
        });
    };

    // 5. Video Modal System
    const initModal = () => {
        const modal = document.getElementById('reelModal');
        const modalVideo = document.getElementById('reelVideo');
        if (!modal || !modalVideo) return;

        const closeBtn = modal.querySelector('.close-modal');
        const modalBg = modal.querySelector('.modal-bg');

        const openModal = (src) => {
            const source = modalVideo.querySelector('source');
            if (source) source.src = src;
            modalVideo.load();
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.classList.add('is-open');
                modalVideo.play().catch(() => { });
            }, 10);
        };

        const closeModal = () => {
            modal.classList.remove('is-open');
            setTimeout(() => {
                modal.style.display = 'none';
                modalVideo.pause();
                modalVideo.currentTime = 0;
            }, 500);
        };

        document.querySelectorAll('[data-video-src]').forEach(card => {
            card.addEventListener('click', () => openModal(card.getAttribute('data-video-src')));
        });

        closeBtn?.addEventListener('click', closeModal);
        modalBg?.addEventListener('click', closeModal);
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });
    };

    // 6. Background Effects (Spotlight)
    const initGlow = () => {
        const glowBg = document.querySelector('.glow-bg');
        if (!glowBg || 'ontouchstart' in window) return;

        window.addEventListener('mousemove', (e) => {
            glowBg.style.setProperty('--gx', `${e.clientX}px`);
            glowBg.style.setProperty('--gy', `${e.clientY}px`);
        });
    };

    // 7. Hero Typing Effect
    const initTyping = () => {
        const target = document.querySelector('.type-effect');
        if (!target) return;
        const text = target.innerText;
        target.innerText = '';
        let i = 0;
        const type = () => {
            if (i < text.length) {
                target.innerText += text.charAt(i);
                i++;
                setTimeout(type, 100);
            }
        };
        setTimeout(type, 800);
    };

    // 8. Scroll Progress
    const initScrollProgress = () => {
        const bar = document.querySelector('.scroll-progress');
        if (!bar) return;
        window.addEventListener('scroll', () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            bar.style.width = scrolled + "%";
        });
    };

    // 9. Command Card Scanner Pulse
    const initScanners = () => {
        document.querySelectorAll('.command-card').forEach(card => {
            const scanner = card.querySelector('.card-scanner');
            if (scanner) {
                setInterval(() => {
                    scanner.style.top = '-10%';
                    setTimeout(() => { scanner.style.top = '110%'; }, 100);
                }, 4000);
            }
        });
    };

    // 10. Mobile Menu Logic
    const initMobileMenu = () => {
        const toggle = document.querySelector('.menu-toggle');
        const navLinks = document.querySelector('.nav-links');
        const links = document.querySelectorAll('.nav-links a');

        if (!toggle || !navLinks) return;

        const toggleMenu = () => {
            toggle.classList.toggle('active');
            navLinks.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        };

        toggle.addEventListener('click', toggleMenu);

        links.forEach(link => {
            link.addEventListener('click', () => {
                toggle.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.classList.remove('no-scroll');
            });
        });
    };

    // Initialization
    initScrollReveals();
    initCursor();
    initMagnetic();
    initModal();
    initGlow();
    initTyping();
    initScrollProgress();
    initScanners();
    initMobileMenu();

    // Accordion
    document.querySelectorAll('.accordion-item').forEach(item => {
        const activate = () => {
            document.querySelectorAll('.accordion-item').forEach(el => el.classList.remove('active'));
            item.classList.add('active');
        };
        item.addEventListener('mouseenter', activate);
        item.addEventListener('click', activate);
    });
});