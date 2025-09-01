# instalar playwright -> pip install playwright
# También se debe instalar -> playwright install
# Importamos la librerias

# importamos asyncio para escribir codigo concurrente
import asyncio
from bs4 import BeautifulSoup
# permite integraciones con el navegador que se realicen de forma asincrona
from playwright.async_api import async_playwright

# La programacion concurrente es un paradigma de la programacion
# que permite que multiples tareas(hilos) se ejecuten o avancen en paralelo
# Esto hace que se alterne rapidamente entre las distintas tareas
# Esto permite la gestión más eficiente de recursos


# se define la función de forma asincronica
async def main():
    """
    Usamos la función asincronica porque se debe esperar
    a que se entre al navegador para reaunudar el proceso
    """

    url = "http://quotes.toscrape.com/scroll"
    SCROLL_PAUSE_TIME = 2

    async with async_playwright() as p:
        # Se lanza el navegador
        browser = await p.chromium.launch(headless=False)  # con headless habilitamos la visuación(False)
        # crear una instancia de contexto para la pagina
        context = await browser.new_context()
        # creamos una instancia para obtener el contexto de la pagina
        page = await context.new_page()
        # vamos a la pagina web
        await page.goto(url)

        # se inicia el quotes_set()
        quotes_set = set()  # el quote set se usa para
        # se verifica la última altura de la web
        last_height = await page.evaluate("document.body.scrollHeight")

        # se realizan hasta 3 scrolls
        for i in range(3):
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            await page.wait_for_timeout(SCROLL_PAUSE_TIME * 1000)

            # Extraer todas las frases actualmente visibles
            quote_elements = await page.query_selector_all(".quote")

            # se recorren todas las frases
            for quote in quote_elements:
                text_span = await quote.query_selector(".text")
                if text_span:
                    text = await text_span.inner_text()
                    quotes_set.add(text)

            # se obtiene la nueva altura de la pagina
            new_height = await page.evaluate("document.body.scrollHeight")

            # verificar si se alcanzo la altura máxima
            if new_height == last_height:
                break

            # actualizar altura
            last_height = new_height
        # se espara a cerrar el browser
        await browser.close()

        print(f"Total de frases únicas cargadas {len(quotes_set)}")
        for quote in quotes_set:
            print(quote)

# ejecutamos el script
asyncio.run(main())
