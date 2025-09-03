# Scraping Profesional — Playwright · Requests · Selenium/ChromeDriver

Repositorio de prácticas del curso **Scraping Ético y Profesional**. Reúne *notebooks* y scripts que cubren:
- Navegación y extracción con **Playwright** (headless y no headless).
- Uso de **Selenium** con **ChromeDriver** para páginas dinámicas y login.
- Buenas prácticas: respeto de **robots.txt**, *rate limiting*, *backoff* y limpieza de sesiones.

> **Ética primero**: respeta ToS, `robots.txt` y la legislación local. No satures servidores ni extraigas datos sensibles.

---

## 📂 Contenidos del repo

| Archivo / Carpeta | Tipo | Descripción |
|---|---|---|
| `resultados/` | carpeta | Carpeta sugerida para salidas (HTML/JSON/CSV, screenshots, trazas). |
| `1_mi_primer_scraper.ipynb` | notebook | Primer acercamiento a scraping: requests/bs4 + parsing básico. |
| `2_obtencion_productos_completa.ipynb` | notebook | Pipeline de extracción “producto a producto”: requests → parseo → normalización → guardado. |
| `3_scraping_etico.ipynb` | notebook | Principios de scraping responsable, lectura de `robots.txt`, `crawl-delay` y límites. |
| `4_pagina_interactiva.ipynb` | notebook | Manejo de páginas con eventos, waits, y elementos dinámicos. |
| `5_chrome_web_driver.ipynb` | notebook | Selenium + ChromeDriver: selección de elementos y acciones. |
| `6_login_chrome_web_driver.ipynb` | notebook | Flujo de login con Selenium (cookies/sesión persistente). |
| `7_playwright.py` | script | Playwright básico: abrir URL, extraer texto/atributos y guardar resultados. |
| `8_playwright_scroll_infinito.py` | script | Estrategia de *scroll infinito* y espera por nuevos nodos. |
| `9_formularios_playwright_part_1.py` | script | Formularios con Playwright (inputs, selects, clicks). |
| `9_formularios_playwright_part_2.py` | script | Casos avanzados: validaciones, errores y reintentos. |
| `Scraping profesional.code-workspace` | config | Workspace para VS Code. |
| `chromedriver.exe` | binario (Windows) | ChromeDriver local (usa *webdriver-manager* como alternativa portable). |

---

## ⚙️ Requisitos

- **Python 3.10+**
- **Google Chrome/Chromium** actualizado
- **ChromeDriver** compatible con tu Chrome (o usa `webdriver-manager`)
- **Jupyter** para ejecutar los `.ipynb`

### Dependencias sugeridas (`requirements.txt`)
```txt
playwright>=1.46
beautifulsoup4>=4.12
csv
requests>=2.32
selenium>=4.23
webdriver-manager>=4.0
