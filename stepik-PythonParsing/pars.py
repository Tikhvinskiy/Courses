def handler(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    link = 'http://icanhazip.com/'

    try:
        print(f'Try {proxy}')
        response = requests.get(link, proxies=proxies, timeout=2).text
        return (f'IP: {response} Well done')
    except:
        return (f'{proxy} is broken')


def my_function(x):
    """The function you want to compute in parallel."""
    x += 1
    return x