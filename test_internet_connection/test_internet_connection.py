import requests
import socket


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("SOCKET_CONNECTION: True")
        return True
    except socket.error as ex:
        print(ex)
        return False


def web_site_online(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        print("STATUS_CODE: " + str(req.status_code))
        print("CONNECTION: " + str(req.ok))
        print("TEXT: " + req.text)
        # HTTP errors are not raised by default, this statement does that
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def lambda_handler(event, context):
    print("--- TRYING WITH SOCKET ---")
    internet()
    print("--- TRYING WITH REQUEST ---")
    web_site_online()

