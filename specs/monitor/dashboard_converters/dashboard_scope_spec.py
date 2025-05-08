from expects import equal, expect, be_false, start_with
from mamba import description, it

from sdcclient.monitor.dashboard_converters import convert_scope_string_to_expression

with description("Dashboard Scopes"):
    with it("parses correctly: agent.id is foo"):
        param = "agent.id is foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "equals",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id = foo"):
        param = "agent.id = foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "equals",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it('parses correctly: agent.id = "foo"'):
        param = 'agent.id = "foo"'
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "equals",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it('parses correctly: cluster.id-number = "foo-bar"'):
        param = 'cluster.id-number = "foo-bar"'
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "cluster.id-number",
                            "operator": "equals",
                            "value": ["foo-bar"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id = 'foo'"):
        param = "agent.id = 'foo'"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "equals",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id is not foo"):
        param = "agent.id is not foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "notEquals",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id in foo"):
        param = "agent.id in foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "in",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id in [foo]"):
        param = "agent.id in [foo]"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "in",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id in [foo, bar]"):
        param = "agent.id in [foo, bar]"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "in",
                            "value": ["foo", "bar"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id in [foo, bar, baz]"):
        param = "agent.id in [foo, bar, baz]"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "in",
                            "value": ["foo", "bar", "baz"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id in [foo, bar, baz] and agent.name is 'foobar'"):
        param = "agent.id in [foo, bar, baz] and agent.name is 'foobar'"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "in",
                            "value": ["foo", "bar", "baz"],
                        },
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.name",
                            "operator": "equals",
                            "value": ["foobar"],
                        },
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id not in foo"):
        param = "agent.id not in foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "notIn",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id not in [foo, bar, baz]"):
        param = "agent.id not in [foo, bar, baz]"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "notIn",
                            "value": ["foo", "bar", "baz"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id contains foo"):
        param = "agent.id contains foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "contains",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id does not contain foo"):
        param = "agent.id does not contain foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "notContains",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("parses correctly: agent.id starts with foo"):
        param = "agent.id starts with foo"
        res = convert_scope_string_to_expression(param)
        expect(res).to(
            equal(
                [
                    True,
                    [
                        {
                            "displayName": "",
                            "isVariable": False,
                            "operand": "agent.id",
                            "operator": "startsWith",
                            "value": ["foo"],
                        }
                    ],
                ]
            )
        )

    with it("returns ok, but empty if scope is None"):
        res = convert_scope_string_to_expression(None)
        expect(res).to(equal([True, []]))

    with it("returns error when parsing incorrect: agent.id starts with [foo, bar]"):
        param = "agent.id starts with [foo, bar]"
        ok, res = convert_scope_string_to_expression(param)
        expect(ok).to(be_false)
        expect(res).to(start_with(f"invalid scope: {param}"))

    with it("returns error when parsing incorrect: agent.id is [foo, bar]"):
        param = "agent.id is [foo, bar]"
        ok, res = convert_scope_string_to_expression(param)
        expect(ok).to(be_false)
        expect(res).to(start_with(f"invalid scope: {param}"))

    with it("returns error when parsing incorrect: agent.id contains [foo, bar]"):
        param = "agent.id contains [foo, bar]"
        ok, res = convert_scope_string_to_expression(param)
        expect(ok).to(be_false)
        expect(res).to(start_with(f"invalid scope: {param}"))

    with it("returns error when parsing incorrect: agent.id"):
        param = "agent.id"
        ok, res = convert_scope_string_to_expression(param)
        expect(ok).to(be_false)
        expect(res).to(start_with(f"invalid scope: {param}"))

    with it("returns error when parsing incorrect: agent.id is"):
        param = "agent.id is"
        ok, res = convert_scope_string_to_expression(param)
        expect(ok).to(be_false)
        expect(res).to(start_with(f"invalid scope: {param}"))
