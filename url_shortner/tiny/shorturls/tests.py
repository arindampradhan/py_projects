from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
from .models import Link


class ShortenerText(TestCase):

    def test_shortens(self):
        """
        Test that urls get shortn
        """
        url = "http://example.com"
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))

    def test_recover_link(self):
        url = "http://example.com"
        l = Link(url=url)
        short_url = Link.shorten(l)
        l.save()

        exp_url = Link.expand(short_url)
        self.assertEqual(url, exp_url)

    def test_homepage(self):
        """
        Tests that a home page exists and it contains a form
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_shortener_form(self):
        """
        Tests that submitting the returns link object
        """
        url = "http://example.com/"
        response = self.client.post(reverse('home'),
                                    {'url': url}, follow=True)
        # print "the response: ", response
        self.assertEqual(response.status_code, 200)
        self.assertIn('link', response.context)
        l = response.context['link']
        short_url = Link.shorten(l)
        self.assertEqual(url, l.url)
        self.assertIn(short_url, response.content)

    def test_redirect_to_long_link(self):
        """
        Tests that submitting the returns link object
        """
        url = "http://example.com"
        l = Link.objects.create(url=url)
        short_url = Link.shorten(l)
        response = self.client.get(reverse('redirect_short_url',
                                           kwargs={'short_url': short_url}
                                           ))
        self.assertRedirects(response, url)
