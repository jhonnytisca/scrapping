# Librerias
import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Archivos
import urls  # Gestión de urls


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log_title(msg, type=""):
    print("\n" + "-" * len(msg) + f"\n{type}{msg}{BColors.ENDC}\n" + "-" * len(msg))


def log_message(msg, type=""):
    print(f"\t{type}{msg}{BColors.ENDC}")


def log_message_ln(msg):
    log_message(msg + "\n")


def open_url(url, ignore_ssl=True, verbose=False):
    if verbose:
        log_title(f"Retrieving html from: {url}")
    return check_url(url, ignore_ssl, verbose)


def read_url(url, ignore_ssl=True):
    return open_url(url, ignore_ssl).read()


def check_url(url, ignore_ssl=True, verbose=False):
    if verbose:
        log_title(f"Check URL response: {url}")
    ctx = ctx_ignore_ssl() if ignore_ssl else ssl.create_default_context()
    try:
        response = urllib.request.urlopen(url, context=ctx)
        if verbose:
            log_message(f"Conexión válida", BColors.OKGREEN)
            log_message(f"Status: {response.code} {response.reason}")
        return response
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        if verbose:
            log_message(f"Fallo en la conexión", BColors.FAIL)
            log_message(e.reason)
        return None


def ctx_ignore_ssl():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


if __name__ == '__main__':

    # Read data from url
    #
    # file_handler = urllib.request.urlopen(urls.get_url(0))
    # for line in file_handler:
    #     print(line.decode().strip())

    # Test connection
    #
    # print(f"{open_url(urls.get_url(6)).headers._headers[2]}")

    for url in urls.get_url_list():
        check_url(url, ignore_ssl=True, verbose=True)

    # Retrieve a tags
    #
    #     html = read_url(url)
    #     soup = BeautifulSoup(html, 'html.parser')
    #
    #     tags = soup('a')
    #
    #     for tag in tags:
    #         print(tag.get('href', None))
