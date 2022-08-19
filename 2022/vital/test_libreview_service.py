from config import (
    email,
    password,
)
from libreview_service import (
    LibreViewService,
    _auth_login,
    _auth_result,
    _auth_send_code,
)

from icecream import ic


class TestLibreViewService:
    """Alternative for external calls: mock the external calls."""
    def test_authenticate_ok(self):
        LibreViewService.authenticate(email, password)
        assert LibreViewService.auth_ticket_token is not None

        LibreViewService.authenticate(email, password)
        assert LibreViewService.auth_ticket_token is not None

    def test_login_ok(self):
        # This test needs 'pytest -s' to input the email code.
        LibreViewService.email = email
        LibreViewService.password = password

        LibreViewService.login()
        assert LibreViewService.auth_ticket_token is not None

    def test_login_failed(self):
        # This test needs 'pytest -s' to input the email code.
        LibreViewService.email = 'wrong_email'
        LibreViewService.password = 'wrong_password'

        LibreViewService.login()
        assert LibreViewService.auth_ticket_token is None

    def test_getall(self):
        # This test needs 'pytest -s' to input the email code.
        start, end = '2022-04-15', '2022-04-30'
        patients_glucose = LibreViewService.getall(email, password, start, end)
        ic(patients_glucose)
        assert patients_glucose


def test__auth_login_ok():
    assert _auth_login(email, password) is not None


def test__auth_login_failed():
    assert _auth_login('wrong_email', 'wrong_password') is None


def test__auth_result_ok():
    # This test needs 'pytest -s' to input the email code.
    token = _auth_login(email, password)
    token = _auth_send_code(token)
    code = input('Email Code > ')
    assert _auth_result(code, token) is not None


def test__auth_result_failed():
    assert _auth_result('wrong_code', 'wrong_auth_ticket_token') is None


def test__auth_send_code_ok():
    token = _auth_login(email, password)
    assert _auth_send_code(token) is not None


def test__auth_send_code_failed():
    assert _auth_send_code('wrong_auth_ticket_token') is None

