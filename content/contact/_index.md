---
title: "Contact"
description: "Prenez contact avec Def Intelligence"
---

Décrivez votre projet ou votre besoin, nous vous répondons sous 48h.

---

<form name="contact" method="POST" action="/merci/" data-netlify="true" netlify-honeypot="bot-field" style="display:flex;flex-direction:column;gap:1.2rem;max-width:600px">
  <input type="hidden" name="form-name" value="contact" />
  <p style="display:none"><label>Ne pas remplir : <input name="bot-field" /></label></p>

  <div>
    <label for="name" style="display:block;margin-bottom:.3rem;font-weight:600">Nom / Société</label>
    <input type="text" id="name" name="name" required style="width:100%;padding:.6rem .8rem;background:var(--color-neutral-700,#374151);border:1px solid var(--color-neutral-600,#4b5563);border-radius:.5rem;color:inherit;font-size:1rem" />
  </div>

  <div>
    <label for="email" style="display:block;margin-bottom:.3rem;font-weight:600">Email</label>
    <input type="email" id="email" name="email" required style="width:100%;padding:.6rem .8rem;background:var(--color-neutral-700,#374151);border:1px solid var(--color-neutral-600,#4b5563);border-radius:.5rem;color:inherit;font-size:1rem" />
  </div>

  <div>
    <label for="subject" style="display:block;margin-bottom:.3rem;font-weight:600">Sujet</label>
    <select id="subject" name="subject" style="width:100%;padding:.6rem .8rem;background:var(--color-neutral-700,#374151);border:1px solid var(--color-neutral-600,#4b5563);border-radius:.5rem;color:inherit;font-size:1rem">
      <option value="audit">Audit / Pentest</option>
      <option value="risques">Gestion des risques</option>
      <option value="formation">Formation</option>
      <option value="rssi">RSSI externalisé</option>
      <option value="argos">Démo ARGOS</option>
      <option value="autre">Autre</option>
    </select>
  </div>

  <div>
    <label for="message" style="display:block;margin-bottom:.3rem;font-weight:600">Message</label>
    <textarea id="message" name="message" rows="5" required style="width:100%;padding:.6rem .8rem;background:var(--color-neutral-700,#374151);border:1px solid var(--color-neutral-600,#4b5563);border-radius:.5rem;color:inherit;font-size:1rem;resize:vertical"></textarea>
  </div>

  <button type="submit" style="padding:.75rem 2rem;border-radius:.5rem;font-weight:700;font-size:1rem;cursor:pointer;background:var(--color-primary-600,#4f46e5);color:#fff;border:none">
    Envoyer le message
  </button>
</form>

---

📧 [contact@defintelligence.fr](mailto:contact@defintelligence.fr)
