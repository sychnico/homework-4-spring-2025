ARTICLE_TITLE = "Как получать целевые обращения"

class TestCasesPage:
    def test_click_case_card(self, cases_page):
        cases_page.click_case_card()
        arctile = cases_page.find_case_article()
        assert ARTICLE_TITLE in arctile.text