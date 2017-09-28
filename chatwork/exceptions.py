class ChatworkException(Exception):
    pass


class RoomNotFound(ChatworkException):
    pass


class TooManyRequests(ChatworkException):
    pass


class Unauthorized(ChatworkException):
    pass


class InvalidAuthToken(ChatworkException):
    pass


class NoAuthToken(ChatworkException):
    pass


class InvalidResponse(ChatworkException):
    pass


EXCEPTION_LABEL = {
    'room_not_found': RoomNotFound,
    'too_many_requests': TooManyRequests,
    'unauthorized': Unauthorized,
    'invalid_auth_token': InvalidAuthToken,
    'no_auth_token': NoAuthToken,
    'invalid_response': InvalidResponse,
}
