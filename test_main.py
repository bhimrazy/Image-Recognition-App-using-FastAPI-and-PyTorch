from fastapi.testclient import TestClient

import main
client = TestClient(main.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_predict_route():
    file_name = 'static/images/dog.jpg'
    
    response = client.post(
        "/predict",files={"file":("dog_image",open(file_name,"rb"),"image/jpeg")}
        )
    assert response.status_code == 200