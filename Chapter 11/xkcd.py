#!python3

import bs4, requests, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    
    comic = soup.select('#comic img')
    if comic == []:
        print('Could not find comic img')
    else:
        try:
            imageurl = 'https:'+comic[0].get('src')
            res2 = requests.get(imageurl)
            res2.raise_for_status()
        except requests.exceptions.MissingSchema:
            prev = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prev.get('href')
            continue
    file = open(os.path.join('xkcd', os.path.basename(imageurl)), 'wb')
    for chunk in res2.iter_content(100000):
        file.write(chunk)
    file.close()
    prev = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev.get('href')





print('done')
