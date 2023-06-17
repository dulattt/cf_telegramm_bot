import json


def format_str(s: list) -> str:
    return f"{s[0]}  {s[1]}  {s[2]} \n" if len(s) >= 3 else ""


def get() -> list[str]:
    data = []
    with open("C:\pys\cfbot\cf\data.json", "r") as file:
        data = json.load(file)

    res = []

    for dat in data:
        if dat:
            res.append(format_str(dat))

    return res
