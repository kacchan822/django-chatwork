import json
import os
import traceback
import urllib.parse
import urllib.request
from urllib.error import HTTPError

from django.utils.encoding import force_text
from django.template.loader import render_to_string

from .api import ChatworkApiClient


client = ChatworkApiClient()
api_account_info = client.get_profile()
api_account_id = getattr(api_account_info, 'account_id', '0')
api_room_id = getattr(api_account_info, 'room_id', '0')


def get_rooms(room_type='group'):
    """ 所属するルームを取得する """
    rooms = client.get_rooms()
    return [room for room in rooms if room['type'] == room_type]


def send_chatwork(text, room, title=None, to_all=None):
    context = {}
    context['members'] = [m for m in client.get_members(room)
                          if m.account_id != api_account_id]
    context['body'] = text
    context['title'] = title
    message = force_text(render_to_string('chatwork/message.txt', context))

    return client.add_messages(room, message.strip())


def send_chatwork_many(text, rooms, title=None, to_all=None):
    results = []
    for room in rooms:
        result = send_chatwork(text, room, title=title, to_all=to_all,
                               fail_silently=fail_silently)
        results.append(result)
    return results
