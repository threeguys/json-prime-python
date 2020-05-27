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

from .core import expression, object_reduce

def factory_const(config):
    value = config['const']
    def expr_const(data):
        return value
    return expr_const

def factory_count(config):
    expr = config['count']
    def expr_count(data):
        return object_reduce(expression(expr, data), lambda x: len(x), other=1)
    return expr_count

def factory_sum(config):
    expr = config['sum']
    def expr_sum(data):
        return object_reduce(expression(expr, data), lambda x: sum(x, 0))
    return expr_sum

def factory_rate(config):
    n_expr = config['rate']['n']
    d_expr = config['rate']['d']
    def expr_rate(data):
        return expression(n_expr, data) / expression(d_expr, data)
    return expr_rate

def factory_get(config):
    expr = config['get']
    def expr_get(data):
        return expression(expr, data)
    return expr_get

def factory_unique(config):
    expr = config['unique']
    def expr_unique(data):
        return list(set(expression(expr, data)))
    return expr_unique

def factory_sorted(config):
    data_expr = config['sorted']

    reverse = 'reverse' in config and config['reverse']
    if 'by' in config:
        by_field = config['by']
        sort_func = lambda data: list(sorted(data, key=lambda item: item[by_field], reverse=reverse))
    else:
        sort_func = lambda data: list(sorted(data, reverse=reverse))

    def expr_sorted(data):
        return sort_func(expression(data_expr, data))
    return expr_sorted
