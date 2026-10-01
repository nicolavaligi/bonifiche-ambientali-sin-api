# Italian Environmental Remediation & Brownfield Feed (REST API)

[![RapidAPI Hub](https://img.shields.io/badge/RapidAPI-Houdinick%20Remediation%20API-blueviolet.svg)](https://rapidapi.com/nvaligi/api/houdinick-remediation-api)
[![Status](https://img.shields.io/badge/Status-Operational%20(200%20OK)-brightgreen.svg)](https://houdinick-remediation-api-production.up.railway.app/health)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Feed programmatico in tempo reale per la mappatura e il monitoraggio dei **Siti di Interesse Nazionale (SIN), Siti di Interesse Regionale (SIR) e Brownfield PNRR** in Italia.

Progettato per **Sviluppatori Fotovoltaico (Aree Idonee ex D.Lgs. 199/2021), Imprese di Bonifica Ambientale, Fondi Infrastrutturali e Studi di Ingegneria Ambientale**.

---

## Casi d'Uso Chiave

1. **Sviluppo Rinnovabili (Aree Idonee):** Identifica rapidamente ex discariche, poli chimici dismessi, cave e siti industriali bonificati idonei per autorizzazioni accelerate (PAS/AU) di impianti fotovoltaici a terra e agrivoltaici.
2. **Business Development Imprese di Bonifica:** Monitora lo stato di avanzamento delle procedure di bonifica (Piano di Caratterizzazione, Progetto Operativo di Bonifica POB, Messa in Sicurezza di Emergenza MISE).
3. **Due Diligence Ambientale & ESG:** Verifica la presenza di matrici contaminate (suolo, falda, sedimenti) e contaminanti critici (PCB, Idrocarburi, Metalli pesanti, PFAS) prima dell'acquisizione di terreni e complessi industriali.

---

## Dati Chiave Restituiti dall'API

- **Dati Geografici:** Comune, Provincia, Regione, Coordinate GPS (`lat`, `lng`).
- **Superficie:** Estensione in ettari (`superficie_ha`) e metri quadri (`superficie_mq`).
- **Matrici Contaminate:** Elenco completo (`suolo`, `sottosuolo`, `falda_acquifera`, `sedimenti`).
- **Contaminanti Principali:** Es. PCB, Diossine, Mercurio, Arsenico, Solventi clorurati, Benzene, Idrocarburi C>12.
- **Idoneità Rinnovabili:** Flag booleano `area_idonea_fotovoltaico` e valutazione tecnica del potenziale di repowering.
- **Quadro Giuridico:** Riferimento normativo (Decreti Ministeriali MASE, L. 426/1998, Titolo V D.Lgs. 152/2006) ed Ente Competente (MASE, ARPA regionale).
- **Cursore Delta (`since_seq`):** Interrogazione differenziale per sincronizzare solo i record aggiornati.

---

## Quickstart Python (Pronto all'Uso)

Esegui direttamente con Python 3 standard (nessuna libreria esterna richiesta):

```python
import urllib.request
import json

# Ottieni la tua chiave su RapidAPI Hub: https://rapidapi.com/nvaligi/api/houdinick-remediation-api
API_KEY = "TUA_CHIAVE_RAPIDAPI"

# Cerca siti SIN idonei al fotovoltaico in Lombardia
url = "https://houdinick-remediation-api-production.up.railway.app/api/v1/feed?category=sin&location=Lombardia&limit=5"
req = urllib.request.Request(url, headers={"X-API-Key": API_KEY})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    for site in data["items"]:
        p = site["payload"]
        print(f"[{site['source_id']}] {site['title']}")
        print(f"  Superficie: {p['superficie_ha']} ha | Idonea Solare: {p['area_idonea_fotovoltaico']}")
        print(f"  Contaminanti: {', '.join(p['contaminanti_principali'][:3])}")
        print(f"  Ente: {p['ente_competente']}")
        print("-" * 50)
```

---

## cURL

```bash
curl -X GET "https://houdinick-remediation-api-production.up.railway.app/api/v1/feed?category=sin&limit=5" \
  -H "X-API-Key: TUA_CHIAVE_RAPIDAPI"
```

---

## Piani Tariffari & Accesso Self-Serve

Il servizio è monetizzato e distribuito tramite **RapidAPI Hub**:

| Piano | Prezzo | Quota Inclusa | Costo Chiamata Extra | Accesso |
|---|---|---|---|---|
| **Basic (Free)** | **$0.00 / mese** | 50 chiamate / mese | $0.10 / chiamata | [👉 Attiva su RapidAPI](https://rapidapi.com/nvaligi/api/houdinick-remediation-api) |
| **Pro** | **$49.00 / mese** | 2,000 chiamate / mese | $0.05 / chiamata | [👉 Attiva su RapidAPI](https://rapidapi.com/nvaligi/api/houdinick-remediation-api) |

---

## SDK Ufficiale & Documentazione Completa

Visita il repository principale Houdinick con il client Python e le altre API (Appalti Pubblici e Fotovoltaico):  
👉 **[github.com/nicolavaligi/houdinick-data-feeds](https://github.com/nicolavaligi/houdinick-data-feeds)**  
👉 **[Landing Page Ufficiale](https://nicolavaligi.github.io/houdinick-data-feeds/)**

---

## Licenza

Distribuito sotto licenza [MIT](LICENSE). Copyright © 2026 Houdinick.
