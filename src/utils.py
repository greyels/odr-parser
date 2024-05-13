import pandas as pd


def store_excel_as_json(excel_fn, excel_sheet, json_fn):
    data = pd.read_excel(io=excel_fn, sheet_name=excel_sheet)
    data.to_json(json_fn, orient='records')
