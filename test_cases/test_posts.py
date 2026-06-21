class TestPosts:
    def test_get_all(self,api):
        resp = api.get("/posts")
        assert resp.status_code == 200
        assert len(resp.json()) > 0
        
    def test_get_one(self,api):
        resp = api.get("/posts/1")
        assert resp.status_code == 200
        assert resp.json()["id"] == 1

    def test_create(self,api):
        body = {"title":"测试","body":"内容","userid": 1}
        resp = api.post("/posts",body)
        assert resp.status_code == 201

    def test_not_found(self, api):
            resp = api.get("/posts/99999")
            assert resp.status_code == 404