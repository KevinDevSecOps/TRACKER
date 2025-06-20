# 👥 Guía para Contribuir a TRACKER

¡Gracias por interesarte en mejorar TRACKER! Este proyecto se nutre de la comunidad de seguridad. Sigue estos pasos:

## 🛠️ **Primeros Pasos**
1. **Haz fork** del repositorio
2. **Clona tu fork**:
   ```bash
   git clone https://github.com/tu-usuario/TRACKER.git
   cd TRACKER
   ```
3. **Configura el entorno**:
   ```bash
   pip install -e .[dev]  # Instala dependencias de desarrollo
   pre-commit install  # Hooks para calidad de código
   ```

## 🎯 **¿Cómo Contribuir?**
### 🐛 Reportar Bugs
1. Verifica que no exista ya en [Issues](https://github.com/KevinDevSecOps/TRACKER/issues)
2. Usa la plantilla de bug report e incluye:
   - Comando exacto que ejecutaste
   - Output esperado vs. real
   - Capturas de pantalla (opcional)

### 💡 Sugerir Mejoras
1. Abre un Issue con la etiqueta `enhancement`
2. Describe:
   - El caso de uso concreto
   - Beneficios para la comunidad pentesting

### 📦 Enviar Código
1. Crea una rama descriptiva:
   ```bash
   git checkout -b feat/nombre-funcionalidad
   ```
2. Sigue los estándares:
   - Type hints en Python
   - Docstrings Google Style
   - Tests para código nuevo
3. Envía tu PR con:
   - Descripción clara de los cambios
   - Referencia al Issue relacionado (si aplica)

## 🧪 **Testing**
Corre los tests antes de enviar PR:
```bash
pytest -v tests/ --cov=core/  # Con cobertura
```

## 📜 **Estándares de Código**
- **Python**: Black + Flake8
- **Commits**: Mensajes en inglés, estilo Conventional Commits
- **Documentación**: Actualiza README.md para nuevas features

## 💬 ¿Dudas?
Únete a nuestro [Discord](https://discord.gg/tu-enlace) o menciona a @KevinDevSecOps en Issues.

¡Tu contribución aparecerá en los créditos del proyecto! 🎉
```
