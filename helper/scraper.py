from bs4 import BeautifulSoup
import undetected_chromedriver as uc

from seleniumbase import Driver
from seleniumbase import page_actions
from selenium import webdriver


def get_zona_prop_info(url):
    # from selenium import webdriver
    # from selenium.common.exceptions import TimeoutException
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.firefox.options import Options
    # from selenium.webdriver.firefox.service import Service
    # from selenium.webdriver.support import expected_conditions as EC
    # from selenium.webdriver.support.ui import WebDriverWait
    # from webdriver_manager.firefox import GeckoDriverManager

    # firefoxOptions = Options()
    # firefoxOptions.add_argument("--headless")
    # service = Service(GeckoDriverManager().install())
    # dr = webdriver.Firefox(
    #     options=firefoxOptions,
    #     service=service,
    # )
    dr = Driver(uc=True)
    dr.get(url)
    bs = BeautifulSoup(dr.page_source,"lxml")
    print(bs)
    price_text = bs.find(class_='price-value').get_text(strip=True)
    price = int(''.join(filter(str.isdigit, price_text)))
    address = bs.find('div', class_='section-location-property').get_text(strip=True)
    imgs = []
    image_divs = bs.find_all('div', class_='sc-eXAmlR')
    image_urls = [div['src'] for div in image_divs]
    for url in image_urls:
        imgs.append(url)
    property_type = bs.find('h2', class_='title-type-sup-property').get_text(strip=True).split(' ')
    meters = property_type[2]
    rooms = f'{property_type[4]} {property_type[5]}'
    property_type = property_type[0]
    ul_elements = bs.find_all('ul',class_='section-icon-features section-icon-features-property')
    basic_info = []
    for ul in ul_elements:
        li_elements = ul.find_all('li')
        for li in li_elements:
            basic_info.append(li.get_text(strip=True))
    description = bs.find('div', id='longDescription').get_text(strip=True)
    location = 'https:' + bs.find('img', id='static-map')['src']
    property_info = {
        'price': price,
        'address': address,
        'imgs': imgs,
        'property_type': property_type,
        'meters': meters,
        'Extra_information': basic_info,
        'description': description,
        'location': location,
    }
    return property_info