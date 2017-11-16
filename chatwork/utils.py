from django.utils.encoding import force_text
from django.template.loader import render_to_string

from .api import ChatworkApiClient


client = ChatworkApiClient()
api_account_info = client.get_my_profile()
api_account_id = getattr(api_account_info, 'account_id', '0')
api_room_id = getattr(api_account_info, 'room_id', '0')


def get_rooms(room_type='group'):
    """ 所属するルームを取得する """
    rooms = client.get_rooms()
    return [room for room in rooms if room['type'] == room_type]


def send_chatwork(text, room, title=None, to_all=None):
    """ 一つのルームにメッセージを送信する """
    context = {
        'body': text,
        'title': title,
        'to_all': to_all,
    }
    context['members'] = [m for m in client.get_members(room)
                          if m.get('account_id') != api_account_id]
    message = force_text(render_to_string('chatwork/message.txt', context))
    return client.add_messages(room, message.strip())


def send_chatwork_many(text, rooms, title=None, to_all=None):
    """ 複数のルームにメッセージを送信する """
    results = []
    for room in rooms:
        result = send_chatwork(text, room, title=title, to_all=to_all)
        results.append(result)
    return results


def create_task(text, room, assigned_to, limit=None, **kwargs):
    """ タスクを依頼する """
    data = {
        'body': text,
        'to_ids': ','.join(list(map(str, assigned_to))),
    }
    if limit is not None:
        data['limit'] = int(limit.timestamp())
    return client.add_tasks(room, **data)
