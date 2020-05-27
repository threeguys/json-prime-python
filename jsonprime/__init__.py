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

from .core import expression, generator, evaluate
from . import factories, simple, filters

factories.register_factories({
    'count': simple.factory_count,
    'rate': simple.factory_rate,
    'sum': simple.factory_sum,
    'const': simple.factory_const,
    'get': simple.factory_get,
    'sorted': simple.factory_sorted,
    'unique': simple.factory_unique,
    'filter': filters.factory_filter,
})
