from jinja2 import Template

problem_template = Template("""
(define (problem supermarket_problem) (:domain domain_supermarket)

(:objects
    section0 section1 section2 - section
    ventilator1 - ventilator
)

; init everything thats true, otherwise it is false by default
(:init

    (is-in ventilator1 section0)
    (is-off ventilator1)

    (= (person-count section0) {{ pers_s0 }})
    (= (person-count section1) {{ pers_s1 }})
    (= (person-count section2) {{ pers_s2 }})

    (= (heatindex section0) {{ heat_index }})

    (= (shelf-items section1) {{ shelf_s1 }})
    (= (shelf-items section2) {{ shelf_s2 }})
)

(:goal
    (and
        (< (heatindex section0) 27.0)
        (> (shelf-items section1) 0.0) (> (shelf-items section2) 0.0)
        (< (person-count section0) 5.0) (< (person-count section1) 5.0) (< (person-count section2) 5.0)
    )
)
)
""")


def to_problem_file(heat_index, pers_s0, pers_s1, pers_s2, shelf_s1, shelf_s2):
    output = problem_template.render(heat_index=heat_index, pers_s0=pers_s0, pers_s1=pers_s1,
                                     pers_s2=pers_s2, shelf_s1=shelf_s1, shelf_s2=shelf_s2)
    with open("problem_supermarket_generated.pddl", "w") as text_file:
        text_file.write(output)
