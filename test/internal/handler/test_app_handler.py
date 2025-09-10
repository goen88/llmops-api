import pytest

from pkg.response import HttpCode

class TestAppHandler:
    '''AppHanler 测试类'''

    @pytest.mark.parametrize('query',[None,'你好，你是？'])
    def test_completion(self,query,client):
        r = client.post('/app/completion',json={"query": query})
        assert r.status_code == 200

        if query == None:
            assert r.json.get('code') == HttpCode.VALIDATION_ERROR
        else:
            assert r.json.get('code') == HttpCode.SUCCESS

        print("响应内容",r.json)

