# CLAUDE.md — Defence Intelligence · defintelligence.fr

## Contraintes de contenu

### Règles permanentes — aucune exception

**R1 — Lire avant d'écrire**
Avant d'écrire la moindre affirmation factuelle dans un template, une maquette ou un fichier de contenu, lire `data/facts.yml` et `content/a-propos.md`. Si l'information n'y figure pas, elle n'existe pas.

**R2 — Aucun fait inventé**
Ne jamais inventer de fait concernant Stéphane Desmets ou l'activité : dates, durées, chiffres, certifications, localisations, clients, références, métriques produit, forme juridique. Un fait plausible inventé est plus dangereux qu'un placeholder visible.

**R3 — Placeholder plutôt que valeur inventée**
Quand un gabarit ou une maquette appelle une information absente de `data/facts.yml`, écrire `[[À VÉRIFIER : description de l'info manquante]]` et le signaler explicitement dans la réponse. Ne jamais combler le vide avec une valeur vraisemblable.

**R4 — Aucune donnée fictive présentée comme réelle**
Les données illustratives (métriques ARGOS, exemples de findings, volumes CTI) doivent être explicitement étiquetées "exemple fictif", "données illustratives" ou équivalent. Ne jamais présenter des chiffres fictifs comme temps réel ou connectés, même à titre décoratif, même sur une maquette. Sur un site de cybersécurité, une telle confusion est disqualifiante.

---

## Source de vérité — données biographiques

`data/facts.yml` est la source canonique. Toute donnée factuelle en passe par là.
`content/a-propos.md` tire ses données de `data/facts.yml` via des shortcodes (`{{< facts-experience >}}`, `{{< facts-certifications >}}`, `{{< facts-frameworks >}}`). Ne pas remettre de données en dur dans le markdown.

Données vérifiées (ne pas contredire) :
- Année de fondation Defence Intelligence : 2026
- Forme juridique : auto-entrepreneur, SIRET actif

Données absentes de la source (ne pas inventer) :
- Localisation (ville, région)
- Forme juridique exacte (auto-entrepreneur, SIRET en cours d'immatriculation — déclaré hors documentation)
- Revenus, tarifs, nombre de clients
- Chiffres ARGOS en production réelle

---

## Vocabulaire

- **Non** : "cabinet", "cabinet de conseil", "produit maison", "outil maison"
- **Oui** : "activité de conseil indépendant", "consultant indépendant", "Defence Intelligence", "ARGOS" (nom propre)

---

## Branche de travail

- `design/preview` : maquette en cours, ne pas merger sur `main`
- Ne pas toucher à la typographie ni à la palette tant que le site ne builde pas en Hinode v3.20.0

---

## Inventaire de dette technique (#00c97a hardcodé)

Occurrences de `#00c97a` hors `brand.css` et `params.toml` à remplacer par `var(--bs-primary)` lors du passage au nouveau token d'accent. Par fichier (compté au 2026-08-10) :

| Fichier | Occurrences |
|---|---|
| `content/a-propos.md` | 9 → **0** (migré vers `var(--bs-primary)` et shortcodes) |
| `content/produits/_index.md` | 3 |
| `content/services/_index.md` | 10 |
| `content/7secondes/_index.md` | 1 |
| `content/contact/_index.md` | 1 |
| `content/merci.md` | 1 |
| `layouts/index.html` | 10 |
| `layouts/blog/list.html` | 2 |
| `layouts/cti/list.html` | 1 |
| `layouts/partials/footer/footer.html` | 1 |
| `static/css/brand.css` | 22 (intentionnel — source) |

Total hors brand.css : **30 occurrences** à migrer lors du changement d'accent.
