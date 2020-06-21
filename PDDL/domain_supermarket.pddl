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
        ventilator led - object
        led-red led-green - led
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
    
    ; if ventilator is off and heatindex too high and lots of people in section
    ; --> turn on ventilator
    (:action ventilator-on
        :parameters (?v - ventilator ?s - section)
        :precondition (and 
            (is-off ?v) 
            (> (person-count ?s) 0.0)
        )
        :effect (and 
            (is-on ?v) 
            (assign (heatindex ?s) 28.0)
        )
    
    )
    
    ; if ventilator is on and heatindex is low and only a few people in section
    ; --> turn ventilator off
    (:action ventilator-off
        :parameters (?v - ventilator ?s - section)
        :precondition (and   
            (is-on ?v) 
            (< (person-count ?s) 5.0)
        )
        :effect (and 
            (is-off ?v) 
            (assign (heatindex ?s) 28.0)
        )
    )
    
    ; if not too many people in section and shelf is empty refill it 
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

    ; change led light to red --> do not enter
    (:action led-red-on
        :parameters (?s - section ?lg - led-green ?lr - led-red)
        :precondition (and 
            (is-in ?lr ?s) 
            (is-in ?lg ?s) 
            (is-off ?lr)
            (> (person-count ?s) 4.0)
        )
        :effect (and 
            (is-on ?lr) 
            (is-off ?lg)
            (decrease (person-count ?s) 1) 

        )
    )

    ; led should be green --> possible to enter section 
    (:action led-green-on
        :parameters (?s - section ?lg - led-green ?lr - led-red)
        :precondition (and
            (is-in ?lg ?s)
            (is-in ?lr ?s)
            (is-off ?lg)
            (< (person-count ?s) 5.0)
        )
        :effect (and 
            (is-on ?lg)
            (is-off ?lr)
            (increase (person-count ?s) 1)
        )
    )
    
)

