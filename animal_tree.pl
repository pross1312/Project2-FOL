animal(X) :-  reptile(X) ; fish(X) ; mammal(X) ; bird(X).

bird(X) :- 
 vertebrate(X) ,
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 have_tail(X) ,
 haveBeak(X).

penguin(X) :-
 bird(X) ,
 carnivore(X) ,
 havewebbed_feet(X).

chicken(X) :-
 vertebrate(X) ,
 bird(X) ,
 omnivore(X) ,
 have_combs(X) ,
 have_wattle(X).

owl(X) :-
 bird(X) ,
 can_fly(X) ,
 omnivore(X) ,
 nocturnal(X).

reptile(X) :-
 vertebrate(X) ,
 cold_blooded(X) ,
 layEggs(X) ,
 have_tail(X) ,
 have_scales(X).

dinosaurs(X) :-
 carnivore_dino(X) ;
 herbivore_dino(X).

carnivore_dino(X) :- 
 reptile(X) ,
 extinct(X) ,
 carnivore(X).

herbivore_dino(X) :-
 reptile(X) ,
 extinct(X) ,
 herbivore(X).

crocodile(X) :-
 reptile(X) ,
 carnivore(X) ,
 can_swim(X).

lizard(X) :-
 reptile(X) ,
 carnivore(X) ,
 can_camouflauge(X).

fish(X) :-
 vertebrate(X) ,
 cold_blooded(X) ,
 live_underwater(X) ,
 have_fin(X) ,
 can_swim(X).

cartilanginous(X) :-
 fish(X) ,
 carnivore(X) ,
 dont_have_bone(X).

rayfinned_fish(X) :-
 fish(X) ,
 layEggs(X),
 silver_colored(X).

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
 rayfinned_fish(X), 
 round_body(X).

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
 land_based_species(X) ;
 cetaceans(X).

land_based_species(X) :-
 mammal(X) ,
 have_even_toe(X) ,
 herbivore(X) ,
 have_tail(X).

cetaceans(X) :-
 mammal(X) ,
 have_fin(X) ,
 carnivore(X) ,
 live_underwater(X).

pig(X) :-
 land_based_species(X) ,
 smart(X).

whale(X) :- 
 cetaceans(X) ,
 smart(X).

wolf(X) :- dog(X) , live_in_the_wild(X) ,sharp_teeth(X), sharp_claw(X).
domesticated_dog(X) :- dog(X) , domesticated(X) , friendly(X).
lion(X) :- cat(X) , live_in_the_wild(X) ,sharp_teeth(X), sharp_claw(X), male_have_coat(X).
domesticated_cat(X) :- cat(X) , domesticated(X) , friendly(X).

pet(X) :-  domesticated_dog(X) ; domesticated_cat(X).

cattle(X) :- chicken(X) ; pig(X).

dangerous_animal(X) :- shark(X) ; lion(X) ; crocodile(X) ; wolf(X).
prey(X) :- primate(X) ; land_based_species(X).

eat(X, Y) :- 
 (carnivore_dino(X) , (bird(Y) ; carnivora(Y) ; prey(Y) ; reptile(Y))) ;
 (shark(X) , (human(Y) ; fish(Y))) ;
 (human(X) , food(Y)) ;
 (dangerous_animal(X) , prey(Y)).

food(X) :- chicken(X) ; pig(X) ; tuna(X) ; salmon(X).

vertebrate('Sperm whale').
vertebrate('Huy').
vertebrate('Yorkshire pig').
vertebrate('Corgi').
vertebrate('Sokoke').
vertebrate('Gray wolf').
vertebrate('African lion').
vertebrate('Rhesus macaques').
vertebrate('Emperor penguin').
vertebrate('Cochin chicken').
vertebrate('Barn owl').
vertebrate('Blue fin tuna').
vertebrate('Chinook salmon').
vertebrate('Eagle ray').
vertebrate('Great White shark').
vertebrate('Chameleon').
vertebrate('Nile crocodile').
vertebrate('T-rex').
vertebrate('Triceratops').

have_tail('Yorkshire pig').
have_tail('Sokoke').
have_tail('Corgi').
have_tail('Gray wolf').
have_tail('African lion').
have_tail('Rhesus macaques').
have_tail('Emperor penguin').
have_tail('Cochin chicken').
have_tail('Barn owl').
have_tail('Blue fin tuna').
have_tail('Chinook salmon').
have_tail('Eagle ray').
have_tail('Great White shark').
have_tail('Chameleon').
have_tail('Nile crocodile').
have_tail('T-rex').
have_tail('Triceratops').

warm_blooded('Sperm whale').
warm_blooded('Huy').
warm_blooded('Yorkshire pig').
warm_blooded('Corgi').
warm_blooded('Gray wolf').
warm_blooded('African lion').
warm_blooded('Rhesus macaques').
warm_blooded('Emperor penguin').
warm_blooded('Cochin chicken').
warm_blooded('Barn owl').
warm_blooded('Sokoke').

cold_blooded('Blue fin tuna').
cold_blooded('Chinook salmon').
cold_blooded('Eagle ray').
cold_blooded('Great White shark').
cold_blooded('Chameleon').
cold_blooded('Nile crocodile').
cold_blooded('T-rex').
cold_blooded('Triceratops').

herbivore('Triceratops').
herbivore('Yorkshire pig').

omnivore('Huy').
omnivore('Rhesus macaques').
omnivore('Barn owl').
omnivore('Cochin chicken').

carnivore('Emperor penguin').
carnivore('T-rex').
carnivore('Nile crocodile').
carnivore('Chameleon').
carnivore('Great White shark').
carnivore('Eagle ray').
carnivore('Gray wolf').
carnivore('African lion').
carnivore('Corgi').
carnivore('Sperm whale').
carnivore('Sokoke').

layEggs('Triceratops').
layEggs('T-rex').
layEggs('Nile crocodile').
layEggs('Chameleon').
layEggs('Eagle ray').
layEggs('Blue fin tuna').
layEggs('Chinook salmon').
layEggs('Emperor penguin').
layEggs('Cochin chicken').
layEggs('Barn owl').

have_fin('Blue fin tuna').
have_fin('Chinook salmon').
have_fin('Eagle ray').
have_fin('Great White shark').
have_fin('Sperm whale').

have_scales('Triceratops').
have_scales('T-rex').
have_scales('Nile crocodile').
have_scales('Chameleon').

can_camouflauge('Chameleon').
have_lost_of_teeth('Great White shark').

can_swim('Nile crocodile').
can_swim('Great White shark').
can_swim('Eagle ray').
can_swim('Blue fin tuna').
can_swim('Chinook salmon').

venomous('Eagle ray').
disk_shaped('Eagle ray').

silver_colored('Blue fin tuna').
silver_colored('Chinook salmon').

change_color('Chinook salmon').


live_bearing('Corgi').
live_bearing('Huy').
live_bearing('Sokoke').
live_bearing('Rhesus macaques').
live_bearing('Gray wolf').
live_bearing('African lion').
live_bearing('Yorkshire pig').
live_bearing('Sperm whale').
live_bearing('Great White shark').

produce_milk('Corgi').
produce_milk('Huy').
produce_milk('Sokoke').
produce_milk('Rhesus macaques').
produce_milk('Gray wolf').
produce_milk('African lion').
produce_milk('Yorkshire pig').
produce_milk('Sperm whale').

very_smart('Huy').

smart('Rhesus macaques').
smart('Corgi').
smart('Sokoke').
smart('Gray wolf').
smart('African lion').
smart('Yorkshire pig').
smart('Sperm whale').
 

sensitive_nose('Corgi').
sensitive_nose('Gray wolf').

sharp_eye('African lion').
sharp_eye('Sokoke').

cant_sweat('Yorkshire pig').

live_underwater('Sperm whale').
live_underwater('Great White shark').
live_underwater('Eagle ray').
live_underwater('Blue fin tuna').
live_underwater('Chinook salmon').

haveFeather('Emperor penguin').
haveFeather('Cochin chicken').
haveFeather('Barn owl').


haveWings('Emperor penguin').
haveWings('Cochin chicken').
haveWings('Barn owl').

haveBeak('Emperor penguin').
haveBeak('Cochin chicken').
haveBeak('Barn owl').

can_fly('Barn owl').

nocturnal('Barn owl').

friendly('Corgi').
friendly('Sokoke').

live_in_the_wild('Gray wolf').
live_in_the_wild('African lion').

sharp_claw('Gray wolf').
sharp_claw('African lion').

sharp_teeth('Gray wolf').
sharp_teeth('African lion').

havewebbed_feet('Emperor penguin').

have_combs('Cochin chicken').
have_wattle('Cochin chicken').

extinct('Triceratops').
extinct('T-rex').

dont_have_bone('Great White shark').
dont_have_bone('Eagle ray').

big_brain('Huy').
big_brain('Rhesus macaques').

have_even_toe('Yorkshire pig').

domesticated('Corgi').
domesticated('Sokoke').
male_have_coat('African lion').

round_body('Blue fin tuna').
