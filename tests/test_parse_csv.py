import datetime
import io
import unittest

from app import parse_csv
from app import projects


class ParseCsvTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_parse_is_it_keto_csv(self):
        dummy_file = io.StringIO("""
Month,Unique Visitors,Total Pageviews,Domain Authority (Moz),Ranking Keywords (Moz),Domain Rating (Ahrefs),AdSense Earnings,Amazon Affiliate Earnings,Meal Plan Sales,Total Earnings
2019-9,"28,768","75,487",10,"2,330",N/A,$178.79,$150.06,N/A,$328.85
2019-10,"26,315","66,578",13,"1,574",N/A,$75.65,$159.02,$23.87,$258.54
""".strip())
        parsed_actual, project_actual = parse_csv.parse(dummy_file)
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
                'total_earnings': 328.85,
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
                'total_earnings': 258.54,
            },
        ], parsed_actual)
        self.assertEqual(projects.IS_IT_KETO, project_actual)

    def test_parse_zestful_csv(self):
        dummy_file = io.StringIO("""
Month,Unique Visitors,Total Pageviews,RapidAPI Earnings,Enterprise Plan Earnings,Total Earnings,RapidAPI Earnings (after fees),Enterprise Plan Earnings (after fees)
2019-11,232,320,$81.66,$0.00,$65.33,$65.33,$0.00
2019-12,207,594,$65.30,"$4,000.00","$3,935.94",$52.24,"$3,883.70"
""".strip())
        parsed_actual, project_actual = parse_csv.parse(dummy_file)
        self.assertEqual([
            {
                'month': datetime.date(year=2019, month=11, day=1),
                'unique_visitors': 232,
                'total_pageviews': 320,
                'rapidapi_earnings': 65.33,
                'enterprise_plan_earnings': 0.0,
                'total_earnings': 65.33,
            },
            {
                'month': datetime.date(year=2019, month=12, day=1),
                'unique_visitors': 207,
                'total_pageviews': 594,
                'rapidapi_earnings': 52.24,
                'enterprise_plan_earnings': 3883.7,
                'total_earnings': 3935.94,
            },
        ], parsed_actual)
        self.assertEqual(projects.ZESTFUL, project_actual)
