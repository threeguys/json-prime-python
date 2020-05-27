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

from .core import expression

def factory_filter(config):
    filter_config = config
    negate = False

    if 'not' in config:
        filter_config = config['not']
        negate = True

    if 'equals' in filter_config:
        inner_filter_func = lambda item: item == filter_config['equals']

    elif 'prefix' in filter_config:
        inner_filter_func = lambda item: item.startswith(filter_config['prefix'])

    elif 'prefixes' in filter_config:
        prefixes = filter_config['prefixes']

        def prefixes_filter(item):
            for p in prefixes:
                if item.startswith(p):
                    return True
            return False

        inner_filter_func = prefixes_filter

    else:
        raise ValueError('Unknown filter type: ' + str(config))

    filter_func = lambda item: not inner_filter_func(item) if negate else inner_filter_func(item)

    def expr_filter(data):
        filter_data = expression(config['filter'], data)
        return list(filter(filter_func, filter_data))

    return expr_filter
