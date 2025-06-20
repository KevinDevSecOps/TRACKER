# Configura pyproject.toml (Python moderno)
cat <<EOF > pyproject.toml
[project]
name = "TraceX"
version = "0.1.0"
description = "Advanced Network Tracer"
requires-python = ">=3.10"
dependencies = [
    "scapy>=2.4.5",
    "requests>=2.28.0",
    "python-nmap>=0.7.1"
]

[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"
EOF
