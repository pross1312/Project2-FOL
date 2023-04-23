animal(X) :-  reptile(X) ; fish(X) ; mammal(X) ; bird(X).
bird(X) :- 
 penguin(X) ; 
 chicken(X) ;
 owl(X).

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

penguin(X) :-
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 cant_fly(X) ,
 eat_fish(X)
 haveWebbed_feet(X).

chicken(X) :-
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 cant_fly(X) ,
 have_combs(X) ,
 have_wattle(X).

owl(X) :-
 haveFeather(X) ,
 layEggs(X) ,
 haveWings(X) ,
 warm_blooded(X) ,
 can_fly(X) ,
 nocturnal(X).

cartilanginous(X) :-
 shark(X) ;
 stingray(X).

rayfinned_fish(X) :-
 tuna(X) ;
 salmon(X),

primate(X) :-
 human(X) ;
 monkey(X).

carnivora(X) :-
 cat(X) ;
 dog(X).

even_toed_ungulate(x) :-
 pig(X) ;
 whale(X) .

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
 bear_living(X) ,
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
 live_underwater(X).
 
 





 
 
