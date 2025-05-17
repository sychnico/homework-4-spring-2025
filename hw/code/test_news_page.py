class TestNewsPage:
    def test_click_news_card(self, news_page):
        news_page.click_news_card()
        assert news_page.find_news_article()

    # def test_click_pagination(self, news_page):
    #     news_page.click_pagination()
    #     assert news_page.find_page_in_url()