# LifeNex website

Sito ufficiale LifeNex (IT + EN) per App Store Connect.

## URL attivi (GitHub Pages)

| | IT | EN |
|--|----|----|
| Home | https://stefton71.github.io/lifenex-site/ | https://stefton71.github.io/lifenex-site/en/ |
| Privacy | https://stefton71.github.io/lifenex-site/privacy/ | https://stefton71.github.io/lifenex-site/en/privacy/ |

## Dominio lifenex.it

Oggi il DNS punta ad **Aruba** (parcheggio IIS). Per usare `https://lifenex.it/privacy`:

1. Pannello Aruba → DNS del dominio `lifenex.it`
2. Rimuovi/sostituisci il record **A** su `62.149.128.40`
3. Imposta record **A** apex verso GitHub Pages:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
4. (Opzionale) `www` → CNAME `stefton71.github.io`
5. In questo repo riaggiungi file `CNAME` con contenuto `lifenex.it`
6. GitHub → Settings → Pages → Custom domain → verifica HTTPS

Finché il DNS non è cambiato, in App Store Connect usa gli URL **github.io** sopra.
