def zero(s):
    if s and s[0] == "0":
        return s[1:]


def one(s):
    if s and s[0] == "1":
        return s[1:]


def rule_sequence(s, rules):
    if not rules:
        return s
    result = rules[0](s)
    if result is None:
        return None
    return rule_sequence(result, rules[1:])


print(rule_sequence('0101', [zero, one, zero]))
print(rule_sequence('0101', [zero, zero]))
