'''
pip install requests
'''

from bs4 import BeautifulSoup
import requests, time

def getData():
    html_text = requests.get('https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/').text
    soup = BeautifulSoup(html_text, 'lxml')
    movies = soup.find_all('div', class_='article_movie_title')

    pretend_year = input('Insert year: ')

    for index, movie in enumerate(movies):

        movie_data = movie.text.split()
        movie_name = ' '.join(movie_data[:-2])
        movie_year = movie_data[-2].strip('()')
        more_info = movie.find('a')['href']

        if (pretend_year == movie_year):

            with open(f'output/{index}.txt', 'w') as f:
                f.write(f'Name: {movie_name}\n')
                f.write(f'Year: {movie_year}\n')
                f.write(f'More info: {more_info}')

                print(f'File {index}.txt saved')

if __name__ == '__main__':
    while True:
        getData()
        print('Waiting 10 minutes...')
        time.sleep(600)