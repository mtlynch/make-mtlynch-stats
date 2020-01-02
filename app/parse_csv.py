import csv
import datetime


def parse(csv_file):
    reader = csv.DictReader(csv_file)
    if 'RapidAPI Earnings' in reader.fieldnames:
        return _parse_zestful_csv(reader)
    else:
        return _parse_is_it_keto_csv(reader)


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
                'total_earnings':
                _parse_dollars(row['Total Earnings']),
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
                'amazon_affiliate_earnings':
                _parse_dollars(row['Amazon Affiliate Earnings']),
                'meal_plan_sales':
                _parse_dollars(row['Meal Plan Sales']),
                'total_earnings':
                _parse_dollars(row['Total Earnings']),
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
