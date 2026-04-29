# Def Intelligence — Site vitrine

Site statique Hugo pour **Def Intelligence**, conseil indépendant en cybersécurité.

**URL** : [defintelligence.fr](https://defintelligence.fr)  
**Thème** : [Hinode](https://gethinode.com) v1.23.7 (Bootstrap 5, dark mode)  
**Hébergement** : Netlify — `hilarious-churros-ed28e0.netlify.app`  
**Domaine** : Gandi → Netlify DNS

---

## Stack

| Outil | Usage |
|-------|-------|
| [Hugo](https://gohugo.io) v0.161+ extended | Générateur de site statique |
| [Hinode](https://gethinode.com) v1.23.7 | Thème Bootstrap 5 dark |
| [Netlify](https://netlify.com) | Hébergement + CI/CD + formulaire contact |
| [Gandi](https://gandi.net) | Registrar — nameservers délégués à Netlify DNS |

---

## Prérequis

- Hugo extended ≥ 0.161 (`brew install hugo`)
- Go ≥ 1.19 (pour les modules Hugo)
- Node.js ≥ 18 + npm

---

## Démarrage local

```bash
git clone https://github.com/DefenceIntelligence/defintelligence.fr
cd defintelligence.fr
npm install
hugo mod download
hugo server -D
```

Ouvrir [http://localhost:1313](http://localhost:1313)

---

## Structure du projet

```
defintelligence.fr/
├── config/_default/
│   ├── hugo.toml           # Config principale (baseURL, modules)
│   ├── params.toml         # Thème Hinode (dark mode, nav, footer)
│   ├── menus.toml          # Navigation (Services, Produits, Blog, Contact)
│   └── languages.toml      # Langue FR + description SEO
├── content/
│   ├── _index.md           # Texte hero homepage
│   ├── services/           # 4 pages services
│   ├── produits/           # ARGOS
│   ├── blog/               # Articles
│   └── contact/            # Formulaire Netlify Forms
├── layouts/
│   ├── index.html          # Homepage custom (hero + cards + blog + CTA)
│   └── _markup/
│       └── render-codeblock-math.html  # Override compat Hugo <0.161
├── static/                 # Images, favicon (à compléter)
├── netlify.toml            # Build + headers sécurité + redirects
└── package.json            # Dépendances npm (@gethinode/hinode)
```

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Hero, 4 cards services, section ARGOS, blog récent, CTA |
| `/services/` | Liste des prestations |
| `/services/audit-pentest/` | Audit & Pentest |
| `/services/gestion-risques/` | Gestion des risques |
| `/services/formation/` | Formation & Sensibilisation |
| `/services/rssi-externalise/` | RSSI Externalisé |
| `/produits/argos/` | ARGOS — Attack Surface Monitor |
| `/blog/` | Articles |
| `/contact/` | Formulaire (Netlify Forms) |

---

## Déploiement

Tout push sur `main` → deploy automatique Netlify.

```bash
git add -A && git commit -m "description" && git push
```

Build Netlify : `npm ci && curl ... hugo 0.161.0 && ./hugo --minify`  
> Netlify est bloqué à Hugo 0.140.2 par défaut. Le build télécharge Hugo 0.161.0 directement depuis GitHub releases. À supprimer quand Netlify aura 0.161.0+ dans son CDN.

---

## Formulaire de contact

Netlify Forms — zéro backend. Soumissions visibles dans *Netlify → Forms*.  
Activer les notifications : *Site configuration → Forms → Form notifications → Add notification*.

---

## Fine-tuning à faire

- [ ] Logo `static/img/logo.png` + favicon `static/img/favicon.png`
- [ ] Photo/avatar auteur `static/img/author.jpg`
- [ ] Textes services à personnaliser (tarifs, délais, certifications)
- [ ] Page ARGOS à étoffer (captures d'écran, pricing)
- [ ] Premiers vrais articles de blog
- [ ] Notifications email formulaire de contact (Netlify → Forms)
- [ ] Google Search Console — soumettre le sitemap (`/sitemap.xml`)
- [ ] Renommer le site Netlify : `hilarious-churros` → `defintelligence`
- [ ] Analytics (Netlify Analytics ou Umami self-hosted)
- [ ] Mentions légales + CGU (obligatoire auto-entrepreneur)
- [ ] SIRET à ajouter dès immatriculation

---

## Notes techniques

**Override `render-codeblock-math.html`** : Hinode v1.23.7 utilise la fonction `try` (Hugo 0.161+). Netlify tourne sur Hugo 0.140.2. L'override dans `layouts/_markup/` retire `try` pour compatibilité. Supprimer l'override quand Netlify passe à Hugo 0.161+.

**DNS** : Gandi délègue à Netlify DNS (nameservers `dns[1-4].p06.nsone.net`). Toute modification DNS se fait dans Netlify → Domain management → Netlify DNS.
