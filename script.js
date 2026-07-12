/* ═══════════════════════════════════════════
   QUILLIX — interactions & animations
   ═══════════════════════════════════════════ */

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ── Preloader ── */
window.addEventListener("load", () => {
  setTimeout(() => {
    document.getElementById("preloader").classList.add("done");
  }, prefersReducedMotion ? 0 : 900);
});

/* ── Custom cursor ── */
(() => {
  const dot = document.getElementById("cursorDot");
  const ring = document.getElementById("cursorRing");
  if (window.matchMedia("(hover: none), (pointer: coarse)").matches) return;

  let mx = -100, my = -100, rx = -100, ry = -100;

  window.addEventListener("mousemove", (e) => {
    mx = e.clientX;
    my = e.clientY;
    dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%, -50%)`;
  });

  (function follow() {
    rx += (mx - rx) * 0.16;
    ry += (my - ry) * 0.16;
    ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%, -50%)`;
    requestAnimationFrame(follow);
  })();

  document.querySelectorAll("a, button, [data-tilt]").forEach((el) => {
    el.addEventListener("mouseenter", () => document.body.classList.add("cursor-hover"));
    el.addEventListener("mouseleave", () => document.body.classList.remove("cursor-hover"));
  });
})();

/* ── Scroll progress + navbar state ── */
(() => {
  const bar = document.getElementById("scrollProgress");
  const nav = document.getElementById("nav");

  const onScroll = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = `${max > 0 ? (window.scrollY / max) * 100 : 0}%`;
    nav.classList.toggle("scrolled", window.scrollY > 40);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();

/* ── Mobile nav ── */
(() => {
  const burger = document.getElementById("navBurger");
  const links = document.getElementById("navLinks");

  burger.addEventListener("click", () => {
    burger.classList.toggle("open");
    links.classList.toggle("open");
  });

  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      burger.classList.remove("open");
      links.classList.remove("open");
    })
  );
})();

/* ── Typewriter ── */
(() => {
  const el = document.getElementById("typewriter");
  const words = ["limits.", "deadlines.", "doubt.", "the blank page."];
  let wordIdx = 0, charIdx = 0, deleting = false;

  if (prefersReducedMotion) {
    el.textContent = words[0];
    return;
  }

  (function tick() {
    const word = words[wordIdx];
    charIdx += deleting ? -1 : 1;
    el.textContent = word.slice(0, charIdx);

    let delay = deleting ? 45 : 95;
    if (!deleting && charIdx === word.length) {
      delay = 1800;
      deleting = true;
    } else if (deleting && charIdx === 0) {
      deleting = false;
      wordIdx = (wordIdx + 1) % words.length;
      delay = 350;
    }
    setTimeout(tick, delay);
  })();
})();

/* ── Particle canvas ── */
(() => {
  const canvas = document.getElementById("particles");
  const ctx = canvas.getContext("2d");
  if (prefersReducedMotion) return;

  let particles = [];
  let w, h;

  const resize = () => {
    w = canvas.width = canvas.offsetWidth;
    h = canvas.height = canvas.offsetHeight;
    const count = Math.min(90, Math.floor((w * h) / 16000));
    particles = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      r: Math.random() * 1.8 + 0.6,
    }));
  };

  resize();
  window.addEventListener("resize", resize);

  (function draw() {
    ctx.clearRect(0, 0, w, h);

    for (const p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(139, 92, 246, 0.55)";
      ctx.fill();
    }

    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i], b = particles[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.hypot(dx, dy);
        if (dist < 130) {
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(236, 72, 153, ${0.14 * (1 - dist / 130)})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  })();
})();

/* ── Reveal on scroll ── */
(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );

  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
})();

/* ── Animated counters ── */
(() => {
  const counters = document.querySelectorAll(".stat-number");

  const animate = (el) => {
    const target = Number(el.dataset.count);
    const suffix = el.dataset.suffix || "";
    const duration = 1800;
    const start = performance.now();

    const step = (now) => {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 4);
      el.textContent = Math.round(target * eased) + suffix;
      if (t < 1) requestAnimationFrame(step);
    };

    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animate(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.6 }
  );

  counters.forEach((el) => observer.observe(el));
})();

/* ── 3D tilt cards + glow tracking ── */
(() => {
  if (prefersReducedMotion || window.matchMedia("(hover: none)").matches) return;

  document.querySelectorAll("[data-tilt]").forEach((card) => {
    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width;
      const py = (e.clientY - rect.top) / rect.height;

      card.style.transform =
        `perspective(800px) rotateY(${(px - 0.5) * 10}deg) rotateX(${(0.5 - py) * 10}deg) translateY(-4px)`;
      card.style.setProperty("--mx", `${px * 100}%`);
      card.style.setProperty("--my", `${py * 100}%`);
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "";
    });
  });
})();

/* ── Magnetic buttons ── */
(() => {
  if (prefersReducedMotion || window.matchMedia("(hover: none)").matches) return;

  document.querySelectorAll("[data-magnetic]").forEach((el) => {
    el.addEventListener("mousemove", (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      el.style.transform = `translate(${x * 0.22}px, ${y * 0.22}px)`;
    });

    el.addEventListener("mouseleave", () => {
      el.style.transform = "";
    });
  });
})();

/* ── Timeline progress fill ── */
(() => {
  const line = document.getElementById("timelineLine");
  if (!line) return;

  const update = () => {
    const rect = line.getBoundingClientRect();
    const viewH = window.innerHeight;
    const progress = Math.min(Math.max((viewH * 0.75 - rect.top) / rect.height, 0), 1);
    line.style.setProperty("--fill", `${progress * 100}%`);
  };

  window.addEventListener("scroll", update, { passive: true });
  update();
})();

/* ── Testimonial carousel ── */
(() => {
  const track = document.getElementById("carouselTrack");
  const dotsWrap = document.getElementById("carouselDots");
  const slides = track.children.length;
  let current = 0;
  let timer;

  for (let i = 0; i < slides; i++) {
    const dot = document.createElement("button");
    dot.setAttribute("aria-label", `Go to slide ${i + 1}`);
    dot.addEventListener("click", () => {
      goTo(i);
      restart();
    });
    dotsWrap.appendChild(dot);
  }

  const dots = [...dotsWrap.children];

  const goTo = (i) => {
    current = (i + slides) % slides;
    track.style.transform = `translateX(-${current * 100}%)`;
    dots.forEach((d, idx) => d.classList.toggle("active", idx === current));
  };

  const restart = () => {
    clearInterval(timer);
    if (!prefersReducedMotion) {
      timer = setInterval(() => goTo(current + 1), 5000);
    }
  };

  goTo(0);
  restart();

  /* swipe support */
  let startX = null;
  track.addEventListener("touchstart", (e) => (startX = e.touches[0].clientX), { passive: true });
  track.addEventListener("touchend", (e) => {
    if (startX === null) return;
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) {
      goTo(current + (dx < 0 ? 1 : -1));
      restart();
    }
    startX = null;
  });
})();

/* ── Parallax orbs on mouse ── */
(() => {
  if (prefersReducedMotion || window.matchMedia("(hover: none)").matches) return;

  const orbs = document.querySelectorAll(".orb");

  window.addEventListener("mousemove", (e) => {
    const x = e.clientX / window.innerWidth - 0.5;
    const y = e.clientY / window.innerHeight - 0.5;

    orbs.forEach((orb, i) => {
      const depth = (i + 1) * 14;
      orb.style.translate = `${x * depth}px ${y * depth}px`;
    });
  });
})();
