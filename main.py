import datetime
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime, timedelta

from flask import Flask, render_template, request

from Amondo import Amondo
from CinemaScraper import CinemaScraper
from Iluzjon import Iluzjon

DAY = (datetime.now().date() + timedelta(2)).strftime('%a, %d.%m')

DAYS = {
    'Today': datetime.now().date(),
    'Tomorrow': datetime.now().date() + timedelta(1),
    (datetime.now().date() + timedelta(2)).strftime('%a,'): 
                                                    datetime.now().date() + timedelta(2)
}

app = Flask(__name__)

def amondo(number: str) -> None:
    CinemaScraper.result = []
    cinema = Amondo()
    cinema.retrive_movie_info(number)


def iluzjon(day_number: int) -> None:
    cinema = Iluzjon()
    headings = cinema.html_parser().find_all('h3')
    try:
        counter = [int(i.text[0:2]) for i in headings].index(day_number)

    except ValueError:
        return []


    show_table = cinema.find_elements_by_tag('table')[counter]
    show_table_hour = show_table.find_all(class_='hour')
    time_and_title = [i.text.split(' - ') for i in show_table_hour]
    list_times = [i[0] for i in time_and_title]
    list_title = [i[1] for i in time_and_title]
    years = [i.text.split(',') for i in show_table.find_all('i')]

    if cinema.numer > cinema.id:
        return 0

    show_years = cinema.get_shows_list(years)
    cinema.get_result_map(list_times, list_title, show_years)


@app.route('/', methods=['GET', 'POST'])
def front():
    return render_template('help.html', dzien=DAY)

@app.route('/final', methods=['GET', 'POST'])
def final():
    day_get = request.args.get('day')
    date = DAYS[day_get]

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(amondo, date)
        executor.submit(iluzjon, int(date.day))

    repertuar = CinemaScraper.result
    repertuar.sort(key=lambda x: str(x['rating']), reverse=True)
    if day_get not in ['Today', 'Tomorrow']:
        day_get = DAY
    return render_template('index.html', post=repertuar, 
                           what_day = day_get, what_date = date)


if __name__ == '__main__':
    app.run()