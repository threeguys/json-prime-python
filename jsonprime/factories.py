#
#   Copyright 2020 Ray Cole
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

_factories = {}

def get_factories():
    return _factories

def register_factories(update_factories):
    _factories.update(update_factories)
    return _factories

def register_factory(key, factory):
    return register_factories({ key: factory })
