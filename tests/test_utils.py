from django.test import TestCase

from chatwork.utils import send_chatwork


class SendChatworkTests(TestCase):
    def test_send_chatwork(self):
        response = send_chatwork('test', 1234)
        self.assertEqual(response, {'message_id': '1234'})
