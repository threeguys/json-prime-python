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

import jsonpath_ng
import jsonpath_ng.ext

from .factories import get_factories

def generator(expression_list, data):
    for expr in expression_list:
        yield expression(expr, data)

def expression(expr, data):
    if isinstance(expr, list):
        return [expression(e, data) for e in expr]
    elif isinstance(expr, dict):
        return evaluate(expr, data)
    elif isinstance(expr, str):
        return find(expr, data)
    else:
        raise ValueError('Unknown expression: %s' % str(expr))

def find(expr, data):
    return [m.value for m in jsonpath_ng.ext.parse(expr).find(data)]

def action_generator(expr):
    factories = get_factories()
    for c in set(expr.keys()).intersection(factories.keys()):
        yield factories[c](expr)

def evaluate(expr, data):
    accumulator = data
    for action in action_generator(expr):
        accumulator = action(accumulator)
    return accumulator

def object_reduce(obj, func, other=None):
    if isinstance(obj, list):
        return func(obj)
    elif other is not None:
        return other
    return obj
