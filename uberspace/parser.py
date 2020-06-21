
def get_states(plan):
    start_position = plan.find("step")
    end_position = plan.find("\n     \n\ntime spent:")
    if start_position == -1 or end_position == -1:
        # print("nothing todo")
        return [False, False, False, False, False]
    else:
        steps = plan[start_position + len("step"):end_position]
        lines = steps.split("\n")
        lines = list(map(str.strip, lines))
        lines = [e[3:] for e in lines]
        present_values = set()
        for line in lines:
            present_values.add(line)
        # mapping of steps to states
        if "VENTILATOR-ON VENTILATOR1 SECTION1" in present_values or "VENTILATOR-ON VENTILATOR1 SECTION2" in present_values:
            ventilator_on = True
        if "REFILL-SHELF SECTION1" in present_values:
            refill_shelf_1 = True
        if "REFILL-SHELF SECTION2" in present_values:
            refill_shelf_2 = True
        if "LED-RED-ON SECTION0 LED-GREEN-S2 LED-RED-S2" in present_values:
            block_section_0 = True
        if "LED-RED-ON SECTION1 LED-GREEN-S0 LED-RED-S2" in present_values:
            block_section_1 = True
        if "LED-RED-ON SECTION2 LED-GREEN-S2 LED-RED-S2" in present_values:
            block_section_2 = True
        # print(present_values)

        return [ventilator_on, refill_shelf_1, refill_shelf_2, block_section_0, block_section_1, block_section_2]
