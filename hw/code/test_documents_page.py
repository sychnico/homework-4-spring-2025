class TestDocumentsPage:
    def test_click_document_card(self, documents_page):
        documents_page.click_document_card()
        assert documents_page.find_document_article()