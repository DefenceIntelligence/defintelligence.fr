---
title: "ARGOS — Attack Surface Management"
description: "Cartographiez, surveillez et notez votre exposition externe en continu, à partir d'un simple nom de domaine."
build:
  list: never
  render: always
---

## Vous ne pouvez pas protéger ce que vous ne voyez pas

Sous-domaines oubliés, certificats expirés, serveurs de test exposés, identifiants fuités sur GitHub, domaines de filiales rachetées… Votre surface d'attaque externe grandit en permanence — souvent à votre insu.

**ARGOS** est une plateforme de gestion de la surface d'attaque externe (EASM) qui part d'un **simple nom de domaine racine** et reconstitue automatiquement l'intégralité de votre exposition Internet : actifs, vulnérabilités, fuites et menaces. Le tout noté, priorisé et présenté de façon claire — du dashboard direction au détail technique exploitable.

> **Approche majoritairement passive** — aucune exploitation. La découverte combine des sources passives (Certificate Transparency, WHOIS, BGP, Shodan, CommonCrawl, SecurityTrails, VirusTotal) et des techniques DNS actives non intrusives.
>
> **Validé en production** — testé sur une flotte réelle de **6 370 actifs confirmés**.

---

## Ce qu'ARGOS fait pour vous

### 🔍 Découverte automatique des actifs
Un pipeline de **24 modules de scan** enchaînés reconstruit votre périmètre externe :
- Sous-domaines, IPs, plages réseau, applications web, certificats TLS, applications mobiles
- Variantes de TLD (`.fr`, `.de`, `.co.uk`…) et filiales détectées par mot-clé de marque
- Fuites de code et de secrets dans les dépôts GitHub publics
- **Score de confiance** par actif (HIGH / MEDIUM / LOW) selon le nombre de sources indépendantes — pour distinguer le vrai positif du bruit

### 🎯 Moteur de findings de sécurité
**90 détecteurs** répartis en 12 catégories : sécurité email (SPF/DKIM/DMARC), TLS & certificats, en-têtes HTTP, exposition réseau, mauvaises configurations DNS, fichiers sensibles (`.env`, `.git`), composants vulnérables (CVE), Azure AD / Entra ID, WAF, prise de contrôle de sous-domaine…
- **CVE qualifiées par exploitabilité** : EXPOSÉ / POTENTIEL / vecteur local — fini les listes de CVE théoriques ingérables
- **Détection de subdomain takeover** (21 signatures : GitHub Pages, Azure, S3, Heroku, Vercel…)
- Enrichissement CVSS / EPSS / KEV directement dans chaque finding

### 📊 Scoring clair et actionnable
- Note **0–100 et grade A–F** par actif et par organisation
- Plafonnement automatique par sévérité (1 vulnérabilité critique → grade D maximum), aligné sur les standards type BitSight / SecurityScorecard
- Vision priorisée : on traite d'abord ce qui compte vraiment

### 🛰️ Renseignement sur la menace (CTI) intégré
- **Ransom Monitor** — corrélation de vos actifs avec les fuites des groupes de ransomware
- **Credential & Infostealer leaks** — détection d'identifiants compromis (Telegram, combolists)
- **Brand Monitor** — typosquatting et domaines frauduleux imitant votre marque
- **Threat Landscape** — vue contextuelle menace × exposition, par société, avec synthèse générée

### 📨 Alertes & rapports
- Notifications en temps réel sur nouveaux actifs, chutes de score et vulnérabilités critiques
- Rapports PDF livrables, prêts à présenter à la direction
- Export CSV / JSON pour intégration SIEM

---

## Pourquoi ARGOS

| | |
|---|---|
| 🔒 **Souverain & auto-hébergé** | Vos données restent chez vous. Aucune dépendance à un SaaS tiers. |
| 🤫 **Non intrusif** | Découverte majoritairement passive — pas d'exploitation, pas de risque opérationnel. |
| 🌍 **Pensé pour les groupes** | Filiales, marques rachetées, multi-pays et multi-TLD nativement gérés. |
| ✅ **Validé à l'échelle** | Éprouvé sur plusieurs milliers d'actifs réels. |
| 🇫🇷 **Conformité NIS2** | Cartographie d'exposition et suivi des risques alignés sur les exigences réglementaires. |

---

## Pour qui ?

- **RSSI & équipes sécurité** qui veulent une vision continue et priorisée de leur exposition
- **DSI de PME et ETI** sans SOC dédié, qui ont besoin de l'essentiel sans usine à gaz
- **Groupes multi-filiales** qui doivent suivre une surface d'attaque éclatée
- **Consultants & cabinets d'audit** cherchant un outil de cartographie et de scoring fiable

---

## Passez de l'angle mort à la maîtrise

Découvrez ce qu'un attaquant voit de votre organisation — avant lui.

[Demander une démo](/contact/) · [Nous contacter](/contact/)
