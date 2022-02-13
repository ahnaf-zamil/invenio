# Copyright 2022 DevGuyAhnaf
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask_socketio import SocketIO
from flask import Flask
from .config import get_config
from .service import ServiceManager

import logging

app = Flask(__name__)
service_manager = ServiceManager()
config = get_config("./config.yml")
socketio = SocketIO(app)

logging.basicConfig(
    format="%(asctime)s %(levelname)s -> %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

from .controller.event import register_event_handlers  # noqa: E402
from .controller.rest import controller as rest_controller  # noqa: E402

app.register_blueprint(rest_controller)
register_event_handlers(socketio)
