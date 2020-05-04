import datetime
import unittest

from app import csv_to_table
from app import projects


class ConvertTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_converts_normal_numbers(self):
        self.assertEqual([
            ['Metric', 'September 2019', 'October 2019', 'Change'],
            ['Unique Visitors', '28,768', '26,315', '-2,453 (-9%)'],
            ['Total Pageviews', '75,487', '66,578', '-8,909 (-12%)'],
            ['Domain Rating (Ahrefs)', '4.3', '26.0', '+21.7 (+505%)'],
            ['AdSense Earnings', '$178.79', '$75.65', '-$103.14 (-58%)'],
            ['Amazon Affiliate Earnings', '$150.06', '$159.02', '+$8.96 (+6%)'],
            ['Meal Plan Sales', 'N/A', '$23.87', 'N/A'],
            ['Total Earnings', '$328.85', '$258.54', '-$70.31 (-21%)'],
        ],
                         csv_to_table.convert(
                             projects.IS_IT_KETO,
                             {
                                 'month': datetime.date(
                                     year=2019, month=9, day=1),
                                 'unique_visitors': 28768,
                                 'total_pageviews': 75487,
                                 'domain_authority_moz': 10,
                                 'ranking_keywords_moz': 2330,
                                 'domain_rating_ahrefs': 4.3,
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
                                 'domain_rating_ahrefs': 26.0,
                                 'adsense_earnings': 75.65,
                                 'amazon_affiliate_earnings': 159.02,
                                 'meal_plan_sales': 23.87,
                                 'total_earnings': 258.54,
                             },
                         ))

    def test_handles_zeroes_properly_on_right_side(self):
        self.assertEqual(
            [
                ['Metric', 'September 2019', 'October 2019', 'Change'],
                ['Unique Visitors', '28,768', '0', '-28,768 (-100%)'],
                ['Total Pageviews', '75,487', '0', '-75,487 (-100%)'],
                ['Domain Rating (Ahrefs)', '4.3', '0.0', '-4.3 (-100%)'],
                ['AdSense Earnings', '$178.79', '$0.00', '-$178.79 (-100%)'],
                [
                    'Amazon Affiliate Earnings', '$150.06', '$0.00',
                    '-$150.06 (-100%)'
                ],
                ['Meal Plan Sales', '$5.50', '$0.00', '-$5.50 (-100%)'],
                ['Total Earnings', '$334.35', '$0.00', '-$334.35 (-100%)'],
            ],
            csv_to_table.convert(
                projects.IS_IT_KETO,
                {
                    'month': datetime.date(year=2019, month=9, day=1),
                    'unique_visitors': 28768,
                    'total_pageviews': 75487,
                    'domain_authority_moz': 10,
                    'ranking_keywords_moz': 2330,
                    'domain_rating_ahrefs': 4.3,
                    'adsense_earnings': 178.79,
                    'amazon_affiliate_earnings': 150.06,
                    'meal_plan_sales': 5.50,
                    'total_earnings': 334.35,
                },
                {
                    'month': datetime.date(year=2019, month=10, day=1),
                    'unique_visitors': 0,
                    'total_pageviews': 0,
                    'domain_authority_moz': 0,
                    'ranking_keywords_moz': 0,
                    'domain_rating_ahrefs': 0,
                    'adsense_earnings': 0.0,
                    'amazon_affiliate_earnings': 0.0,
                    'meal_plan_sales': 0.0,
                    'total_earnings': 0.0,
                },
            ))

    def test_handles_zeroes_properly_on_left_side(self):
        self.assertEqual(
            [
                ['Metric', 'September 2019', 'October 2019', 'Change'],
                ['Unique Visitors', '0', '28,768', '+28,768 (+inf%)'],
                ['Total Pageviews', '0', '75,487', '+75,487 (+inf%)'],
                ['Domain Rating (Ahrefs)', '0.0', '26.0', '+26.0 (+inf%)'],
                ['AdSense Earnings', '$0.00', '$178.79', '+$178.79 (+inf%)'],
                [
                    'Amazon Affiliate Earnings', '$0.00', '$150.06',
                    '+$150.06 (+inf%)'
                ],
                ['Meal Plan Sales', '$0.00', '$5.50', '+$5.50 (+inf%)'],
                ['Total Earnings', '$0.00', '$334.35', '+$334.35 (+inf%)'],
            ],
            csv_to_table.convert(
                projects.IS_IT_KETO,
                {
                    'month': datetime.date(year=2019, month=9, day=1),
                    'unique_visitors': 0,
                    'total_pageviews': 0,
                    'domain_authority_moz': 0,
                    'ranking_keywords_moz': 0,
                    'domain_rating_ahrefs': 0,
                    'adsense_earnings': 0.0,
                    'amazon_affiliate_earnings': 0.0,
                    'meal_plan_sales': 0.0,
                    'total_earnings': 0.0,
                },
                {
                    'month': datetime.date(year=2019, month=10, day=1),
                    'unique_visitors': 28768,
                    'total_pageviews': 75487,
                    'domain_authority_moz': 10,
                    'ranking_keywords_moz': 2330,
                    'domain_rating_ahrefs': 26.0,
                    'adsense_earnings': 178.79,
                    'amazon_affiliate_earnings': 150.06,
                    'meal_plan_sales': 5.50,
                    'total_earnings': 334.35,
                },
            ))
