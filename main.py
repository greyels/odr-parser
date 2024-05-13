from config.config import EXCEL_FILE_NAME, EXCEL_FILE_SHEETNAME, JSON_FILENAME, KEYWORD_LIST, LEVEL, NO_LANGUAGE

from src.odrparser import ODRParser
from src.utils import store_excel_as_json

if __name__ == "__main__":
    store_excel_as_json(EXCEL_FILE_NAME, EXCEL_FILE_SHEETNAME, JSON_FILENAME)

    parser = ODRParser()
    parser.find_relevant_jds(JSON_FILENAME, KEYWORD_LIST, LEVEL, NO_LANGUAGE)
    parser.print_relevant_jds()
