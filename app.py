from helper.pdf import *
from helper.scraper import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ.get("API_KEY")

def create_file(url,file_name):
    information = get_zona_prop_info(url)
    create_real_estate_pdf(file_name,information)

