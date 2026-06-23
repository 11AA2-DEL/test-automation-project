class TestPosts:
    def test_get_all(self,api):
        resp = api.get("/posts")
        assert resp.status_code == 200
        assert len(resp.json()) > 0
        
    def test_get_one(self,api):
        resp = api.get("/posts/1")
        assert resp.status_code == 200
        assert resp.json()["id"] == 1
        assert "title" in resp.json()


    def test_create(self,api):
        body = {"title":"测试","body":"内容","userid": 1}
        resp = api.post("/posts",body)
        assert resp.status_code == 201

#这条用例是做异常场景覆盖，保证程序对非法 / 不存在 ID 有正确处理逻辑，不会报错崩溃。
    def test_not_found(self, api):
            resp = api.get("/posts/99999")
            assert resp.status_code == 404

    def test_get_by_user(self,api):
        resp = api.get("/posts?userId=1")
        assert resp.status_code ==200
        for item in resp.json():
            assert item["userId"] == 1

    def test_get_user(self,api):
        resp = api.get("/users")
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data,list)
        assert len(data) >0
        first_user = data [0]
        assert "name" in first_user

class TestComments:
    def test_get_all(self,api):
        resp = api.get("/comments")
        assert resp.status_code ==200
        assert len(resp.json()) > 0
    def test_get_comments(self,api):
        resp = api.get("/comments?postId=1")
        assert resp.status_code ==200
        for item in resp.json():
            assert item["postId"] == 1

    def test_conmments_has_email(self,api):
        resp = api.get("/comments/1")
        assert resp.status_code ==200
        data = resp.json()
        assert "email" in data
        assert "@" in data["email"]
class TestUsers:
    def test_get_all(self,api):
        resp = api.get("/users")
        assert resp.status_code ==200
        assert len(resp.json()) > 0

    def test_get_user(self,api):
        resp = api.get("/users/1")
        assert resp.status_code == 200
        data  = resp.json()
        assert "email" in data
        assert "@" in data["email"]
        assert "name" in data
    def test_get_has_company(self,api):
        resp = api.get("/users/1")
        assert resp.status_code ==200
        data = resp.json()
        assert "company" in data
        assert "name" in data["company"]

    def test_create_users_empty_body(self,api):
        resp = api.post("/comments",{})
        assert resp.status_code == 201