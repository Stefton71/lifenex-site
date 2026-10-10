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
        "nav_terms": "Termini",
        "nav_contact": "Contatti",
        "eyebrow": "iOS · Apple Salute · HealthKit",
        "h1": "Tutti i tuoi dati. Una sola visione.",
        "lead": "Trasforma i dati di Apple Salute in informazioni utili. Allenamenti, prestazioni, carico, recupero, composizione corporea e principali dati di salute — riuniti in un’unica app.",
        "cta_store": "Scarica su App Store",
        "cta_see": "Esplora l’app",
        "video_id": "mnVdDF1LOpA",
        "video_h2": "Guarda LifeNex in azione",
        "video_sub": "Scopri in breve come LifeNex trasforma i dati di Apple Watch e Salute in una visione chiara.",
        "video_title": "LifeNex – La tua forma e i tuoi allenamenti con Apple Watch",
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
        "nav_terms": "Terms",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Health · HealthKit",
        "h1": "All your data. One clear view.",
        "lead": "Turn Apple Health data into useful information. Workouts, performance, training load, recovery, body composition and key health metrics — together in one app.",
        "cta_store": "Download on the App Store",
        "cta_see": "Explore the app",
        "video_id": "H0bXt7V_j98",
        "video_h2": "See LifeNex in action",
        "video_sub": "A quick look at how LifeNex turns Apple Watch and Health data into one clear view.",
        "video_title": "LifeNex – Your fitness and workouts with Apple Watch",
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
        "nav_terms": "Conditions",
        "nav_contact": "Contact",
        "eyebrow": "iOS · Apple Santé · HealthKit",
        "h1": "Toutes vos données. Une seule vision.",
        "lead": "Transformez les données Apple Santé en informations utiles. Séances, performances, charge, récupération, composition corporelle et indicateurs de santé — réunis dans une seule app.",
        "cta_store": "Télécharger sur l’App Store",
        "cta_see": "Explorer l’app",
        "video_id": "KuZ9XnwG6dg",
        "video_h2": "Découvrez LifeNex en action",
        "video_sub": "Un aperçu rapide de la façon dont LifeNex transforme les données Apple Watch et Santé en une vision claire.",
        "video_title": "LifeNex – Votre forme et vos entraînements avec l’Apple Watch",
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
        "nav_terms": "Nutzung",
        "nav_contact": "Kontakt",
        "eyebrow": "iOS · Apple Gesundheit · HealthKit",
        "h1": "Alle deine Daten. Ein klarer Blick.",
        "lead": "Mach aus Apple-Gesundheit nützliche Informationen. Training, Leistung, Last, Erholung, Körperzusammensetzung und wichtige Gesundheitswerte — zusammen in einer App.",
        "cta_store": "Im App Store laden",
        "cta_see": "App entdecken",
        "video_id": "3nGrcsxqma8",
        "video_h2": "LifeNex in Aktion",
        "video_sub": "Ein kurzer Blick darauf, wie LifeNex Daten von Apple Watch und Apple Gesundheit in einen klaren Überblick verwandelt.",
        "video_title": "LifeNex – Deine Form und dein Training mit der Apple Watch",
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

# Immagini App Store (pubblicazione/Marketing/build.py, ordine galleria): titolo, sottotitolo.
STORE_SHOTS = {
    "it": [
        ("La tua forma, a colpo d'occhio", "Anni di dati Salute trasformati in segnali chiari, ogni giorno."),
        ("Tutta la tua storia sportiva, a confronto", "Ritrova ogni sessione e confronta le tue prestazioni."),
        ("Sfida il te stesso di ieri", "Confronta due sessioni sullo stesso percorso."),
        ("Due sessioni, una sfida", "Rivedi come hai corso, fianco a fianco in 3D."),
        ("Rivivi ogni percorso in 3D", "Il tuo allenamento, sul paesaggio dove l'hai fatto."),
        ("Allenati con equilibrio", "Il carico di ogni settimana, confrontato con il tuo ritmo."),
        ("Obiettivi che ti motivano", "Scegli il risultato, LifeNex ti mostra i progressi."),
        ("Capisci cosa sta cambiando", "Trend chiari su allenamento, cuore e corpo."),
        ("La tua evoluzione, spiegata", "L'analisi AI legge i tuoi dati e racconta i tuoi progressi."),
    ],
    "en": [
        ("Your fitness, at a glance", "Years of Health data turned into clear signals, every day."),
        ("Your whole sports history, compared", "Find every session and compare your performance."),
        ("Beat yesterday's you", "Compare two sessions on the same route."),
        ("Two sessions, one race", "See how you ran, side by side in 3D."),
        ("Relive every route in 3D", "Your workout, on the landscape where it happened."),
        ("Train with balance", "Every week's load, compared with your usual rhythm."),
        ("Goals that keep you going", "Pick the result, LifeNex shows your progress."),
        ("See what's changing", "Clear trends on training, heart and body."),
        ("Your progress, explained", "AI reads your data and tells your story."),
    ],
    "fr": [
        ("Votre forme, en un coup d'œil", "Des années de données Santé en signaux clairs, chaque jour."),
        ("Toute votre histoire sportive, comparée", "Retrouvez chaque séance et comparez vos performances."),
        ("Défiez celui que vous étiez hier", "Comparez deux séances sur le même parcours."),
        ("Deux séances, un défi", "Revoyez votre course, côte à côte en 3D."),
        ("Revivez chaque parcours en 3D", "Votre entraînement, sur le paysage où vous l'avez fait."),
        ("Entraînez-vous avec équilibre", "La charge de chaque semaine, comparée à votre rythme."),
        ("Des objectifs qui motivent", "Choisissez le résultat, LifeNex montre vos progrès."),
        ("Comprenez ce qui change", "Des tendances claires sur l'entraînement, le cœur et le corps."),
        ("Votre évolution, expliquée", "L'IA lit vos données et raconte vos progrès."),
    ],
    "de": [
        ("Deine Form auf einen Blick", "Jahre an Health-Daten, jeden Tag klar erklärt."),
        ("Alle Einheiten im Vergleich", "Finde jede Einheit und vergleiche deine Leistung."),
        ("Fordere dein Ich von gestern", "Vergleiche zwei Einheiten auf derselben Strecke."),
        ("Zwei Einheiten, ein Duell", "Sieh, wie du gelaufen bist – Seite an Seite in 3D."),
        ("Erlebe jede Strecke in 3D", "Dein Training auf der Landschaft, in der es stattfand."),
        ("Trainiere ausgewogen", "Die Belastung jeder Woche, verglichen mit deinem Rhythmus."),
        ("Ziele, die motivieren", "Wähle dein Ziel, LifeNex zeigt deinen Fortschritt."),
        ("Verstehe, was sich ändert", "Klare Trends zu Training, Herz und Körper."),
        ("Deine Entwicklung, erklärt", "Die KI liest deine Daten und erzählt deine Fortschritte."),
    ],
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
    blocks = []
    for i, (title, body) in enumerate(STORE_SHOTS[lang], start=1):
        src = f"{a}store/{prefix}-{i}.jpg"
        blocks.append(
            f"""        <figure class="shot">
          <a class="shot-frame" href="{src}"><img src="{src}" alt="{title}" loading="lazy"></a>
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
  <link rel="stylesheet" href="{CSS[lang]}?v=5">
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
          <a href="terms/">{c['nav_terms']}</a>
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

  <section class="section video-section" id="video">
    <div class="section-inner">
      <h2>{c['video_h2']}</h2>
      <p class="sub">{c['video_sub']}</p>
      <div class="video-frame">
        <iframe src="https://www.youtube-nocookie.com/embed/{c['video_id']}?rel=0" title="{c['video_title']}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
        <a href="terms/">{c['nav_terms']}</a> ·
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
        "meta": 'Titolare: Stefano Toncelli · Contatto: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Ultimo aggiornamento: 5 ottobre 2026',
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
    <p><strong>Analisi intelligente con AI (opzionale):</strong> solo se attivi il consenso «Lettura intelligente» in Preferenze e chiedi tu una lettura (Genera / Aggiorna), LifeNex invia <strong>riassunti numerici già calcolati in app</strong> (medie, conteggi, confronti, tipi di allenamento) per preparare il testo. Non partono tracciati GPS, foto né la cronologia grezza di Salute. Puoi revocare il consenso in qualsiasi momento.</p>
    <p>Questi riassunti sono trattati da:</p>
    <ul>
      <li><strong>il nostro server</strong> (Google Firebase, regione Unione Europea), che inoltra la richiesta e conta le analisi usate: non conserva i riassunti né i testi generati;</li>
      <li><strong>OpenAI</strong>, fornitore del modello di intelligenza artificiale, che genera il testo per nostro conto. Riceve solo il testo dei riassunti, senza identificativi dell’abbonamento o del dispositivo. Secondo le condizioni del suo servizio API, OpenAI non usa questi dati per addestrare i propri modelli e può conservarli per un periodo limitato (fino a 30 giorni) solo per prevenire abusi.</li>
    </ul>
    <p>Le letture generate restano salvate sul tuo iPhone.</p>
    <p><strong>Mappe e rilievo:</strong> per mostrare i percorsi l’app scarica le immagini della mappa da Apple Mappe e, nelle viste 3D, le quote del terreno della zona dal servizio pubblico Terrain Tiles (Amazon Web Services, AWS Open Data). Queste richieste indicano solo l’area di mappa da scaricare (riquadri di alcuni chilometri), non il tracciato GPS, i tempi o altri dati di Salute, e non sono collegate a te; come per qualsiasi sito web, il fornitore vede l’indirizzo IP della connessione. Le quote scaricate restano in cache sul tuo iPhone.</p>
    <h2>Cosa non facciamo</h2>
    <ul><li>non vendiamo i tuoi dati</li><li>non usiamo i dati Salute per pubblicità o tracking tra app</li><li>non condividiamo dati sanitari con terze parti a scopo commerciale</li></ul>
    <h2>Conservazione e cancellazione</h2>
    <p>I dati restano sul dispositivo finché l’app è installata. Per cancellarli: elimina LifeNex e, in Impostazioni → Salute → Accesso app e dati, revoca l’accesso.</p>
    <p>Sul nostro server restano solo i <strong>contatori delle analisi AI</strong> per periodo di abbonamento, legati all’identificativo dell’abbonamento Apple e a un identificativo anonimo del dispositivo, insieme ad alcuni dati tecnici dell’ultimo dispositivo usato (modello di iPhone, versione di iOS, versione dell’app e paese dello store App Store) che ci servono per l’assistenza e per capire quali versioni sono in uso: nessun dato di salute. Per farli cancellare scrivi al contatto qui sotto.</p>
    <h2>Permessi</h2>
    <p>Puoi rifiutare o revocare i permessi Salute in qualsiasi momento. Senza permessi l’app funziona in modo limitato.</p>
    <h2>Minori</h2>
    <p>LifeNex non è destinata a bambini. Non raccogliamo consapevolmente dati di minori.</p>
    <h2>Abbonamenti</h2>
    <p>Gli abbonamenti Plus e Max sono gestiti da Apple tramite l’App Store. LifeNex legge lo stato dell’abbonamento per sbloccare funzioni e quote di analisi intelligente e invia al nostro server la prova d’acquisto firmata da Apple (identificativo della transazione, prodotto, date) per verificare l’abbonamento e contare le analisi. LifeNex non riceve né conserva dati di pagamento.</p>
    <h2>Modifiche</h2>
    <p>Se cambierà il modo in cui trattiamo i dati, aggiorneremo questa pagina <strong>prima</strong> che la modifica arrivi nell’app.</p>
    <p>Per domande: <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "en": {
        "title": "Privacy — LifeNex",
        "h1": "Privacy policy",
        "meta": 'Controller: Stefano Toncelli · Contact: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Last updated: 5 October 2026',
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
    <p>Health data stays <strong>on your iPhone</strong> (local storage). There is no mandatory LifeNex account.</p>
    <p><strong>Optional AI analysis:</strong> only if you turn on the «Smart reading» consent in Settings and request a reading yourself (Generate / Update), LifeNex sends <strong>numeric summaries already computed in the app</strong> (averages, counts, comparisons, workout types) to prepare the text. GPS tracks, photos and raw Health history are never sent. You can withdraw consent at any time.</p>
    <p>These summaries are processed by:</p>
    <ul>
      <li><strong>our server</strong> (Google Firebase, European Union region), which forwards the request and counts the analyses used: it does not keep the summaries or the generated texts;</li>
      <li><strong>OpenAI</strong>, the AI model provider, which generates the text on our behalf. It receives only the summary text, without subscription or device identifiers. Under its API terms, OpenAI does not use this data to train its models and may keep it for a limited time (up to 30 days) only to prevent abuse.</li>
    </ul>
    <p>Generated readings stay saved on your iPhone.</p>
    <p><strong>Maps and terrain:</strong> to show your routes the app downloads map imagery from Apple Maps and, in 3D views, terrain elevation for the area from the public Terrain Tiles service (Amazon Web Services, AWS Open Data). These requests only specify the map area to download (tiles a few kilometres wide), not your GPS track, times or any other Health data, and they are not linked to you; as with any website, the provider sees the IP address of the connection. Downloaded elevation data stays cached on your iPhone.</p>
    <h2>What we do not do</h2>
    <ul><li>we do not sell your data</li><li>we do not use Health data for advertising or cross-app tracking</li><li>we do not share health data with third parties for commercial purposes</li></ul>
    <h2>Retention and deletion</h2>
    <p>Data stays on the device while the app is installed. To delete it, remove LifeNex and revoke access in Settings → Health → Data Access &amp; Devices.</p>
    <p>Our server keeps only the <strong>AI analysis counters</strong> per subscription period, linked to the Apple subscription identifier and to an anonymous device identifier, together with some technical data about the last device used (iPhone model, iOS version, app version and App Store country) that we need for support and to see which versions are in use: no health data. To have them deleted, write to the contact below.</p>
    <h2>Permissions</h2>
    <p>You can refuse or revoke Health permissions at any time. Without permissions the app works in a limited way.</p>
    <h2>Children</h2>
    <p>LifeNex is not intended for children. We do not knowingly collect data from minors.</p>
    <h2>Subscriptions</h2>
    <p>Plus and Max subscriptions are managed by Apple through the App Store. LifeNex reads the subscription status to unlock features and smart analysis quotas, and sends our server the purchase proof signed by Apple (transaction identifier, product, dates) to verify the subscription and count analyses. LifeNex does not receive or store payment data.</p>
    <h2>Changes</h2>
    <p>If the way we process data changes, we will update this page <strong>before</strong> the change reaches the app.</p>
    <p>Questions: <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "fr": {
        "title": "Confidentialité — LifeNex",
        "h1": "Politique de confidentialité",
        "meta": 'Responsable : Stefano Toncelli · Contact : <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Dernière mise à jour : 5 octobre 2026',
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
    <p>Les données Santé restent <strong>sur votre iPhone</strong> (stockage local). Aucun compte LifeNex n’est obligatoire.</p>
    <p><strong>Analyse par IA (facultative) :</strong> uniquement si vous activez le consentement « Lecture intelligente » dans Préférences et demandez vous-même une lecture (Générer / Mettre à jour), LifeNex envoie des <strong>résumés chiffrés déjà calculés dans l’app</strong> (moyennes, comptages, comparaisons, types de séances) pour préparer le texte. Aucun tracé GPS, aucune photo ni l’historique brut de Santé ne sont envoyés. Vous pouvez retirer votre consentement à tout moment.</p>
    <p>Ces résumés sont traités par :</p>
    <ul>
      <li><strong>notre serveur</strong> (Google Firebase, région Union européenne), qui transmet la demande et compte les analyses utilisées : il ne conserve ni les résumés ni les textes générés ;</li>
      <li><strong>OpenAI</strong>, fournisseur du modèle d’intelligence artificielle, qui génère le texte pour notre compte. Il reçoit uniquement le texte des résumés, sans identifiant d’abonnement ni d’appareil. Selon les conditions de son service API, OpenAI n’utilise pas ces données pour entraîner ses modèles et peut les conserver pendant une durée limitée (jusqu’à 30 jours) uniquement pour prévenir les abus.</li>
    </ul>
    <p>Les lectures générées restent enregistrées sur votre iPhone.</p>
    <p><strong>Cartes et relief :</strong> pour afficher vos parcours, l’app télécharge les images de carte depuis Plans d’Apple et, dans les vues 3D, l’altitude du terrain de la zone depuis le service public Terrain Tiles (Amazon Web Services, AWS Open Data). Ces requêtes indiquent uniquement la zone de carte à télécharger (des tuiles de quelques kilomètres), pas votre tracé GPS, vos horaires ni d’autres données Santé, et ne sont pas liées à vous ; comme pour tout site web, le fournisseur voit l’adresse IP de la connexion. Les altitudes téléchargées restent en cache sur votre iPhone.</p>
    <h2>Ce que nous ne faisons pas</h2>
    <ul><li>nous ne vendons pas vos données</li><li>nous n’utilisons pas les données Santé pour la publicité ou le suivi entre apps</li><li>nous ne partageons pas de données de santé avec des tiers à des fins commerciales</li></ul>
    <h2>Conservation et suppression</h2>
    <p>Les données restent sur l’appareil tant que l’app est installée. Pour les supprimer, supprimez LifeNex et révoquez l’accès dans Réglages → Santé → Accès aux données et appareils.</p>
    <p>Notre serveur conserve uniquement les <strong>compteurs d’analyses IA</strong> par période d’abonnement, liés à l’identifiant de l’abonnement Apple et à un identifiant anonyme de l’appareil, ainsi que quelques données techniques du dernier appareil utilisé (modèle d’iPhone, version d’iOS, version de l’app et pays de l’App Store) dont nous avons besoin pour l’assistance et pour savoir quelles versions sont utilisées : aucune donnée de santé. Pour les faire supprimer, écrivez au contact ci-dessous.</p>
    <h2>Autorisations</h2>
    <p>Vous pouvez refuser ou révoquer les autorisations Santé à tout moment. Sans autorisations, l’app fonctionne de façon limitée.</p>
    <h2>Mineurs</h2>
    <p>LifeNex n’est pas destinée aux enfants. Nous ne collectons pas sciemment de données de mineurs.</p>
    <h2>Abonnements</h2>
    <p>Les abonnements Plus et Max sont gérés par Apple via l’App Store. LifeNex lit l’état de l’abonnement pour débloquer des fonctions et des quotas d’analyse intelligente, et envoie à notre serveur la preuve d’achat signée par Apple (identifiant de transaction, produit, dates) pour vérifier l’abonnement et compter les analyses. LifeNex ne reçoit ni ne conserve de données de paiement.</p>
    <h2>Modifications</h2>
    <p>Si notre façon de traiter les données change, nous mettrons cette page à jour <strong>avant</strong> que la modification arrive dans l’app.</p>
    <p>Questions : <a href="mailto:support@lifenex.it">support@lifenex.it</a></p>
""",
    },
    "de": {
        "title": "Datenschutz — LifeNex",
        "h1": "Datenschutzerklärung",
        "meta": 'Verantwortlich: Stefano Toncelli · Kontakt: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Stand: 5. Oktober 2026',
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
    <p>Health-Daten bleiben <strong>auf deinem iPhone</strong> (lokaler Speicher). Ein LifeNex-Konto ist nicht nötig.</p>
    <p><strong>KI-Analyse (optional):</strong> nur wenn du in den Einstellungen die Einwilligung «Intelligente Lesung» aktivierst und selbst eine Auswertung anforderst (Erstellen / Aktualisieren), sendet LifeNex <strong>bereits in der App berechnete Zahlenzusammenfassungen</strong> (Mittelwerte, Zählungen, Vergleiche, Trainingsarten), um den Text zu erstellen. GPS-Routen, Fotos und der Health-Rohverlauf werden nie gesendet. Du kannst die Einwilligung jederzeit widerrufen.</p>
    <p>Diese Zusammenfassungen werden verarbeitet von:</p>
    <ul>
      <li><strong>unserem Server</strong> (Google Firebase, Region Europäische Union), der die Anfrage weiterleitet und die genutzten Analysen zählt: Er speichert weder die Zusammenfassungen noch die erzeugten Texte;</li>
      <li><strong>OpenAI</strong>, dem Anbieter des KI-Modells, der den Text in unserem Auftrag erzeugt. OpenAI erhält nur den Text der Zusammenfassungen, ohne Abo- oder Gerätekennungen. Laut den Bedingungen seines API-Dienstes nutzt OpenAI diese Daten nicht zum Training seiner Modelle und kann sie für begrenzte Zeit (bis zu 30 Tage) ausschließlich zur Missbrauchsverhinderung aufbewahren.</li>
    </ul>
    <p>Erzeugte Auswertungen bleiben auf deinem iPhone gespeichert.</p>
    <p><strong>Karten und Gelände:</strong> Um deine Routen anzuzeigen, lädt die App Kartenbilder von Apple Karten und in den 3D-Ansichten Geländehöhen der Umgebung vom öffentlichen Dienst Terrain Tiles (Amazon Web Services, AWS Open Data). Diese Anfragen enthalten nur den zu ladenden Kartenbereich (Kacheln von einigen Kilometern), nicht deine GPS-Route, Zeiten oder andere Health-Daten, und sind nicht mit dir verknüpft; wie bei jeder Website sieht der Anbieter die IP-Adresse der Verbindung. Die geladenen Höhendaten bleiben im Cache auf deinem iPhone.</p>
    <h2>Was wir nicht tun</h2>
    <ul><li>wir verkaufen deine Daten nicht</li><li>wir nutzen Health-Daten nicht für Werbung oder App-übergreifendes Tracking</li><li>wir geben Gesundheitsdaten nicht zu kommerziellen Zwecken an Dritte weiter</li></ul>
    <h2>Speicherung und Löschung</h2>
    <p>Die Daten bleiben auf dem Gerät, solange die App installiert ist. Zum Löschen entferne LifeNex und widerrufe den Zugriff unter Einstellungen → Health → Datenzugriff &amp; Geräte.</p>
    <p>Auf unserem Server bleiben nur die <strong>Zähler der KI-Analysen</strong> pro Abo-Zeitraum, verknüpft mit der Kennung des Apple-Abos und einer anonymen Gerätekennung, zusammen mit einigen technischen Daten des zuletzt genutzten Geräts (iPhone-Modell, iOS-Version, App-Version und App-Store-Land), die wir für den Support und zur Übersicht der genutzten Versionen brauchen: keine Gesundheitsdaten. Zum Löschen schreib an den Kontakt unten.</p>
    <h2>Berechtigungen</h2>
    <p>Du kannst Health-Berechtigungen jederzeit verweigern oder widerrufen. Ohne Berechtigungen funktioniert die App nur eingeschränkt.</p>
    <h2>Kinder</h2>
    <p>LifeNex ist nicht für Kinder bestimmt. Wir erheben nicht wissentlich Daten von Minderjährigen.</p>
    <h2>Abonnements</h2>
    <p>Die Abos Plus und Max werden von Apple über den App Store verwaltet. LifeNex liest den Abo-Status, um Funktionen und Kontingente für die intelligente Auswertung freizuschalten, und sendet unserem Server den von Apple signierten Kaufnachweis (Transaktionskennung, Produkt, Daten), um das Abo zu prüfen und Analysen zu zählen. LifeNex erhält und speichert keine Zahlungsdaten.</p>
    <h2>Änderungen</h2>
    <p>Wenn sich die Art der Datenverarbeitung ändert, aktualisieren wir diese Seite, <strong>bevor</strong> die Änderung in die App kommt.</p>
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
          <a href="../terms/">{COPY[lang]['nav_terms']}</a>
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


TERMS = {
    "it": {
        "title": "Termini di utilizzo — LifeNex",
        "h1": "Termini di utilizzo",
        "meta": 'Titolare: Stefano Toncelli · Contatto: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Ultimo aggiornamento: 29 settembre 2026',
        "body": """
    <p>Usando LifeNex accetti questi termini. Se non sei d’accordo, non usare l’app.</p>

    <h2>Cos’è LifeNex</h2>
    <p>LifeNex è un’app iOS di benessere e fitness che <strong>osserva</strong> i dati già presenti in Apple Salute e può <strong>motivarti</strong> rispetto a obiettivi che scegli tu. <strong>Non è un dispositivo medico</strong>: non diagnostica, non cura, non prescrive terapie, farmaci, intensità di allenamento o piani clinici.</p>

    <h2>Licenza d’uso</h2>
    <p>Ti concediamo una licenza personale, non esclusiva e non trasferibile per usare LifeNex sul tuo dispositivo Apple. Non puoi copiare, modificare, distribuire o fare reverse engineering dell’app oltre quanto consentito dalla legge.</p>

    <h2>Apple Salute (HealthKit)</h2>
    <p>L’app legge i dati di Salute solo con il tuo consenso. I dati restano sul dispositivo, salvo le funzioni opzionali che richiedono un’ulteriore autorizzazione (vedi <a href="../privacy/">Informativa privacy</a>).</p>

    <h2>Analisi intelligente (opzionale)</h2>
    <p>Se attivi il consenso in Preferenze e chiedi una lettura, LifeNex può inviare riassunti numerici già calcolati in app a un gateway per produrre un testo. Il servizio ha un tetto di letture per periodo di abbonamento. Non sostituisce un parere professionale.</p>

    <h2>Abbonamenti Plus e Max</h2>
    <ul>
      <li>Acquisti e rinnovi sono gestiti da Apple tramite l’App Store.</li>
      <li>Prezzi e prove gratuite, se presenti, sono quelli mostrati in App Store al momento dell’acquisto.</li>
      <li>Puoi gestire o disdire l’abbonamento in Impostazioni iPhone → Apple ID → Abbonamenti.</li>
      <li>I rimborsi seguono le regole Apple.</li>
      <li>Plus e Max (mensile o annuale) sbloccano funzioni e quote di analisi intelligente come descritto in app.</li>
    </ul>
    <p>Per gli abbonamenti auto-rinnovabili vale anche il <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener noreferrer">Contratto di licenza standard per applicazioni (EULA) di Apple</a>, oltre a questi termini.</p>

    <h2>Responsabilità</h2>
    <p>Non è obbligatorio un account LifeNex. Sei responsabile dell’uso dell’app e delle decisioni che prendi. LifeNex non è responsabile di danni derivanti da un uso non conforme o da dati Salute incompleti o errati.</p>

    <h2>Limitazione di garanzia</h2>
    <p>L’app è fornita «così com’è», nei limiti consentiti dalla legge. Non garantiamo assenza di interruzioni o errori, né risultati di fitness o salute.</p>

    <h2>Modifiche</h2>
    <p>Possiamo aggiornare questi termini. La data in alto indica l’ultima revisione.</p>

    <p>Domande: <a href="mailto:support@lifenex.it">support@lifenex.it</a> · <a href="../privacy/">Privacy</a></p>
""",
    },
    "en": {
        "title": "Terms of use — LifeNex",
        "h1": "Terms of use",
        "meta": 'Controller: Stefano Toncelli · Contact: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Last updated: 29 September 2026',
        "body": """
    <p>By using LifeNex you agree to these terms. If you do not agree, do not use the app.</p>

    <h2>What LifeNex is</h2>
    <p>LifeNex is an iOS wellness and fitness app that <strong>observes</strong> data already in Apple Health and can <strong>motivate</strong> you toward goals you choose. <strong>It is not a medical device</strong>: it does not diagnose, treat, or prescribe therapy, medication, training intensity, or clinical plans.</p>

    <h2>License</h2>
    <p>We grant you a personal, non-exclusive, non-transferable license to use LifeNex on your Apple device. You may not copy, modify, distribute, or reverse-engineer the app beyond what applicable law allows.</p>

    <h2>Apple Health (HealthKit)</h2>
    <p>The app reads Health data only with your consent. Data stays on device except for optional features that need further explicit permission (see the <a href="../privacy/">Privacy policy</a>).</p>

    <h2>Optional smart analysis</h2>
    <p>If you enable consent in Settings and request a reading, LifeNex may send numeric summaries already computed in the app to a gateway to produce text. Usage is capped per subscription period. It does not replace professional advice.</p>

    <h2>Plus and Max subscriptions</h2>
    <ul>
      <li>Purchases and renewals are handled by Apple via the App Store.</li>
      <li>Prices and free trials, if any, are those shown in the App Store at purchase time.</li>
      <li>Manage or cancel in iPhone Settings → Apple ID → Subscriptions.</li>
      <li>Refunds follow Apple’s rules.</li>
      <li>Plus and Max (monthly or yearly) unlock features and AI reading quotas as described in the app.</li>
    </ul>
    <p>Auto-renewable subscriptions are also subject to Apple’s <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener noreferrer">Standard Licensed Application End User License Agreement (EULA)</a>, in addition to these terms.</p>

    <h2>Responsibility</h2>
    <p>No LifeNex account is required. You are responsible for how you use the app and the decisions you make. LifeNex is not liable for damages from non-compliant use or incomplete or inaccurate Health data.</p>

    <h2>Disclaimer</h2>
    <p>The app is provided “as is,” to the extent permitted by law. We do not warrant uninterrupted or error-free operation, or any fitness or health outcomes.</p>

    <h2>Changes</h2>
    <p>We may update these terms. The date above shows the latest revision.</p>

    <p>Questions: <a href="mailto:support@lifenex.it">support@lifenex.it</a> · <a href="../privacy/">Privacy</a></p>
""",
    },
    "fr": {
        "title": "Conditions d’utilisation — LifeNex",
        "h1": "Conditions d’utilisation",
        "meta": 'Responsable : Stefano Toncelli · Contact : <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Dernière mise à jour : 29 septembre 2026',
        "body": """
    <p>En utilisant LifeNex, vous acceptez ces conditions. Sinon, n’utilisez pas l’app.</p>

    <h2>Qu’est-ce que LifeNex</h2>
    <p>LifeNex est une app iOS de bien-être et de fitness qui <strong>observe</strong> les données déjà présentes dans Apple Santé et peut vous <strong>motiver</strong> vers des objectifs que vous choisissez. <strong>Ce n’est pas un dispositif médical</strong> : elle ne diagnostique pas, ne soigne pas et ne prescrit ni thérapies, ni médicaments, ni intensité d’entraînement.</p>

    <h2>Licence</h2>
    <p>Nous vous accordons une licence personnelle, non exclusive et non transférable pour utiliser LifeNex sur votre appareil Apple.</p>

    <h2>Apple Santé (HealthKit)</h2>
    <p>L’app lit les données Santé uniquement avec votre consentement. Les données restent sur l’appareil, sauf fonctions optionnelles avec autorisation supplémentaire (voir la <a href="../privacy/">politique de confidentialité</a>).</p>

    <h2>Analyse intelligente (optionnelle)</h2>
    <p>Si vous activez le consentement et demandez une lecture, LifeNex peut envoyer des résumés numériques déjà calculés dans l’app à une passerelle pour produire un texte. Le service a un plafond par période d’abonnement. Cela ne remplace pas un avis professionnel.</p>

    <h2>Abonnements Plus et Max</h2>
    <ul>
      <li>Achats et renouvellements gérés par Apple via l’App Store.</li>
      <li>Prix et essais affichés dans l’App Store au moment de l’achat.</li>
      <li>Gestion / résiliation : Réglages iPhone → Apple ID → Abonnements.</li>
      <li>Remboursements selon les règles Apple.</li>
    </ul>
    <p>Les abonnements à renouvellement automatique sont aussi soumis à l’<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener noreferrer">EULA standard Apple</a>.</p>

    <h2>Responsabilité</h2>
    <p>Aucun compte LifeNex n’est obligatoire. Vous êtes responsable de l’usage de l’app et de vos décisions.</p>

    <h2>Modifications</h2>
    <p>Nous pouvons mettre à jour ces conditions. La date ci-dessus indique la dernière révision.</p>

    <p>Questions : <a href="mailto:support@lifenex.it">support@lifenex.it</a> · <a href="../privacy/">Confidentialité</a></p>
""",
    },
    "de": {
        "title": "Nutzungsbedingungen — LifeNex",
        "h1": "Nutzungsbedingungen",
        "meta": 'Verantwortlich: Stefano Toncelli · Kontakt: <a href="mailto:support@lifenex.it">support@lifenex.it</a><br>Stand: 29. September 2026',
        "body": """
    <p>Mit der Nutzung von LifeNex akzeptierst du diese Bedingungen. Wenn nicht, verwende die App nicht.</p>

    <h2>Was LifeNex ist</h2>
    <p>LifeNex ist eine iOS-App für Wellness und Fitness, die Daten in Apple Gesundheit <strong>beobachtet</strong> und dich zu selbst gewählten Zielen <strong>motivieren</strong> kann. <strong>Kein Medizinprodukt</strong>: keine Diagnose, Therapie, Medikamente oder Vorgaben zur Trainingsintensität.</p>

    <h2>Lizenz</h2>
    <p>Du erhältst eine persönliche, nicht ausschließliche, nicht übertragbare Lizenz zur Nutzung auf deinem Apple-Gerät.</p>

    <h2>Apple Gesundheit (HealthKit)</h2>
    <p>Die App liest Gesundheitsdaten nur mit deiner Zustimmung. Daten bleiben auf dem Gerät, außer optionale Funktionen mit zusätzlicher Erlaubnis (siehe <a href="../privacy/">Datenschutzerklärung</a>).</p>

    <h2>Optionale intelligente Analyse</h2>
    <p>Mit Zustimmung in den Einstellungen und auf Anfrage kann LifeNex bereits berechnete Zahlenzusammenfassungen an ein Gateway senden. Es gibt ein Kontingent pro Abo-Zeitraum. Kein Ersatz für fachlichen Rat.</p>

    <h2>Abos Plus und Max</h2>
    <ul>
      <li>Käufe und Verlängerungen über den App Store von Apple.</li>
      <li>Preise und Testphasen wie im App Store zum Kaufzeitpunkt angezeigt.</li>
      <li>Verwalten/kündigen: iPhone-Einstellungen → Apple-ID → Abonnements.</li>
      <li>Erstattungen nach Apple-Regeln.</li>
    </ul>
    <p>Für Auto-Renew-Abos gilt zusätzlich Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener noreferrer">Standard-EULA</a>.</p>

    <h2>Verantwortung</h2>
    <p>Kein LifeNex-Konto erforderlich. Du bist für die Nutzung der App und deine Entscheidungen verantwortlich.</p>

    <h2>Änderungen</h2>
    <p>Wir können diese Bedingungen aktualisieren. Das Datum oben zeigt die letzte Fassung.</p>

    <p>Fragen: <a href="mailto:support@lifenex.it">support@lifenex.it</a> · <a href="../privacy/">Datenschutz</a></p>
""",
    },
}


def terms_html(lang: str) -> str:
    t = TERMS[lang]
    p = PRIVACY[lang]
    codes = ("it", "en", "fr", "de")
    if lang == "it":
        asset = "../assets/"
        css = "../styles.css"
        hrefs = {code: "./" if code == "it" else f"../{code}/terms/" for code in codes}
    else:
        asset = "../../assets/"
        css = "../../styles.css"
        hrefs = {code: "./" if code == lang else ("../../terms/" if code == "it" else f"../../{code}/terms/") for code in codes}
    active = ' class="active"'
    links = "\n".join(
        f'          <a href="{hrefs[code]}"{active if code == lang else ""}>{code.upper()}</a>'
        for code in codes
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t['title']}</title>
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
      <a class="brand" href="../">
        <img src="{asset}app-icon.png" alt="" width="36" height="36">
        LifeNex
      </a>
      <div class="header-right">
        <nav class="nav-links" aria-label="Main">
          <a href="../">{COPY[lang]['nav_home']}</a>
          <a href="../privacy/">{p['nav']}</a>
          <a class="active" href="./">{COPY[lang]['nav_terms']}</a>
          <a href="mailto:support@lifenex.it">{p['contact']}</a>
        </nav>
        <div class="lang-switch" aria-label="Language">
{links}
        </div>
      </div>
    </div>
  </header>
  <article class="legal-page">
    <h1>{t['h1']}</h1>
    <p class="legal-meta">{t['meta']}</p>
{t['body']}  </article>
  <footer class="site-footer">
    <div class="footer-inner">
      <span>© 2026 LifeNex</span>
      <a href="../">{p['back']}</a>
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

        tpath = (ROOT if lang == "it" else ROOT / lang) / "terms" / "index.html"
        tpath.parent.mkdir(parents=True, exist_ok=True)
        tpath.write_text(terms_html(lang))
        print("wrote", tpath)


if __name__ == "__main__":
    main()
