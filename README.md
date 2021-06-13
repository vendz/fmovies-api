# Fmovies API

This API is capable of fetching movies/shows from fmovies and provide you a URL to stream it

---
**NOTE:** this api works on torrent so it is possible you might not be able to get requests. in order to overcome this problem I have set up `proxy`. 

so, if you are not able to get requests, add `proxy=true` to your parameters.

example - https://fmovies-api.herokuapp.com/home?suggest=all&proxy=true

- **but bear in mind that average response time after using proxy is 20-30 seconds for each request**

- **it may fail to get requests due to time out so do reload the page and give it some time**

- **IT IS RECOMMENDED TO USE HEROKU DEPLOYMENT WHILE USING PROXY**
---

## Endpoints

This API has 3 endpoints...

1. `home`: this endpoint recommends movies/shows and prvides user with trending section

2. `Search`: this endpoint takes user arguments and provides with relevant results

3. `details`: after the user selects a movie/show, they can view it's details


---

## Usage

get suggestions for movies/shows
```
https://movie.vandit.cf/home?suggest=<your-query>
```
Example - https://movie.vandit.cf/home?suggest=shows

parameters:
  - suggest
    - all
    - movies
    - shows
    - trending

---
search for your favourite movies/shows
```
https://movie.vandit.cf/search?keyword=<your-query>&page=<your-query>
```
Example - https://movie.vandit.cf/search?keyword=who+killed+sara&page=4

parameters:
  - search
  - page
  - proxy

`page` and `proxy` are optional parameters and default value of `page` is 1

---
get details of your favourite movie/show
```
https://movie.vandit.cf/details?link=<your-query>
```
Example - https://movie.vandit.cf/details?link=https://fmovies.to/film/infinite.lrvkq

parameters:
  - link

you will get the link of your favourite movies/show when you search for them using `search` endpoint

---

## Response Format

The response JSON Object looks something like this - 

```
{
currentPage: "1",
data: 
[
  {
    cover: "https://static.bunnycdn.ru/i/cache/images/e/e7/e7627572838131e2198089b1dd4a3102.jpg-w180",
    duration: "101 min",
    episodes: "N/A",
    imdb: " 6.60",
    link: "https://fmovies.to/film/friends.37x69",
    quality: "HDRip",
    seasons: "N/A",
    title: "Friends",
    type: "Movie",
    year: "1971"
  },
  {
    cover: "https://static.bunnycdn.ru/i/cache/images/5/5d/5d0dafce1ea12454d1332a2368f5f49f.jpg-w180",
    duration: "N/A",
    episodes: "17",
    imdb: " 8.90",
    link: "https://fmovies.to/film/friends.3rvj9",
    quality: "HD",
    seasons: "10",
    title: "Friends",
    type: "TV",
    year: "N/A"
  },
],
query: "friends",
success: true,
totalPages: "15"
}
```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---

### You can fork the repo and deploy on VPS, Heroku or Vercel :)
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/)

---
#### :star: the Repo in case you liked it :)
#### Made with :heart: in India

# © [Vandit](https://github.com/vendz)
