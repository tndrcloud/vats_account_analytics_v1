class AccountAnalyticsException(Exception):
    pass


class AlembicException(AccountAnalyticsException):
    """Migration failure"""
    