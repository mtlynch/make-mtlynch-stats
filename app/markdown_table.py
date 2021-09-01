def generate(table):
    formatted_table = table
    formatted_table = _add_change_formatting(formatted_table)
    formatted_table = _add_total_summary_formatting(formatted_table)

    column_widths = _find_column_widths(formatted_table)
    formatted_table = _add_padding(formatted_table, column_widths)

    lines = []
    lines.append(_make_row(formatted_table[0]))
    lines.append(_make_header_separators(column_widths))
    for row in formatted_table[1:]:
        lines.append(_make_row(row))
    return '\n'.join(lines)


def _add_change_formatting(table):
    rows = []
    rows.append(table[0])
    for row in table[1:]:
        columns = []
        for i, column in enumerate(row):
            if i == len(row) - 1:
                if column.startswith('-'):
                    columns.append('<font color="red">%s</font>' % column)
                elif column.startswith('+'):
                    columns.append('<font color="green">%s</font>' % column)
                else:
                    columns.append(column)
            else:
                columns.append(column)
        rows.append(columns)
    return rows


def _add_total_summary_formatting(table):
    rows = table[:-1]
    final_row = []
    for value in table[-1]:
        final_row.append('**%s**' % value)
    rows.append(final_row)
    return rows


def _add_padding(table, column_widths):
    rows = []
    for unformatted_row in table:
        row = []
        for column_index, value in enumerate(unformatted_row):
            if len(value) >= column_widths[column_index]:
                row.append(value)
            else:
                padding = ' ' * (column_widths[column_index] - len(value))
                row.append(value + padding)
        rows.append(row)
    return rows


def _find_column_widths(table):
    column_count = len(table[0])
    widths = [0] * column_count
    for row in table:
        for i, column in enumerate(row):
            widths[i] = max(widths[i], len(column))
    return widths


def _make_header_separators(column_widths):
    separators = []
    for width in column_widths:
        separators.append('-' * width)
    return _make_row(separators)


def _make_row(row):
    return '| ' + ' | '.join(row) + ' |'
