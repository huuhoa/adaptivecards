from unittest import TestCase
from adaptivecards.adaptivecard import AdaptiveCard


class TestAdaptiveCard(TestCase):
    def test_generate_card(self):
        apt = AdaptiveCard()
        obj = apt.render()
        expected = {
            'type': 'AdaptiveCard',
            'version': '1.2',
            '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json'
        }
        self.assertDictEqual(obj, expected)

