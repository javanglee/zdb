#-*- encoding=utf8 -*-
import pytest

class TestClass(object):
    def test_zne(self):
        x = "this"
        assert 'h' in x

    @pytest.mark.slow
    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')

    def test_a(self):
        assert 1==2