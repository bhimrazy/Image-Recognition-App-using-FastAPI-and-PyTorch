from fastapi.testclient import TestClient

import main
client = TestClient(main.app)


def test_home_route():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_route():
    file_name = 'static/images/dog.jpg'
    
    response = client.post(
        "/predict",files={"file":("dog_image",open(file_name,"rb"),"image/jpeg")}
        )
    assert response.status_code == 200