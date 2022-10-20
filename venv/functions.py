import json

DATA_SOURCE = 'candidates.json'

'''`load_candidates()`, которая загрузит данные из файла

`get_all()`, которая покажет всех кандидатов

`get_by_pk(pk)`, которая вернет кандидата по pk

`get_by_skill(skill_name)`, которая вернет кандидатов по навыку'''


def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_all(path):
    candidates = load_candidates(path)
    return candidates


def get_by_pk(pk, path):
    candidate = []
    data = load_candidates(path)
    candidate.append(data[pk + 1])
    return candidate


def get_by_skill(skill_name, path):
    data = load_candidates(path)
    candidates = []
    for candidate in data:
        if skill_name in candidate["skills"].split(', '):
            candidates.append(candidate)
    return candidates


