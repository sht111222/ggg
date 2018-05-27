import allure

import pytest


class Test01:


    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("aaa",[1,2,3])
    def test001(self,aaa):
        assert aaa == 1
    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("aaa",[4,2,3])
    def test002(self,aaa):
        assert aaa != 1
