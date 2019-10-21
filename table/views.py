import csv
import os

from django.shortcuts import render
from app.settings import BASE_DIR


CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]

def table_view(request):
    template = 'table.html'
    csv_file = os.path.join(BASE_DIR, CSV_FILENAME)
    if csv_file:
        with open(csv_file, 'r') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                        for idx, value in enumerate(table_row)}
                    table.append(row)
            context = {
                'columns': COLUMNS,
                'table': table,
                'csv_file': CSV_FILENAME
            }
            result = render(request, template, context)
        return result
