import os


"""Constants"""
DEFAULT_ENCODING = 'utf-8'
REQUEST_TIME_OUT = 5

PROVINCE_CURL_JSON_PATH = f"{os.path.dirname(__file__)}/config/curl.json"

PROVINCE_LIST = ['shandong', 'jiangsu']

METADATA_SAVE_PATH = f"{os.path.dirname(__file__)}/data/metadata/"

MAPPING_SAVE_PATH = f"{os.path.dirname(__file__)}/data/mapping/"
