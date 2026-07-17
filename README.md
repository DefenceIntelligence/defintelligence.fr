# Defence Intelligence — Site vitrine

Site statique Hugo pour **Defence Intelligence**, conseil indépendant en cybersécurité :
**audit de sécurité**, **Attack Surface Management (ASM)** et **Cyber Threat Intelligence (CTI)**
(+ RSSI externalisé, gestion des risques, formation).

**URL** : [defintelligence.fr](https://defintelligence.fr)
**Thème** : [Hinode](https://gethinode.com) v1.23.7 (Bootstrap 5, dark mode)
**Hébergement** : GitHub Pages (déploiement via GitHub Actions)
**Domaine** : Gandi (LiveDNS)

---

## Stack

| Outil | Usage |
|-------|-------|
| [Hugo](https://gohugo.io) v0.161 extended | Générateur de site statique |
| [Hinode](https://gethinode.com) v1.23.7 | Thème Bootstrap 5 dark (module Hugo via `go.mod`) |
| [GitHub Pages](https://pages.github.com) + Actions | Hébergement + CI/CD (gratuit, repo public) |
| [Gandi](https://gandi.net) | Registrar + DNS (LiveDNS) |
| [Formspree](https://formspree.io) | Backend du formulaire de contact |

---

## Prérequis (dev local)

- Hugo extended ≥ 0.161 (`brew install hugo`)
- Go ≥ 1.19 (pour les modules Hugo)
- Node.js ≥ 18 + npm

## Démarrage local

```bash
git clone https://github.com/DefenceIntelligence/defintelligence.fr
cd defintelligence.fr
npm install
hugo server -D
```

Ouvrir [http://localhost:1313](http://localhost:1313)

---

## Structure du projet

```
defintelligence.fr/
├── .github/workflows/
│   ├── deploy.yml          # Build Hugo (modules+npm) → GitHub Pages
│   └── sync-cti.yml        # Récupère le digest CTI quotidien → content/cti/
├── config/_default/
│   ├── hugo.toml           # Config principale (baseURL, modules, outputs)
│   ├── params.toml         # Thème Hinode + schema.org (separator = "·")
│   ├── menus.toml          # Navigation
│   └── languages.toml      # Langue FR + description SEO
├── content/
│   ├── _index.md           # Texte hero homepage
│   ├── services/           # Pages services (audit/ASM, RSSI, risques, formation)
│   ├── produits/argos.md   # ARGOS (Attack Surface Management)
│   ├── cti/                # Digests CTI quotidiens (générés par sync-cti.yml)
│   ├── blog/               # Articles
│   └── contact/            # Formulaire (Formspree)
├── layouts/
│   ├── index.html          # Homepage custom (hero + cards + blog + CTA)
│   ├── cti/list.html       # Liste des digests CTI
│   ├── sitemap.xml         # Override sitemap (toutes les pages)
│   └── _markup/render-codeblock-math.html  # Compat Hinode/Hugo
├── static/
│   ├── CNAME               # defintelligence.fr (domaine custom Pages)
│   └── google*.html        # Vérification Google Search Console
└── package.json            # Dépendances npm (@gethinode/hinode)
```

---

## Déploiement

Tout push sur `main` → **build + deploy automatique via GitHub Actions** (`deploy.yml`).

```bash
git add -A && git commit -m "description" && git push
```

Le workflow installe Hugo 0.161 extended, récupère les modules (Go) + dépendances npm,
build (`hugo --minify --gc`) et publie sur GitHub Pages. Certificat HTTPS auto (Let's Encrypt).

> ⚠️ **CTI quotidienne** : `sync-cti.yml` (cron 08:00 UTC) commit le digest du jour avec le
> compte `github-actions[bot]`. Comme un push du bot ne redéclenche pas de workflow, `deploy.yml`
> a un **cron 08:20 UTC** qui republie le site pour mettre la CTI en ligne.

---

## DNS (Gandi LiveDNS)

| Nom | Type | Valeur |
|-----|------|--------|
| `@` | A | `185.199.108.153` / `.109` / `.110` / `.111` (GitHub Pages) |
| `www` | CNAME | `defenceintelligence.github.io.` |
| `@` | TXT | `v=spf1 -all` (anti-spoofing — aucun envoi depuis le domaine) |
| `_dmarc` | TXT | `v=DMARC1; p=reject; rua=mailto:defintelligence@proton.me` |

Pas de MX (l'email de contact est une adresse Proton ; le formulaire passe par Formspree).

---

## SEO

- `<title>`/meta/canonical, Open Graph, JSON-LD (Organization), sitemap complet, robots.
- **Google Search Console + Bing Webmaster Tools** validés (fichier `static/google*.html`), sitemap soumis.
- Toute la CTI quotidienne est indexable (une page par digest).

---

## Fine-tuning restant

- [ ] Textes services à affiner (tarifs, délais)
- [ ] Page ARGOS à étoffer (captures, pricing)
- [ ] Premiers vrais articles de blog
- [ ] SIRET + CGV dès immatriculation
- [ ] (Optionnel) `<title>` de la home enrichi (Hinode utilise le titre du site pour la home)
- [ ] (Optionnel) renommer l'URL `/services/audit-pentest/` → `audit-asm` avec redirection

---

## Notes techniques

**Modules Hugo** : Hinode est un module (`go.mod`), pas un thème vendu. Go doit être installé
pour que `hugo` récupère le module au build (géré par le workflow).

**Sitemap** : `hugo.toml` ne doit **pas** inclure `SITEMAP` dans `[outputs] home`
(sinon le sitemap est limité aux pages de niveau 1). Le sitemap natif Hugo couvre tout.

**Historique** : migré de **Netlify** vers **GitHub Pages** le 2026-07-17 (crédits Netlify
épuisés par les builds CTI quotidiens). `netlify.toml`/`vercel.json` conservés à titre indicatif.
