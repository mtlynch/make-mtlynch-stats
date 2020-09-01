import projects


def convert(project, a, b):
    converter_fns = {
        projects.TINYPILOT: _convert_tinypilot,
        projects.IS_IT_KETO: _convert_isitketo,
        projects.ZESTFUL: _convert_zestful,
        projects.TOTALS: _convert_totals,
    }
    return converter_fns[project](a, b)


def _convert_tinypilot(a, b):
    rows = []
    rows.append([
        'Metric',
        _format_month(a['month']),
        _format_month(b['month']), 'Change'
    ])
    rows.append(_integer_row('Unique Visitors', 'unique_visitors', a, b))
    rows.append(_integer_row('Total Pageviews', 'total_pageviews', a, b))
    rows.append(_dollar_amount_row('Sales Revenue', 'net_sales', a, b))
    rows.append(_dollar_amount_row('Donations', 'donations', a, b))
    rows.append(_dollar_amount_row('Total Earnings', 'total_earnings', a, b))

    return rows


def _convert_isitketo(a, b):
    rows = []
    rows.append([
        'Metric',
        _format_month(a['month']),
        _format_month(b['month']), 'Change'
    ])
    rows.append(_integer_row('Unique Visitors', 'unique_visitors', a, b))
    rows.append(_integer_row('Total Pageviews', 'total_pageviews', a, b))
    rows.append(
        _float_row('Domain Rating (Ahrefs)', 'domain_rating_ahrefs', a, b))
    if a['adsense_earnings'] or b['adsense_earnings']:
        rows.append(
            _dollar_amount_row('AdSense Earnings', 'adsense_earnings', a, b))
    if a['adthrive_earnings'] or b['adthrive_earnings']:
        rows.append(
            _dollar_amount_row('AdThrive Earnings', 'adthrive_earnings', a, b))
    # Before AdSense earnings, total earnings == amazon affiliate earnings
    if a['adsense_earnings'] or b['adsense_earnings']:
        rows.append(
            _dollar_amount_row('Amazon Affiliate Earnings',
                               'amazon_affiliate_earnings', a, b))
    if a['other_affiliate_earnings'] or b['other_affiliate_earnings']:
        rows.append(
            _dollar_amount_row('Other Affiliate Earnings',
                               'other_affiliate_earnings', a, b))
    if a['meal_plan_sales'] or b['meal_plan_sales']:
        rows.append(
            _dollar_amount_row('Meal Plan Sales', 'meal_plan_sales', a, b))
    rows.append(_dollar_amount_row('Total Earnings', 'total_earnings', a, b))

    return rows


def _convert_zestful(a, b):
    rows = []
    rows.append([
        'Metric',
        _format_month(a['month']),
        _format_month(b['month']), 'Change'
    ])
    rows.append(_integer_row('Unique Visitors', 'unique_visitors', a, b))
    rows.append(_integer_row('Total Pageviews', 'total_pageviews', a, b))
    if a['rapidapi_earnings'] or b['rapidapi_earnings']:
        rows.append(
            _dollar_amount_row('RapidAPI Earnings', 'rapidapi_earnings', a, b))
    # Before AdSense earnings, total earnings == amazon affiliate earnings
    if a['enterprise_plan_earnings'] or b['enterprise_plan_earnings']:
        rows.append(
            _dollar_amount_row('Enterprise Plan Earnings',
                               'enterprise_plan_earnings', a, b))
    rows.append(_dollar_amount_row('Total Earnings', 'total_earnings', a, b))

    return rows


def _convert_totals(a, b):
    rows = []
    rows.append([
        'Metric',
        _format_month(a['month']),
        _format_month(b['month']), 'Change'
    ])
    rows.append(_dollar_amount_row('TinyPilot', 'tinypilot', a, b))
    rows.append(_dollar_amount_row('Is It Keto', 'isitketo', a, b))
    rows.append(_dollar_amount_row('Zestful', 'zestful', a, b))
    rows.append(_dollar_amount_row('Total', 'total', a, b))

    return rows


def _format_month(dt):
    return dt.strftime('%B %Y')


def _integer_row(metric_name, key, a, b):
    return [
        metric_name,
        _format_integer(a[key]),
        _format_integer(b[key]),
        _format_integer_difference(a[key], b[key])
    ]


def _format_integer_difference(a, b):
    if a is None or b is None:
        return 'N/A'
    difference = b - a
    if difference == 0:
        return '0'
    if difference > 0:
        sign = '+'
    else:
        sign = ''
    if a != 0.0:
        percentage = '%s%.0f%%' % (sign, 100.0 * (float(difference) / a))
    else:
        percentage = '+inf%'
    formatted_difference = _format_integer(difference)
    return '%s%s (%s)' % (sign, formatted_difference, percentage)


def _format_integer(i):
    if i is None:
        return 'N/A'
    return '{:,}'.format(i)


def _float_row(metric_name, key, a, b):
    return [
        metric_name,
        _format_float(a[key]),
        _format_float(b[key]),
        _format_float_difference(a[key], b[key])
    ]


def _format_float_difference(a, b):
    if a is None or b is None:
        return 'N/A'
    difference = b - a
    if difference == 0:
        return '0'
    if difference > 0:
        sign = '+'
    else:
        sign = ''
    if a != 0.0:
        percentage = '%s%.0f%%' % (sign, 100.0 * (float(difference) / a))
    else:
        percentage = '+inf%'
    formatted_difference = _format_float(difference)
    return '%s%s (%s)' % (sign, formatted_difference, percentage)


def _format_float(f):
    if f is None:
        return 'N/A'
    return '%.1f' % f


def _dollar_amount_row(metric_name, key, a, b):
    return [
        metric_name,
        _format_dollar_amount(a[key]),
        _format_dollar_amount(b[key]),
        _format_dollar_difference(a[key], b[key])
    ]


def _format_dollar_difference(a, b):
    if a is None or b is None:
        return 'N/A'

    difference = b - a
    if difference == 0:
        return '0'
    if difference > 0:
        sign = '+'
    else:
        sign = ''
    formatted_difference = _format_dollar_amount(difference)
    formatted_difference = formatted_difference.replace('$-', '-$')
    if a != 0.0:
        percentage = '%s%.0f%%' % (sign, 100.0 * (float(difference) / a))
    else:
        percentage = '+inf%'
    return '%s%s (%s)' % (sign, formatted_difference, percentage)


def _format_dollar_amount(d):
    if d is None:
        return 'N/A'
    return f'${d:,.2f}'
