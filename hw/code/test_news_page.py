ARTICLE_TITLE = "Повышайте эффективность Промо в Дзене"

class TestNewsPage:
    def test_click_news_card(self, news_page):
        news_page.click_news_card()
        arctile = news_page.find_news_article()
        assert ARTICLE_TITLE in arctile.text
