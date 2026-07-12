# Quillix ✒️

A fully animated landing page for **Quillix**, a fictional writing platform — built with pure HTML, CSS and vanilla JavaScript. No frameworks, no build step: open `index.html` and it just works.

## ✨ Animations & effects

- **Preloader** — bouncing gradient letters with a sliding progress bar
- **Custom cursor** — a dot with a smoothly trailing ring that reacts to hover targets
- **Particle canvas** — floating, interconnected particles in the hero
- **Typewriter headline** — cycles through phrases with a blinking caret
- **Gradient orbs** — blurred blobs that drift on their own and follow the mouse (parallax)
- **Scroll progress bar** — gradient bar tied to page scroll
- **Scroll-reveal** — staggered fade-and-rise on every section (IntersectionObserver)
- **Infinite marquee** — tilted, spinning-star ticker that pauses on hover
- **3D tilt cards** — feature & pricing cards tilt in perspective with a cursor-tracked glow
- **Animated counters** — stats ease up from zero when scrolled into view
- **Scroll-filled timeline** — a gradient line that fills as you read the workflow
- **Auto-playing carousel** — testimonials with dots and touch-swipe support
- **Magnetic buttons** — CTAs that gently pull toward the cursor
- **Twinkling stars, floating editor card, animated footer wave** and more

Respects `prefers-reduced-motion` — all animation is disabled for users who opt out.

## 🚀 Run it

```bash
# any static server works, e.g.
python3 -m http.server 8000
# then open http://localhost:8000
```

Or just double-click `index.html`.

## 📁 Structure

```
index.html   # markup for all sections
styles.css   # design system + keyframe/transition animations
script.js    # cursor, particles, reveals, counters, tilt, carousel…
```
