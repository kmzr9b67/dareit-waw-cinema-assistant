from iluzjon import Iluzjon

def test_get_year():
    expected_result_year = '2024'
    data_in_year = ['Łotwa', ' Francja', ' Belgia', ' 2024']
    excepted_result_string = '0000'
    data_in_string = ['w cyklu:']

    assert Iluzjon._Iluzjon__get_year(data_in_year) == expected_result_year
    assert Iluzjon._Iluzjon__get_year(data_in_string) == excepted_result_string

# Przetestowac pierwsza funkcję 
# Ustawić aby testy przy commit uruchamiłay się automatycznie 
