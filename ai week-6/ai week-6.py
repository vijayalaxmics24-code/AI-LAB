def implies(p, q):
    return (not p) or q


def pl_true_kb(model):
    P = model['P']
    Q = model['Q']
    R = model['R']

    # Knowledge Base: (P -> Q) AND (Q -> R) AND P
    return implies(P, Q) and implies(Q, R) and P


def pl_true_query(model):
    # Query: R
    return model['R']


def tt_check_all(kb, query, symbols, model):
    # Base case: all symbols have been assigned
    if len(symbols) == 0:
        if kb(model):
            return query(model)
        else:
            return True

    # Select the first symbol
    P = symbols[0]
    rest = symbols[1:]

    # Check both true and false assignments
    model_true = model.copy()
    model_true[P] = True

    model_false = model.copy()
    model_false[P] = False

    return (
        tt_check_all(kb, query, rest, model_true)
        and
        tt_check_all(kb, query, rest, model_false)
    )


def display_truth_table():
    symbols = ['P', 'Q', 'R']

    print("Knowledge Base: (P -> Q) AND (Q -> R) AND P")
    print("Query: R\n")
    print("P Q R | P->Q | Q->R | KB | Query")
    print("------------------------------------")

    # Display rows in FFF, FFT, FTF, FTT, TFF, TFT, TTF, TTT order
    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                model = {'P': p, 'Q': q, 'R': r}

                s1 = implies(p, q)
                s2 = implies(q, r)
                kb_value = pl_true_kb(model)
                query_value = pl_true_query(model)

                def tf(value):
                    return 'T' if value else 'F'

                print(
                    f"{tf(p)} {tf(q)} {tf(r)} |"
                    f"  {tf(s1)}   |"
                    f"  {tf(s2)}   |"
                    f" {tf(kb_value)}  |"
                    f"   {tf(query_value)}"
                )


def tt_entails(kb, query):
    symbols = ['P', 'Q', 'R']
    return tt_check_all(kb, query, symbols, {})


# Main program
display_truth_table()

print("\nEntailment Result:")
if tt_entails(pl_true_kb, pl_true_query):
    print("KB entails Query: True (KB |= R)")
else:
    print("KB entails Query: False (KB !|= R)")