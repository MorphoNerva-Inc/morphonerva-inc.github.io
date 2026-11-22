// Theme management and mobile nav
(function() {
  const root = document.documentElement;
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const themeText = document.getElementById('theme-text');
  const mobileToggle = document.getElementById('mobile-toggle');
  const mainNav = document.getElementById('main-nav');

  function getPreferredTheme() {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setTheme(theme) {
    root.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (themeIcon && themeText) {
      if (theme === 'dark') {
        themeIcon.innerHTML = '&#9728;'; // Sun symbol
        themeText.textContent = 'Light';
      } else {
        themeIcon.innerHTML = '&#9790;'; // Moon symbol
        themeText.textContent = 'Dark';
      }
    }
  }

  // Initial theme setup
  const currentTheme = getPreferredTheme();
  setTheme(currentTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const active = root.getAttribute('data-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      setTheme(active === 'dark' ? 'light' : 'dark');
    });
  }

  // Mobile menu toggle
  if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mainNav.classList.contains('open');
      if (isOpen) {
        mainNav.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      } else {
        mainNav.classList.add('open');
        mobileToggle.setAttribute('aria-expanded', 'true');
      }
    });
  }

  // Listen to system theme changes if user hasn't explicitly set preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      setTheme(e.matches ? 'dark' : 'light');
    }
  });
})();
