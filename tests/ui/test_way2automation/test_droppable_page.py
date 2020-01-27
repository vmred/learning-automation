from src.shared.ui.utils import switch_to_frame, drag_n_drop, log


class TestDroppablePage:
    def test_verify_default_tab_checked(self, test_case, droppable_page):
        switch_to_frame(droppable_page.default_functionality_frame)
        destination_el_location = droppable_page.default_tab_drop_to.location
        destination_el_size = droppable_page.default_tab_drop_to.get_actual_webelement().size
        log.info(f'destination element location: {destination_el_location}')
        log.info(f'destination element size: {destination_el_size}')
        draggable_el_size = droppable_page.default_tab_drag_from.get_actual_webelement().size
        log.info(f'element to drag n drop size: {draggable_el_size}')

        text_before = droppable_page.default_tab_drop_to.text.lower()
        drag_n_drop(droppable_page.default_tab_drag_from, droppable_page.default_tab_drop_to)
        draggable_el_location = droppable_page.default_tab_drag_from.location
        test_case.verify(
            'dropped' in droppable_page.default_tab_drop_to.text.lower() and 'droppend' not in text_before, True,
            'Verify text changed after drag n drop')
        log.info(f'element after drag n drop location: {draggable_el_location}')

        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], True, 'Verifying X coordinate')
        test_case.verify(destination_el_location['y'] < draggable_el_location['y'] <= destination_el_location['y'] +
                         destination_el_size['height'], True, 'Verifying Y coordinate')

        drag_n_drop(droppable_page.default_tab_drag_from, [destination_el_size['width'], 0])
        draggable_el_location = droppable_page.default_tab_drag_from.location
        log.info(f'element after drag n drop location: {draggable_el_location}')
        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], False, 'Verifying OUT OF X coordinate')
