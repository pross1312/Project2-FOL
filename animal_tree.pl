animal(X) :-  reptile(X) ; fish(X) ; mammal(X) ; bird(X).

bird(X) :- 
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 haveBeak(X).

penguin(X) :-
 bird(X) ,
 cant_fly(X) ,
 eat_fish(X) ,
 havewebbed_feet(X).

chicken(X) :-
 bird(X) ,
 cant_fly(X) ,
 have_combs(X) ,
 have_wattle(X).

owl(X) :-
 bird(X) ,
 can_fly(X) ,
 nocturnal(X).

reptile(X) :-
 cold_blooded(X) ,
 layEggs(X) ,
 have_scales(X).

dinosaurs(X) :-
 carnivore_dino(X) ;
 herbivore_dino(X)

carnivore_dino(X) :- 
 reptile(X) ,
 carnivore(X).

herbivore_dino(X) :-
 reptile(X) ,
 herbivore(X).

crocodile(X) :-
 reptile(X) ,
 can_swim(X).

lizard(X) :-
 reptile(X) ,
 can_camouflauge(X).

fish(X) :-
 cold_blooded(X) ,
 can_swim(X).

cartilanginous(X) :-
 fish(X) ,
 dont_have_bone(X).

rayfinned_fish(X) :-
 fish(X) ,
 layEggs(X),
 silver_colored(X) ,
 have_bone(X).

shark(X) :-
 cartilanginous(X) ,
 have_lost_of_teeth(X),
 live_bearing(X).

stingray(X) :-
 cartilanginous(X) ,
 layEggs(X) ,
 venomous(X) ,
 disk_shaped(X).

tuna(X) :-
 rayfinned_fish(X).

salmon(X) :-
 rayfinned_fish(X) ,
 change_color(X).

mammal(X) :-
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X).

primate(X) :-
 mammal(X) ,
 big_brain(X) ,
 omnivore(X).

human(X) :- 
 primate(X) ,
 very_smart(X).

monkey(X) :-
 primate(X) ,
 have_tail(X) ,
 smart(X).

carnivora(X) :-
 mammal(X) ,
 have_tail(X) ,
 carnivore(X).

dog(X) :- 
 carnivora(X) ,
 sensitive_nose(X) ,
 smart(X).

cat(X) :- 
 carnivora(X) ,
 sharp_eye(X) ,
 smart(X).
 
even_toed_ungulate(X) :-
 pig(X) ,
 whale(X). 

pig(X) :-
 mammal(X)
 have_tail(X) ,
 cant_sweat(X) ,
 omnivore(X) ,
 smart(X).

whale(X) :- 
 mammal(X) ,
 have_tail(X) ,
 carnivore(X) ,
 live_underwater(X) ,
 smart(X).

wolf(X) :- dog(X) , live_in_the_wild(X).
domesticated_dog(X) :- dog(X) , domesticated(X) , friendly(X).
tiger(X) :- cat(X) , live_in_the_wild(X) , have_stripe(X).
lion(X) :- cat(X) , live_in_the_wild(X) , male_have_coat(X).
domesticated_cat(X) :- cat(X) , domesticated(X) , friendly(X).

pet(X) :- domesticated_cat(X) ; domesticated_dog(X).


cattle(X) :- chicken(X) ; pig(X).
extinct(X) :- dinosaurs(X).
live_in_sea(X) :- shark(X) ; whale(X).
live_underwater(X) :- fish(X) ; whale(X).
weaker_animal(X) :- bird(X) , mammal(X).
stronger_animal(X) :- crocodile(X) , dinosaurs(X).
eat(X, Y) :- stronger_animal(X) , weaker_animal(Y).
predator(X) :- crocodile(X) ; shark(X) ; dinosaur(X).
prey(X) :- bird(X) ; pig(X).
hunt(X, Y) :- predator(X) , prey(Y).

warm_blooded('sperm whale').
warm_blooded('human').
warm_blooded('VN pig').
warm_blooded('dog').
warm_blooded('cat').
warm_blooded('moneky').
warm_blooded('penguin').
warm_blooded('chicken').
warm_blooded('owl').

cold_blooded('tuna').
cold_blooded('salmon').
cold_blooded('stingray').
cold_blooded('shark').
cold_blooded('lizard').
cold_blooded('crocodile').
cold_blooded('dinosaur').

layEggs('dinosaur').
layEggs('crocodile').
layEggs('lizard').
layEggs('stingray').
layEggs('tuna').
layEggs('salmon').
layEggs('penguin').
layEggs('chicken').
layEggs('owl').

have_scales('dinosaur').
have_scales('crocodile').
have_scales('lizard').

can_camouflauge('lizard').
have_lost_of_teeth('shark').

can_swim('crocodile').
can_swim('shark').
can_swim('stingray').
can_swim('tuna').
can_swim('salmon').

venomous('stingray').
disk_shaped('stingray').

silver_colored('tuna').
silver_colored('salmon').

change_color('salmon').

vertebrate('human').
vertebrate('monkey').
vertebrate('dog').
vertebrate('cat').
vertebrate('pig').
vertebrate('whale').

live_bearing('human').
live_bearing('monkey').
live_bearing('dog').
live_bearing('cat').
live_bearing('pig').
live_bearing('whale').

produce_milk('human').
produce_milk('monkey').
produce_milk('dog').
produce_milk('cat').
produce_milk('pig').
produce_milk('whale').

very_smart('human').

smart('monkey').
smart('dog').
smart('cat').
smart('pig').
smart('whale').
 
have_tail('monkey').
have_tail('dog').
have_tail('cat').
have_tail('pig').
have_tail('whale').

can_climb('monkey').
can_climb('cat').

sensitive_nose('dog').
eat_meat('cat').

cant_sweat('pig').
live_underwater('whale').

haveFeather('penguin').
haveFeather('chicken').
haveFeather('owl').


haveWings('penguin').
haveWings('chicken').
haveWings('owl').

haveBeak('penguin').
haveBeak('chicken').
haveBeak('owl').

cant_fly('penguin').
cant_fly('chicken').

can_fly('owl').

nocturnal('owl').
eat_fish('penguin').

havewebbed_feet('penguin').

have_combs('chicken').
have_wattle('chicken').

