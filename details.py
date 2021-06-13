from proxy import Random_Proxy
import requests
from bs4 import BeautifulSoup

def getDetails(link, proxie):
    detailsDictionary = {
        'success': True,
        'link': link,
        'data': []
    }

    proxy = Random_Proxy()

    if(proxie == 'true'):
        try:
            base_url = link
            r = proxy.Proxy_Request(url=base_url, request_type='get')
            soup = BeautifulSoup(r.content, 'lxml')
        except requests.exceptions.RequestException as e:
            detailsDictionary['success'] = False,
            detailsDictionary['error'] = str(e),
            return detailsDictionary
    else:
        try:
            base_url = link
            soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
        except requests.exceptions.RequestException as e:
            detailsDictionary['success'] = False,
            detailsDictionary['error'] = str(e),
            return detailsDictionary

    items = soup.find_all('section', class_='info')
    
    for item in items:
        try:
            img = item.find('div', class_='poster')
            poster = img.find('img')['src']
        except Exception as e:
            poster = str(e)

        try:
            title = item.find('h1', class_='title').text
        except Exception as e:
            title = str(e)
        
        try:
            quality = item.find('span', class_='quality').text
        except Exception as e:
            quality = str(e)

        try:
            imdb = item.find('span', class_='imdb').text
        except Exception as e:
            imdb = str(e)

        try:
            desc = item.find('div', class_='desc').text
        except Exception as e:
            desc = str(e)

        try:
            meta_data = item.find_all('div', class_='meta')
        except Exception as e:
            meta_data = str(e)

        for meta in meta_data:
            try:
                spans = meta.find_all('span')
            except Exception as e:
                spans = ""
            releaseDate = ''
            substring = 'dateCreated'
            for span in spans:
                if substring in str(span):
                    releaseDate = span.text

            try:
                a = meta.find_all('a')
            except Exception as e:
                a = ""
            country = []
            genres = []
            cast = []
            for link in a:
                href = link.get('href')
                
                substring = 'country'
                if substring in href:
                    country.append(link.text)
                
                substring = 'genre'
                if substring in href:
                    genres.append(link.text)

                substring = 'star'
                if substring in href:
                    cast.append(link.text)

        try:
            director = item.find('span', class_='shorting').text
        except Exception as e:
            director = str(e)

    detailsObject = {
        'poster': poster,
        'title': title,
        'quality': quality,
        'imdb': imdb,
        'description': desc,
        'country': country,
        'genre': genres,
        'cast': cast,
        'director': director,
        'releaseDate': releaseDate
    }
    detailsDictionary['data'].append(detailsObject)
    detailsDictionary['you-may-also-like'] = getSimilarSuggstions(soup)
    return detailsDictionary


def getSimilarSuggstions(soup):
    suggestion = {
        'data': []
    }
    items = soup.find_all('div', class_='bl-2')

    for item in items:
        rows = item.find_all('div', class_='item')
        for row in rows:
            try:
                a = row.find('a')
                href = a.get('href')
                link = f'https://fmovies.to{href}'
            except Exception as e:
                link = str(e)

            try:
                a = row.find('a')
                title = a.get('title')
            except Exception as e:
                title = str(e)

            try:
                img = row.find('img')
                cover = img['src']
            except Exception as e:
                cover = str(e)

            try:
                quality = row.find('div', class_="quality").text
            except Exception as e:
                quality = str(e)

            try:
                type = row.find('i', class_='type').text
            except Exception as e:
                type = str(e)

            try:
                if(type == 'Movie'):
                    rawData = row.find('div', class_='meta').text
                    listData = rawData.split()
                    year = listData[0]
                else:
                    year = 'N/A'
            except Exception as e:
                year = str(e)

            try:
                if(type == 'Movie'):
                    rawData = row.find('div', class_='meta').text
                    listData = rawData.split()
                    duration = listData[1] + " " + listData[2]
                else:
                    duration = 'N/A'
            except Exception as e:
                duration = str(e)

            try:
                if(type == 'TV'):
                    rawData = row.find('div', class_='meta').text
                    listData = rawData.split()
                    seasons = listData[1]
                else:
                    seasons = 'N/A'
            except Exception as e:
                seasons = str(e)

            try:
                if(type == 'TV'):
                    rawData = item.find('div', class_='meta').text
                    listData = rawData.split()
                    episodes = listData[-2]
                else:
                    episodes = 'N/A'
            except Exception as e:
                episodes = str(e)

            suggestObject = {
            'link': link,
            'cover': cover,
            'quality': quality,
            'title': title,
            'type': type,
            'year': year,
            'duration': duration,
            'seasons': seasons,
            'episodes': episodes
            }
            suggestion['data'].append(suggestObject)
    return suggestion 