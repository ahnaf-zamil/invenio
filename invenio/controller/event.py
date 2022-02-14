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
from ..app import registry
from ..service import Instance
from flask import session

import time
import logging
import uuid


def register_event_handlers(sio: SocketIO):
    sio.on_event("connect", on_connect)
    sio.on_event("disconnect", on_disconnect)


def on_connect(payload: dict = None):
    # payload sometimes can be None if debug mode is enabled on client
    if not payload:
        return

    service_name = payload["service_name"]
    instance_id = uuid.uuid4().hex
    instance_host = payload["host"]
    instance_port = payload["port"]
    instance_created_at = int(time.time())

    session["service_name"] = service_name
    session["instance_id"] = instance_id

    service = registry.get_service(service_name)
    if not service:
        service = registry.create_service(service_name)
        logging.info(f"Created new service: {service_name}")

    instance = Instance(instance_id, instance_host, instance_port, instance_created_at)
    service.add_instance(instance)
    logging.info(
        f"Added instance to service '{service_name}', Instance ID: {instance_id}"
    )


def on_disconnect():
    service = registry.get_service(session["service_name"])
    instance_id = session["instance_id"]

    service.instances = list(filter(lambda x: x.id != instance_id, service.instances))
    logging.info(f"Removed instance '{instance_id}' from service '{service.name}'")

    if not len(service.instances):
        registry.remove_service(service.name)
        logging.info(f"Service '{service.name}' has no instances, removing...")

    session.clear()
