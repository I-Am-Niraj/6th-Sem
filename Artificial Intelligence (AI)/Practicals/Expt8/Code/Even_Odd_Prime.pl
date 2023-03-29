is_even(X) :-
    X mod 2 =:= 0.

is_odd(X) :-
    X mod 2 =:= 1.

is_prime(X) :-
    X > 1,
    Upper is floor(sqrt(X)),
    \+ (between(2, Upper, Y), X mod Y =:= 0).