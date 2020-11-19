import tatsu


def convert_scope_string_to_expression(scope=None):
    if scope is None or not scope:
        return [True, []]

    _SCOPE_GRAMMAR = """
        @@grammar::CALC

        start = expression $ ;

        expression
            =
            |   operand simple_operator word
            |   operand multiple_operator multiple_value
            ;

        simple_operator
            =
            |  'is not'
            |  'is'
            |  'contains'
            |  'does not contain'
            |  'starts with'
            |  '='
            ;

        multiple_operator
            =
            |  'not in'
            |  'in'
            ;

        operand = /[a-zA-Z0-9_\-\.]+/ ;

        multiple_value
            =
            | '[' word_array ']'
            | word
            ;

        word_array
            =
            | word ',' word_array
            | word
            ;

        word =
            | /[a-zA-Z0-9-_\-\.]+/
            | '"' /[a-zA-Z0-9-_\-\.]+/ '"'
            | "'" /[a-zA-Z0-9-_\-\.]+/ "'"
            ;
    """

    def flatten(S):
        if S == [] or S == ():
            return list(S)
        if isinstance(S[0], list) or isinstance(S[0], tuple):
            return flatten(S[0]) + flatten(S[1:])
        return list(S[:1]) + flatten(S[1:])

    try:
        grammar = tatsu.compile(_SCOPE_GRAMMAR)
        scope_list = []

        scope_expressions = scope.strip(' \t\n\r').split(' and ')

        for scope in scope_expressions:

            operand, parsed_operator, value = grammar.parse(scope)

            operator_match = {
                "is": "equals",
                "=": "equals",
                "is not": "notEquals",
                "in": "in",
                "not in": "notIn",
                "contains": "contains",
                "does not contain": "notContains",
                "starts with": "startsWith",
            }

            if isinstance(value, tuple) or isinstance(value, list):
                value = flatten(value)
                if len(value) > 1:
                    value = list(value[1:-1])  # Remove '[' and ']'
                    value = [elem for elem in value if elem != ',']  # Remove ','
            else:
                value = [value]

            operator = "" if parsed_operator not in operator_match else operator_match[parsed_operator]

            scope_list.append({
                'displayName': "",
                "isVariable": False,
                'operand': operand,
                'operator': operator,
                'value': value
            })
        return [True, scope_list]
    except Exception as ex:
        return [False, f"invalid scope: {scope}, {ex.message}"]
