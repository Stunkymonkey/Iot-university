from jinja2 import Template

problem_template = Template("""
(define (problem supermarket_problem) (:domain domain_supermarket)

(:objects
    section1 section2 - section
    main-hall1 - main-hall
    supermarket1 - supermarket
    ventilator1 - ventilator
)

; init everything thats true, otherwise it is false by default
(:init

    (is-in ventilator1 main-hall1)
    (is-off ventilator1)

    (= (person-count supermarket1) {{ pers_s0 }})
    (= (person-count main-hall1) {{ pers_s0 }})
    (= (person-count section1) {{ pers_s1 }})
    (= (person-count section2) {{ pers_s2 }})

    (= (temperature supermarket1) {{ temperature }})
    (= (temperature main-hall1) {{ temperature }})
    (= (heatindex supermarket1) {{ heat_index }})
    (= (heatindex main-hall1) {{ heat_index }})

    (= (shelf-items section1) {{ shelf_s1 }})
    (= (shelf-items section2) {{ shelf_s2 }})
)

(:goal
    (and
        (< (heatindex main-hall1) 35) (< (heatindex supermarket1) 27)
        (> (shelf-items section1) 0) (> (shelf-items section2) 0)
        (< (person-count supermarket1) 7)
        (< (person-count main-hall1) 10)
        (< (person-count section1) 5) (< (person-count section2) 5)
    )
)
)
""")


def to_problem_file(temperature, heat_index, pers_s0, pers_s1, pers_s2, shelf_s1, shelf_s2):
    output = problem_template.render(temperature=temperature, heat_index=heat_index,
                                     pers_s0=pers_s0, pers_s1=pers_s1, pers_s2=pers_s2,
                                     shelf_s1=shelf_s1, shelf_s2=shelf_s2)
    with open("problem_supermarket_generated.pddl", "w") as text_file:
        text_file.write(output)
