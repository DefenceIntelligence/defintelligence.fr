# Def Intelligence — Site vitrine

Site statique Hugo pour **Def Intelligence**, conseil indépendant en cybersécurité.

**URL** : [defintelligence.fr](https://defintelligence.fr)  
**Thème** : [Hinode](https://gethinode.com) v1.23.7 (Bootstrap 5, dark mode)  
**Hébergement** : Netlify  
**Domaine** : Gandi

---

## Stack

| Outil | Usage |
|-------|-------|
| [Hugo](https://gohugo.io) v0.161+ extended | Générateur de site statique |
| [Hinode](https://gethinode.com) | Thème Bootstrap 5 |
| [Netlify](https://netlify.com) | Hébergement + formulaire contact |
| [Gandi](https://gandi.net) | DNS — defintelligence.fr |

---

## Prérequis

- Hugo extended ≥ 0.161 (`brew install hugo`)
- Go ≥ 1.19 (pour les modules Hugo)
- Node.js ≥ 18 + npm

---

## Démarrage local

```bash
# Cloner avec les modules
git clone https://github.com/DefenceIntelligence/defintelligence.fr
cd defintelligence.fr

# Installer les dépendances npm
npm install

# Télécharger le module Hinode
hugo mod download

# Lancer le serveur de dev (drafts inclus)
hugo server -D
```

Ouvrir [http://localhost:1313](http://localhost:1313)

---

## Structure du projet

```
defintelligence.fr/
├── config/_default/        # Configuration Hugo (hugo.toml, params, menus, langues)
├── content/
│   ├── _index.md           # Contenu page d'accueil
│   ├── services/           # Pages services (audit, risques, formation, RSSI)
│   ├── produits/           # Pages produits (ARGOS)
│   ├── blog/               # Articles de blog
│   └── contact/            # Page contact (formulaire Netlify)
├── layouts/
│   └── index.html          # Layout homepage custom (hero + cards + blog + CTA)
├── static/                 # Fichiers statiques (images, favicon)
├── netlify.toml            # Config déploiement + headers sécurité
└── package.json            # Dépendances npm (Hinode)
```

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Accueil — hero, cards services, ARGOS, blog récent, CTA |
| `/services/` | Liste des prestations |
| `/services/audit-pentest/` | Audit & Pentest |
| `/services/gestion-risques/` | Gestion des risques |
| `/services/formation/` | Formation & Sensibilisation |
| `/services/rssi-externalise/` | RSSI Externalisé |
| `/produits/` | Liste des produits |
| `/produits/argos/` | ARGOS — Attack Surface Monitor |
| `/blog/` | Articles |
| `/contact/` | Formulaire de contact (Netlify Forms) |

---

## Ajouter un article de blog

```bash
hugo new content blog/mon-article.md
```

Puis éditer `content/blog/mon-article.md` et passer `draft: false` pour publier.

---

## Déploiement

Tout push sur `main` déclenche un déploiement automatique sur Netlify.

```bash
git add -A && git commit -m "description" && git push
```

---

## Formulaire de contact

Le formulaire utilise **Netlify Forms** (zéro backend). Les soumissions sont visibles dans le dashboard Netlify sous *Forms*. Pour activer les notifications email : *Site settings → Forms → Form notifications*.

---

## Mise en prod (première fois)

1. Connecter le repo GitHub à Netlify
2. Build command : `hugo --minify` — Publish dir : `public`
3. Dans Gandi : ajouter `CNAME @ → <site>.netlify.app`
4. Dans Netlify : *Domain management → Add custom domain → defintelligence.fr*
