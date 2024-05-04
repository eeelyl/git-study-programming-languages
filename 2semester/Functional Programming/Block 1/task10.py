def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


def rule_sequence(s, rules):
    for rule in rules:
        result = rule(s)
        if result is not None:
            s = result
        else:
            return None
    return result


print(rule_sequence('0101', [zero, one, zero]))
print(rule_sequence('0101', [zero, zero]))
