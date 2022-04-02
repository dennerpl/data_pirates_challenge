from crawler import post_request,scrapper,next_page_check
from constants import data_frame_format

def test_request():
    request_result = post_request('SP', 1, 50)
    assert request_result.status_code == 200

def test_scrapper():
    request_result = post_request('AC', 1, 50)
    assert scrapper(request_result, 'AC') == 'scrapper executado com sucesso'

def test_next_page_check():
    request_result_sp = post_request('SP', 1, 50)
    request_result_ac = post_request('AC', 1, 50)
    assert (next_page_check(request_result_sp) is not None) and (next_page_check(request_result_ac) is not None)
