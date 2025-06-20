from scapy.all import sr1, IP, TCP
from typing import Optional

class StealthScanner:
    """Escaneo SYN para evadir detección básica"""
    
    @staticmethod
    def syn_scan(target: str, port: int, timeout: int = 2) -> bool:
        """
        Realiza escaneo SYN (half-open)
        Returns:
            bool: True si el puerto está abierto
        """
        packet = IP(dst=target)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=timeout, verbose=0)
        
        if response is None:
            return False
            
        return (
            response.haslayer(TCP) and 
            response.getlayer(TCP).flags == 0x12  # SYN-ACK
        )
