% Facts
father(nitin, niraj).
father(nitin, isha).
father(shrikant, nitin).
father(shrikant, suhas).
father(sitaram, shrikant).
father(suhas, sujal).
father(suhas, sagarika).
mother(nidhi, niraj).
mother(nidhi, isha).
brother(niraj, isha).
brother(suhas, nitin).
sister(isha, niraj).
wife(nidhi, nitin).
wife(suvidha, suhas).

% Rules
parent(X, Y) :- father(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
greatgrandparent(X, Y) :- grandparent(X, Z), parent(Z, Y).
siblings(X, Y) :- brother(X, Y), sister(Y, X).