class TestCasesPage:
    def test_click_case_card(self, cases_page):
        cases_page.click_case_card()
        assert cases_page.find_case_article()