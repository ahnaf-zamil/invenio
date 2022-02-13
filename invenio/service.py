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

from typing import Mapping, List
from dataclasses import dataclass


@dataclass
class Instance:
    id: str
    host: str
    port: int
    started_at: int

    def to_dict(self):
        return {
            "id": self.id,
            "host": self.host,
            "port": self.port,
            "started_at": self.started_at,
        }


@dataclass
class Service:
    name: str
    instances: List[Instance]

    _last_instance_index = 0

    def add_instance(self, instance: Instance):
        self.instances.append(instance)

    def to_dict(self):
        return {"name": self.name, "instances": [i.to_dict() for i in self.instances]}


class ServiceManager:
    def __init__(self):
        self.state: Mapping[str, Service] = {}

    def all(self):
        return [i.to_dict() for i in self.state.values()]

    def get_service(self, name: str):
        service = self.state.get(name.lower())
        return service

    def create_service(self, name: str):
        new_service = Service(name.lower(), [])
        self.state[name.lower()] = new_service
        return new_service

    def remove_service(self, name: str):
        del self.state[name.lower()]
