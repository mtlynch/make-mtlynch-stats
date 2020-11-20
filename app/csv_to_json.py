import collections
import json

import csv_to_table
import markdown_table
import parse_csv


def convert(csv_file):
    csv_rows, _ = parse_csv.parse(csv_file)
    projects = collections.defaultdict(dict)
    for row in csv_rows:
      month = row['month']
      for k, v in row.items():
        if k == 'month' or k == 'total':
          continue
        if v is None:
          continue
        projects[k][month.isoformat()[:7]] = v
    return json.dumps(projects, sort_keys=True, indent=4)
