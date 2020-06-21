
def get_states(plan):
    start_position = plan.find("step")
    end_position = plan.find("\n     \n\ntime spent:")
    if start_position == -1 or end_position == -1:
        print("nothing todo")
    else:
        steps = plan[start_position + len("step"):end_position]
        lines = steps.split("\n")
        lines = list(map(str.strip, lines))
        # todo find good mapping of steps to states
        print(lines)

    return [False, False, False, False, False]
