
def get_states(plan):
    start_position = plan.find("step")
    end_position = plan.find("\n     \n\ntime spent:")
    if start_position == -1 or end_position == -1:
        # print("nothing todo")
        return [False, False, False, False, False, False]
    else:
        steps = plan[start_position + len("step"):end_position]
        lines = steps.split("\n")
        lines = list(map(str.strip, lines))
        lines = [e[3:] for e in lines]

        present_values = set()
        for line in lines:
            present_values.add(line)

        # mapping of steps to states
        result = dict()
        # if one ventilator is on turn on the ventilator
        result["iot/actuators/section0/ventilator"] = "VENTILATOR-ON VENTILATOR1 SECTION1" in present_values or \
                                                      "VENTILATOR-ON VENTILATOR1 SECTION2" in present_values
        result["iot/actuators/section1/refill_shelf"] = "REFILL-SHELF SECTION1" in present_values
        result["iot/actuators/section2/refill_shelf"] = "REFILL-SHELF SECTION2" in present_values
        result["iot/actuators/section0/gate"] = "LED-RED-ON SECTION0 LED-GREEN-S2 LED-RED-S2" in present_values
        result["iot/actuators/section1/gate"] = "LED-RED-ON SECTION1 LED-GREEN-S0 LED-RED-S2" in present_values
        result["iot/actuators/section2/gate"] = "LED-RED-ON SECTION2 LED-GREEN-S2 LED-RED-S2" in present_values
        return result
