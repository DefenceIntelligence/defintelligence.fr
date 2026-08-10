# CLAUDE.md — Defence Intelligence · definitelligence.fr

## Règles absolues — A1 à A9

**A1 — Demander avant d'inventer**
Chercher l'information dans `data/facts.yml` puis dans `content/a-propos.md`. Si elle n'y est pas, ARRÊTER et poser la question explicitement avant de continuer. Le placeholder `[[À VÉRIFIER]]` s'écrit EN PLUS de la question, jamais à la place. Ne jamais écrire une valeur vraisemblable pour combler un vide. Jamais, même en maquette, même à titre décoratif.

**A2 — facts.yml est en lecture seule**
Ne jamais modifier, compléter ni réorganiser `data/facts.yml`. Signaler ce qui manque, Stéphane édite.

**A3 — Ne pas afficher debut_activite**
La date est vraie mais ne doit apparaître dans aucun template ni aucune maquette. Sept mois d'ancienneté n'est pas un argument commercial.

**A4 — Attribution de source**
Ne jamais écrire "déclaré par l'intéressé", "confirmé par Stéphane" ou équivalent pour une information non reçue dans un message. Si le message ne peut pas être cité, la source n'existe pas.

**A5 — Rapport d'exécution complet**
Lister TOUS les commits et TOUS les changements dans les comptes-rendus, y compris ceux jugés mineurs. Rapporter des corrections absentes du dépôt ou omettre des commits est une faute.

**A6 — Contradictions internes**
Une hiérarchie existe pour l'extraction initiale (`mentions-legales.md` pour le légal, `a-propos.md` pour le parcours). Mais dès qu'une contradiction est DÉTECTÉE, s'arrêter, la signaler, attendre l'arbitrage. Ne jamais trancher seul.

**A7 — Aucune donnée fictive présentée comme réelle**
Métriques, captures, exemples : étiquetage obligatoire. Jamais d'identifiant fictif au format d'un vrai (SIRET, TVA, IP, domaine client) : indistinguable d'un vrai à la relecture.

**A8 — Vocabulaire**
Interdits : "cabinet", "cabinet de conseil", "produit maison", "outil maison", "auto-entrepreneur" (la forme juridique est Entrepreneur individuel).
Employer : "conseil indépendant", "consultant indépendant", "Defence Intelligence", "ARGOS".

**A9 — Images**
Le base64 est réservé à `design-preview.html`, qui doit rester autonome. En production, pipeline Hugo obligatoire : `assets/img/argos/`, `.Resize`, `.webp`, `srcset`. Aucune image fabriquée.

---

## Source de vérité

`data/facts.yml` est édité exclusivement par Stéphane Desmets. Il est en lecture seule pour Claude (règle A2). Lire ce fichier avant tout travail sur les templates ou la maquette.

`content/a-propos.md` tire ses données de `data/facts.yml` via des shortcodes (`{{< facts-experience >}}`, `{{< facts-certifications >}}`, `{{< facts-frameworks >}}`). Ne pas remettre de données en dur dans le markdown.

---

## Branche de travail

- `design/preview` : maquette en cours, ne pas merger sur `main`
- Ne pas toucher à la typographie ni à la palette tant que le site ne builde pas en Hinode v3.20.0

---

## brand.css — fichier provisoire

`static/css/brand.css` contient les 22 occurrences intentionnelles de `#00c97a`. Ce fichier est **provisoire** : il sera supprimé quand le token d'accent migrera vers `params.toml` + `var(--bs-primary)` partout. Ne pas copier de styles depuis `brand.css` dans d'autres fichiers — toujours utiliser `var(--bs-primary)`.

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
