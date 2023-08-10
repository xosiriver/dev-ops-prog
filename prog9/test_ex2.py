import stufftotest
import pytest

class TestClass:

    def test_one(self):
        x = "hello"
        x = stufftotest.change(x)
        assert "h" in x

    def test_three(self):
        with pytest.raises(ValueError):
            stufftotest.exceg()