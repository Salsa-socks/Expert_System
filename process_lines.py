from values import rules, inital_facts, queries, facts

def process_lines(file_text):
    global rules
    global inital_facts
    global queries

    # Clean up file.
    for line in file_text:
        # Seperate the rules
        if "=>" in line or "<=>" in line:
            rules.append(line)
        # Seperate the initial facts.
        if line:
            if line[0] == '=':
                inital_facts.append(line)
            if line[0] == '?':
                queries.append(line)


def set_initial_facts():
    global facts
    for query in queries:
        for x in range(len(query) - 1):
            if query[x + 1] != ' ':
                print(query[x + 1])
                fact = query[x + 1]
                facts[fact] = True
            else:
                break
