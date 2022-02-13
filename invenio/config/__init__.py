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

import yaml
import os
import shutil


def _create_config(path: str):
    shutil.copyfile(os.path.join(os.path.dirname(__file__), "config_default.yml"), path)


def get_config(path: str):
    if not os.path.isfile(path):
        _create_config(path)

    with open(path, "r") as fp:
        config: dict = yaml.safe_load(fp)
    return config
