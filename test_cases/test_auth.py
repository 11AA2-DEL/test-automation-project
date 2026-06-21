class TestAuth:
    def test_set_token(self, api):
        api.set_token("fake-token-123")
        assert api.session.headers["Authorization"] =="Bearer fake-token-123"

    def test_get_without_token(self, api):
        resp = api.get("/posts/1")
        assert resp.status_code ==200
