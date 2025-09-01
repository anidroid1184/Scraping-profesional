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

    async with async_playwright() as p:
        # Se lanza el navegador
        browser = await p.chromium.launch(headless=False)
        # crear una instancia de contexto para la pagina
        context = await browser.new_context()
        # creamos una instancia para obtener el contexto de la pagina
        page = await context.new_page()

        # vamos a la pagina web
        await page.goto(url)
        # espera 3 segundos para que se renderice la pagina
        await page.wait_for_timeout(3000)

        # Obtener el html de la página renderizada
        html = await page.content()
        await browser.close()

        # Procesar con Beuatiful soup
        soup = BeautifulSoup(html, "html.parser")  # se parsea el html
        quotes = soup.select("div.quote")  # se obtiene el div contenedor

        # se muestran las citas obtenidas
        print("Citas encontradas: ", len(quotes))

        # se muestra cita por cita
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            print(f"{text} - {author}")

# ejecutamos el script
asyncio.run(main())
