from jsonschema.validators import validate
from helper import load_json_schema, CustomSession, reqres_session

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
    name = "John"
    job = "Boss"

    schema = load_json_schema("put_update_user_schema.json")

    response = reqres_session.put("/api/users/23", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)


def test_post_create_user_schema_validation():
    name = "John"
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
