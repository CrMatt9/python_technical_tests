from unittest.mock import patch

import requests

from src.problem_1.exercise_11 import make_request, make_some_requests


@patch("requests.get")
def test_make_request_success(mock_get, mock_response, test_url):
    """
    Test make_request function for successful HTTP GET request.
    GIVEN a URL to make an HTTP GET request,
    WHEN make_request is called,
    THEN it should return a response with status code 200.
    """
    mock_get.return_value = mock_response
    response = make_request(test_url)
    assert response.status_code == 200


@patch("requests.get")
def test_make_request_failure(mock_get, test_url):
    """
    Test make_request function for failed HTTP GET request.
    GIVEN a URL to make an HTTP GET request,
    WHEN make_request encounters an error,
    THEN it should return False.
    """
    mock_get.side_effect = requests.RequestException("Mock error")
    response = make_request(test_url)
    assert response is False


def test_make_some_requests(test_url):
    """
    Test make_some_requests function for making multiple HTTP GET requests.
    GIVEN a URL, number of requests, and number of processes,
    WHEN make_some_requests is called,
    THEN it should return the total time taken to make the requests.
    """
    total_time = make_some_requests(test_url, number_of_requests=5, num_processes=2)
    assert total_time > 0
