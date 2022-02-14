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

from ..app import registry
from flask import Blueprint, abort, Response

import zlib
import json

controller = Blueprint("rest", __name__)


@controller.route("/service/all")
def get_all_services():
    return {"services": registry.all()}


@controller.route("/service/<service_name>")
def get_service(service_name: str):
    service = registry.get_service(service_name)
    return service.to_dict() if service else abort(404)


@controller.route("/service/<service_name>/instance")
def get_loadbalanced_instance(service_name: str):
    service = registry.get_service(service_name)

    if not service:
        # 503 because service is None ONLY IF no instances are available
        abort(503)

    # A very trivial round-robin cycler
    if service._last_instance_index == len(service.instances):
        service._last_instance_index = 0

    instance = service.instances[service._last_instance_index]
    service._last_instance_index += 1

    return f"{instance.host}:{instance.port}"


@controller.route("/registry/fetch")
def get_compressed_services():
    json_data = json.dumps({"services": registry.all()}, indent=0)
    resp = Response(zlib.compress(json_data.encode()))
    resp.headers["Content-Type"] = "application/octet-stream"
    return resp
