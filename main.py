from setap_page import iteraciones_pelis_año
from clean_data_frame import clean_dataframe
import sys
import os

url_padre="https://sede.mcu.gob.es/CatalogoICAA"
if len(sys.argv) != 2:
    year=2024
else:
    year = sys.argv[1]

data_frame_final = iteraciones_pelis_año(url_padre,year)
cleaned_df = clean_dataframe(data_frame_final)

output_folder = 'excel_final'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
pdf_filename = "icaa_{}.xlsx".format(year)
file_path = os.path.join(output_folder, pdf_filename)
cleaned_df.to_excel(file_path, index=False)
