from src.shared.ui.utils import switch_to_frame, drag_n_drop, log


class TestDroppablePage:
    def test_verify_default_tab_checked(self, test_case, droppable_page):
        switch_to_frame(droppable_page.default_functionality_frame)
        destination_el_location = droppable_page.drop_to.location
        destination_el_size = droppable_page.drop_to.get_actual_webelement().size
        log.info(f'destination element location: {destination_el_location}')
        log.info(f'destination element size: {destination_el_size}')
        draggable_el_size = droppable_page.drag_from.get_actual_webelement().size
        log.info(f'element to drag n drop size: {draggable_el_size}')

        text_before = droppable_page.drop_to.text.lower()
        drag_n_drop(droppable_page.drag_from, droppable_page.drop_to)
        draggable_el_location = droppable_page.drag_from.location
        test_case.verify(
            'dropped' in droppable_page.drop_to.text.lower() and 'dropped' not in text_before, True,
            'Verify text changed after drag n drop')
        log.info(f'element after drag n drop location: {draggable_el_location}')

        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], True, 'Verifying X coordinate')
        test_case.verify(destination_el_location['y'] < draggable_el_location['y'] <= destination_el_location['y'] +
                         destination_el_size['height'], True, 'Verifying Y coordinate')

        drag_n_drop(droppable_page.drag_from, [destination_el_size['width'], 0])
        draggable_el_location = droppable_page.drag_from.location
        log.info(f'element after drag n drop location: {draggable_el_location}')
        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], False, 'Verifying OUT OF X coordinate')

    def test_verify_accept_tab_not_droppable_element(self, test_case, accept_tab_droppable_page):
        switch_to_frame(accept_tab_droppable_page.accept_tab_frame)
        log.info([x for x in accept_tab_droppable_page.droppable_elements])
        log.info([x for x in accept_tab_droppable_page.draggable_elements])
        text_before = accept_tab_droppable_page.drop_to.text
        drag_n_drop(accept_tab_droppable_page.accept_tab_drag_from_not_valid, accept_tab_droppable_page.drop_to)
        text_after = accept_tab_droppable_page.drop_to.text
        test_case.verify(text_before, text_after, 'Verify not droppable element')
        drag_n_drop(accept_tab_droppable_page.accept_tab_drag_from_not_valid, [200, 0])

        drag_n_drop(accept_tab_droppable_page.drag_from, accept_tab_droppable_page.drop_to)
        text_after = accept_tab_droppable_page.drop_to.text
        test_case.verify('dropped' in text_after.lower(), True, 'Verify droppable element')
