from django.test import TestCase

from chatwork.utils import send_chatwork, create_task


class SendChatworkTests(TestCase):
    def test_send_chatwork(self):
        response = send_chatwork('test', 1234)
        self.assertEqual(response, {'message_id': '1234'})


class CreateTaskTests(TestCase):
    def test_create_task(self):
        response = create_task('test', 1234, [123, 124])
        self.assertEqual(response, {'task_ids': [123, 124]})
