import csv
import datetime


def parse(csv_file):
    reader = csv.DictReader(csv_file)
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
    return float(value[1:])
