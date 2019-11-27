import datetime
import unittest

from app import csv_to_table


class ConvertTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_convert(self):
        self.assertEqual([
            ['Metric', 'September 2019', 'October 2019', 'Change'],
            ['Unique Visitors', '28,768', '26,315', '-2,453 (-9%)'],
            ['Total Pageviews', '75,487', '66,578', '-8,909 (-12%)'],
            ['Domain Authority (Moz)', '10', '13', '+3 (+30%)'],
            ['Ranking Keywords (Moz)', '2,330', '1,574', '-756 (-32%)'],
            ['AdSense Earnings', '$178.79', '$75.65', '-$103.14 (-58%)'],
            ['Amazon Affiliate Earnings', '$150.06', '$159.02', '+$8.96 (+6%)'],
            ['Meal Plan Sales', 'N/A', '$23.87', 'N/A'],
            ['Total Earnings', '$328.85', '$258.54', '-$70.31 (-21%)'],
        ],
                         csv_to_table.convert(
                             {
                                 'month': datetime.date(
                                     year=2019, month=9, day=1),
                                 'unique_visitors': 28768,
                                 'total_pageviews': 75487,
                                 'domain_authority_moz': 10,
                                 'ranking_keywords_moz': 2330,
                                 'domain_rating_ahrefs': None,
                                 'adsense_earnings': 178.79,
                                 'amazon_affiliate_earnings': 150.06,
                                 'meal_plan_sales': None,
                                 'total_earnings': 328.85,
                             },
                             {
                                 'month': datetime.date(
                                     year=2019, month=10, day=1),
                                 'unique_visitors': 26315,
                                 'total_pageviews': 66578,
                                 'domain_authority_moz': 13,
                                 'ranking_keywords_moz': 1574,
                                 'domain_rating_ahrefs': None,
                                 'adsense_earnings': 75.65,
                                 'amazon_affiliate_earnings': 159.02,
                                 'meal_plan_sales': 23.87,
                                 'total_earnings': 258.54,
                             },
                         ))
