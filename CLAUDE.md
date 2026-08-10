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

**A11 — facts.yml ne contient que des faits**
Aucune décision de présentation (couleur, ordre, mise en avant, badge) n'est encodée dans `data/facts.yml`. La présentation vit dans les templates.

---

## Source de vérité

`data/facts.yml` est édité exclusivement par Stéphane Desmets. Il est en lecture seule pour Claude (règle A2). Lire ce fichier avant tout travail sur les templates ou la maquette.

`content/a-propos.md` tire ses données de `data/facts.yml` via des shortcodes (`{{< facts-experience >}}`, `{{< facts-certifications >}}`, `{{< facts-frameworks >}}`). Ne pas remettre de données en dur dans le markdown.

---

## Branche de travail

- `design/preview` : maquette en cours, ne pas merger sur `main`
- Ne pas toucher à la typographie ni à la palette tant que le site ne builde pas en Hinode v3.20.0

---

## Accent couleur

Défini dans `config/_default/params.toml` → `[style] primary`. Valeur active : `#b89450` (or/ambre, Étape 2).
Tous les templates utilisent `var(--bs-primary)` — ne jamais hardcoder la valeur hex dans les layouts ou le contenu.

`static/css/brand.css` a été supprimé en Étape 1 (commit ce51ddb).

---

## Lancer le serveur local

Homebrew Hugo n'embarque pas Dart Sass — il faut pointer vers le binaire npm :

```bash
cd /Users/stephane/defintelligence
PATH="node_modules/sass-embedded-darwin-arm64/dart-sass:$PATH" /opt/homebrew/bin/hugo server --port 1313 --bind 127.0.0.1
```

Accès : `http://127.0.0.1:1313/`
