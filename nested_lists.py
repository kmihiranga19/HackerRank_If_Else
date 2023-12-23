if __name__ == '__main__':
    records = []
    for a in range(int(input())):
        record = {
            "name": "",
            "score": ""
        }
        name = input()
        score = float(input())
        record["name"] = name
        record["score"] = score
        records.append(record)
    records.sort(key=lambda x: x["score"])
    first_score = records[0]["score"]

    i = len(records) - 1
    while i >= 1:
        if records[i]["score"] == first_score:
            records.pop(i)
        i -= 1

    seconds_lower_score = records[1]["score"]
    _names = []
    for record in records:
        if record["score"] == seconds_lower_score:
            _names.append(record["name"])
    ase_order_names = sorted(_names)

    for ase_order_name in ase_order_names:
        print(ase_order_name)
