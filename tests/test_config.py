import pytest
from conf import AppDevConfig


@pytest.mark.unit
def test_dev_config():
    cfg = AppDevConfig
    assert hasattr(cfg, "SQLALCHEMY_DATABASE_URI")
