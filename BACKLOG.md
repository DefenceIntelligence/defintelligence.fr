# Backlog — defintelligence.fr

> Créé le 2026-04-29. Prioriser ensemble à chaque session.

---

## 🔴 Priorité 1 — Indispensable avant de partager le site

- [ ] **Logo PNG fond transparent** — version navbar propre (pas de carré sombre)
- [ ] **Favicon** — dériver du logo SD pour l'onglet navigateur
- [ ] **SIRET** — à ajouter dans mentions légales dès immatriculation
- [ ] **Notifications email contact** — Netlify → Forms → Form notifications
- [ ] **Page de confirmation contact** — après soumission formulaire, rediriger vers `/merci/`
- [ ] **CGV** — Conditions Générales de Vente (obligatoire pour facturer)

---

## 🟠 Priorité 2 — Qualité & crédibilité

- [ ] **Page À propos** — photo, bio, parcours, certifications (OSCP, CEH, etc.)
- [ ] **Vrais articles de blog** — 3 à 5 articles pour crédibiliser le site au lancement
  - Idées : NIS2 en pratique, phishing en 2026, checklist PME cybersécurité, Zero Trust pour les nuls
- [ ] **Couleurs cohérentes avec le logo** — le vert néon `#00ff80` du logo SD dans les accents du site (remplacer l'orange actuel)
- [ ] **Tarifs indicatifs** — même "à partir de X€" rassure le prospect et filtre les curieux
- [ ] **Témoignages clients** — 2-3 verbatims (anonymisés si besoin) avec titre/secteur
- [ ] **Renommer site Netlify** — `hilarious-churros` → `defintelligence`
- [ ] **Google Search Console** — soumettre sitemap `/sitemap.xml` pour indexation

---

## 🟡 Priorité 3 — Conversion & acquisition

- [ ] **Bouton "Devis rapide"** — form pré-rempli selon le service (lien depuis chaque page service)
- [ ] **Intégration Calendly** — "Réserver un appel découverte 30 min gratuit" sur la homepage et contact
- [ ] **Open Graph / partage réseaux sociaux** — image de prévisualisation quand le lien est partagé sur LinkedIn
- [ ] **Analytics** — Umami (self-hosted, RGPD-friendly) ou Plausible pour mesurer le trafic
- [ ] **LinkedIn auto-post** — notifier LinkedIn à chaque nouvel article (Zapier ou n8n)
- [ ] **Newsletter** — abonnement blog via Brevo (anciennement Sendinblue, gratuit jusqu'à 300 emails/j)

---

## 🟢 Priorité 4 — Contenu & SEO long terme

- [ ] **Études de cas** — missions réalisées, résultats concrets (anonymisées)
- [ ] **FAQ** — 10 questions fréquentes des PME sur la cybersécurité
- [ ] **Glossaire** — lexique cyber accessible (pentest, ransomware, zero-day...)
- [ ] **Ressources téléchargeables** — checklist sécurité PME PDF (lead magnet)
- [ ] **Partenaires** — logos partenaires/revendeurs si applicable
- [ ] **Page presse** — bio courte + photo HD pour journalistes/podcasts

---

## ⚙️ Technique

- [ ] **Images WebP** — convertir logo.jpg en WebP pour perf
- [ ] **Page 404 custom** — `layouts/404.html` avec lien retour accueil
- [ ] **Background hero** — pattern circuit board SVG subtil pour renforcer l'identité cyber
- [ ] **Animations** — fade-in des cards au scroll (AOS.js léger)
- [ ] **Dark/light toggle** — visible dans la navbar (déjà dans Hinode, à vérifier)
- [ ] **Schema.org** — LocalBusiness markup pour le SEO local

---

## 💡 Idées à explorer

- **ARGOS landing page** — page dédiée plus détaillée avec démo visuelle (screenshots, vidéo)
- **Simulateur de risque** — questionnaire interactif "Évaluez votre niveau de risque" → génère un score et propose un service adapté
- **Badge "Vérifié auto-entrepreneur"** — lien Annuaire Entreprises INSEE une fois immatriculé
- **Webinaires** — mini-conférences en ligne sur des sujets cyber, enregistrées et publiées en blog
