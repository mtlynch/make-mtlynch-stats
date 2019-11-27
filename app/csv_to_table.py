def convert(a, b):
    rows = []
    rows.append([
        'Metric',
        _format_month(a['month']),
        _format_month(b['month']), 'Change'
    ])
    rows.append(_integer_row('Unique Visitors', 'unique_visitors', a, b))
    rows.append(_integer_row('Total Pageviews', 'total_pageviews', a, b))
    rows.append(
        _integer_row('Domain Authority (Moz)', 'domain_authority_moz', a, b))
    rows.append(
        _integer_row('Ranking Keywords (Moz)', 'ranking_keywords_moz', a, b))
    if a['adsense_earnings'] or b['adsense_earnings']:
      rows.append(_dollar_amount_row('AdSense Earnings', 'adsense_earnings', a,
                                    b))
    # Before AdSense earnings, total earnings == amazon affiliate earnings
    if a['adsense_earnings'] or b['adsense_earnings']:
      rows.append(
          _dollar_amount_row('Amazon Affiliate Earnings',
                            'amazon_affiliate_earnings', a, b))
    if a['meal_plan_sales'] or b['meal_plan_sales']:
      rows.append(_dollar_amount_row('Meal Plan Sales', 'meal_plan_sales', a, b))
    a['total_earnings'] = sum(
        filter(None, (a['adsense_earnings'], a['amazon_affiliate_earnings'],
                      a['meal_plan_sales'])))
    b['total_earnings'] = sum(
        filter(None, (b['adsense_earnings'], b['amazon_affiliate_earnings'],
                      b['meal_plan_sales'])))
    rows.append(_dollar_amount_row('Total Earnings', 'total_earnings', a, b))

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
    if not a or not b:
        return 'N/A'
    difference = b - a
    percentage = 100.0 * (float(difference) / a)
    if difference > 0:
        sign = '+'
    elif difference < 0:
        sign = ''
    else:
        return '0'
    formatted_difference = _format_integer(difference)
    return '%s%s (%s%.0f%%)' % (sign, formatted_difference, sign, percentage)


def _format_integer(i):
    if not i:
        return 'N/A'
    return '{:,}'.format(i)


def _dollar_amount_row(metric_name, key, a, b):
    return [
        metric_name,
        _format_dollar_amount(a[key]),
        _format_dollar_amount(b[key]),
        _format_dollar_difference(a[key], b[key])
    ]


def _format_dollar_difference(a, b):
    if not a or not b:
        return 'N/A'
    difference = b - a
    percentage = 100.0 * (difference / a)
    if difference > 0:
        sign = '+'
    elif difference < 0:
        sign = ''
    else:
        return '0'
    formatted_difference = _format_dollar_amount(difference)
    formatted_difference = formatted_difference.replace('$-', '-$')
    return '%s%s (%s%.0f%%)' % (sign, formatted_difference, sign, percentage)


def _format_dollar_amount(d):
    if not d:
        return 'N/A'
    return '$%.2f' % d
