greatest(X, Y, Z, G) :-
    X >= Y, X >= Z,
    G is X.
greatest(X, Y, Z, G) :-
    Y >= X, Y >= Z,
    G is Y.
greatest(_, _, Z, G) :-
    G is Z.