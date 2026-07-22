/* Override defintelligence.fr : site toujours en mode sombre, sans bouton de bascule. */
(() => {
  'use strict';
  document.documentElement.setAttribute('data-bs-theme', 'dark');
  document.documentElement.setAttribute('data-bs-main-theme', 'dark');
  // Masquer le sélecteur clair/sombre (injecté dans le <head>, avant le rendu du body : pas de flash)
  var s = document.createElement('style');
  s.textContent = '#navbar-mode{display:none!important}';
  document.head.appendChild(s);
})();
