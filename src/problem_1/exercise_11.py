import requests
import time
from multiprocessing import Pool


def make_request(url):
    """
    Make an HTTP GET request to the specified URL.
    :param url: The URL to request.
    :return: True if the request was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False


def make_some_requests(url, number_of_requests=1000, num_processes=20):
    """
    Make HTTP GET requests to the specified URL in parallel.

    :param url: The URL to request.
    :param num_processes: The number of processes to use.
    :param number_of_requests: The number of requests to make.
    :return: The total time taken to make the requests.
    """
    start_time = time.time()
    with Pool(processes=num_processes) as pool:
        _ = pool.map(make_request, [url] * number_of_requests)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    total_time = make_some_requests(url)
    print(f"Done in a total of: {total_time:.2f} seconds")
