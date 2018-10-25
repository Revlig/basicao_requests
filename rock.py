u"""Extraindo notícias com requests & beautifulsoup."""
from requests import get
from bs4 import BeautifulSoup as bs

# definindo um user agent
HEADERS = {
     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
     }

# nossa url alvo
url = 'http://campinasrockcity.com.br/noticias/'

# criado elemento requests a partir da URL
r = get(url)

# parseando o html
page = bs(r.text, 'html.parser')

# criando as listas de data e noticias
html_datas = page.find_all('div', {'class': 'card-news-date'})
html_noticias = page.find_all('div', {'class': 'card-news-title'})

# mostrando na tela noticias e data
for indice in range(len(html_datas)):
    print(html_datas[indice].text, html_noticias[indice].text)

# pegando o elemento paginator
lista_href = page.find_all('ul', {'class': 'paginate'})[0].find_all('a')

# o elemento que quero sempre estará na última posição
href = lista_href[-1].get('href')

# pegar url para próxima página
nova_url = r.url.replace(r.request.path_url, href)
