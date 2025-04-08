import requests
import bs4
from urllib.parse import urljoin
from EnviarMensagem import env_mensagem

def buscar_noticias():
    url = 'https://ge.globo.com/futebol/times/corinthians/'
    req = requests.get(url)
    page = bs4.BeautifulSoup(req.text, "html.parser")

    listanoticias = page.find_all("div", class_="feed-post-body")
    print(f"Total de notícias encontradas: {len(listanoticias)}")

    for noticia in listanoticias[:3]:
        link_tag = noticia.find("a", class_="feed-post-link")
        img_tag = noticia.find("img")

        titulo = link_tag.text.strip() if link_tag else "Sem título"
        link = link_tag.get("href") if link_tag else "#"

        img_src = img_tag.get("src") if img_tag and img_tag.has_attr("src") else None
        img_url = urljoin(url, img_src) if img_src else None
        img_none = "https://s3.glbimg.com/v1/AUTH_378ee63fe83141e69caddd838034e850/static/preview-share-min.png"

        full_msg = f"{titulo}\n{link}"

        if img_url and img_url.startswith("http"):
            env_mensagem(full_msg, img_url)
            print(f"Enviado:\n{full_msg}\n {img_url}")
        else:
            env_mensagem(full_msg, img_none)
            print(f"Enviado:\n{full_msg}\n {img_none}")

        print("-" * 40)