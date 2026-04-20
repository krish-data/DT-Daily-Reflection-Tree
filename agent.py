#!/usr/bin/env python3
import csv
from collections import defaultdict

TREE_FILE = "reflection-tree.tsv"

def load_tree(path):
    nodes = {}
    children = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            row = {k: (v if v != "" else None) for k, v in row.items()}
            nodes[row["id"]] = row
            if row["parentId"] and row["parentId"] != "null":
                children[row["parentId"]].append(row["id"])
    return nodes, children

def apply_signal(state, signal):
    if not signal or signal == "none":
        return
    if ":" in signal:
        axis, pole = signal.split(":", 1)
        state["counts"][axis][pole] += 1

def dominant(counts):
    result = {}
    for axis, d in counts.items():
        if not d:
            result[axis] = "mixed"
            continue
        items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        if len(items) == 1 or items[0][1] > items[1][1]:
            result[axis] = items[0][0]
        else:
            result[axis] = "mixed"
    return result

def interpolate(text, state):
    if not text:
        return ""
    out = text
    for qid, ans in state["answers"].items():
        out = out.replace("{%s.answer}" % qid, ans)
    dom = dominant(state["counts"])
    for axis, pole in dom.items():
        out = out.replace("{%s.dominant}" % axis, pole)
    return out

def choose(prompt, options):
    while True:
        print("\n" + prompt)
        for i, op in enumerate(options, 1):
            print(f"{i}. {op}")
        val = input("Choose an option number: ").strip()
        if val.isdigit() and 1 <= int(val) <= len(options):
            return options[int(val)-1]

def decision_target(rule_text, prev_answer):
    rules = rule_text.split(";")
    for r in rules:
        cond, target = r.split(":")
        cond = cond.replace("answer=", "")
        values = cond.split("|")
        if prev_answer in values:
            return target
    raise ValueError(f"No route found for answer: {prev_answer}")

def next_child(children, node_id):
    kids = children.get(node_id, [])
    return kids[0] if kids else None

def run():
    nodes, children = load_tree(TREE_FILE)
    state = {"answers": {}, "counts": defaultdict(lambda: defaultdict(int))}
    current = "START"
    last_answer = None

    while current:
        node = nodes[current]
        ntype = node["type"]
        text = interpolate(node["text"], state)
        apply_signal(state, node.get("signal"))

        if ntype == "start":
            print(text)
            current = next_child(children, current)
        elif ntype == "question":
            options = (node["options"] or "").split("|")
            answer = choose(text, options)
            state["answers"][current] = answer
            last_answer = answer
            current = node["target"] or next_child(children, current)
        elif ntype == "decision":
            current = decision_target(node["text"] or node["options"], last_answer)
        elif ntype in {"reflection", "bridge", "summary", "end"}:
            print("\n" + text)
            if ntype == "end":
                break
            input("\nPress Enter to continue...")
            current = node["target"] or next_child(children, current)
        else:
            raise ValueError(f"Unknown node type: {ntype}")

if __name__ == "__main__":
    run()
