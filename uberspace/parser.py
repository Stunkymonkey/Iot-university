
def get_states(plan):
    print(plan)
    start_position = plan.find("step")
    # end_position = plan.find("\n     \n\ntime spent:")
    end_position = plan.find("\ntime spent:")
    if start_position == -1 or end_position == -1:
        print("no steps provided")
        return {
            "iot/actuators/section0/ventilator": False,
            "iot/actuators/section1/refill_shelf": False,
            "iot/actuators/section2/refill_shelf": False,
            "iot/actuators/section0/gate": False,
            "iot/actuators/section1/gate": False,
            "iot/actuators/section2/gate": False
        }
    else:
        steps = plan[start_position + len("step"):end_position]
        lines = steps.split("\n")
        lines = list(map(str.strip, lines))
        lines = [e[3:] for e in lines]

        present_values = set()
        for line in lines:
            present_values.add(line)

        # print(present_values)

        # mapping of steps to states
        result = dict()
        # if one ventilator is on turn on the ventilator
        result["iot/actuators/section0/ventilator"] = "VENTILATOR-ON VENTILATOR1 SUPERMARKET1" in present_values
        result["iot/actuators/section1/refill_shelf"] = "REFILL-SHELF SECTION1" in present_values
        result["iot/actuators/section2/refill_shelf"] = "REFILL-SHELF SECTION2" in present_values
        result["iot/actuators/section0/gate"] = "GATE-CLOSED MAIN-HALL1" in present_values
        result["iot/actuators/section1/gate"] = "SECTION-CLOSED SECTION1" in present_values
        result["iot/actuators/section2/gate"] = "SECTION-CLOSED SECTION2" in present_values
        return result
