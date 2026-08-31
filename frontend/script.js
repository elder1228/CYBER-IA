// Aguarda o DOM carregar completamente
document.addEventListener('DOMContentLoaded', () => {
  const themeSwitch = document.getElementById('theme-switch');

  if (themeSwitch) {
    themeSwitch.addEventListener('click', () => {
      document.body.classList.toggle('theme-light');
      const isLight = document.body.classList.contains('theme-light');
      themeSwitch.setAttribute('aria-checked', isLight);
    });

    // Permite trocar o tema usando a tecla Enter ou Espaço no controle
    themeSwitch.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        themeSwitch.click();
      }
    });
  }
});
