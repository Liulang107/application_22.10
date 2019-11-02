import csv
import os

from django.shortcuts import render
from .models import FilePath, Field
from django.conf import settings


def table_view(request):
    CSV_FILENAME = FilePath.objects.get(pk=1)
    COLUMNS = Field.objects.all()
    template = 'table.html'
    csv_file = os.path.join(settings.BASE_DIR, CSV_FILENAME.get_path())
    if csv_file:
        with open(csv_file, 'r') as csv_file:
            table = []
            table_reader = csv.DictReader(csv_file, delimiter=';')
            for table_row in table_reader:
                table.append(table_row)
            context = {
                'columns': COLUMNS,
                'table': table,
                'csv_file': CSV_FILENAME
            }
            result = render(request, template, context)
        return result
