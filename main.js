/* ================================
   LOVE STORIES – main.js
   Luxury Wedding Planner · Rhodes
================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ========================
     CUSTOM CURSOR
  ======================== */
  const dot  = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');

  let mouseX = 0, mouseY = 0;
  let ringX  = 0, ringY  = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = mouseX + 'px';
    dot.style.top  = mouseY + 'px';
  });

  // Smooth ring follow
  function animateRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;
    ring.style.left = ringX + 'px';
    ring.style.top  = ringY + 'px';
    requestAnimationFrame(animateRing);
  }
  animateRing();

  // Scale cursor on hover
  document.querySelectorAll('a, button, .service-card, .arch-item').forEach(el => {
    el.addEventListener('mouseenter', () => {
      dot.style.width  = '12px';
      dot.style.height = '12px';
      ring.style.width  = '48px';
      ring.style.height = '48px';
    });
    el.addEventListener('mouseleave', () => {
      dot.style.width  = '7px';
      dot.style.height = '7px';
      ring.style.width  = '32px';
      ring.style.height = '32px';
    });
  });

  /* ========================
     NAVBAR SCROLL
  ======================== */
  const navbar = document.getElementById('navbar');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
    updateFloatCta();
    parallaxHero();
  }, { passive: true });

  /* ========================
     HERO PARALLAX
  ======================== */
  const heroImg = document.getElementById('heroImg');

  function parallaxHero() {
    if (!heroImg) return;
    const offset = window.scrollY * 0.08;
    heroImg.style.transform = `scale(1.04) translateY(${offset}px)`;
  }

  /* ========================
     MOBILE MENU
  ======================== */
  const hamburger  = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileLinks = document.querySelectorAll('.mobile-link');
  let menuOpen = false;

  hamburger.addEventListener('click', () => {
    menuOpen = !menuOpen;
    mobileMenu.classList.toggle('open', menuOpen);
    // Animate hamburger
    const spans = hamburger.querySelectorAll('span');
    if (menuOpen) {
      spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
      spans[1].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.transform = '';
    }
  });

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      menuOpen = false;
      mobileMenu.classList.remove('open');
      const spans = hamburger.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.transform = '';
    });
  });

  /* ========================
     SCROLL REVEAL
  ======================== */
  const revealEls = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = parseInt(entry.target.dataset.delay || 0);
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -60px 0px',
  });

  revealEls.forEach(el => revealObserver.observe(el));

  /* ========================
     VIDEO SCROLL PLAY
  ======================== */
  const stripVideo = document.getElementById('stripVideo');
  if (stripVideo) {
    const videoObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          stripVideo.play().catch(e => console.log('Autoplay prevented:', e));
        } else {
          stripVideo.pause();
        }
      });
    }, { threshold: 0.2 });
    videoObserver.observe(stripVideo);
  }

  /* ========================
     FLOATING CTA
  ======================== */
  const floatCta = document.getElementById('floatCta');

  function updateFloatCta() {
    if (window.scrollY > 300) {
      floatCta.classList.add('visible');
    } else {
      floatCta.classList.remove('visible');
    }
  }

  /* ========================
     CONTACT FORM
  ======================== */
  const form       = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const data = {
        name:    form.name.value.trim(),
        email:   form.email.value.trim(),
        date:    form.date.value.trim(),
        message: form.message.value.trim(),
      };

      if (!data.name || !data.email) {
        // Simple validation highlight
        if (!data.name)  animateError(form.querySelector('#name'));
        if (!data.email) animateError(form.querySelector('#email'));
        return;
      }

      // --- Wire up your email / CRM here ---
      // Example: fetch('/api/contact', { method: 'POST', body: JSON.stringify(data) });
      console.log('Form data:', data);

      // Show success
      form.style.opacity = '0';
      form.style.transition = 'opacity .4s';
      setTimeout(() => {
        form.style.display = 'none';
        formSuccess.style.display = 'block';
        formSuccess.style.opacity = '0';
        requestAnimationFrame(() => {
          formSuccess.style.transition = 'opacity .5s';
          formSuccess.style.opacity = '1';
        });
      }, 400);
    });
  }

  function animateError(input) {
    if (!input) return;
    input.style.borderBottomColor = '#c0392b';
    input.style.transition = 'border-color .3s';
    setTimeout(() => { input.style.borderBottomColor = ''; }, 2000);
  }

  /* ========================
     SMOOTH ACTIVE NAV LINKS
  ======================== */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a');

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navAnchors.forEach(a => {
          a.style.opacity = a.getAttribute('href') === `#${id}` ? '1' : '0.55';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));

  /* ========================
     GALLERY DRAG SCROLL
  ======================== */
  const archRow = document.querySelector('.arch-row');
  if (archRow) {
    let isDown = false, startX, scrollLeft;

    archRow.addEventListener('mousedown', (e) => {
      isDown = true;
      startX = e.pageX - archRow.offsetLeft;
      scrollLeft = archRow.scrollLeft;
    });
    archRow.addEventListener('mouseleave', () => isDown = false);
    archRow.addEventListener('mouseup', () => isDown = false);
    archRow.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - archRow.offsetLeft;
      archRow.scrollLeft = scrollLeft - (x - startX) * 1.5;
    });
  }

  /* ========================
     SERVICE CARD HOVER
     (border-top fix for CSS-only hover)
  ======================== */
  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.borderTopColor = 'var(--gold)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.borderTopColor = 'transparent';
    });
  });

});
