#!/usr/bin/env python3
import argparse
from core.scanner import PortScanner

def main():
    parser = argparse.ArgumentParser(description="TraceX - Network Tracer")
    parser.add_argument("--target", required=True, help="IP/Domain to scan")
    parser.add_argument("--ports", default="1-1024", help="Port range (e.g. 20-80)")
    args = parser.parse_args()

    scanner = PortScanner(args.target)
    print(f"[*] Scanning {args.target}...")
    
    # Ejemplo básico (implementar rango completo)
    result = scanner.scan_port(80)
    if result:
        print(f"Port {result['port']} ({result['service']}) is OPEN")

if __name__ == "__main__":
    main()
