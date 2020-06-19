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
        button led ventilator proximity - object
        button-in button-out - button 
        led-red led-green - led
    )


    (:predicates
       
        ; change state of actuators
        (is-in ?o - object ?s - section)
        (is-on ?o - object)
        (is-off ?o - object)
        (is-pressed ?b - button)
        
    
        ; shelf empty?
        (shelf-empty ?s - section)
        (send-notification ?s - section)
    )
    
    (:functions 
        (person-count ?s - section)
        (airquality ?s - section)
        (heatindex ?s - section)
        (led-number ?s - section)
        
    )
    
    ; if ventilator is off and heatindex too high and lots of people in section
    ; --> turn on ventilator
    (:action ventilator-on
        :parameters (?v - ventilator ?s - section)
        :precondition (and 
            (is-off ?v) 
            (< (heatindex ?s) 32.0) 
            (> (heatindex ?s) 27.0) 
            (> (person-count ?s) 0.0)
        )
        :effect (and 
            (is-on ?v) 
            (increase (airquality ?s) 2.0)
        )
    
    )
    
    ; if ventilator is on and heatindex is low and only a few people in section
    ; --> turn ventilator off
    (:action ventilator-off
        :parameters (?v - ventilator ?s - section)
        :precondition (and   
            (is-on ?v) 
            (> (heatindex ?s) 32.0) 
            (< (heatindex ?s) 27.0) 
            (< (person-count ?s) 5.0)
        )
        :effect (and (is-off ?v) (decrease (airquality ?s) 2.0))
    )
    
    ; if section is occupied and shelf is empty send message to bot 
    (:action refill-shelf
        :parameters (?s - section)
        :precondition (and 
            (shelf-empty ?s) 
            (> (person-count ?s) 3.0)
        )
        :effect (send-notification ?s)
    )
    
    ; people can only enter supermarket if there are less then 10 people in all sections
    (:action enter-supermarket
        :parameters (?s1 ?s2 - section ?lr - led-red ?lg - led-green)
        :precondition (and 
            (not (shelf-empty ?s1))
            (not (shelf-empty ?s2))
            (< (person-count ?s1) 5.0)
            (< (person-count ?s2) 5.0)
        )
        :effect (and 
            (is-on ?lg) 
            (is-off ?lr)
        )
    )
    
     
    (:action do-not-enter-supermarket
        :parameters (?s1 ?s2 - section ?lr - led-red ?lg - led-green)
        :precondition (and 
            (> (person-count ?s1) 5.0)
            (> (person-count ?s2) 5.0)
        )
        :effect (and 
            (is-on ?lr)
            (is-off ?lg) 
        )
    )
    
    (:action enter-section
        :parameters (?s - section ?b - button-in ?l - led)
        :precondition (and 
            (not (shelf-empty ?s)) 
            (is-pressed ?b) 
            (is-in ?l ?s)
            (is-in ?b ?s)
            (< (person-count ?s) 5.0)
        )
        :effect (and 
            (increase (person-count ?s) 1.0)
            (decrease (airquality ?s) 1.0)
            (assign (led-number ?s) (person-count ?s))
        ) 
    )
    
    (:action leave-section
        :parameters (?s - section ?b - button-out ?l - led)
        :precondition (and 
            (is-pressed ?b) 
            (is-in ?l ?s)
            (is-in ?b ?s)
        )
        :effect (and
            (decrease (person-count ?s) 1.0)
            (increase (airquality ?s) 1.0)
            (assign (led-number ?s) (person-count ?s))
        )
    )
    
    
    
    
    
    
)

