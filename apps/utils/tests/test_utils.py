import pytest

from apps.utils.cron import fetch_and_update_currencies


@pytest.mark.django_db
def test_fetch_and_update_currencies_success():
    result = fetch_and_update_currencies()
    assert result == 'Currency data updated successfully.'
