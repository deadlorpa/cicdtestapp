import random

items = ['cabbage', '22 potato', 'tomato', 'egg', 'gym', 'ketchup', 'salat', 'cream', 'meat']
actions = ['bake', 'boil', 'kill', 'steal', 'research', 'take care of ', 'paper ']


def sample(array, n=1):
    result = random.sample(array, n)
    if n == 1:
        return result[0]
    return result


def get_random_items_and_actions(n=4):
    return sample(items, n), sample(actions, n)


def get_recepie(its, acts):
    recepie = 'Recepie:\n'
    for i in range(0, len(its)):
        recepie += str(i+1) + ') ' + acts[i] + ' ' + its[i] + '\n'
    recepie += 'Ready!'
    return recepie


if __name__ == '__main__':
    its, acts = get_random_items_and_actions(5)
    print(get_recepie(its, acts))