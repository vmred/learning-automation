from src.shared.ui.utils import switch_to_frame, drag_n_drop


class TestDroppablePage:
    def test_verify_default_tab_checked(self, test_case, droppable_page):
        switch_to_frame(droppable_page.default_functionality_frame)
        drag_n_drop(droppable_page.default_tab_draggable, droppable_page.default_tab_droppable)
        # TODO add assert here
