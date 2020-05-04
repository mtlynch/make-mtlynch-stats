import unittest

from app import markdown_table


class MarkdownTableTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_generate(self):
        self.assertEqual(
            """
| Metric                    | September 2019 | October 2019 | Change                                      |
| ------------------------- | -------------- | ------------ | ------------------------------------------- |
| Unique Visitors           | 28,768         | 26,315       | <font color="red">-2,453 (-9%)</font>       |
| Total Pageviews           | 75,487         | 66,578       | <font color="red">-8,909 (-12%)</font>      |
| AdSense Earnings          | $178.79        | $75.65       | <font color="red">-$103.14 (-58%)</font>    |
| Amazon Affiliate Earnings | $150.06        | $159.02      | <font color="green">+$8.96 (+6%)</font>     |
| Meal Plan Sales           | N/A            | $23.87       | N/A                                         |
| **Total Earnings**        | **$328.85**    | **$258.54**  | **<font color="red">-$70.31 (-21%)</font>** |
""".strip(),
            markdown_table.generate([
                ['Metric', 'September 2019', 'October 2019', 'Change'],
                ['Unique Visitors', '28,768', '26,315', '-2,453 (-9%)'],
                ['Total Pageviews', '75,487', '66,578', '-8,909 (-12%)'],
                ['AdSense Earnings', '$178.79', '$75.65', '-$103.14 (-58%)'],
                [
                    'Amazon Affiliate Earnings', '$150.06', '$159.02',
                    '+$8.96 (+6%)'
                ],
                ['Meal Plan Sales', 'N/A', '$23.87', 'N/A'],
                ['Total Earnings', '$328.85', '$258.54', '-$70.31 (-21%)'],
            ]))
