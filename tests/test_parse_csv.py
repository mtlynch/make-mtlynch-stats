import datetime
import io
import unittest

from app import parse_csv


class ParseCsvTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_parse(self):
        dummy_file = io.StringIO("""
Month,Unique Visitors,Total Pageviews,Domain Authority (Moz),Ranking Keywords (Moz),Domain Rating (Ahrefs),AdSense Earnings,Amazon Affiliate Earnings,Meal Plan Sales
2019-9,"28,768","75,487",10,"2,330",N/A,$178.79,$150.06,N/A
2019-10,"26,315","66,578",13,"1,574",N/A,$75.65,$159.02,$23.87
""".strip())
        self.assertEqual([
            {
                'month': datetime.date(year=2019, month=9, day=1),
                'unique_visitors': 28768,
                'total_pageviews': 75487,
                'domain_authority_moz': 10,
                'ranking_keywords_moz': 2330,
                'domain_rating_ahrefs': None,
                'adsense_earnings': 178.79,
                'amazon_affiliate_earnings': 150.06,
                'meal_plan_sales': None,
            },
            {
                'month': datetime.date(year=2019, month=10, day=1),
                'unique_visitors': 26315,
                'total_pageviews': 66578,
                'domain_authority_moz': 13,
                'ranking_keywords_moz': 1574,
                'domain_rating_ahrefs': None,
                'adsense_earnings': 75.65,
                'amazon_affiliate_earnings': 159.02,
                'meal_plan_sales': 23.87,
            },
        ], parse_csv.parse(dummy_file))
