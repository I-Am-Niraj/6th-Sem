factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    Prev is N - 1,
    factorial(Prev, PrevResult),
    Result is N * PrevResult.