import requests
from jsonschema.validators import validate
from helper import load_json_schema, CustomSession, reqres_session

host = 'https://reqres.in'

def test_login_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url=f'{host}/api/login', data=data)
    assert response.status_code == 200
    assert 'token' in response.json()


def test_login_unsuccess():
    data = {
        "email": "sydney@fifen",
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_register_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'token' in response.json()


def test_register_unsuccess():
    data = {
        "email": "sydney@fifen",
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_delete():
    response = requests.delete(url=f'{host}/api/users/2')
    assert response.status_code == 204
    assert response.text == ''


def test_single_user():
    response = requests.get(url=f'{host}/api/users/2')
    assert response.status_code == 200
    assert 'id' in response.json()['data']
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['support']['url'] == 'https://reqres.in/#support-heading'


def test_single_user_not_found():
    response = requests.get(url=f'{host}/api/users/23')
    assert response.status_code == 404


def test_resource_not_found():
    response = requests.get(url=f'{host}/api/unknown/23')
    assert response.status_code == 404
    assert response.text == '{}'


def test_requested_page_number():
    response = requests.get(
        "https://reqres.in/api/users", params={"page": 2}
    )

    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert response.json()["total"] == 12


def test_users_list_default_lenght():
    response = requests.get("https://reqres.in/api/users")

    assert len(response.json()["data"]) == 6


def test_get_single_user_not_found_schema_validation():
    schema = load_json_schema("get_single_user_not_found.json")

    response = reqres_session.get("/api/users/23")

    validate(instance=response.json(), schema=schema)


def test_post_user_register_unsuccessful_schema_validation():
    email = "sydney@fife"

    schema = load_json_schema("post_user_register_unsuccessful.json")

    response = reqres_session.post("/api/register", json={"email": email})

    validate(instance=response.json(), schema=schema)


def test_post_login_successful_schema_validation():
    email = "eve.holt@reqres.in"
    password = "pistol"

    schema = load_json_schema("post_login_successful.json")

    response = reqres_session.post("/api/login", json={"email": email, "password": password})

    validate(instance=response.json(), schema=schema)


def test_post_user_register_successful_schema_validation():
    email = "eve.holt@reqres.in"
    password = "pistol"

    schema = load_json_schema("post_user_register_successful.json")

    response = reqres_session.post(
        "/api/register", json={"email": email, "password": password}
    )

    validate(instance=response.json(), schema=schema)


def test_get_list_resources_schema_validation():
    schema = load_json_schema("get_list_resources.json")

    response = reqres_session.get("/api/unknown")

    validate(instance=response.json(), schema=schema)


def test_get_single_resource_schema_validation():
    id = 2

    schema = load_json_schema("get_single_resource.json")

    response = reqres_session.get(f"/api/unknown/{id}")

    validate(instance=response.json(), schema=schema)


def test_put_update_user_schema_validation():
    name = "Kate"
    job = "leader"

    schema = load_json_schema("put_update_user_schema.json")

    response = reqres_session.put("/api/users/23", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)


def test_post_create_user_schema_validation():
    name = "jane"
    job = "job"
    schema = load_json_schema("post_create_user.json")

    response = reqres_session.post("/api/users", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)


def test_get_requested_page_number_schema_validation():
    schema = load_json_schema("get_page_number.json")

    response = reqres_session.get("/api/users")

    validate(instance=response.json(), schema=schema)


def test_get_user_list_schema_validation():
    schema = load_json_schema("get_user_list.json")

    response = reqres_session.get("/api/users")

    validate(instance=response.json(), schema=schema)
