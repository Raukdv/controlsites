#SSL CHECKER and Website checker
from threading import Thread
import socket
import ssl
import datetime
import http.client as httplib
import urllib.parse
from urllib.request import urlopen, build_opener
import dns.resolver
from bs4 import BeautifulSoup
import re

def ssl_check(hostname):

    #print(f'Checking SSL for: {hostname}')
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname,)
    conn.settimeout(3.0)

    try:
        conn.connect((hostname, 443))
        #Get the main info about the SSL cert
        ssl_info = conn.getpeercert()
        #Get expiration date of the SSL cert
        Exp_on = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        #print(f'{hostname} SSL Enable')
        # print(f'{hostname} expires on: {Exp_on}')
        # print('------------------------')
        # print('------------------------')
        return True
    except:
        #print('domain has not SSL')
        # print('------------------------')
        # print('------------------------')
        return False

def website_code_status(url):
    try:
        protocol, host, path, query, fragment = urllib.parse.urlsplit(url)
        #Check for no schema given
        custom_protocol = 'Empty Protocol' if not protocol else protocol

        #validate schema for the correct requst
        if protocol == "http":
            conntype = httplib.HTTPConnection
        elif protocol == "https":
            conntype = httplib.HTTPSConnection
        else:
            raise ValueError("unsupported protocol: " + custom_protocol)
        
        conn = conntype(host)
        conn.request("HEAD", path)
        resp = conn.getresponse()
        conn.close()

        return resp.status, resp.reason
    
    except Exception as e:
        print(f'[ERROR]: {e}: No Response from {url}')
        return None
    
def imgs_caption(url):
    #Try to get all related info about the url and imgs/caption
    try:

        opener = build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')]
        soup = BeautifulSoup(opener.open(url), features="html.parser")
        imgs = soup.find_all("img")
        captions = [img.parent.parent.text.encode('utf-8').strip() for img in imgs]
        zipped = list(zip(imgs, captions))
        return zipped

    except Exception as e:
        print(f'[ERROR]: {e}: No Response from {url}')
        return None
    

def async_dns_resolver(domain, record):
    #Init Thread for dns resolver
	thread = Thread(target=dns_resolver, args=[domain, record])
	thread.start()

#This may take some time for each iteration in the dns resolver. 
def dns_resolver(domain=None, records=None):

    if records == None:
        records = [
            'NONE',
            'A',
            'NS',
            'MD',
            'MF',
            'CNAME',
            'SOA',
            'MB',
            'MG',
            'MR',
            'NULL',
            'WKS',
            'PTR',
            'HINFO',
            'MINFO',
            'MX',
            'TXT',
            'RP',
            'AFSDB',
            'X25',
            'ISDN',
            'RT',
            'NSAP',
            'NSAP-PTR',
            'SIG',
            'KEY',
            'PX',
            'GPOS',
            'AAAA',
            'LOC',
            'NXT',
            'SRV',
            'NAPTR',
            'KX',
            'CERT',
            'A6',
            'DNAME',
            'OPT',
            'APL',
            'DS',
            'SSHFP',
            'IPSECKEY',
            'RRSIG',
            'NSEC',
            'DNSKEY',
            'DHCID',
            'NSEC3',
            'NSEC3PARAM',
            'TLSA',
            'HIP',
            'CDS',
            'CDNSKEY',
            'CSYNC',
            'SPF',
            'UNSPEC',
            'EUI48',
            'EUI64',
            'TKEY',
            'TSIG',
            'IXFR',
            'AXFR',
            'MAILB',
            'MAILA',
            'ANY',
            'URI',
            'CAA',
            'TA',
            'DLV',
        ]

    dict_values = dict()
    parse_content = list()
    for record in records:

        answers = dns.resolver.resolve(domain,record)
        if record == 'A':
            dict_values['A'] = [answer.to_text() for answer in answers]
        elif record == 'TXT':
            dict_values['TXT'] = [answer.to_text() for answer in answers]
        elif record == 'NS':
            dict_values['NS'] = [answer.to_text() for answer in answers]

    return dict_values

def parsing_img(texto):
    # Utiliza una expresión regular para buscar el valor de data-lazy-src
    pattern = r'data-lazy-src="([^"]+)"'
    result = re.search(pattern, texto)

    if result:
        valor_data_lazy_src = result.group(1)
        #print("Valor de data-lazy-src:", valor_data_lazy_src)
    else:
        #print("No se encontró data-lazy-src en el texto.")
        valor_data_lazy_src = None

    return f'<img alt="" class="card-img-top mt-2" src="{valor_data_lazy_src}" style="max-width: 280px;"/>'

#This will verify is wwww.domain.com or domain.com is valit, avoid full/canonical urls like https://domain.com or https://www.domain.com
'''ensures that each segment

    contains at least one character and a maximum of 63 characters
    consists only of allowed characters
    doesn't begin or end with a hyphen.

It also avoids double negatives (not disallowed), and if hostname ends in a . 
that's OK, too. It will (and should) fail if hostname ends in more than one dot.'''

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))