import pytest
import influxdb_client_python_boost


def test_sum_as_string():
    assert influxdb_client_python_boost.sum_as_string(1, 1) == "2"
