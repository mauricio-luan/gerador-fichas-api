# Tomticket
class TomticketApiError(Exception):
    pass


class TicketNotFountError(TomticketApiError):
    pass


class AuthenticationError(TomticketApiError):
    pass
