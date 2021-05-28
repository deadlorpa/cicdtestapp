import random

items = ['шмоток укропа', '22 картошки', 'помидор', 'яйцо', 'тесто', 'кетчуп', 'лист салата', 'майонез', 'дрова']
actions = ['замешать', 'запечь', 'украсть', 'уничтожить', 'пожарить на медленном огне', 'изучить', 'сварить']


def sample(array, n=1): # получение n айтемов из передаваемого array
    result = random.sample(array, n)
    if n == 1:
        return result[0]
    return result


def get_random_items_and_actions(n=4): # получение списков с ингридиентами и действиями длины n
    return sample(items, n), sample(actions, n)


def get_recepie(its, acts):
    recepie = 'Рецепт:\n'
    for i in range(0, len(its)):
        recepie += str(i+1) + ') ' + acts[i] + ' ' + its[i] + '\n'
    recepie += 'Готово!'
    return recepie


if __name__ == '__main__':
    its, acts = get_random_items_and_actions(5)
    print(get_recepie(its, acts))