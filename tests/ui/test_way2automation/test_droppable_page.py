from src.shared.ui.utils import switch_to_frame, drag_n_drop, log


class TestDroppablePage:
    def test_verify_default_tab_checked(self, test_case, droppable_page):
        switch_to_frame(droppable_page.default_functionality_frame)
        destination_el_location = droppable_page.default_tab_droppable.location
        destination_el_size = droppable_page.default_tab_droppable.get_actual_webelement().size
        log.info(f'destination element location: {destination_el_location}')
        log.info(f'destination element size: {destination_el_size}')
        draggable_el_size = droppable_page.default_tab_draggable.get_actual_webelement().size
        log.info(f'element to drag n drop size: {draggable_el_size}')

        drag_n_drop(droppable_page.default_tab_draggable, droppable_page.default_tab_droppable)
        draggable_el_location = droppable_page.default_tab_draggable.location
        log.info(f'element after drag n drop location: {draggable_el_location}')

        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], True, 'Verifying X coordinate')
        test_case.verify(destination_el_location['y'] < draggable_el_location['y'] <= destination_el_location['y'] +
                         destination_el_size['height'], True, 'Verifying Y coordinate')

        drag_n_drop(droppable_page.default_tab_draggable, [destination_el_size['width'], 0])
        draggable_el_location = droppable_page.default_tab_draggable.location
        log.info(f'element after drag n drop location: {draggable_el_location}')
        test_case.verify(destination_el_location['x'] < draggable_el_location['x'] <= destination_el_location['x'] +
                         destination_el_size['width'], False, 'Verifying OUT OF X coordinate')
