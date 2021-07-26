from unittest import TestCase

from adaptivecards import types
from adaptivecards.adaptivecard import AdaptiveCard, TeamsAdaptiveMessage
from adaptivecards.elements import TextBlock
from adaptivecards.containers import Column, ColumnSet, Container, FactSet, Fact
from adaptivecards.types import SpacingType


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

    def generate_weekly_notification(self):
        card = AdaptiveCard()
        card.body = [
            Container(
                items=[
                    TextBlock(text="DOS - Weekly Coverage Report", size=types.FontSize.EXTRA_LARGE, wrap=True),
                    TextBlock(text="Reported week: W35", isSubtle=True, spacing=types.SpacingType.NONE, wrap=True),
                    TextBlock(
                        text="The weekly coverage report summaries **New Code Coverage** and **Overall Coverage** "
                             "at portfolio level for W35 and comparisons to previous week.",
                        spacing=SpacingType.SMALL, wrap=True),
                ]
            ),
            Container(
                spacing=SpacingType.MEDIUM,
                items=[
                    ColumnSet(separator=True, columns=[
                        Column(width="stretch", items=[
                            TextBlock(text="Coverage", size=types.FontSize.MEDIUM,
                                      weight=types.FontWeight.BOLDER, wrap=True,
                                      color=types.ColorType.ACCENT,
                                      spacing=SpacingType.NONE),
                            TextBlock(text="32.99% ", size=types.FontSize.EXTRA_LARGE, wrap=True,
                                      spacing=SpacingType.NONE),
                            TextBlock(text="▲ 1.24 (3.22%)",
                                      wrap=True, spacing=SpacingType.NONE,
                                      color=types.ColorType.GOOD),
                        ]),
                        Column(width="auto", items=[
                            FactSet(facts=[
                                Fact(title="Average", value="32.99% "),
                                Fact(title="Max", value="33.24% "),
                                Fact(title="Min", value="30.23% "),
                            ])
                        ]),
                    ])
                ]
            ),
            Container(
                spacing=SpacingType.MEDIUM,
                items=[
                    ColumnSet(separator=True, columns=[
                        Column(width="stretch", items=[
                            TextBlock(text="New Code Coverage",
                                      size=types.FontSize.MEDIUM,
                                      weight=types.FontWeight.BOLDER, wrap=True,
                                      color=types.ColorType.ACCENT,
                                      spacing=SpacingType.NONE),
                            TextBlock(text="47.47% ", size=types.FontSize.EXTRA_LARGE, wrap=True,
                                      spacing=SpacingType.NONE),
                            TextBlock(
                                text="▼ 1.40 (3.45%)",
                                wrap=True, spacing=SpacingType.NONE,
                                color=types.ColorType.ATTENTION),
                        ]),
                        Column(width="auto", items=[
                            FactSet(facts=[
                                Fact(title="Average", value="47.47% "),
                                Fact(title="Max", value="50.05% "),
                                Fact(title="Min", value="45.05% "),
                            ])
                        ]),
                    ])
                ]
            )
        ]
        message = TeamsAdaptiveMessage(card)
        return message

    def test_weekly_notification(self):
        import json
        with open('weekly_coverage_expected.json') as fin:
            test_data = json.load(fin)
        message = self.generate_weekly_notification()

        jstr = str(message)
        # with open('weekly_coverage_expected.json', 'wt') as fout:
        #     fout.write(jstr)
        generated_data = json.loads(jstr)

        self.maxDiff = None
        self.assertDictEqual(test_data, generated_data)
