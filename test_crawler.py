from crawler import post_request,scrapper,next_page_check
from constants import data_frame_format

def test_request():
    request_result = post_request('SP', 1, 50)
    assert request_result.status_code == 200

def test_scrapper():
    request_result = post_request('AC', 1, 50)
    assert scrapper(request_result, 'AC') == 'scrapper executado com sucesso'

def test_next_page_check():
    request_result = post_request('SP', 1, 50)
    assert next_page_check(request_result) is not None
