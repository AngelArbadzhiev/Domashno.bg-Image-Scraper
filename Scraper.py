import requests
from bs4 import BeautifulSoup
import os

login_url = 'https://domashno.bg/login'
data = {
    'username': 'email',
    'password': 'password'
}

with requests.Session() as s:
    response = requests.post(login_url , data)
    print(response.text)
    index_page= s.get('https://domashno.bg/login')
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print(soup.title)
def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find('img')
    for image in images:
        for img in images.select('img[alt]'):
            img.replace_with(img['alt'])
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

imagedown('https://domashno.bg/matematika/8/arhimed-new/uroci', 'Pictures')

