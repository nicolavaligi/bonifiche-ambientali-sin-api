#!/usr/bin/env python3
"""
Example script for querying the Houdinick Remediation & Brownfield API.
Get your production API key at: https://rapidapi.com/nvaligi/api/houdinick-remediation-api
"""
import os
import json
import urllib.request
import urllib.parse

# Default to demo key if RAPIDAPI_KEY is not set in environment
API_KEY = os.environ.get("RAPIDAPI_KEY", "hn_remediation_test_key_001")
BASE_URL = "https://houdinick-remediation-api-production.up.railway.app/api/v1/feed"

def fetch_remediation_sites(category="sin", location="Lombardia", limit=5):
    params = {
        "category": category,
        "location": location,
        "limit": str(limit),
    }
    query_string = urllib.parse.urlencode({k: v for k, v in params.items() if v})
    full_url = f"{BASE_URL}?{query_string}"
    
    headers = {
        "User-Agent": "Houdinick-Remediation-Client/1.0",
        "X-API-Key": API_KEY,
    }
    
    print("Fetching from Houdinick Remediation & Brownfield API...")
    print(f"URL: {full_url}\n")
    req = urllib.request.Request(full_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("items", [])
            print(f"✅ Success! Retrieved {len(items)} remediation sites (Total matching in DB: {data.get('count', 0)}):\n")
            for item in items:
                p = item.get("payload", {})
                title = item.get("title", "")
                ha = p.get("superficie_ha", "N/A")
                mq = p.get("superficie_mq", 0)
                matrices = ", ".join(p.get("matrice_contaminata", []))
                pollutants = ", ".join(p.get("contaminanti_principali", []))
                solar_ok = "✅ SÌ" if p.get("area_idonea_fotovoltaico") else "❌ NO"
                competent = p.get("ente_competente", "N/A")
                status = item.get("value_text", "N/A")
                
                print(f"🏭 {title} ({item.get('location')})")
                print(f"   Stato Procedura   : {status}")
                print(f"   Superficie        : {ha} ha ({mq:,.0f} mq)")
                print(f"   Matrici Critiche  : {matrices}")
                print(f"   Contaminanti      : {pollutants}")
                print(f"   Idonea Solare     : {solar_ok}")
                print(f"   Ente Competente   : {competent}")
                print("-" * 65)
                
            print(f"\nNext cursor for delta updates: since_seq={data.get('next_seq')}")
            print("Get full high-concurrency access at: https://rapidapi.com/nvaligi/api/houdinick-remediation-api")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_remediation_sites()
