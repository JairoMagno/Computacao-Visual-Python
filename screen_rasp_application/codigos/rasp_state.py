from random import choice

def rasp_update(modules_states, rasp_connect):
    for i in range(len(modules_states)):
        modules_states[i] = choice(rasp_connect)
    return modules_states