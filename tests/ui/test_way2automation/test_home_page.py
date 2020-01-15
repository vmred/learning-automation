class TestHomePage:
    def test_one(self, home_page, test_case):
        pass

    def test_go_to_droppable_page(self, droppable_page, test_case):
        test_case.verify(droppable_page.page_content.is_displayed(), True)
