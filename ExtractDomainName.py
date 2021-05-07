# Extract the domain name from a URL

def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    url = url.split('.', 1)[0]
    
    return url 
