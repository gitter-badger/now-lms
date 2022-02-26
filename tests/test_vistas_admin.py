# Copyright 2020 William José Moreno Reyes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Contributors:
# - William José Moreno Reyes

# pylint: disable=redefined-outer-name
import pytest
from now_lms import app, database, init_app, Configuracion, crear_usuarios_predeterminados, log

app.config["SECRET_KEY"] = "jgjañlsldaksjdklasjfkjj"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config["DEBUG"] = True
app.app_context().push()

with app.app_context():
    database.drop_all()
    database.create_all()
    config = Configuracion(
        titulo="NOW LMS",
        descripcion="Sistema de aprendizaje en linea.",
    )
    database.session.add(config)
    database.session.commit()
    crear_usuarios_predeterminados()

app.app_context().push()


def test_dummy():
    assert app.config["DEBUG"] == True


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def runner():
    return app.test_cli_runner()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self):
        return self._client.post("/login", data={"usuario": "lms-admin", "acceso": "lms-admin"})

    def logout(self):
        return self._client.get("/salir")


@pytest.fixture
def auth(client):
    return AuthActions(client)


def test_login(client):
    response = client.get("/login")
    assert b"Inicio" in response.data
    assert b"BMO Soluciones" in response.data


def test_app(client, auth):
    auth.login()
    response = client.get("/panel")
    log.error(response.data)

    assert b"Administrador del Sistema." in response.data
