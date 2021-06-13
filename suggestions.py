from proxy import Random_Proxy
import requests
from bs4 import BeautifulSoup

def getSuggestions(suggest, proxie):
    suggestionsDictionary = {
        'success': True,
        'type': suggest,
    }

    proxy = Random_Proxy()

    if proxie == 'true':
        try:
            base_url = f'https://fmovies.to/home'
            r = proxy.Proxy_Request(url=base_url, request_type='get')
            soup = BeautifulSoup(r.content, 'lxml')
        except requests.exceptions.RequestException as e:
            suggestionsDictionary['success'] = False,
            suggestionsDictionary['error'] = str(e),
            return suggestionsDictionary
    else:
        try:
            base_url = f'https://fmovies.to/home'
            soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
        except requests.exceptions.RequestException as e:
            suggestionsDictionary['success'] = False,
            suggestionsDictionary['error'] = str(e),
            return suggestionsDictionary

    items = soup.find_all('div', class_='tab-content')
    types = []
    for item in items:
        types.append(item)

    if suggest == 'movies' :
        suggestionsDictionary['data'] = recommendMovies(types[0])
    elif suggest == 'shows':
        suggestionsDictionary['data'] = recommendShows(types[1])
    elif suggest == 'trending':
        suggestionsDictionary['data'] = trending(types[2])
    elif suggest == 'all':
        suggestionsDictionary['data'] = {}
        suggestionsDictionary['data']['movies'] = recommendMovies(types[0])
        suggestionsDictionary['data']['shows'] = recommendShows(types[1])
        suggestionsDictionary['data']['trending'] = trending(types[2])
    else:
        suggestionsDictionary['success'] = False,
        suggestionsDictionary['error'] = 'category doesn\'t exist',
        suggestionsDictionary['allowedCategories'] = ['all', 'movies', 'shows', 'trending']
        return suggestionsDictionary

    return suggestionsDictionary

def recommendMovies(type):
    data = []
    items = type.find_all('div', class_='item')

    for item in items:
        try:
            a = item.find('a')
            href = a.get('href')
            link = f'https://fmovies.to{href}'
        except Exception as e:
            link = str(e)

        try:
            a = item.find('a')
            title = a.get('title')
        except Exception as e:
            title = str(e)
        
        try:
            img = item.find('img')
            cover = img['src']
        except Exception as e:
            cover = str(e)
        
        try:
            quality = item.find('div', class_="quality").text
        except Exception as e:
            quality = str(e)

        try:
            imdb = item.find('span', class_='imdb').text
        except Exception as e:
            imdb = str(e)

        try:
            type = item.find('i', class_='type').text
        except Exception as e:
            type = str(e)

        try:
            rawData = item.find('div', class_='meta').text
            listData = rawData.split()
            year = listData[0]
        except Exception as e:
            year = str(e)
        
        try:
            rawData = item.find('div', class_='meta').text
            listData = rawData.split()
            duration = listData[1] + " " + listData[2]
        except Exception as e:
            duration = str(e)

        movieSuggestionObject = {
            'link': link,
            'cover': cover,
            'quality': quality,
            'imdb': imdb,
            'title': title,
            'type': type,
            'year': year,
            'duration': duration
        }
        data.append(movieSuggestionObject)
    return data

def recommendShows(type):
    data = []
    items = type.find_all('div', class_='item')

    for item in items:
        try:
            a = item.find('a')
            href = a.get('href')
            link = f'https://fmovies.to{href}'
        except Exception as e:
            link = str(e)

        try:
            a = item.find('a')
            title = a.get('title')
        except Exception as e:
            title = str(e)
        
        try:
            img = item.find('img')
            cover = img['src']
        except Exception as e:
            cover = str(e)
        
        try:
            quality = item.find('div', class_="quality").text
        except Exception as e:
            quality = str(e)

        try:
            imdb = item.find('span', class_='imdb').text
        except Exception as e:
            imdb = str(e)

        try:
            type = item.find('i', class_='type').text
        except Exception as e:
            type = str(e)

        try:
            rawData = item.find('div', class_='meta').text
            listData = rawData.split()
            seasons = listData[1]
        except Exception as e:
            seasons = str(e)

        try:
            rawData = item.find('div', class_='meta').text
            listData = rawData.split()
            episodes = listData[-2]
        except Exception as e:
            episodes = str(e)

        showSuggestionObject = {
            'link': link,
            'cover': cover,
            'quality': quality,
            'imdb': imdb,
            'title': title,
            'type': type,
            'seasons': seasons,
            'episodes': episodes
        }
        data.append(showSuggestionObject)
    return data

def trending(type):
    data = []
    items = type.find_all('div', class_='item')

    for item in items:
        try:
            a = item.find('a')
            href = a.get('href')
            link = f'https://fmovies.to{href}'
        except Exception as e:
            link = str(e)

        try:
            a = item.find('a')
            title = a.get('title')
        except Exception as e:
            title = str(e)
        
        try:
            img = item.find('img')
            cover = img['src']
        except Exception as e:
            cover = str(e)
        
        try:
            quality = item.find('div', class_="quality").text
        except Exception as e:
            quality = str(e)

        try:
            imdb = item.find('span', class_='imdb').text
        except Exception as e:
            imdb = str(e)

        try:
            type = item.find('i', class_='type').text
        except Exception as e:
            type = str(e)

        try:
            if(type == 'Movie'):
                rawData = item.find('div', class_='meta').text
                listData = rawData.split()
                year = listData[0]
            else:
                year = 'N/A'
        except Exception as e:
            year = str(e)
        
        try:
            if(type == 'Movie'):
                rawData = item.find('div', class_='meta').text
                listData = rawData.split()
                duration = listData[1] + " " + listData[2]
            else:
                duration = 'N/A'
        except Exception as e:
            duration = str(e)

        try:
            if(type == 'TV'):
                rawData = item.find('div', class_='meta').text
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

        trendingObject = {
            'link': link,
            'cover': cover,
            'quality': quality,
            'imdb': imdb,
            'title': title,
            'type': type,
            'year': year,
            'duration': duration,
            'seasons': seasons,
            'episodes': episodes
        }
        data.append(trendingObject)
    return data

