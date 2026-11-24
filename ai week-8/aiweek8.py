facts = [
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
]

rules = [
    ([("Missile", "x")],
     ("Weapon", "x")),

    ([("Missile", "x"), ("Owns", "A", "x")],
     ("Sells", "Robert", "x", "A")),

    ([("Enemy", "x", "America")],
     ("Hostile", "x")),

    ([("American", "p"), ("Weapon", "q"),
      ("Sells", "p", "q", "r"), ("Hostile", "r")],
     ("Criminal", "p"))
]

variables = {"x", "p", "q", "r"}

def match(pattern, fact, sub):
    if pattern[0] != fact[0]:
        return None

    sub = sub.copy()

    for p, f in zip(pattern[1:], fact[1:]):
        if p in variables:
            if p in sub and sub[p] != f:
                return None
            sub[p] = f
        elif p != f:
            return None

    return sub


def forward_chaining(facts, rules, query):
    iteration = 1

    while True:
        new_facts = []

        print("\nIteration", iteration)

        for premises, conclusion in rules:

            def apply_rule(index, sub):
                if index == len(premises):
                    result = tuple(
                        sub.get(x, x) for x in conclusion
                    )

                    if result not in facts and result not in new_facts:
                        new_facts.append(result)
                    return

                for fact in facts:
                    s = match(premises[index], fact, sub)
                    if s is not None:
                        apply_rule(index + 1, s)

            apply_rule(0, {})

        if not new_facts:
            break

        for fact in new_facts:
            print("Derived:", fact)
            facts.append(fact)

        if query in facts:
            return True

        iteration += 1

    return query in facts


query = ("Criminal", "Robert")

print("Initial Knowledge Base:")
for fact in facts:
    print(fact)

if forward_chaining(facts, rules, query):
    print("\nQuery Proved:", query)
else:
    print("\nQuery Not Proved")