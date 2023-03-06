import pytest


@pytest.fixture()
def set_up():
    print('\nНачало теста.')
    yield
    print('\nКонец теста.')

@pytest.fixture(scope="module")
def set_group():
    print('\nВход в систему.')
    yield
    print('\nВыход из системы.')