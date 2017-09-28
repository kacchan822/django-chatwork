import urllib.parse

from .backends import get_backend


class ChatworkApiClient(object):
    """ API Base Class """

    def __init__(self, backend=None, api_token=None, endpoint=None):
        self.backend = get_backend(backend)(api_token=api_token,
                                            endpoint=endpoint)

    def get_my_profile(self):
        """ 自分自身の情報を取得 """
        return self.backend.get('/me')

    def get_my_status(self):
        """ 自分の未読数、未読To数、未完了タスク数を取得 """
        return self.backend.get('/my/status')

    def get_my_tasks(self, **kwargs):
        """ 自分のタスク一覧を取得（最大100件）

            絞り込み条件
            assigned_by_account_id: タスク依頼者のアカウントID
            status: タスクのステータス（open、doneのいずれか）
        """
        uri = '/my/tasks'
        query = [(key, val) for key, val in kwargs.items() if val]
        uri += '?' + urllib.parse.urlencode(query)
        return self.backend.get(uri)

    def get_contacts(self):
        """ 自分のコンタクト一覧

            コンタクトになっているユーザーの情報が辞書のリストで得られる
        """
        return self.backend.get('/contacts')

    def get_rooms(self):
        """ 自分のチャット一覧 """
        return self.backend.get('/rooms')

    def add_room(self, **kwargs):
        """ グループチャットを新規作成

            必須のkwargs
            member_admin_ids: 管理者権限のユーザー
            name: グループチャット名
        """
        return self.backend.post('/rooms', data=kwargs)

    def get_room(self, room_id):
        """ チャットの名前、アイコン、種類(my/direct/group)を取得 """
        uri = '/rooms/' + str(room_id)
        return self.backend.get(uri)

    def mod_room(self, room_id, **kwargs):
        """ チャットの名前、アイコンをアップデート

        """
        uri = '/rooms/' + str(room_id)
        return self.backend.put(uri, data=kwargs)

    def del_room(self, room_id, action_type):
        """ グループチャットを退席/削除する

            action_type: leave/delete
        """
        data = {'action_type': action_type}
        uri = '/rooms/' + str(room_id)
        return self.backend.delete(uri, data=data)

    def get_members(self, room_id):
        """ チャットのメンバー一覧を取得 """
        uri = '/rooms/{0}/members'.format(room_id)
        return self.backend.get(uri)

    def mod_members(self, room_id, **kwargs):
        """ チャットのメンバーを一括変更 """
        uri = '/rooms/{0}/members'.format(room_id)
        return self.backend.put(uri, data=kwargs)

    def get_messages(self, room_id, force=False):
        """ チャットのメッセージ一覧を取得（最大100件まで）

            force=False: 前回取得分からの差分のみ
        """
        uri = '/rooms/{0}/messages'.format(room_id)
        if force:
            uri += '?force=1'
        return self.backend.get(uri)

    def add_messages(self, room_id, message):
        """ チャットに新しいメッセージを追加 """
        data = {'body': message}
        uri = '/rooms/{0}/messages'.format(room_id)
        return self.backend.post(uri, data=data)

    def get_message(self, room_id, message_id):
        """ メッセージ情報を取得 """
        uri = '/rooms/{0}/messages/{1}'.format(room_id, message_id)
        return self.backend.get(uri)

    def get_tasks(self, room_id):
        """ チャットのタスク一覧を取得（100件まで）"""
        uri = '/rooms/{0}/tasks'.format(room_id)
        return self.backend.get(uri)

    def add_tasks(self, room_id, **kwargs):
        """ チャットに新しいタスクを追加 """
        uri = '/rooms/{0}/tasks'.format(room_id)
        return self.backend.post(uri, data=kwargs)

    def get_task(self, room_id, task_id):
        """ タスク情報を取得 """
        uri = '/rooms/{0}/tasks/{1}'.format(room_id, task_id)
        return self.backend.get(uri)

    def get_files(self, room_id):
        """ チャットのファイル一覧を取得（100件まで) """
        uri = '/rooms/{0}/files'.format(room_id)
        return self.backend.get(uri)

    def get_file(self, room_id, file_id):
        """ ファイル情報を取得 """
        uri = '/rooms/{0}/files/{1}'.format(room_id, file_id)
        return self.backend.get(uri)

    def get_incoming_requests(self):
        """ 自分に対するコンタクト承認依頼の一覧 """
        return self.backend.get('/incoming_requests')

    def allow_incoming_request(self, request_id):
        """ 自分に対するコンタクト承認依頼を承認する """
        uri = '/incoming_requests/{0}'.format(request_id)
        return self.backend.put(uri)

    def disallow_incoming_request(self, request_id):
        """ 自分に対するコンタクト承認依頼をキャンセルする """
        uri = '/incoming_requests/{0}'.format(request_id)
        return self.backend.delete(uri)
