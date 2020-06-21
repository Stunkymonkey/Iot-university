(define (problem supermarket_problem) (:domain domain_supermarket)

(:objects
    section0 section1 section2 - section
    ventilator1 - ventilator
    led-green-s0  led-green-s1 led-green-s2 - led-green
    led-red-s0 led-red-s1 led-red-s2 - led-red
)

; init everything thats true, otherwise it is false by default
(:init
    (is-in led-green-s0 section1)
    (is-in led-green-s1 section1)
    (is-in led-green-s2 section2)

    (is-in led-red-s2 section0)
    (is-in led-red-s2 section1)
    (is-in led-red-s2 section2)

    (is-on led-green-s0)
    (is-off led-red-s0)

    (is-on led-green-s1)
    (is-off led-red-s1)

    (is-on led-green-s2)
    (is-off led-red-s2)

    (is-off ventilator1)

    (= (person-count section1) 2.0)
    (= (person-count section2) 6.0)

    (= (heatindex section1) 28.0)
    (= (heatindex section2) 33.0)

    (= (shelf-items section1) 0.0)
    (= (shelf-items section2) 2.0)
)

(:goal
    (and
        (> (heatindex section1) 27.0) (< (heatindex section1) 32.0)
        (> (heatindex section2) 27.0) (< (heatindex section2) 32.0)
        (> (shelf-items section1) 0.0) (> (shelf-items section2) 0.0)
        (< (person-count section1) 5.0) (< (person-count section2) 5.0)
    )
)
)
