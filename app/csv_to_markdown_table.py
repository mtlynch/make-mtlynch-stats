import csv_to_table
import markdown_table
import parse_csv


def convert(csv_file, offset):
    csv_rows, project = parse_csv.parse(csv_file)
    table = csv_to_table.convert(project, csv_rows[offset - 1],
                                 csv_rows[offset])
    return markdown_table.generate(table)
