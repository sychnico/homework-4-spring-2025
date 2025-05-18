class TestInsightsPage:
    def test_click_insight_card(self, insights_page):
        insights_page.click_insight_card()
        assert insights_page.find_insight_article()