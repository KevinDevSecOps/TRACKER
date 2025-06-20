import requests
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class GeoIPData:
    country: str
    city: str
    isp: str

class GeoIPLocator:
    """Obtiene datos de geolocalización usando IPAPI"""
    
    API_URL = "http://ip-api.com/json/{ip}?fields=country,city,isp"
    
    def locate(self, ip: str) -> Optional[GeoIPData]:
        try:
            response = requests.get(self.API_URL.format(ip=ip), timeout=3)
            data = response.json()
            return GeoIPData(
                country=data.get("country", "Unknown"),
                city=data.get("city", "Unknown"),
                isp=data.get("isp", "Unknown")
            )
        except Exception as e:
            print(f"[!] Error en geolocalización: {e}")
            return None
