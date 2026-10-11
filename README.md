# LifeNex website

Sito ufficiale di LifeNex in quattro lingue (IT, EN, FR, DE), pubblicato con GitHub Pages su **https://lifenex.it**.

## Pagine

| | IT | EN | FR | DE |
|--|----|----|----|----|
| Home | [/](https://lifenex.it/) | [/en/](https://lifenex.it/en/) | [/fr/](https://lifenex.it/fr/) | [/de/](https://lifenex.it/de/) |
| Privacy | [/privacy/](https://lifenex.it/privacy/) | [/en/privacy/](https://lifenex.it/en/privacy/) | [/fr/privacy/](https://lifenex.it/fr/privacy/) | [/de/privacy/](https://lifenex.it/de/privacy/) |
| Termini | [/terms/](https://lifenex.it/terms/) | [/en/terms/](https://lifenex.it/en/terms/) | [/fr/terms/](https://lifenex.it/fr/terms/) | [/de/terms/](https://lifenex.it/de/terms/) |

Le pagine italiane alla radice reindirizzano a `/en/`, `/fr/` o `/de/` in base alla lingua del browser; la scelta fatta con il selettore lingua viene ricordata.

## Modificare i testi

Le pagine HTML sono generate: non modificarle a mano.

1. Cambia i testi in `scripts/generate_pages.py` (`COPY` per i testi delle pagine, `SHOTS` per le didascalie delle schermate).
2. Rigenera: `python3 scripts/generate_pages.py`
3. Controlla `git diff`, poi commit e push su `main`: GitHub Pages pubblica in circa un minuto.

## Struttura

- `index.html`, `en/`, `fr/`, `de/`: home, privacy e termini per lingua (generati)
- `styles.css`, `lightbox.js`: stile e visualizzazione delle schermate
- `assets/`: icona, badge App Store, schermate (`screenshots/`, `store/`)
- `CNAME`: dominio personalizzato `lifenex.it`

## Dominio

Il DNS di `lifenex.it` (gestito su Aruba) punta a GitHub Pages con i record **A** `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. HTTPS è gestito da GitHub (Settings → Pages).
