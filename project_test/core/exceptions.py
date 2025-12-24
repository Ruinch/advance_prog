# core/exceptions.py


class AppError(Exception):
    """
    Base application exception.
    All custom exceptions must inherit from this class.
    """


class UserAlreadyExistsError(AppError):
    """
    Raised when trying to create a user that already exists.
    """


class UserNotFoundError(AppError):
    """
    Raised when user is not found.
    """


class InvalidCredentialsError(AppError):
    """
    Raised when email or password is invalid.
    """


class InactiveUserError(AppError):
    """
    Raised when user account is inactive.
    """


class PermissionDeniedError(AppError):
    """
    Raised when user does not have required permissions.
    """
