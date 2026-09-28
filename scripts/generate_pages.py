#!/usr/bin/env python3
"""Generate LifeNex site pages IT/EN/FR/DE with screenshot captions."""
from pathlib import Path

ROOT = Path("/Users/stefano/Documents/lifenex-site")

SHOTS = {
    "it": [
        ("Metriche e Spotlight", "Dashboard salute e sport: recupero, HRV, attività, VO₂ max e FC a riposo, filtrabili per Sport, Corpo e Movimento."),
        ("Cronologia sessioni", "Tutte le uscite da Salute: cerca, filtra, ordina e apri ogni allenamento con durata, km e kcal."),
        ("Confronta 2 sessioni", "Scegli due uscite (stesso percorso o simili) e confronta prestazioni, mappa e metriche affiancate."),
        ("Carico di allenamento", "Vedi se il carico recente è sopra o sotto il tuo ritmo abituale, per sport e finestra temporale."),
        ("Trend e analisi AI", "Lettura su 15–90 giorni di allenamento, cuore, HRV e peso, con lettura intelligente opzionale."),
        ("Mix della settimana", "Riepilogo 7 giorni: volume, costanza e quota di tempo per tipo di sessione (forza, corsa, bici…)."),
        ("Confronto 3D con pallini", "Due sessioni sulla stessa mappa 3D: i pallini colorati si muovono insieme nel replay, con tempo, passo, FC e pendenza a confronto."),
        ("Volo Satellite 3D", "Rivedi il percorso in Satellite 3D con play e velocità (fino a 10×): zone FC e metriche sync mentre ‘voli’ sul tracciato."),
    ],
    "en": [
        ("Metrics & Spotlight", "Health and sport dashboard: recovery, HRV, activity, VO₂ max and resting HR, filterable by Sport, Body and Movement."),
        ("Workout history", "Every session from Health: search, filter, sort and open each workout with duration, distance and calories."),
        ("Compare 2 sessions", "Pick two workouts (same or similar route) and compare performance, map and metrics side by side."),
        ("Training load", "See whether recent load sits above or below your habitual rhythm, by sport and time window."),
        ("Trends & AI analysis", "15–90 day readouts on training, heart, HRV and weight, plus optional smart readings."),
        ("Weekly mix", "7-day summary: volume, consistency and time share by session type (strength, run, bike…)."),
        ("3D compare with moving dots", "Two sessions on the same 3D map: colored dots move together in replay, with time, pace, HR and grade side by side."),
        ("3D Satellite flight", "Replay the route in Satellite 3D with play and speed (up to 10×): HR zones and metrics stay in sync as you fly the track."),
    ],
    "fr": [
        ("Métriques et Spotlight", "Tableau de bord santé et sport : récupération, VFC, activité, VO₂ max et FC au repos, filtrable par Sport, Corps et Mouvement."),
        ("Historique des séances", "Toutes les sorties depuis Santé : recherchez, filtrez, triez et ouvrez chaque entraînement avec durée, km et kcal."),
        ("Comparer 2 séances", "Choisissez deux sorties (même parcours ou similaires) et comparez perfos, carte et métriques côte à côte."),
        ("Charge d’entraînement", "Voyez si la charge récente est au-dessus ou en dessous de votre rythme habituel, par sport et période."),
        ("Tendances et analyse IA", "Lecture sur 15–90 jours (entraînement, cœur, VFC, poids), avec lectures intelligentes optionnelles."),
        ("Mix de la semaine", "Résumé 7 jours : volume, constance et part du temps par type de séance (force, course, vélo…)."),
        ("Comparaison 3D avec pastilles", "Deux séances sur la même carte 3D : les pastilles colorées avancent ensemble en replay, avec temps, allure, FC et pente en face."),
        ("Vol Satellite 3D", "Revivez le parcours en Satellite 3D avec lecture et vitesse (jusqu’à 10×) : zones FC et métriques synchronisées pendant le vol."),
    ],
    "de": [
        ("Metriken & Spotlight", "Dashboard für Gesundheit und Sport: Erholung, HRV, Aktivität, VO₂ max und Ruhepuls — filterbar nach Sport, Körper und Bewegung."),
        ("Trainingshistorie", "Alle Einheiten aus Gesundheit: suchen, filtern, sortieren und jede Einheit mit Dauer, km und kcal öffnen."),
        ("2 Einheiten vergleichen", "Zwei Einheiten wählen (gleiche oder ähnliche Route) und Leistung, Karte und Kennzahlen vergleichen."),
        ("Trainingslast", "Siehst du, ob die aktuelle Last über oder unter deinem gewohnten Rhythmus liegt — nach Sport und Zeitraum."),
        ("Trends & KI-Analyse", "Auswertung über 15–90 Tage zu Training, Herz, HRV und Gewicht, plus optionale intelligente Lesungen."),
        ("Wochen-Mix", "7-Tage-Übersicht: Volumen, Beständigkeit und Zeitanteil nach Einheitstyp (Kraft, Lauf, Rad…)."),
        ("3D-Vergleich mit Punkten", "Zwei Einheiten auf derselben 3D-Karte: farbige Punkte bewegen sich gemeinsam im Replay — Zeit, Tempo, HF und Steigung im Vergleich."),
        ("3D-Satellitenflug", "Route im Satelliten-3D mit Play und Tempo (bis 10×) nochmal erleben: HF-Zonen und Kennzahlen synchron zum Flug."),
    ],
}

COPY = {
    "it": {
        "lang": "it",
        "title": "LifeNex — Analisi Fitness, Salute e IA",
        "desc": "LifeNex — analisi fitness, salute e IA dai dati Apple Salute. Trend, sessioni, carico e obiettivi.",
        "nav_app": "App",
        "nav_privacy": "Privacy",
        "nav_contact": "Contatti",
        "eyebrow": "iOS · Apple Salute · HealthKit",
        "h1": "Analisi Fitness, Salute e IA",
        "lead": "Trasforma i dati già in Apple Salute in trend chiari: sessioni, carico, composizione e obiettivi — senza diagnosi e senza piani clinici.",
        "cta_store": "Scarica su App Store",
        "cta_see": "Vedi l’app",
        "what_h2": "Cosa fa LifeNex",
        "what_sub": "Osserva i tuoi dati, spiega i trend e ti motiva verso obiettivi che scegli tu.",
        "c1_t": "Trend e analisi",
        "c1_b": "Periodi 15–90 giorni su attività, cardio, sonno e composizione — in linguaggio semplice.",
        "c2_t": "Sessioni e carico",
        "c2_b": "Cronologia allenamenti, zone FC, mappe e andamento del carico nel tempo.",
        "c3_t": "IA opzionale",
        "c3_b": "Letture intelligenti solo con consenso, su riassunti già calcolati sul tuo iPhone.",
        "show_h2": "Dentro l’app",
        "show_sub": "Otto schermate chiave: cosa vedi e a cosa servono.",
        "band_h2": "Pronto a leggere i tuoi dati?",
        "band_p": "LifeNex osserva, spiega e motiva. Non è un’app medica.",
        "band_cta": "Vai su App Store",
        "alt": [
            "Schermata Metriche LifeNex",
            "Schermata Sessioni",
            "Confronto tra due sessioni",
            "Schermata Carico",
            "Schermata Trend con AI",
            "Mix sessioni settimanale",
            "Confronto 3D con pallini",
            "Volo Satellite 3D",
        ],
    },
    "en": {
        "lang": "en",
        "title": "LifeNex — Fitness, Health & AI Analysis",
        "desc": "LifeNex — fitness, health and AI analysis from Apple Health. Trends, workouts, training load and goals.",
        "nav_app": "App",
        "nav_privacy": "Privacy",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Health · HealthKit",
        "h1": "Fitness, Health &amp; AI Analysis",
        "lead": "Turn the data already in Apple Health into clear trends: workouts, training load, body composition and goals — without diagnosis or clinical plans.",
        "cta_store": "Download on the App Store",
        "cta_see": "See the app",
        "what_h2": "What LifeNex does",
        "what_sub": "It observes your data, explains trends, and motivates you toward goals you choose.",
        "c1_t": "Trends &amp; analysis",
        "c1_b": "15–90 day windows on activity, cardio, sleep and composition — in plain language.",
        "c2_t": "Workouts &amp; load",
        "c2_b": "Workout history, heart-rate zones, maps and how your training load evolves.",
        "c3_t": "Optional AI",
        "c3_b": "Smart readings only with consent, based on summaries already computed on your iPhone.",
        "show_h2": "Inside the app",
        "show_sub": "Eight key screens: what you see and what you can do.",
        "band_h2": "Ready to read your data?",
        "band_p": "LifeNex observes, explains, and motivates. Not a medical app.",
        "band_cta": "Go to the App Store",
        "alt": [
            "LifeNex Metrics screen",
            "Sessions screen",
            "Compare two sessions",
            "Training load screen",
            "Trend screen with AI",
            "Weekly session mix",
            "3D compare with moving dots",
            "3D Satellite flight",
        ],
    },
    "fr": {
        "lang": "fr",
        "title": "LifeNex — Analyse Fitness, Santé et IA",
        "desc": "LifeNex — analyse fitness, santé et IA à partir d’Apple Santé. Tendances, séances, charge et objectifs.",
        "nav_app": "App",
        "nav_privacy": "Confidentialité",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Santé · HealthKit",
        "h1": "Analyse Fitness, Santé et IA",
        "lead": "Transformez les données déjà dans Apple Santé en tendances claires : séances, charge, composition et objectifs — sans diagnostic ni plan clinique.",
        "cta_store": "Télécharger sur l’App Store",
        "cta_see": "Voir l’app",
        "what_h2": "Ce que fait LifeNex",
        "what_sub": "Il observe vos données, explique les tendances et vous motive vers les objectifs que vous choisissez.",
        "c1_t": "Tendances et analyse",
        "c1_b": "Fenêtres de 15–90 jours sur activité, cardio, sommeil et composition — en langage simple.",
        "c2_t": "Séances et charge",
        "c2_b": "Historique d’entraînement, zones FC, cartes et évolution de la charge dans le temps.",
        "c3_t": "IA optionnelle",
        "c3_b": "Lectures intelligentes uniquement avec consentement, à partir de résumés déjà calculés sur l’iPhone.",
        "show_h2": "Dans l’app",
        "show_sub": "Huit écrans clés : ce que vous voyez et ce que vous pouvez faire.",
        "band_h2": "Prêt à lire vos données ?",
        "band_p": "LifeNex observe, explique et motive. Ce n’est pas une app médicale.",
        "band_cta": "Aller sur l’App Store",
        "alt": [
            "Écran Métriques LifeNex",
            "Écran Séances",
            "Comparer deux séances",
            "Écran Charge",
            "Écran Tendances avec IA",
            "Mix des séances de la semaine",
            "Comparaison 3D avec pastilles",
            "Vol Satellite 3D",
        ],
    },
    "de": {
        "lang": "de",
        "title": "LifeNex — Fitness-, Gesundheits- &amp; KI-Analyse",
        "desc": "LifeNex — Fitness-, Gesundheits- und KI-Analyse aus Apple Gesundheit. Trends, Einheiten, Last und Ziele.",
        "nav_app": "App",
        "nav_privacy": "Datenschutz",
        "nav_contact": "Kontakt",
        "eyebrow": "iOS · Apple Gesundheit · HealthKit",
        "h1": "Fitness, Gesundheit &amp; KI-Analyse",
        "lead": "Mach aus den Daten in Apple Gesundheit klare Trends: Einheiten, Trainingslast, Körperzusammensetzung und Ziele — ohne Diagnose und ohne klinische Pläne.",
        "cta_store": "Im App Store laden",
        "cta_see": "App ansehen",
        "what_h2": "Was LifeNex macht",
        "what_sub": "Beobachtet deine Daten, erklärt Trends und motiviert dich zu Zielen, die du selbst wählst.",
        "c1_t": "Trends &amp; Analyse",
        "c1_b": "Fenster von 15–90 Tagen zu Aktivität, Cardio, Schlaf und Zusammensetzung — in klarer Sprache.",
        "c2_t": "Einheiten &amp; Last",
        "c2_b": "Trainingshistorie, HF-Zonen, Karten und wie sich deine Trainingslast entwickelt.",
        "c3_t": "Optionale KI",
        "c3_b": "Intelligente Lesungen nur mit Einwilligung, basierend auf Zusammenfassungen auf dem iPhone.",
        "show_h2": "In der App",
        "show_sub": "Acht zentrale Screens: was du siehst und wozu sie dienen.",
        "band_h2": "Bereit, deine Daten zu lesen?",
        "band_p": "LifeNex beobachtet, erklärt und motiviert. Keine Medizin-App.",
        "band_cta": "Zum App Store",
        "alt": [
            "LifeNex-Metriken",
            "Einheiten-Übersicht",
            "Zwei Einheiten vergleichen",
            "Trainingslast",
            "Trend mit KI",
            "Wochen-Mix der Einheiten",
            "3D-Vergleich mit Punkten",
            "3D-Satellitenflug",
        ],
    },
}

HOME_PATH = {"it": ".", "en": "en", "fr": "fr", "de": "de"}
PREFIX = {"it": "", "en": "../", "fr": "../", "de": "../"}
SHOT_PREFIX = {"it": "it", "en": "en", "fr": "fr", "de": "de"}
ASSET = {"it": "assets/", "en": "../assets/", "fr": "../assets/", "de": "../assets/"}
CSS = {"it": "styles.css", "en": "../styles.css", "fr": "../styles.css", "de": "../styles.css"}
HOME_HREF = {"it": "./", "en": "./", "fr": "./", "de": "./"}
PRIVACY_HREF = {"it": "privacy/", "en": "privacy/", "fr": "privacy/", "de": "privacy/"}
ROOT_HOME = {"it": "./", "en": "../", "fr": "../", "de": "../"}


def lang_switch(active: str, base: str) -> str:
    # base is path prefix to site root from current page ("" or "../")
    it_href = f"{base}" if base else "./"
    if it_href == "":
        it_href = "./"
    links = [
        ("it", it_href if base == "" else f"{base}", "IT"),
        ("en", f"{base}en/", "EN"),
        ("fr", f"{base}fr/", "FR"),
        ("de", f"{base}de/", "DE"),
    ]
    # From non-IT home, IT should be ../
    if base == "../":
        links[0] = ("it", "../", "IT")
    parts = []
    for code, href, label in links:
        cls = ' class="active"' if code == active else ""
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<div class="lang-switch" aria-label="Language">' + "".join(parts) + "</div>"


def shots_html(lang: str) -> str:
    a = ASSET[lang]
    prefix = SHOT_PREFIX[lang]
    alts = COPY[lang]["alt"]
    blocks = []
    for i, ((title, body), alt) in enumerate(zip(SHOTS[lang], alts), start=1):
        src = f"{a}screenshots/{prefix}-{i}.png"
        blocks.append(
            f"""        <figure class="shot">
          <a class="shot-frame" href="{src}"><img src="{src}" alt="{alt}" loading="lazy"></a>
          <figcaption><strong>{title}</strong><span>{body}</span></figcaption>
        </figure>"""
        )
    return "\n".join(blocks)


def home_html(lang: str) -> str:
    c = COPY[lang]
    base = PREFIX[lang] if lang != "it" else ""
    if lang == "it":
        base_for_lang = "./"
        # for IT root, links to en/ fr/ de/ are relative without ../
        switch = lang_switch("it", "")
    else:
        switch = lang_switch(lang, "../")
    a = ASSET[lang]
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{c['desc']}">
  <title>{c['title']}</title>
  <link rel="icon" href="{a}app-icon.png" type="image/png">
  <link rel="apple-touch-icon" href="{a}apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{CSS[lang]}">
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{HOME_HREF[lang]}">
        <img src="{a}app-icon.png" alt="" width="36" height="36">
        LifeNex
      </a>
      <div class="header-right">
        <nav class="nav-links" aria-label="Main">
          <a href="#app">{c['nav_app']}</a>
          <a href="{PRIVACY_HREF[lang]}">{c['nav_privacy']}</a>
          <a href="mailto:support@lifenex.it">{c['nav_contact']}</a>
        </nav>
        {switch}
      </div>
    </div>
  </header>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">{c['eyebrow']}</p>
        <p class="brand-hero">LifeNex</p>
        <h1>{c['h1']}</h1>
        <p class="lead">{c['lead']}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="https://apps.apple.com/" rel="noopener noreferrer">{c['cta_store']}</a>
          <a class="btn btn-ghost" href="#app">{c['cta_see']}</a>
        </div>
      </div>
      <div class="hero-phones" aria-hidden="true">
        <div class="phone phone-left"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-7.png" alt=""></div>
        <div class="phone phone-main"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-8.png" alt=""></div>
        <div class="phone phone-right"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-1.png" alt=""></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <h2>{c['what_h2']}</h2>
      <p class="sub">{c['what_sub']}</p>
      <div class="grid-3">
        <article class="card">
          <h3>{c['c1_t']}</h3>
          <p>{c['c1_b']}</p>
        </article>
        <article class="card">
          <h3>{c['c2_t']}</h3>
          <p>{c['c2_b']}</p>
        </article>
        <article class="card">
          <h3>{c['c3_t']}</h3>
          <p>{c['c3_b']}</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section showcase" id="app">
    <div class="section-inner">
      <h2>{c['show_h2']}</h2>
      <p class="sub">{c['show_sub']}</p>
      <div class="shot-grid">
{shots_html(lang)}
      </div>
    </div>
  </section>

  <div class="cta-band">
    <h2>{c['band_h2']}</h2>
    <p>{c['band_p']}</p>
    <a class="btn btn-primary" href="https://apps.apple.com/" rel="noopener noreferrer">{c['band_cta']}</a>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <span>© 2026 LifeNex</span>
      <span>
        <a href="{PRIVACY_HREF[lang]}">{c['nav_privacy']}</a> ·
        <a href="mailto:support@lifenex.it">support@lifenex.it</a>
      </span>
    </div>
  </footer>
</body>
</html>
"""


PRIVACY = {
    "it": {
        "title": "Privacy — LifeNex",
        "h1": "Informativa sulla privacy",
        "meta": 'Titolare: Stefano Toncelli · Contatto: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Ultimo aggiornamento: 28 settembre 2026',
        "nav": "Privacy",
        "contact": "Contatti",
        "back": "Torna alla home",
        "body": """
    <p>LifeNex è un’app iOS che ti aiuta a osservare l’evoluzione dei dati già presenti in Apple Salute e a restare motivato verso i tuoi obiettivi. Non è un dispositivo medico, non diagnostica e non prescrive intensità o terapie.</p>
    <h2>Dati che l’app legge</h2>
    <p>Con il tuo consenso, LifeNex <strong>legge</strong> da Salute (HealthKit), in sola lettura:</p>
    <ul>
      <li>attività (passi, energie, minuti esercizio, distanza)</li>
      <li>sessioni (allenamenti, percorso GPS se presente, sforzo, frequenza cardiaca di sessione)</li>
      <li>cardio (FC, FC a riposo, HRV, VO₂ max)</li>
      <li>corpo (peso, altezza, BMI, massa grassa e magra)</li>
      <li>sonno e, se presenti in Salute, vitali come pressione e saturazione</li>
      <li>dinamiche di corsa e cammino, se le scrive il tuo dispositivo</li>
    </ul>
    <p>LifeNex <strong>non scrive</strong> e <strong>non modifica</strong> i dati in Salute.</p>
    <h2>Dove vengono trattati</h2>
    <p>I dati di Salute restano <strong>sul tuo iPhone</strong> (archivio locale). Non c’è un account LifeNex obbligatorio.</p>
    <p><strong>Analisi intelligente (opzionale):</strong> solo se attivi il consenso in Preferenze e chiedi tu una lettura (Genera / Aggiorna), LifeNex può usare <strong>riassunti numerici già calcolati in app</strong> per preparare il testo tramite un gateway sicuro. Non partono tracciati GPS, foto né la cronologia grezza di Salute.</p>
    <h2>Cosa non facciamo</h2>
    <ul><li>non vendiamo i tuoi dati</li><li>non usiamo i dati Salute per pubblicità o tracking tra app</li><li>non condividiamo dati sanitari con terze parti a scopo commerciale</li></ul>
    <h2>Conservazione e cancellazione</h2>
    <p>I dati restano sul dispositivo finché l’app è installata. Per cancellarli: elimina LifeNex e, in Impostazioni → Salute → Accesso app e dati, revoca l’accesso.</p>
    <h2>Permessi</h2>
    <p>Puoi rifiutare o revocare i permessi Salute in qualsiasi momento.</p>
    <h2>Minori</h2>
    <p>LifeNex non è destinata a bambini.</p>
    <h2>Abbonamenti</h2>
    <p>Plus e Max sono gestiti da Apple tramite l’App Store.</p>
    <h2>Modifiche</h2>
    <p>Se in futuro alcuni dati usciranno dal telefono (solo con consenso), questa pagina verrà aggiornata <strong>prima</strong>.</p>
    <p>Per domande: <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "en": {
        "title": "Privacy — LifeNex",
        "h1": "Privacy policy",
        "meta": 'Controller: Stefano Toncelli · Contact: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Last updated: 28 September 2026',
        "nav": "Privacy",
        "contact": "Contact",
        "back": "Back to home",
        "body": """
    <p>LifeNex is an iOS app that helps you observe how the data already in Apple Health evolves and stay motivated toward goals you choose. It is not a medical device, does not diagnose, and does not prescribe intensity or therapy.</p>
    <h2>Data the app reads</h2>
    <p>With your consent, LifeNex <strong>reads</strong> from Health (HealthKit), read-only:</p>
    <ul>
      <li>activity (steps, energy, exercise minutes, distance)</li>
      <li>workouts (sessions, GPS route if present, effort, session heart rate)</li>
      <li>cardio (HR, resting HR, HRV, VO₂ max)</li>
      <li>body (weight, height, BMI, body fat and lean mass)</li>
      <li>sleep and, if present in Health, vitals such as blood pressure and oxygen saturation</li>
      <li>running and walking dynamics, if written by your device</li>
    </ul>
    <p>LifeNex does <strong>not write</strong> or <strong>modify</strong> Health data.</p>
    <h2>Where data is processed</h2>
    <p>Health data stays <strong>on your iPhone</strong>. There is no mandatory LifeNex account.</p>
    <p><strong>Optional smart analysis:</strong> only with consent in Settings and when you request a reading, LifeNex may use <strong>numeric summaries already computed in the app</strong> via a secure gateway. GPS tracks, photos and raw Health history are not sent.</p>
    <h2>What we do not do</h2>
    <ul><li>we do not sell your data</li><li>we do not use Health data for advertising or cross-app tracking</li><li>we do not share health data with third parties for commercial purposes</li></ul>
    <h2>Retention and deletion</h2>
    <p>Data stays on the device while the app is installed. Remove LifeNex and revoke access in Settings → Health.</p>
    <h2>Permissions</h2>
    <p>You can refuse or revoke Health permissions at any time.</p>
    <h2>Children</h2>
    <p>LifeNex is not intended for children.</p>
    <h2>Subscriptions</h2>
    <p>Plus and Max are managed by Apple through the App Store.</p>
    <h2>Changes</h2>
    <p>If some data ever leaves the phone (only with explicit consent), this page will be updated <strong>first</strong>.</p>
    <p>Questions: <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "fr": {
        "title": "Confidentialité — LifeNex",
        "h1": "Politique de confidentialité",
        "meta": 'Responsable : Stefano Toncelli · Contact : <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Dernière mise à jour : 28 septembre 2026',
        "nav": "Confidentialité",
        "contact": "Contact",
        "back": "Retour à l’accueil",
        "body": """
    <p>LifeNex est une app iOS qui vous aide à observer l’évolution des données déjà présentes dans Apple Santé et à rester motivé vers vos objectifs. Ce n’est pas un dispositif médical, elle ne diagnostique pas et ne prescrit ni intensité ni thérapie.</p>
    <h2>Données lues par l’app</h2>
    <p>Avec votre consentement, LifeNex <strong>lit</strong> dans Santé (HealthKit), en lecture seule :</p>
    <ul>
      <li>activité (pas, énergie, minutes d’exercice, distance)</li>
      <li>séances (entraînements, parcours GPS si présent, effort, FC de séance)</li>
      <li>cardio (FC, FC au repos, VFC, VO₂ max)</li>
      <li>corps (poids, taille, IMC, masse grasse et maigre)</li>
      <li>sommeil et, si présents, des signes vitaux comme tension et saturation</li>
      <li>dynamiques de course et de marche, si votre appareil les écrit</li>
    </ul>
    <p>LifeNex <strong>n’écrit</strong> ni <strong>ne modifie</strong> les données Santé.</p>
    <h2>Où les données sont traitées</h2>
    <p>Les données Santé restent <strong>sur votre iPhone</strong>. Aucun compte LifeNex obligatoire.</p>
    <p><strong>Analyse intelligente (optionnelle) :</strong> uniquement avec consentement et sur demande, LifeNex peut utiliser des <strong>résumés numériques déjà calculés dans l’app</strong> via une passerelle sécurisée. Pas de traces GPS, photos ni historique brut.</p>
    <h2>Ce que nous ne faisons pas</h2>
    <ul><li>nous ne vendons pas vos données</li><li>pas de pub ni de tracking croisé avec les données Santé</li><li>pas de partage commercial de données de santé</li></ul>
    <h2>Conservation et suppression</h2>
    <p>Les données restent sur l’appareil tant que l’app est installée. Supprimez LifeNex et révoquez l’accès dans Réglages → Santé.</p>
    <h2>Autorisations</h2>
    <p>Vous pouvez refuser ou révoquer les autorisations Santé à tout moment.</p>
    <h2>Mineurs</h2>
    <p>LifeNex n’est pas destinée aux enfants.</p>
    <h2>Abonnements</h2>
    <p>Plus et Max sont gérés par Apple via l’App Store.</p>
    <h2>Modifications</h2>
    <p>Si des données quittaient un jour le téléphone (seulement avec consentement), cette page serait mise à jour <strong>avant</strong>.</p>
    <p>Questions : <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "de": {
        "title": "Datenschutz — LifeNex",
        "h1": "Datenschutzerklärung",
        "meta": 'Verantwortlich: Stefano Toncelli · Kontakt: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Stand: 28. September 2026',
        "nav": "Datenschutz",
        "contact": "Kontakt",
        "back": "Zur Startseite",
        "body": """
    <p>LifeNex ist eine iOS-App, die dir hilft, die Entwicklung der Daten in Apple Gesundheit zu beobachten und motiviert bei Zielen zu bleiben, die du selbst wählst. Kein Medizinprodukt, keine Diagnose, keine Vorgabe von Intensität oder Therapie.</p>
    <h2>Daten, die die App liest</h2>
    <p>Mit deiner Einwilligung <strong>liest</strong> LifeNex aus Gesundheit (HealthKit), nur lesend:</p>
    <ul>
      <li>Aktivität (Schritte, Energie, Trainingsminuten, Distanz)</li>
      <li>Einheiten (Workouts, GPS-Route falls vorhanden, Aufwand, Einheiten-Herzfrequenz)</li>
      <li>Cardio (HF, Ruhepuls, HRV, VO₂ max)</li>
      <li>Körper (Gewicht, Größe, BMI, Fett- und Magermasse)</li>
      <li>Schlaf und, falls vorhanden, Werte wie Blutdruck und Sättigung</li>
      <li>Lauf- und Geh-Dynamik, falls dein Gerät sie schreibt</li>
    </ul>
    <p>LifeNex <strong>schreibt</strong> und <strong>ändert</strong> keine Gesundheitsdaten.</p>
    <h2>Wo Daten verarbeitet werden</h2>
    <p>Gesundheitsdaten bleiben <strong>auf dem iPhone</strong>. Kein Pflicht-Account.</p>
    <p><strong>Optionale intelligente Analyse:</strong> nur mit Einwilligung und auf Anfrage kann LifeNex <strong>bereits in der App berechnete Zahlenzusammenfassungen</strong> über ein sicheres Gateway nutzen. Keine GPS-Spuren, Fotos oder Rohhistorie.</p>
    <h2>Was wir nicht tun</h2>
    <ul><li>wir verkaufen deine Daten nicht</li><li>keine Werbung oder Cross-App-Tracking mit Gesundheitsdaten</li><li>keine kommerzielle Weitergabe von Gesundheitsdaten</li></ul>
    <h2>Speicherung und Löschung</h2>
    <p>Daten bleiben auf dem Gerät, solange die App installiert ist. LifeNex löschen und den Zugriff unter Einstellungen → Gesundheit widerrufen.</p>
    <h2>Berechtigungen</h2>
    <p>Du kannst Gesundheitsberechtigungen jederzeit ablehnen oder widerrufen.</p>
    <h2>Kinder</h2>
    <p>LifeNex ist nicht für Kinder bestimmt.</p>
    <h2>Abonnements</h2>
    <p>Plus und Max werden von Apple über den App Store verwaltet.</p>
    <h2>Änderungen</h2>
    <p>Sollten Daten künftig das Telefon verlassen (nur mit ausdrücklicher Einwilligung), wird diese Seite <strong>zuerst</strong> aktualisiert.</p>
    <p>Fragen: <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
}


def privacy_html(lang: str) -> str:
    p = PRIVACY[lang]
    a = ASSET[lang] if lang == "it" else ("../" + ASSET[lang].lstrip("../") if False else ASSET[lang])
    # From privacy/ subfolder, assets are one level deeper for non-root... 
    # IT privacy is at privacy/ → ../assets/
    # EN privacy at en/privacy/ → ../../assets/
    if lang == "it":
        asset = "../assets/"
        css = "../styles.css"
        home = "../"
        switch = lang_switch("it", "../")
        # Fix IT lang switch from privacy: IT home is ../, EN is ../en/
        switch = '''<div class="lang-switch" aria-label="Language">
          <a href="./" class="active">IT</a>
          <a href="../en/privacy/">EN</a>
          <a href="../fr/privacy/">FR</a>
          <a href="../de/privacy/">DE</a>
        </div>'''
    else:
        asset = "../../assets/"
        css = "../../styles.css"
        home = "../"
        switch = f'''<div class="lang-switch" aria-label="Language">
          <a href="../../privacy/">IT</a>
          <a href="../../en/privacy/"{' class="active"' if lang=='en' else ''}>EN</a>
          <a href="../../fr/privacy/"{' class="active"' if lang=='fr' else ''}>FR</a>
          <a href="../../de/privacy/"{' class="active"' if lang=='de' else ''}>DE</a>
        </div>'''
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title']}</title>
  <link rel="icon" href="{asset}app-icon.png" type="image/png">
  <link rel="apple-touch-icon" href="{asset}apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body class="page-shell">
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{home}">
        <img src="{asset}app-icon.png" alt="" width="36" height="36">
        LifeNex
      </a>
      <div class="header-right">
        <nav class="nav-links" aria-label="Main">
          <a class="active" href="./">{p['nav']}</a>
          <a href="mailto:support@lifenex.it">{p['contact']}</a>
        </nav>
        {switch}
      </div>
    </div>
  </header>
  <article class="legal-page">
    <h1>{p['h1']}</h1>
    <p class="legal-meta">{p['meta']}</p>
    {p['body']}
  </article>
  <footer class="site-footer">
    <div class="footer-inner">
      <span>© 2026 LifeNex</span>
      <a href="{home}">{p['back']}</a>
    </div>
  </footer>
</body>
</html>
"""


def main():
    for lang in ("it", "en", "fr", "de"):
        if lang == "it":
            path = ROOT / "index.html"
        else:
            path = ROOT / lang / "index.html"
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(home_html(lang))
        print("wrote", path)

        if lang == "it":
            ppath = ROOT / "privacy" / "index.html"
        else:
            ppath = ROOT / lang / "privacy" / "index.html"
            ppath.parent.mkdir(parents=True, exist_ok=True)
        ppath.write_text(privacy_html(lang))
        print("wrote", ppath)


if __name__ == "__main__":
    main()
