from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class CherryTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_type_a_qns_and_ans_a_qns(self):

		# Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Ask and Answer', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Ask A Question', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_qns')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter your question:'
        )

        #She types "which country is your favorite?" into a text box
        inputbox.send_keys('Which country is your favorite?')
        inputbox.send_keys(Keys.ENTER)

		#When she hits enter, the page updates and the question is saved to the server. At the
		#same time, a question pop up and she is invited to answer the question

		#Cherry types the answer into a text box.

		#When she hits enter, the answer is saved and she goes back to sleep.
        self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()

