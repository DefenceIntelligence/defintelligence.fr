---
title: "7 Secondes — Jeu de sensibilisation à la cybersécurité | Defence Intelligence"
description: "Un jeu de sensibilisation cyber. Testez vos réflexes face aux pièges qui visent les entreprises et leurs dirigeants. Gratuit, sans compte, sans publicité."
showToc: false
---

<style>
:root {
  --s7-bg: #080c14;
  --s7-surface: #0d141f;
  --s7-border: #16202e;
  --s7-cyan: #00c8ff;
  --s7-gold: #e8c97a;
  --s7-text: #e6f0f8;
  --s7-text2: #9fb3c8;
  --s7-mono: "SF Mono","Fira Mono","Cascadia Code","Consolas","Courier New",monospace;
}

.s7 { background: var(--s7-bg); color: var(--s7-text); font-family: system-ui,-apple-system,sans-serif; margin: -1rem -1.25rem 0; }
.s7 * { box-sizing: border-box; }
.s7 a { color: var(--s7-cyan); text-decoration: none; }
.s7 a:hover { text-decoration: underline; }

.s7-wrap { max-width: 960px; margin: 0 auto; padding: 0 1.25rem; }

.s7-label {
  font-family: var(--s7-mono);
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--s7-cyan);
  margin: 0 0 .75rem;
}

/* HERO */
.s7-hero { padding: 5rem 0 4rem; text-align: center; }
.s7-hero h1 {
  font-family: var(--s7-mono);
  font-size: clamp(2.8rem, 9vw, 5rem);
  letter-spacing: .04em;
  color: var(--s7-text);
  margin: 0 0 .4rem;
  line-height: 1.05;
}
.s7-hero h1 span { color: var(--s7-cyan); }
.s7-slogan {
  font-family: var(--s7-mono);
  font-size: clamp(.8rem, 2.5vw, 1rem);
  color: var(--s7-gold);
  letter-spacing: .06em;
  margin: 0 0 1.75rem;
}
.s7-hero-lead {
  font-size: 1.05rem;
  color: var(--s7-text2);
  max-width: 560px;
  margin: 0 auto 2rem;
  line-height: 1.65;
}
.s7-appstore-btn {
  display: inline-flex;
  align-items: center;
  gap: .65rem;
  background: var(--s7-text);
  color: #050a10;
  padding: .8rem 1.6rem;
  border-radius: .75rem;
  font-family: var(--s7-mono);
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .04em;
  text-decoration: none;
  transition: opacity .15s;
}
.s7-appstore-btn:hover { opacity: .88; text-decoration: none; color: #050a10; }
.s7-badge-free {
  margin-top: .9rem;
  font-family: var(--s7-mono);
  font-size: .7rem;
  color: var(--s7-text2);
  letter-spacing: .08em;
}
.s7-screenshot-hero {
  margin: 3rem auto 0;
  max-width: 280px;
  border-radius: 2rem;
  overflow: hidden;
  border: 1px solid var(--s7-border);
  display: block;
}
.s7-screenshot-hero img { width: 100%; display: block; }

/* SECTIONS */
.s7-section { padding: 4rem 0; border-top: 1px solid var(--s7-border); }
.s7-section:first-of-type { border-top: none; }

.s7-constat-text {
  font-size: 1.1rem;
  line-height: 1.75;
  color: var(--s7-text);
  max-width: 680px;
  margin: 0;
}

.s7-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}
.s7-card {
  background: var(--s7-surface);
  border: 1px solid var(--s7-border);
  border-radius: .75rem;
  padding: 1.5rem;
}
.s7-card-name {
  font-family: var(--s7-mono);
  font-size: .75rem;
  letter-spacing: .1em;
  color: var(--s7-cyan);
  text-transform: uppercase;
  margin: 0 0 .6rem;
}
.s7-card-desc { font-size: .9rem; line-height: 1.6; color: var(--s7-text2); margin: 0 0 1rem; }
.s7-screenshot-sm {
  border-radius: .75rem;
  overflow: hidden;
  border: 1px solid var(--s7-border);
  margin-top: auto;
  display: block;
}
.s7-screenshot-sm img { width: 100%; display: block; }

.s7-quote {
  border-left: 2px solid var(--s7-cyan);
  padding: .9rem 1.25rem;
  background: var(--s7-surface);
  border-radius: 0 .5rem .5rem 0;
  margin: 1.5rem 0 0;
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--s7-text);
  font-style: italic;
}

.s7-limite-box {
  border: 1px solid var(--s7-border);
  border-radius: .6rem;
  padding: 1.1rem 1.4rem;
  margin-top: 1.5rem;
  font-size: .9rem;
  color: var(--s7-text2);
  line-height: 1.6;
}
.s7-limite-box strong { color: var(--s7-gold); font-family: var(--s7-mono); font-size: .75rem; letter-spacing: .06em; text-transform: uppercase; }

.s7-cabinet-text { font-size: 1rem; line-height: 1.65; color: var(--s7-text2); margin: .75rem 0 0; }

/* FOOTER 7S */
.s7-foot { padding: 2.25rem 0; border-top: 1px solid var(--s7-border); }
.s7-foot-links { display: flex; flex-wrap: wrap; gap: .4rem 1.25rem; margin-bottom: .75rem; }
.s7-foot-links a { color: var(--s7-text2); font-family: var(--s7-mono); font-size: .68rem; letter-spacing: .04em; }
.s7-foot-links a:hover { color: var(--s7-cyan); text-decoration: none; }
.s7-foot-notice { font-family: var(--s7-mono); font-size: .65rem; letter-spacing: .02em; color: #3a5060; line-height: 1.5; max-width: 680px; }

@media (max-width: 600px) {
  .s7-hero { padding: 3.5rem 0 2.5rem; }
  .s7-section { padding: 2.75rem 0; }
  .s7-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 400px) {
  .s7-grid { grid-template-columns: 1fr; }
}
</style>

<div class="s7">

<!-- HERO -->
<section class="s7-hero">
  <div class="s7-wrap">
    <p class="s7-label">Defence Intelligence · Application iOS</p>
    <h1>7 <span>SECONDES</span></h1>
    <p class="s7-slogan">La faille, c'est vous. Le rempart aussi.</p>
    <p class="s7-hero-lead">Un jeu de sensibilisation cyber. Testez vos réflexes face aux pièges qui visent les entreprises et leurs dirigeants.</p>

    <a href="#appstore" class="s7-appstore-btn" aria-label="Télécharger 7 Secondes sur l'App Store">
      <svg width="20" height="20" viewBox="0 0 22 22" fill="none" aria-hidden="true" focusable="false">
        <path d="M16.5 11.55c-.02-2.27 1.85-3.36 1.93-3.41-1.05-1.54-2.69-1.75-3.28-1.77-1.39-.14-2.73.82-3.43.82-.7 0-1.78-.8-2.93-.78-1.5.02-2.89.88-3.66 2.22-1.57 2.73-.4 6.75 1.12 8.96.74 1.08 1.62 2.29 2.78 2.25 1.12-.05 1.54-.72 2.9-.72 1.36 0 1.74.72 2.93.7 1.2-.02 1.96-1.1 2.69-2.18.85-1.24 1.2-2.45 1.22-2.51-.03-.01-2.34-.9-2.37-3.58z" fill="currentColor"/>
        <path d="M14.27 5.27c.62-.75 1.03-1.79.92-2.83-.89.04-1.97.59-2.6 1.33-.57.66-1.07 1.72-.93 2.73.99.08 2-.5 2.61-1.23z" fill="currentColor"/>
      </svg>
      Télécharger sur l'App Store
    </a>
    <p class="s7-badge-free">Gratuit · Sans compte · Sans publicité</p>

    <div class="s7-screenshot-hero">
      <img src="/img/7secondes/home.png" alt="Écran d'accueil de 7 Secondes — les quatre modes de jeu" loading="lazy">
    </div>
  </div>
</section>

<!-- LE CONSTAT -->
<section class="s7-section">
  <div class="s7-wrap">
    <p class="s7-label">Le constat</p>
    <p class="s7-constat-text">La plupart des cyberattaques ne visent pas les machines : elles visent les gens. Un mail piégé, un faux SMS, un appel frauduleux, et un clic suffit. 7 Secondes apprend à reconnaître ces pièges, non pas en récitant des règles, mais en mettant en situation.</p>
  </div>
</section>

<!-- QUATRE MODES -->
<section class="s7-section">
  <div class="s7-wrap">
    <p class="s7-label">Quatre modes de jeu</p>
    <div class="s7-grid">

      <div class="s7-card">
        <p class="s7-card-name">Réflexe</p>
        <p class="s7-card-desc">Face à un piège du quotidien, sept secondes pour décider. On apprend à repérer ce qui cloche avant de cliquer.</p>
        <div class="s7-screenshot-sm">
          <img src="/img/7secondes/reflexe.png" alt="Mode Réflexe — un mail piégé avec pièce jointe inattendue" loading="lazy">
        </div>
      </div>

      <div class="s7-card">
        <p class="s7-card-name">Crise</p>
        <p class="s7-card-desc">Dans la peau d'un dirigeant, on traverse une crise cyber décision après décision : rançongiciel, fraude au virement, fuite de données. Aucune réponse parfaite, rien que des arbitrages.</p>
        <div class="s7-screenshot-sm">
          <img src="/img/7secondes/crise.png" alt="Mode Crise — scénario ransomware, le DSI alerte" loading="lazy">
        </div>
      </div>

      <div class="s7-card">
        <p class="s7-card-name">Quiz</p>
        <p class="s7-card-desc">Des questions pour tester, et corriger, ses idées reçues sur la sécurité.</p>
        <div class="s7-screenshot-sm">
          <img src="/img/7secondes/quiz.png" alt="Mode Quiz — question à choix multiples sur les bons réflexes" loading="lazy">
        </div>
      </div>

      <div class="s7-card">
        <p class="s7-card-name">Le saviez-vous</p>
        <p class="s7-card-desc">Des fiches courtes sur les menaces du moment et les bons réflexes, mises à jour régulièrement.</p>
        <div class="s7-screenshot-sm">
          <img src="/img/7secondes/about.png" alt="Écran de présentation de 7 Secondes et ses quatre modes" loading="lazy">
        </div>
      </div>

    </div>
  </div>
</section>

<!-- POURQUOI C'EST DIFFÉRENT -->
<section class="s7-section">
  <div class="s7-wrap">
    <p class="s7-label">Pourquoi c'est différent</p>
    <p class="s7-quote">7 Secondes ne cherche pas à faire peur. Il apprend à douter au bon moment, à vérifier, à réfléchir avant d'agir. Se faire piéger ici, c'est ne pas se faire piéger ailleurs.</p>
  </div>
</section>

<!-- QUI EST DERRIÈRE -->
<section class="s7-section">
  <div class="s7-wrap">
    <p class="s7-label">Une création Defence Intelligence</p>
    <p class="s7-cabinet-text">Cabinet de conseil en cybersécurité, nous accompagnons les PME et ETI sur la menace cyber au quotidien : audit, Attack Surface Management, Threat Intelligence, gestion des risques.<br>
    <a href="/">En savoir plus sur Defence Intelligence →</a></p>
  </div>
</section>

<!-- LA LIMITE -->
<section class="s7-section">
  <div class="s7-wrap">
    <div class="s7-limite-box">
      <strong>Une application de sensibilisation</strong><br>
      7 Secondes ne remplace ni une formation, ni un audit, ni un accompagnement en cybersécurité.
    </div>
  </div>
</section>

<!-- FOOTER 7S -->
<footer class="s7-foot">
  <div class="s7-wrap">
    <div class="s7-foot-links">
      <a href="/7secondes/confidentialite/">Politique de confidentialité</a>
      <a href="/7secondes/cgu/">Conditions d'utilisation</a>
      <a href="/7secondes/mentions-legales/">Mentions légales</a>
    </div>
    <p class="s7-foot-notice">Tous les noms d'entreprises, de personnes et les scénarios présentés dans l'application sont fictifs, à des fins pédagogiques uniquement.</p>
  </div>
</footer>

</div>
