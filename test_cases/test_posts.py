class TestPosts:
    def test_get_all(self,api):
        resp = api.get("/posts")
        assert resp.status_code == 200
    def test_create(self,api):
        body = {"title":"测试","body":"内容","userid": 1}
        resp = api.post("/posts",body)
        assert resp.status_code == 201