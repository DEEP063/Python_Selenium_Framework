from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class waitUtils:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        
    def wait_for_alert_present(self):
        """
        Wait for an alert to be present.

        Usage:
        alert = your_instance.wait_for_alert_present()
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()
        )

    def wait_for_alert_state(self, state):
        """
        Wait for the alert state to be as specified.

        Usage:
        alert_state_present = your_instance.wait_for_alert_state(True)
        # OR
        alert_state_not_present = your_instance.wait_for_alert_state(False)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.alert_state_to_be(state)
        )

    def wait_for_element_exists(self, by, value):
        """
        Wait for an element to exist.

        Usage:
        element_exists = your_instance.wait_for_element_exists(By.XPATH, "//div[@id='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_visible(self, by, value):
        """
        Wait for an element to be visible.

        Usage:
        element_visible = your_instance.wait_for_element_visible(By.XPATH, "//div[@id='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_for_element_selection_state_to_be(self, by, value, selected):
        """
        Wait for the selection state of an element to be as specified.

        Usage:
        element_selection_state = your_instance.wait_for_element_selection_state_to_be(By.XPATH, "//input[@type='checkbox']", True)
        # OR
        element_selection_state = your_instance.wait_for_element_selection_state_to_be(By.XPATH, "//input[@type='checkbox']", False)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_selection_state_to_be((by, value), selected)
        )

    def wait_for_element_selection_state_by_element(self, element, selected):
        """
        Wait for the selection state of an element to be as specified.

        Usage:
        checkbox_element = your_instance.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        element_selection_state_by_element = your_instance.wait_for_element_selection_state_by_element(checkbox_element, True)
        # OR
        element_selection_state_by_element = your_instance.wait_for_element_selection_state_by_element(checkbox_element, False)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_selection_state_to_be(element, selected)
        )

    def element_to_be_clickable(self, element):
        """
        Wait for an element to be clickable.

        Usage:
        clickable_element = your_instance.element_to_be_clickable(your_element)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(element)
        )

    def element_to_be_clickable_by_locator(self, by, value):
        """
        Wait for an element (located by a given method) to be clickable.

        Usage:
        clickable_element = your_instance.element_to_be_clickable_by_locator(By.XPATH, "//button[@id='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def element_to_be_selected(self, element, selected):
        """
        Wait for an element's selection state to be as specified.

        Usage:
        element_selected_state = your_instance.element_to_be_selected(your_element, True)
        # OR
        element_selected_state = your_instance.element_to_be_selected(your_element, False)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_selection_state_to_be(element, selected)
        )

    def element_to_be_selected_by_locator(self, by, value):
        """
        Wait for an element's selection state (located by a given method) to be as specified.

        Usage:
        element_selected_state = your_instance.element_to_be_selected_by_locator(By.XPATH, "//input[@type='checkbox']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_selection_state_to_be((by, value), True)
        )

    def element_to_be_selected_by_element(self, element):
        """
        Wait for an element's selection state to be as specified.

        Usage:
        element_selected_state = your_instance.element_to_be_selected_by_element(your_element)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_selection_state_to_be(element, True)
        )

    def frame_to_be_available_and_switch_to_it_by_locator(self, by, value):
        """
        Wait for a frame (located by a given method) to be available and switch to it.

        Usage:
        switched_frame = your_instance.frame_to_be_available_and_switch_to_it_by_locator(By.XPATH, "//iframe[@id='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.frame_to_be_available_and_switch_to_it((by, value))
        )

    def frame_to_be_available_and_switch_to_it_by_string(self, frame_locator):
        """
        Wait for a frame (located by a string) to be available and switch to it.

        Usage:
        switched_frame = your_instance.frame_to_be_available_and_switch_to_it_by_string("exampleFrame")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.frame_to_be_available_and_switch_to_it(frame_locator)
        )

    def invisibility_of_element_located(self, by, value):
        """
        Wait for an element (located by a given method) to be invisible.

        Usage:
        invisible_element = your_instance.invisibility_of_element_located(By.XPATH, "//div[@id='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located((by, value))
        )

    def invisibility_of_element_with_text(self, by, value, text):
        """
        Wait for an element (located by a given method) with specific text to be invisible.

        Usage:
        invisible_element_with_text = your_instance.invisibility_of_element_with_text(By.XPATH, "//div[@id='example']", "Example Text")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_with_text((by, value), text)
        )

    def presence_of_all_elements_located_by(self, by, value):
        """
        Wait for all elements (located by a given method) to be present.

        Usage:
        all_elements = your_instance.presence_of_all_elements_located_by(By.XPATH, "//div[@class='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def staleness_of_element(self, element):
        """
        Wait for an element to become stale.

        Usage:
        staleness = your_instance.staleness_of_element(your_element)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.staleness_of(element)
        )

    def text_to_be_present_in_element(self, element, text):
        """
        Wait for specific text to be present in an element.

        Usage:
        text_present_in_element = your_instance.text_to_be_present_in_element(your_element, "Example Text")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element(element, text)
        )

    def text_to_be_present_in_element_located(self, by, value, text):
        """
        Wait for specific text to be present in an element located by a given method.

        Usage:
        text_present_in_element_by_locator = your_instance.text_to_be_present_in_element_located(By.XPATH, "//div[@id='example']", "Example Text")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_located((by, value), text)
        )

    def text_to_be_present_in_element_value(self, by, value, text):
        """
        Wait for specific text to be present in an element's value located by a given method.

        Usage:
        text_present_in_element_value = your_instance.text_to_be_present_in_element_value(By.XPATH, "//input[@id='example']", "Example Text")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_value((by, value), text)
        )

    def text_to_be_present_in_element_value_by_element(self, element, text):
        """
        Wait for specific text to be present in an element's value.

        Usage:
        text_present_in_element_value_by_element = your_instance.text_to_be_present_in_element_value_by_element(your_element, "Example Text")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_value(element, text)
        )

    def title_contains(self, title):
        """
        Wait for the title to contain specific text.

        Usage:
        title_contains_text = your_instance.title_contains("Example Title")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.title_contains(title)
        )

    def title_is(self, title):
        """
        Wait for the title to be a specific text.

        Usage:
        title_is_text = your_instance.title_is("Example Title")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.title_is(title)
        )

    def url_contains(self, fraction):
        """
        Wait for the URL to contain specific text.

        Usage:
        url_contains_text = your_instance.url_contains("example")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(fraction)
        )

    def url_matches(self, regex):
        """
        Wait for the URL to match a regular expression.

        Usage:
        url_matches_regex = your_instance.url_matches("https://example\.com.*")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_matches(regex)
        )

    def url_to_be(self, url):
        """
        Wait for the URL to be a specific text.

        Usage:
        url_is_text = your_instance.url_to_be("https://example.com")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_to_be(url)
        )

    def visibility_of_all_elements_located_by_collection(self, elements):
        """
        Wait for all elements in a collection to be visible.

        Usage:
        all_elements_visible = your_instance.visibility_of_all_elements_located_by_collection(your_elements)
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(elements)
        )

    def visibility_of_all_elements_located_by_locator(self, by, value):
        """
        Wait for all elements located by a given method to be visible.

        Usage:
        all_elements_visible_by_locator = your_instance.visibility_of_all_elements_located_by_locator(By.XPATH, "//div[@class='example']")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )

