class TestEventsPage:
    def test_click_event_card(self, events_page):
        events_page.click_event_card()
        assert events_page.find_event_article()