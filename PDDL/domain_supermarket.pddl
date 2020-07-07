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
    )
    
    
    (:action ventilator-on
        :parameters (?v - ventilator ?m - main-hall)
        :precondition (and
            (is-off ?v)
            (is-in ?v ?m)
            (or
                (and
                    (> (temperature ?m) 25)
                    (> (heatindex ?m) 27)
                )
                (> (person-count ?m) 7)
            )
        )
        :effect (and
            (is-on ?v)
            (when 
                (and 
                    (< (person-count ?m) 11) 
                    (> (person-count ?m) 7)
                    (> (heatindex ?m) 27)
                    (< (heatindex ?m) 33)
                )
                (and 
                    ;(assign (temperature ?m) 1.0)
                    (assign (heatindex ?m) 1)
                )
            )
            (assign (person-count ?m) 1.0)
        )
    )

    (:action refill-shelf
        :parameters (?s - section)
        :precondition (and
            (= (shelf-items ?s) 0) 
            (< (person-count ?s) 3)
        )
        :effect (and
            (assign (shelf-items ?s) 6)
        )
    )

    (:action section-closed
        :parameters (?s - section)
        :precondition (or
            (> (person-count ?s) 4)
            (and
                (> (person-count ?s) 2)
                (= (shelf-items ?s) 0)
            )
         )
        :effect (and
            (assign (person-count ?s) 1)
        )
    )

    (:action gate-closed
        :parameters (?m - main-hall)
        :precondition (or
            (> (person-count ?m) 9)
            ;(forall (?s - section) (> (person-count ?s) 4.0))
            (forall (?s - section) (= (shelf-items ?s) 0))
            (and
                (> (temperature ?m) 25)
                (> (heatindex ?m) 32)
            )
        )
        :effect (and
            (assign (person-count ?m) 1)
            (assign (heatindex ?m) 1)
        )
    )
)