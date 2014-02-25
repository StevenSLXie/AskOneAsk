from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import new_ask
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Qns,Ans
from unittest import skip
# Create your tests here.
'''
class HomePageTest(TestCase):

    @skip
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    @skip
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #1
        response = home_page(request) #2
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)
'''

class QnsAndAnsModelTese(TestCase):
'''
    @skip
    def test_instance_save_and_retrieve(self):
        first_qns = Qns()
        first_qns.qns = 'Which country do you like best?'
        first_qns.save()

        second_qns = Qns()
        second_qns.qns = 'Are you a Democrat or a Republican?'
        second_qns.save()

        saved_qns = Qns.objects.all()
        self.assertEqual(saved_qns.count(),2)

        first_saved_qns = saved_qns[0]
        second_saved_qns = saved_qns[1]

        self.assertEqual(first_saved_qns.qns,'Which country do you like best?')
        self.assertEqual(second_saved_qns.qns,'Are you a Democrat or a Republican?')

    @skip
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['qns_text'] = 'A new qns'

        response = new_ask(request)

        self.assertEqual(Qns.objects.all().count(), 1) #1
        new_qns = Qns.objects.all()[0] #2
        self.assertEqual(new_qns.qns, 'A new qns') #3

    def test_redirect_after_saving_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['qns_text'] = 'A new qns'

        response = new_ask(request)

        expected_html = render_to_string('qns.html')
        self.assertEqual(response.content.decode(),expected_html)
'''
    def test_model_relationship(self):
        Qns.objects.create(qns='Q1',author='A1')
        Qns.objects.create(qns='Q2',author='A2')

        q1 = Qns.objects.get(id=1)
        q2 = Qns.objects.get(id=2)
        
        q1.answerSet.add(Ans.objects.create(answer='A1',person='P1'))
        q1.answerSet.add(Ans.objects.create(answer='A2',person='P2'))

        q2.answerSet.add(Ans.objects.create(answer='A3',person='P2'))
        q2.answerSet.add(Ans.objects.create(answer='A4',person='P3'))

        self.assertIn('A1',q1.answerSet.answer)


        

