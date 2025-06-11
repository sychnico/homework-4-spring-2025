ARTICLE_TITLE = "Что такое digital marketing"

class TestInsightsPage:
    def test_click_insight_card(self, insights_page):
        insights_page.click_insight_card()
        arctile = insights_page.find_insight_article()
        assert ARTICLE_TITLE in arctile.text