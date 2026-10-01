#!/usr/bin/env python3
"""Generate LifeNex site pages IT/EN/FR/DE with screenshot captions."""
from pathlib import Path

ROOT = Path("/Users/stefano/Documents/lifenex-site")

SHOTS = {
    "it": [
        ("Metriche e Spotlight", "Una sola visione su recupero, HRV, attività, VO₂ max e FC a riposo — filtrabile per Sport, Corpo e Movimento."),
        ("Analizza ogni allenamento", "Durata, distanza, passo, FC, zone, kcal, dislivello e mappa GPS: tutto ciò che serve per capire la sessione."),
        ("Confronta le prestazioni", "Due uscite affiancate: durata, distanza, passo, FC, energia, dislivello e carico — vedi cosa è cambiato."),
        ("Carico di allenamento", "Durata, intensità, volume e carico nel tempo: una lettura più completa del tuo allenamento."),
        ("Analisi intelligente", "Gli ultimi 30 giorni in relazione: allenamento, carico, corpo, cuore, movimento, recupero e obiettivi."),
        ("Mix della settimana", "Volume, costanza e quota di tempo per tipo di sessione — la settimana in un colpo d’occhio."),
        ("Confronto live", "Due sessioni sulla stessa mappa 3D: i pallini avanzano insieme con tempo, passo, FC e pendenza."),
        ("Volo Satellite 3D", "Rivedi il percorso in Satellite 3D con play e velocità: zone FC e metriche sync mentre voli sul tracciato."),
    ],
    "en": [
        ("Metrics & Spotlight", "One view of recovery, HRV, activity, VO₂ max and resting HR — filter by Sport, Body and Movement."),
        ("Analyze every workout", "Duration, distance, pace, HR, zones, calories, elevation and GPS map — everything to understand the session."),
        ("Compare performance", "Two workouts side by side: duration, distance, pace, HR, energy, elevation and load — see what changed."),
        ("Training load", "Duration, intensity, volume and load over time: a fuller read of how you train."),
        ("Smart analysis", "The last 30 days connected: training, load, body, heart, movement, recovery and goals."),
        ("Weekly mix", "Volume, consistency and time share by session type — your week at a glance."),
        ("Live compare", "Two sessions on the same 3D map: dots move together with time, pace, HR and grade."),
        ("3D Satellite flight", "Replay the route in Satellite 3D with play and speed: HR zones and metrics stay in sync as you fly."),
    ],
    "fr": [
        ("Métriques et Spotlight", "Une seule vue sur récupération, VFC, activité, VO₂ max et FC au repos — filtrable par Sport, Corps et Mouvement."),
        ("Analysez chaque séance", "Durée, distance, allure, FC, zones, kcal, dénivelé et carte GPS : tout pour comprendre la séance."),
        ("Comparez vos perfs", "Deux sorties côte à côte : durée, distance, allure, FC, énergie, dénivelé et charge — voyez ce qui a changé."),
        ("Charge d’entraînement", "Durée, intensité, volume et charge dans le temps : une lecture plus complète de votre entraînement."),
        ("Analyse intelligente", "Les 30 derniers jours reliés : entraînement, charge, corps, cœur, mouvement, récupération et objectifs."),
        ("Mix de la semaine", "Volume, constance et part du temps par type de séance — la semaine d’un coup d’œil."),
        ("Comparaison live", "Deux séances sur la même carte 3D : les pastilles avancent ensemble avec temps, allure, FC et pente."),
        ("Vol Satellite 3D", "Revivez le parcours en Satellite 3D avec lecture et vitesse : zones FC et métriques synchronisées pendant le vol."),
    ],
    "de": [
        ("Metriken & Spotlight", "Ein Blick auf Erholung, HRV, Aktivität, VO₂ max und Ruhepuls — filterbar nach Sport, Körper und Bewegung."),
        ("Jede Einheit analysieren", "Dauer, Distanz, Tempo, HF, Zonen, kcal, Höhenmeter und GPS-Karte — alles, um die Einheit zu verstehen."),
        ("Leistungen vergleichen", "Zwei Einheiten nebeneinander: Dauer, Distanz, Tempo, HF, Energie, Höhenmeter und Last — sieh, was sich geändert hat."),
        ("Trainingslast", "Dauer, Intensität, Volumen und Last über die Zeit: ein vollständigeres Bild deines Trainings."),
        ("Intelligente Analyse", "Die letzten 30 Tage verbunden: Training, Last, Körper, Herz, Bewegung, Erholung und Ziele."),
        ("Wochen-Mix", "Volumen, Beständigkeit und Zeitanteil nach Einheitstyp — die Woche auf einen Blick."),
        ("Live-Vergleich", "Zwei Einheiten auf derselben 3D-Karte: Punkte laufen gemeinsam mit Zeit, Tempo, HF und Steigung."),
        ("3D-Satellitenflug", "Route im Satelliten-3D mit Play und Tempo nochmals erleben: HF-Zonen und Kennzahlen synchron zum Flug."),
    ],
}

COPY = {
    "it": {
        "lang": "it",
        "title": "LifeNex — Tutti i tuoi dati. Una sola visione.",
        "desc": "LifeNex trasforma i dati di Apple Salute in informazioni utili: allenamenti, prestazioni, carico, recupero, composizione corporea e salute — in un’unica app.",
        "nav_home": "Home",
        "nav_app": "App",
        "nav_privacy": "Privacy",
        "nav_contact": "Contatti",
        "eyebrow": "iOS · Apple Salute · HealthKit",
        "h1": "Tutti i tuoi dati. Una sola visione.",
        "lead": "Trasforma i dati di Apple Salute in informazioni utili. Allenamenti, prestazioni, carico, recupero, composizione corporea e principali dati di salute — riuniti in un’unica app.",
        "cta_store": "Scarica su App Store",
        "cta_see": "Esplora l’app",
        "what_h2": "Dal dato all’interpretazione",
        "what_sub": "Non è solo un diario degli allenamenti. È lo strumento per osservare nel tempo come cambiano prestazioni, corpo e indicatori principali.",
        "features": [
            ("Analizza ogni allenamento", "Durata, distanza, passo, velocità, calorie, dislivello, frequenza cardiaca, zone di intensità e mappa GPS: capisci come hai svolto ogni sessione."),
            ("Confronta le tue prestazioni", "Metti a confronto due allenamenti e verifica cosa è cambiato: durata, distanza, passo, FC, energia, dislivello e carico."),
            ("Vedi l’evoluzione nel tempo", "Grafici e serie temporali mostrano andamenti e cambiamenti che un singolo dato non rivela."),
            ("Una visione completa", "FC, FC a riposo, HRV, VO₂ max, pressione, ossigenazione, sonno, peso, BMI, massa grassa e magra, passi e attività — organizzati in un unico spazio."),
            ("Carico e corpo", "Monitora durata, intensità, volume e carico nel tempo. Segui peso, massa grassa e magra sullo storico."),
            ("Obiettivi e analisi intelligente", "Imposta obiettivi e segui i progressi. L’analisi mette in relazione gli ultimi 30 giorni di allenamento, carico, corpo, cuore, movimento e recupero."),
        ],
        "show_h2": "Tutto in un’unica app",
        "show_sub": "Riepilogo, Allenamenti, Carico, Obiettivi e Analisi: un’esperienza pensata per passare dal dato alla sua interpretazione.",
        "band_h2": "Vedi i dati. Confrontali. Analizzali. Segui la tua evoluzione.",
        "band_p": "LifeNex riunisce ciò che Apple Salute raccoglie — e te lo fa leggere.",
        "band_cta": "Vai su App Store",
        "alt": [
            "Schermata Metriche LifeNex",
            "Schermata Sessioni",
            "Confronto tra due sessioni",
            "Schermata Carico",
            "Schermata Trend con AI",
            "Mix sessioni settimanale",
            "Confronto sessioni live",
            "Volo Satellite 3D",
        ],
    },
    "en": {
        "lang": "en",
        "title": "LifeNex — All your data. One clear view.",
        "desc": "LifeNex turns Apple Health data into useful insight: workouts, performance, training load, recovery, body composition and health — in one app.",
        "nav_home": "Home",
        "nav_app": "App",
        "nav_privacy": "Privacy",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Health · HealthKit",
        "h1": "All your data. One clear view.",
        "lead": "Turn Apple Health data into useful information. Workouts, performance, training load, recovery, body composition and key health metrics — together in one app.",
        "cta_store": "Download on the App Store",
        "cta_see": "Explore the app",
        "what_h2": "From data to insight",
        "what_sub": "Not just a workout diary. A tool to watch how your performance, body and key indicators change over time.",
        "features": [
            ("Analyze every workout", "Duration, distance, pace, speed, calories, elevation, heart rate, intensity zones and GPS map — understand how you did each session."),
            ("Compare your performance", "Put two workouts side by side and see what changed: duration, distance, pace, HR, energy, elevation and load."),
            ("See evolution over time", "Charts and time series reveal trends and shifts a single number never shows."),
            ("A complete health view", "HR, resting HR, HRV, VO₂ max, blood pressure, oxygen, sleep, weight, BMI, fat and lean mass, steps and activity — organized in one place."),
            ("Load and body", "Track duration, intensity, volume and load over time. Follow weight, fat and lean mass on your history."),
            ("Goals and smart analysis", "Set goals and follow progress. Analysis connects the last 30 days of training, load, body, heart, movement and recovery."),
        ],
        "show_h2": "Everything in one app",
        "show_sub": "Summary, Workouts, Load, Goals and Analysis — designed to move from the number to what it means.",
        "band_h2": "See the data. Compare it. Analyze it. Follow your evolution.",
        "band_p": "LifeNex brings together what Apple Health collects — and helps you read it.",
        "band_cta": "Go to the App Store",
        "alt": [
            "LifeNex Metrics screen",
            "Sessions screen",
            "Compare two sessions",
            "Training load screen",
            "Trend screen with AI",
            "Weekly session mix",
            "Live session compare",
            "3D Satellite flight",
        ],
    },
    "fr": {
        "lang": "fr",
        "title": "LifeNex — Toutes vos données. Une seule vision.",
        "desc": "LifeNex transforme les données Apple Santé en informations utiles : séances, perfs, charge, récupération, composition corporelle et santé — dans une seule app.",
        "nav_home": "Accueil",
        "nav_app": "App",
        "nav_privacy": "Confidentialité",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Santé · HealthKit",
        "h1": "Toutes vos données. Une seule vision.",
        "lead": "Transformez les données Apple Santé en informations utiles. Séances, performances, charge, récupération, composition corporelle et indicateurs de santé — réunis dans une seule app.",
        "cta_store": "Télécharger sur l’App Store",
        "cta_see": "Explorer l’app",
        "what_h2": "De la donnée à l’interprétation",
        "what_sub": "Pas seulement un journal d’entraînement. Un outil pour observer comment évoluent vos performances, votre corps et vos indicateurs clés.",
        "features": [
            ("Analysez chaque séance", "Durée, distance, allure, vitesse, calories, dénivelé, fréquence cardiaque, zones d’intensité et carte GPS : comprenez chaque sortie."),
            ("Comparez vos performances", "Mettez deux séances face à face et voyez ce qui a changé : durée, distance, allure, FC, énergie, dénivelé et charge."),
            ("Voyez l’évolution dans le temps", "Graphiques et séries temporelles révèlent des tendances qu’un chiffre isolé ne montre jamais."),
            ("Une vision santé complète", "FC, FC au repos, VFC, VO₂ max, tension, oxygénation, sommeil, poids, IMC, masse grasse et maigre, pas et activité — organisés au même endroit."),
            ("Charge et corps", "Suivez durée, intensité, volume et charge dans le temps. Contrôlez poids, masse grasse et maigre sur l’historique."),
            ("Objectifs et analyse intelligente", "Fixez vos objectifs et suivez les progrès. L’analyse relie les 30 derniers jours d’entraînement, charge, corps, cœur, mouvement et récupération."),
        ],
        "show_h2": "Tout dans une seule app",
        "show_sub": "Résumé, Séances, Charge, Objectifs et Analyse : une expérience conçue pour passer de la donnée à son sens.",
        "band_h2": "Voyez les données. Comparez-les. Analysez-les. Suivez votre évolution.",
        "band_p": "LifeNex rassemble ce qu’Apple Santé collecte — et vous aide à le lire.",
        "band_cta": "Aller sur l’App Store",
        "alt": [
            "Écran Métriques LifeNex",
            "Écran Séances",
            "Comparer deux séances",
            "Écran Charge",
            "Écran Tendances avec IA",
            "Mix des séances de la semaine",
            "Comparaison séances live",
            "Vol Satellite 3D",
        ],
    },
    "de": {
        "lang": "de",
        "title": "LifeNex — Alle deine Daten. Ein klarer Blick.",
        "desc": "LifeNex macht aus Apple-Gesundheit nützliche Informationen: Training, Leistung, Last, Erholung, Körperzusammensetzung und Gesundheit — in einer App.",
        "nav_home": "Home",
        "nav_app": "App",
        "nav_privacy": "Datenschutz",
        "nav_contact": "Kontakt",
        "eyebrow": "iOS · Apple Gesundheit · HealthKit",
        "h1": "Alle deine Daten. Ein klarer Blick.",
        "lead": "Mach aus Apple-Gesundheit nützliche Informationen. Training, Leistung, Last, Erholung, Körperzusammensetzung und wichtige Gesundheitswerte — zusammen in einer App.",
        "cta_store": "Im App Store laden",
        "cta_see": "App entdecken",
        "what_h2": "Vom Wert zur Einsicht",
        "what_sub": "Nicht nur ein Trainingstagebuch. Ein Werkzeug, um zu sehen, wie sich Leistung, Körper und zentrale Indikatoren verändern.",
        "features": [
            ("Jede Einheit analysieren", "Dauer, Distanz, Tempo, Geschwindigkeit, Kalorien, Höhenmeter, Herzfrequenz, Intensitätszonen und GPS-Karte — verstehe jede Einheit."),
            ("Leistungen vergleichen", "Zwei Einheiten nebeneinander: Dauer, Distanz, Tempo, HF, Energie, Höhenmeter und Last — sieh, was sich geändert hat."),
            ("Entwicklung über die Zeit", "Diagramme und Zeitreihen zeigen Trends und Veränderungen, die eine einzelne Zahl nie verrät."),
            ("Ein vollständiger Gesundheitsblick", "HF, Ruhepuls, HRV, VO₂ max, Blutdruck, Sauerstoff, Schlaf, Gewicht, BMI, Fett- und Magermasse, Schritte und Aktivität — an einem Ort."),
            ("Last und Körper", "Verfolge Dauer, Intensität, Volumen und Last über die Zeit. Behalte Gewicht, Fett- und Magermasse im Blick."),
            ("Ziele und intelligente Analyse", "Setze Ziele und folge dem Fortschritt. Die Analyse verbindet die letzten 30 Tage aus Training, Last, Körper, Herz, Bewegung und Erholung."),
        ],
        "show_h2": "Alles in einer App",
        "show_sub": "Übersicht, Einheiten, Last, Ziele und Analyse — gemacht, um vom Wert zur Bedeutung zu kommen.",
        "band_h2": "Sieh die Daten. Vergleiche sie. Analysiere sie. Folge deiner Entwicklung.",
        "band_p": "LifeNex bündelt, was Apple Gesundheit sammelt — und hilft dir, es zu lesen.",
        "band_cta": "Zum App Store",
        "alt": [
            "LifeNex-Metriken",
            "Einheiten-Übersicht",
            "Zwei Einheiten vergleichen",
            "Trainingslast",
            "Trend mit KI",
            "Wochen-Mix der Einheiten",
            "Live-Einheitenvergleich",
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



def features_html(lang: str) -> str:
    blocks = []
    for title, body in COPY[lang]["features"]:
        blocks.append(
            f"""        <article class="card">
          <h3>{title}</h3>
          <p>{body}</p>
        </article>"""
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
    lightbox_js = "lightbox.js" if lang == "it" else "../lightbox.js"
    close_label = {"it": "Chiudi", "en": "Close", "fr": "Fermer", "de": "Schließen"}[lang]
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
  <link rel="stylesheet" href="{CSS[lang]}?v=4">
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
          <a href="{HOME_HREF[lang]}">{c['nav_home']}</a>
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
          <a class="store-badge" href="https://apps.apple.com/it/app/lifenex-salute-e-fitness/id6804388724" rel="noopener noreferrer">
            <img src="{a}badges/app-store-{lang}.svg" alt="{c['cta_store']}" height="40" width="120">
          </a>
          <a class="btn btn-ghost" href="#app">{c['cta_see']}</a>
        </div>
      </div>
      <div class="hero-phones" aria-hidden="true">
        <div class="phone phone-left"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-7.png" alt=""></div>
        <div class="phone phone-main"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-1.png" alt=""></div>
        <div class="phone phone-right"><img src="{a}screenshots/{SHOT_PREFIX[lang]}-8.png" alt=""></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <h2>{c['what_h2']}</h2>
      <p class="sub">{c['what_sub']}</p>
      <div class="grid-features">
{features_html(lang)}
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
    <a class="store-badge" href="https://apps.apple.com/it/app/lifenex-salute-e-fitness/id6804388724" rel="noopener noreferrer">
      <img src="{a}badges/app-store-{lang}.svg" alt="{c['band_cta']}" height="40" width="120">
    </a>
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

  <div id="lightbox" class="lightbox" style="display:none" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Screenshot">
    <div class="lightbox-dialog">
      <button type="button" class="lightbox-close" aria-label="{close_label}">&times;</button>
      <img class="lightbox-img" alt="">
    </div>
  </div>
  <script src="{lightbox_js}?v=2" defer></script>
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
          <a href="{home}">{COPY[lang]['nav_home']}</a>
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
