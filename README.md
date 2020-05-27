# json-prime
A JSONPath-based expressions library for aggregating and transforming JSON

The core of the library is the notion of everything as an **expression**. An expression can be one of several
types of elements:

* **string** - Evaluated as a jsonpath query against the document and returns an array of values
* **list** - Each entry is evaluated as an expression and returns a list of the results
* **dict** - Evaluated as a single expression and the result is returned

The heart of the notion of expressions is both the *JsonExpression* class, as well as the *expression()* function,
however the function maps directly to these three basic elements.

# Operations
Just expressions alone is not enough unless we have some operations we can perform on the results. In order to
implement operations, a more functional approach is taken to make it easier to integrate other elements.

The core library defines some basic operations that make it easier to transform the JSON:

## count
Returns the length of the list returned by the expression
```json
{
    "count": "$[*].competition_gender"
}
```

## sum
Returns a single value, which is the sum of all values in the expression
```json
{
    "sum": { "count": "$[*].competition_gender" }
}
```

## rate
Takes two expressions, a numerater and a denominator and returns the **rate**, or n/d. Probably should be called "div"...
```json
{
    "rate": {
        "n": { "sum": { "count": { "filter": "$[*].competition_gender", "prefixes": [ "fem" ] } } },
        "d": { "sum": { "count": "$[*].competition_gender" } }
    }
}
```

## const
Returns a constant value
```json
{
    "const": "Testing"
}
```

## filter
The filter operation takes a few forms but the basic gist is it allows you to filter a list to only
elements that meet your criteria. Right now the only thing it supports is operating on string lists
because that all I really need to do here. It's basically just used to limit cipher names.

### prefixes
The *prefixes* filter allows you to limit strings to only ones that begin with one of the entries
in the list. You can also use *prefix* if you only have one value to filter.
```json
{
    "count": {
        "filter": "$[*].competition_gender",
        "prefix": "m"
    }
}
```

### equals
Match a value exactly.
```json
{
    "count": {
        "filter": "$[*].competition_gender",
        "equals": "female"
    }
}
```

### not
Negates a filter expression. In this case, the value of the *not* key should be the filter expression
that you want to negate.
```json
{
    "rate": {
        "n": { "sum": { "count": { "filter": "$[*].competition_gender", "prefixes": [ "fem" ] } } },
        "d": {
            "sum": {
                "count": {
                    "filter": "$[*].competition_gender",
                    "not": { "equals": "male" }
                }
            }
        }
    }
}
```

See the configuration files under the
<a href="test/football/mappings">test/football/mappings</a> directory  for more detailed examples of created transformation expressions.

# License
This library is release under the Apache 2.0 license, see <a href="LICENSE">LICENSE</a> for more details.

# Contributing
Please feel free to file issues and create pull requests, I will try to be as attentive as possible.
