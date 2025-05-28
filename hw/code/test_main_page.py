class TestMainPage:
	def test_click_news_button(self, main_page):
		main_page.click_news_button()
		assert main_page.find_news_card()

	def test_click_events_button(self, main_page):
		main_page.click_events_button()
		assert main_page.find_event_card()

	def test_click_cases_button(self, main_page):
		main_page.click_cases_button()
		assert main_page.find_case_card()

	def test_click_insights_button(self, main_page):
		main_page.click_insights_button()
		assert main_page.find_insight_card()

	def test_click_partner_button(self, main_page):
		main_page.click_partner_button()
		assert main_page.check_partner_redirect()

	def test_click_signup_button(self, main_page):
		main_page.click_signup_button()
		assert main_page.check_signup_redirect()

	def test_click_expert_button(self, main_page):
		main_page.click_expert_button()
		assert main_page.check_expert_redirect()

	def test_click_help_button(self, main_page):
		main_page.click_help_button()
		assert main_page.check_help_redirect()

	def test_click_documents_button(self, main_page):
		main_page.click_documents_button()
		assert main_page.check_documents_redirect()