import csv_to_table
import parse_csv
import markdown_table

def convert(csv_file, offset):
  csv_rows = parse_csv.parse(csv_file)
  table = csv_to_table.convert(csv_rows[offset - 1], csv_rows[offset])
  return markdown_table.generate(table)