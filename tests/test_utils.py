from django.test import TestCase

from chatwork.utils import send_chatwork, delete_message, create_task


class SendChatworkTests(TestCase):
    def test_send_chatwork(self):
        response = send_chatwork('test', 1234)
        self.assertEqual(response, {'message_id': '1234'})


class DeleteMessageTests(TestCase):
    def test_delete_message(self):
        response = delete_message(1234, 'message_id')
        self.assertEqual(response, {'message_id': '1234'})


class CreateTaskTests(TestCase):
    def test_create_task(self):
        response = create_task('test', 1234, [123, 124])
        self.assertEqual(response, {'task_ids': [123, 124]})
