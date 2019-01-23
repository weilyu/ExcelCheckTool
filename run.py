import os
from openpyxl import load_workbook

ALLOWED_FONT_NAMES = ['Calibri']
ALLOWED_FONT_SIZES = [12]
ALLOWED_BG_RGBS = ['00000000']

if __name__ == '__main__':

    for path, _, files in os.walk('.'):
        for file in files:
            if file.endswith('xls') or file.endswith('xlsx'):
                wb = load_workbook(os.path.join(path, file))
                for ws in wb.worksheets:
                    for row in ws.rows:
                        for cell in row:
                            if cell.font.name not in ALLOWED_FONT_NAMES:
                                print('Wrong font:', file, ws.title, cell.coordinate)
                            if int(cell.font.size not in ALLOWED_FONT_SIZES):
                                print('Wrong size:', file, ws.title, cell.coordinate)
                            if cell.fill.bgColor.rgb not in ALLOWED_BG_RGBS:
                                print('Wrong color:', file, ws.title, cell.coordinate)
