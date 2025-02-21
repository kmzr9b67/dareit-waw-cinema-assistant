import sys
from datetime import datetime, timedelta

sys.path.insert(0, '/Users/kingamazur/PycharmProjects/dareit-waw-cinema-assistant/') 

from main import DAYS

def test_main_day():
    except_day = (datetime.now().date() + timedelta(2)).strftime('%a,')
    except_date = (datetime.now().date() + timedelta(2))

    assert DAYS[except_day] == except_date



    
