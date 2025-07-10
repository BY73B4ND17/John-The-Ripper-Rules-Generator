commands = [
    ":", "l", "u", "c",
    "sa@", "sa4", "sA4", "sA@", "se3", "sE3",
    "si1", "si!", "sI1", "sI!", "so0", "sO0",
    "ss$", "ss5", "sS$", "sS5", "sT7", "st7",
    "sl1", "sL1", "sg9", "sG9", "sz2", "sZ2",
    "sb8", "sB8", 'Az"[0-9][0-9][0-9][0-9]"'
]

rules = [""]

for command in commands:
    current_rules = rules[:]
    for rule in current_rules:
        new_rule = f"{rule} {command}".strip()
        rules.append(new_rule)
        print(new_rule)
