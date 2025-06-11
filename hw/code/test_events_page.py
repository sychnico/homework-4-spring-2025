ARTICLE_TITLE = "Бизнес-прожарка"

class TestEventsPage:
    def test_click_event_card(self, events_page):
        events_page.click_event_card()
        arctile = events_page.find_event_article()
        assert ARTICLE_TITLE in arctile.text