import yaml

import parse_csv


def convert(project, csv_file):
    csv_rows, _ = parse_csv.parse(csv_file)
    project_finances = {}
    for row in csv_rows:
      month = row['month']
      entry = {
          'totalRevenue': row['total_revenue'],
      }
      if 'profit' in row and row['profit'] is not None:
          entry['profit'] = row['profit']
      project_finances[month.isoformat()[:7]] = entry


    return yaml.dump({project: project_finances})
