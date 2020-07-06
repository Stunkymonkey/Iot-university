(define (domain domain_supermarket)

    (:requirements
        :negative-preconditions
        :strips
        :typing
        :adl
        :fluents
    )

    (:types
        main-hall section - location
        ventilator - object
    )


    (:predicates
        (is-in ?o - object ?l - location)
        (is-on ?o - object)
        (is-off ?o - object)
    )
    
    (:functions 
        (person-count ?l - location)
        (temperature ?s - main-hall)
        (heatindex ?s - main-hall)
        (shelf-items ?s - section)
        (is-safe ?l - location)
    )
    
    
    (:action ventilator-on
        :parameters (?v - ventilator ?m - main-hall)
        :precondition (and
            (is-off ?v)
            (is-in ?v ?m)
            (or
                (and
                    (> (temperature ?m) 25.0)
                    (> (heatindex ?m) 27.0)
                )
                (exists (?s1 - section) (> (person-count ?s1) 3.0))
            )
        )
        :effect (and
            (is-on ?v)
            (assign (heatindex ?m) 0.0)
            
        )
    )

    (:action refill-shelf
        :parameters (?s - section)
        :precondition (and
            (= (shelf-items ?s) 0.0) 
            (< (person-count ?s) 3.0)
        )
        :effect (and 
            (assign (shelf-items ?s) 6.0)
        )
    )

    (:action section-closed
        :parameters (?s - section)
        :precondition (or
            (> (person-count ?s) 4.0)
            (and
                (> (person-count ?s) 2.0)
                (= (shelf-items ?s) 0.0)
            )
         )
        :effect (and
            (assign (person-count ?s) 1.0)
        )
    )

    (:action gate-closed
        :parameters (?m - main-hall)
        :precondition (or
            (> (person-count ?m) 9.0)
            (forall (?s - section) (> (person-count ?s) 4.0))
            (forall (?s - section) (= (shelf-items ?s) 0.0))
            (and
                (> (temperature ?m) 25.0)
                (> (heatindex ?m) 31.0)
            )
        )
        :effect (and
            (assign (person-count ?m) 1.0)
            (assign (temperature ?m) 1.0)
            (assign (is-safe ?m) 1.0)
        )
    )
)

