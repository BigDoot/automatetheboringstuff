import requests, bs4, os
from selenium import webdriver

print('what pictures do you want?')
searchitem = input()
os.makedirs('Pics_%s' %(searchitem), exist_ok=True)
browser = webdriver.Chrome('C:\seledrivers\chromedriver.exe')
browser.get('https://imgur.com/')
searchelem = browser.find_element_by_class_name('Searchbar-textInput')
searchelem.send_keys(searchitem)
searchelem.submit()
url = browser.current_url
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
picselem = soup.select('a img')
numpics = min(10, len(picselem))
for i in range(numpics):
    imageurl = 'https:' + picselem[i].get('src')
    res2 = requests.get(imageurl)
    res2.raise_for_status()
    file = open(os.path.join('Pics_%s' %(searchitem), os.path.basename(imageurl)), 'wb')
    for chunk in res2.iter_content(100000):
        file.write(chunk)
    file.close()
browser.quit()
print('Done downloading %s pics about %s!' %(numpics,searchitem))
