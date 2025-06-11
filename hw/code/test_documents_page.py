ARTICLE_TITLE = "Оферта на оказание рекламных услуг"

class TestDocumentsPage:
    def test_click_document_card(self, documents_page):
        documents_page.click_document_card()
        arctile = documents_page.find_document_article()
        assert ARTICLE_TITLE in arctile.text