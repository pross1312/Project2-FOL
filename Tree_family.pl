husband(Person, Wife) :- married(Person, Wife) , male(Person), female(Wife).
wife(Person, Husband) :- married(Person, Husband) , female(Person), male(Husband).

father(Parent, Child) :- parent(Parent, Child) , male(Parent).  
mother(Parent, Child) :- parent(Parent, Child) , female(Parent).  

child(Child, Parent) :- parent(Parent, Child). 
son(Child, Parent) :- 
  parent(Parent, Child) , 
  male(Child).

daughter(Child, Parent) :- 
  parent(Parent, Child) , 
  female(Child).


grandparent(GP, GC) :- 
  parent(GP,X) , 
  parent(X, GC). 

grandmother(GM, GC) :- 
  female(GM) , 
  parent(GM,X) , 
  parent(X, GC). 

grandfather(GF, GC) :- 
  male(GF) , 
  parent(GF, X), 
  parent(X, GC).

grandchild(GC,GP) :- 
  parent(GP,X) , 
  parent(X, GC). 

grandson(GS,GP) :- 
  parent(GP,X) , 
  parent(X, GS), 
  male(GS). 

granddaughter(GD, GP) :- 
  parent(GP,X) , 
  parent(X, GD), 
  male(GD).

sibling(Person1, Person2) :- 
  parent(Z, Person1) , 
  parent(Z, Person2) ,
  male(Z), 
  parent(Y, Person1) , 
  parent(Y, Person2) ,
  female(Y), 
  Person1 \= Person2. 

brother(Person,Sibling) :- 
  male(Person), 
  parent(Z, Person) , 
  parent(Z, Sibling) , 
  male(Z) ,
  parent(Y, Person) , 
  parent(Y, Sibling) , 
  female(Y), 
  Person \= Sibling. 

sister(Person,Sibling) :- 
  female(Person), 
  parent(Z, Person) , 
  parent(Z, Sibling) , 
  male(Z) ,
  parent(Y, Person) , 
  parent(Y, Sibling) , 
  female(Y), 
  Person \= Sibling. 

aunt(Person, NieceNephew) :-
  (female(Person),
  parent(X, NieceNephew) ,
  parent(Z, Person) , 
  parent(Z, X) ,
  male(Z) ,
  parent(Y, Person) , 
  parent(Y, X) ,
  female(Y),
  X \= Person );

  (male(U), 
  parent(X , NieceNephew), 
  parent(Z1, U) , 
  parent(Z1, X) , 
  male(Z1) ,
  parent(Y1, U) , 
  parent(Y1, X) , 
  female(Y1), 
  U \= X, 
  married(U, Person)). 

uncle(Person, NieceNephew) :-
  (male(Person),
  parent(X, NieceNephew) ,
  parent(Z, Person) , 
  parent(Z, X) ,
  male(Z) ,
  parent(Y, Person) , 
  parent(Y, X) ,
  female(Y) , 
  X \= Person ); 

  (female(A), 
  parent(K , NieceNephew), 
  parent(Z1, A) , 
  parent(Z1, K) , 
  male(Z1) ,
  parent(Y1, A) , 
  parent(Y1, K) , 
  female(Y1), 
  A \= K, 
  married(A, Person)). 


niece(Person, AuntUncle) :-
  (female(Person),
  parent(Z, AuntUncle) , 
  parent(Z, X) ,
  male(Z), 
  parent(Y, AuntUncle) , 
  parent(Y, X) ,
  female(Y), 
  AuntUncle \= X , 
  parent(X, Person)); 

  (parent(X, Person), 
  parent(Z, T) , 
  parent(Z, X) ,
  male(Z), 
  parent(Y, T) , 
  parent(Y, X) ,
  female(Y), 
  T \= X , 
  married(T, AuntUncle)).

nephew(Person, AuntUncle) :-
  (male(Person),
  parent(Z, AuntUncle) , 
  parent(Z, X) ,
  male(Z), 
  parent(Y, AuntUncle) , 
  parent(Y, X) ,
  female(Y), 
  AuntUncle \= X , 
  parent(X, Person)); 

  (parent(X, Person), 
  parent(Z, T) , 
  parent(Z, X) ,
  male(Z), 
  parent(Y, T) , 
  parent(Y, X) ,
  female(Y), 
  T \= X , 
  married(T, AuntUncle)).


divorced('Queen Elizabeth II', 'Prince Phillip'). 
divorced('Princess Diana', 'Prince Charles'). 
divorced('Captain Mark Phillips', 'Princess Anne'). 
divorced('Sarah Ferguson', 'Prince Andrew'). 

married('Prince Charles', 'Camilla Parker Bowles'). 
married('Timothy Laurence', 'Princess Anne'). 
married('Prince William', 'Kate Middleton').
married('Sophie Rhys-jones', 'Prince Edward'). 
married('Autumn Kelly', 'Peter Phillips').
married('Zara Phillips', 'Mike Tindall').

parent('Queen Elizabeth II','Prince Charles').
parent('Queen Elizabeth II','Princess Anne').
parent('Queen Elizabeth II','Prince Andrew').
parent('Queen Elizabeth II','Prince Edward').
parent('Prince Phillip','Prince Charles').
parent('Prince Phillip','Princess Anne').
parent('Prince Phillip','Prince Andrew').
parent('Prince Phillip','Prince Edward').


parent('Princess Diana', 'Prince William').
parent('Princess Diana', 'Prince Harry').
parent('Prince Charles', 'Prince William').
parent('Prince Charles', 'Prince Harry').

parent('Captain Mark Phillips', 'Peter Phillips').
parent('Captain Mark Phillips', 'Zara Phillips').
parent('Princess Anne', 'Peter Phillips').
parent('Princess Anne', 'Zara Phillips').

parent('Sarah Ferguson','Princess Beatrice').
parent('Sarah Ferguson','Princess Eugenie').
parent('Prince Andrew','Princess Beatrice'). 
parent('Prince Andrew','Princess Eugenie'). 

parent('Sophie Rhys-jones', 'James,Viscount Severn'). 
parent('Sophie Rhys-jones', 'Lady Louise Mountbatten-Windsor'). 
parent('Prince Edward', 'James,Viscount Severn'). 
parent('Prince Edward', 'Lady Louise Mountbatten-Windsor'). 

parent('Prince William', 'Prince George').
parent('Prince William', 'Princess Charlotte').
%parent('Kate Middleton', 'Prince George').
%parent('Kate Middleton', 'Princess Charlotte').

parent('Autumn Kelly', 'Savannah Phillips').
parent('Autumn Kelly', 'Isla Phillips').
parent('Peter Phillips', 'Savannah Phillips').
parent('Peter Phillips', 'Isla Phillips').

parent('Zara Phillips', 'Mia Grace Tindall').
parent('Mike Tindall', 'Mia Grace Tindall').

% Sex
male('Prince Phillip'). 

male('Prince Charles'). 
male('Captain Mark Phillips').
male('Timothy Laurence'). 
male('Prince Andrew'). 
male('Prince Edward'). 


male('Prince William').
male('Prince Harry').
male('Peter Phillips').
male('Mike Tindall').
male('James,Viscount Severn').
male('Prince George'). 


female('Queen Elizabeth II'). 
female('Princess Diana'). 
female('Camilla Parker Bowles'). 
female("Princess Anne"). 
female('Sarah Ferguson'). 
female('Sophie Rhys-jones').
female('Kate Middleton').
female('Autumn Kelly').
female('Zara Phillips').
female('Princess Beatrice').
female('Princess Eugenie').
female('Lady Louise Mountbatten-Windsor').
female('Princess Charlotte'). 
female('Savannah Phillips').
female('Isla Phillips'). 
female('Mia Grace Tindall').


