import os
import yaml
import pytest
yaml_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "test_data",
    "test_data.yaml"
)
with open(yaml_path, "r", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)

class TestBoundary:
    @pytest.mark.parametrize("case", test_data["boundary_ids"])
    def test_boundary_ids(self,api,case):
        resp = api.get(f"/posts/{case['id']}")
        assert resp.status_code == case['expected_status']
    @pytest.mark.parametrize("case", test_data["create_boundary"])
    def test_create_boundary(self,api,case):
        body = {"title": case["title"], "body": case["body"], "userID":1}
        resp = api.post("/posts", body)
        assert resp.status_code ==case["expected_status"]



