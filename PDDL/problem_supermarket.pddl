(define (problem supermarket_problem) (:domain domain_supermarket)

(:objects 
    section0 section1 section2 - section    
    proximity1 proximity2 - proximity
    ledmatrix1 ledmatrix2 - led 
    ventilator1 - ventilator
    b-in-s0 b-in-s1 b-in-s2 - button-in
    b-out-s0 b-out-s1 b-out-s2 - button-out
    ledEntrance - led-green
    ledExit - led-red
)

; init everything thats true, otherwise it is false by default
(:init 
    (is-in ledmatrix1 section1)
    (is-in ledmatrix2 section2)
    (is-in proximity1 section1)
    (is-in proximity2 section2)
    (is-in b-in-s0 section0)
    (is-in b-out-s0 section0)
    (is-in b-in-s1 section1)
    (is-in b-out-s1 section1)
    (is-in b-in-s2 section2)
    (is-in b-out-s2 section2)
    (is-off ventilator1)
    (= (airquality section1) 4.0)
    (= (airquality section2) 4.0)
    (= (person-count section1) 4.0)
    (= (person-count section2) 4.0)
    (= (led-number section1) 0.0)
    (= (led-number section2) 0.0)
    (is-pressed b-in-s1)
    (= (heatindex section1) 28.0)
    (= (heatindex section2) 28.0)
)

(:goal (and (> (airquality section1) 5.0) (> (airquality section2) 5.0)) )


)