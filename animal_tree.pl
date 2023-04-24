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

reptile(X) :-
 dinosaurs(X) ;
 crocodile(X) ;
 lizard(X).

fish(X) :-
 cartilanginous(X) ;
 rayfinned_fish(X).

mammal(X) :-
 primate(X) ;
 carnivora(X) ;
 even_toed_ungulate(X).

chicken(X) :-
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 cant_fly(X) ,
 have_combs(X) ,
 haveBeak(X) ,
 have_wattle(X).

owl(X) :-
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 can_fly(X) ,
 haveBeak(X) ,
 nocturnal(X).

cartilanginous(X) :-
 shark(X) ;
 stingray(X).

rayfinned_fish(X) :-
 tuna(X) ;
 salmon(X).

primate(X) :-
 human(X) ;
 monkey(X).

carnivora(X) :-
 cat(X) ;
 dog(X).

even_toed_ungulate(X) :-
 pig(X) ;
 whale(X).

dinosaurs(X) :-
 cold_blooded(X) ,
 layEggs(X) ,
 have_scales(X).

crocodile(X) :-
 cold_blooded(X) ,
 layEggs(X) ,
 have_scales(X) ,
 can_swim(X).

lizard(X) :-
 cold_blooded(X) ,
 layEggs(X) ,
 have_scales(X) ,
 can_camouflauge(X).

shark(X) :-
 live_bearing(X) ,
 can_swim(X) ,
 cold_blooded(X) ,
 have_lost_of_teeth(X).

stingray(X) :- 
 cold_blooded(X) ,
 layEggs(X) ,
 can_swim(X) ,
 venomous(X) ,
 disk_shaped(X).

tuna(X) :-
 cold_blooded(X) ,
 silver_colored(X) ,
 layEggs(X) ,
 can_swim(X).

salmon(X) :-
 cold_blooded(X) ,
 layEggs(X) ,
 silver_colored(X) ,
 change_color(X) ,
 can_swim(X).

human(X) :- 
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 very_smart(X).

monkey(X) :-
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 have_tail(X) ,
 can_climb(X) ,
 smart(X).

dog(X) :- 
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 have_tail(X) ,
 sensitive_nose(X) ,
 smart(X).

cat(X) :-
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 have_tail(X) ,
 smart(X),
 eat_meat(X) ,
 can_climb(X).

pig(X) :-
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 have_tail(X) ,
 cant_sweat(X) ,
 smart(X).

whale(X) :- 
 vertebrate(X) ,
 live_bearing(X) ,
 warm_blooded(X) ,
 produce_milk(X) ,
 have_tail(X) ,
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

