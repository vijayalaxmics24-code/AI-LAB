def is_variable(x):
    return isinstance(x, str) and x.islower()


def parse(expr):
    expr = expr.replace(" ", "")

    if "(" not in expr:
        return expr

    predicate, args = expr.split("(", 1)
    args = args.rstrip(")")

    return (predicate,) + tuple(args.split(","))


def occurs_check(var, expr):
    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs_check(var, item) for item in expr[1:])

    return False


def apply_substitution(subst, expr):
    if isinstance(expr, str):
        while expr in subst:
            expr = subst[expr]
        return expr

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            apply_substitution(subst, item)
            for item in expr[1:]
        )

    return expr


def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = apply_substitution(subst, x)
    y = apply_substitution(subst, y)

    if x == y:
        return subst

    if is_variable(x):
        if occurs_check(x, y):
            return None
        subst[x] = y
        return subst

    if is_variable(y):
        if occurs_check(y, x):
            return None
        subst[y] = x
        return subst

    if not isinstance(x, tuple) or not isinstance(y, tuple):
        return None

    if x[0] != y[0] or len(x) != len(y):
        return None

    for a, b in zip(x[1:], y[1:]):
        subst = unify(a, b, subst)

        if subst is None:
            return None

    return subst


# Main Program
print("UNIFICATION IN FIRST ORDER LOGIC")

expr1 = "Eats(x, Apple)"
expr2 = "Eats(Riya, y)"

x = parse(expr1)
y = parse(expr2)

result = unify(x, y)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)

    unified = apply_substitution(result, x)

    print("Unified Expression:",
          unified[0] + "(" + ", ".join(unified[1:]) + ")")