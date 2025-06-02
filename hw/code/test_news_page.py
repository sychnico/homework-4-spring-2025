class TestNewsPage:
    def test_click_news_card(self, news_page):
        news_page.click_news_card()
        assert news_page.find_news_article()
