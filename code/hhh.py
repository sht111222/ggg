import pytest


class Test01:
    @pytest.mark.parametrize("aaa",[1,2,3])
    def test001(self,aaa):
        print('aaa')
        return aaa
