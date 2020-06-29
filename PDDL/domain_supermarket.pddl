(define (domain domain_supermarket)

    (:requirements
        :negative-preconditions
        :strips
        :typing
        :adl
        :fluents
    )

    (:types
        section - location
        ventilator - object
    )


    (:predicates
        (is-in ?o - object ?s - section)
        (is-on ?o - object)
        (is-off ?o - object)
    )
    
    (:functions 
        (person-count ?s - section)
        (heatindex ?s - section)
        (shelf-items ?s - section)
    )
    
    
    (:action ventilator-on
        :parameters (?v - ventilator ?s - section)
        :precondition (and
            (is-off ?v)
            (is-in ?v ?s)
            (> (heatindex ?s) 27.0)
            (exists (?s1 - section) (> (person-count ?s1) 0.0))
        )
        :effect (and
            (is-on ?v)
            (assign (heatindex ?s) 26.0)
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
            (forall (?s1 - section) (> (person-count ?s1) 4.0))
            (> (heatindex ?s) 31.0)
         )
        :effect (and
            (assign (person-count ?s) 1.0)
            (assign (heatindex ?s) 0.0)
        )
    )
)

