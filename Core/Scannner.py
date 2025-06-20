#!/usr/bin/env python3
from typing import Optional, Dict, List
import socket
import requests

class PortScanner:
    """Escaneo de puertos con detección de servicios"""
    
    def __init__(self, target: str, stealth: bool = False):
        self.target = target
        self.stealth = stealth
    
    def scan_port(self, port: int) -> Optional[Dict]:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1 if self.stealth else 0.5)
                if s.connect_ex((self.target, port)) == 0:
                    service = self._get_service(port)
                    return {"port": port, "status": "open", "service": service}
        except Exception:
            return None
    
    def _get_service(self, port: int) -> str:
        # Mapeo básico (ampliable)
        services = {
            22: "SSH",
            80: "HTTP",
            443: "HTTPS"
        }
        return services.get(port, "unknown")
