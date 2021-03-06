from csirtg_indicator import Indicator
from csirtg_indicator.utils import is_subdomain


def _not(data):
    for d in data:
        d = Indicator(d)
        assert d.itype != 'fqdn'


def test_fqdn_ip():
    data = ['192.168.1.0/24', '192.168.1.1', '2001:1608:10:147::21', '2001:4860:4860::8888']
    _not(data)


def test_fqdn_urls():
    data = [
        'http://192.168.1.1/1.html',
        'http://www41.xzmnt.com',
        'http://get.ahoybest.com/n/3.6.16/12205897/microsoft lync server 2010.exe',
        'https://example.com:443/1.html'
    ]
    _not(data)


def test_fqdn_ok():
    data = ['example.org', '1.2.3.4.com', 'xn----jtbbmekqknepg3a.xn--p1ai']

    for d in data:
        d = Indicator(d)
        assert d.itype is 'fqdn'


def test_fqdn_subdomain():
    data = [
        'www.yahoo.com',
        'www.ww2.yahoo.com',
    ]

    for d in data:
        print(Indicator(indicator=d).is_subdomain())
        assert Indicator(indicator=d).is_subdomain()


    data = [
        'yahoo.com',
        'google.com',
        'http://google.com',
        'https://www.google.com',
        'http://www2.www.google.com',
    ]

    for d in data:
        assert not Indicator(indicator=d).is_subdomain()
