import csv
import datetime

import projects


def parse(csv_file):
    reader = csv.DictReader(csv_file)
    project = _infer_project(reader.fieldnames)
    parse_fns = {
        projects.TINYPILOT: _parse_tinypilot_csv,
        projects.ZESTFUL: _parse_zestful_csv,
        projects.IS_IT_KETO: _parse_is_it_keto_csv,
        projects.HIT_THE_FRONT_PAGE: _parse_htfp_csv,
        projects.TOTALS: _parse_totals_csv,
    }
    return parse_fns[project](reader), project


def _infer_project(field_names):
    if 'Total Sales' in field_names:
        return projects.TINYPILOT
    elif 'RapidAPI Earnings' in field_names:
        return projects.ZESTFUL
    elif 'Gumroad Earnings' in field_names:
        return projects.HIT_THE_FRONT_PAGE
    elif 'Meal Plan Sales' in field_names:
        return projects.IS_IT_KETO
    elif 'TinyPilot' in field_names:
        return projects.TOTALS
    raise ValueError('could not infer project')


def _parse_tinypilot_csv(reader):
    rows = []
    for row in reader:
        rows.append(
            {
                'month': _parse_month(row['Month']),
                'unique_visitors': _parse_integer(row['Unique Visitors']),
                'total_pageviews': _parse_integer(row['Total Pageviews']),
                'net_sales': _parse_dollars(row['Net Sales']),
                'donations': _parse_dollars(row['Donations']),
                'total_revenue': _parse_dollars(
                    row['Total Earnings']),
                'total_profit': _parse_dollars(
                    row['Total Profit']),
            },)
    return rows


def _parse_htfp_csv(reader):
    rows = []
    for row in reader:
        rows.append(
            {
                'month': _parse_month(row['Month']),
                'unique_visitors': _parse_integer(row['Unique Visitors']),
                'gumroad_earnings': _parse_dollars(row['Gumroad Earnings']),
                'bfd_earnings': _parse_dollars(row['Blogging for Devs Earnings']),
                'total_revenue': _parse_dollars(
                    row['Total Earnings']),
            },)
    return rows

def _parse_zestful_csv(reader):
    rows = []
    for row in reader:
        rows.append(
            {
                'month':
                _parse_month(row['Month']),
                'unique_visitors':
                _parse_integer(row['Unique Visitors']),
                'total_pageviews':
                _parse_integer(row['Total Pageviews']),
                'rapidapi_earnings':
                _parse_dollars(row['RapidAPI Earnings (after fees)']),
                'enterprise_plan_earnings':
                _parse_dollars(row['Enterprise Plan Earnings (after fees)']),
                'total_revenue':
                _parse_dollars(row['Total Earnings (after fees)']),
            },)
    return rows


def _parse_is_it_keto_csv(reader):
    rows = []
    for row in reader:
        rows.append(
            {
                'month':
                _parse_month(row['Month']),
                'unique_visitors':
                _parse_integer(row['Unique Visitors']),
                'total_pageviews':
                _parse_integer(row['Total Pageviews']),
                'domain_authority_moz':
                _parse_integer(row['Domain Authority (Moz)']),
                'ranking_keywords_moz':
                _parse_integer(row['Ranking Keywords (Moz)']),
                'domain_rating_ahrefs':
                _parse_float(row['Domain Rating (Ahrefs)']),
                'adsense_earnings':
                _parse_dollars(row['AdSense Earnings']),
                'adthrive_earnings':
                _parse_dollars(row['AdThrive Earnings']),
                'amazon_affiliate_earnings':
                _parse_dollars(row['Amazon Affiliate Earnings']),
                'other_affiliate_earnings':
                _parse_dollars(row['Kiss My Keto Affiliate Earnings']),
                'meal_plan_sales':
                _parse_dollars(row['Meal Plan Sales']),
                'total_revenue':
                _parse_dollars(row['Total Earnings']),
            },)
    return rows


def _parse_totals_csv(reader):
    rows = []
    for row in reader:
        rows.append(
            {
                'month': _parse_month(row['Month']),
                'tinypilot': _parse_dollars(row['TinyPilot']),
                'htfp': _parse_dollars(row['Hit the Front Page']),
                'isitketo': _parse_dollars(row['Is It Keto']),
                'zestful': _parse_dollars(row['Zestful']),
                'total': _parse_dollars(row['Total']),
            },)
    return rows


def _parse_month(month):
    year, month = month.split('-')
    return datetime.date(year=int(year), month=int(month), day=1)


def _parse_integer(value):
    try:
        return int(value.replace(',', ''))
    except ValueError:
        return None


def _parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def _parse_dollars(value):
    if not value.startswith('$'):
        return None
    return float(value[1:].replace(',', ''))
