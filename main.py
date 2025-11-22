from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):                  #PORTABLE
        facts.append("portable")

    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):             #LONG_BATTERY
        facts.append("long_battery")

    if input("Is your budget high? (y/n): ").lower().startswith("y"):                       #BUGGET_HIGH
        facts.append("budget_high")

    if input("Is your budget medium? (y/n): ").lower().startswith("y"):                     #BUDGET_MEDIUM
        facts.append("budget_medium")

    if input("Is your budget low(y/n): ").lower().startswith("y"):                          #BUDGET_LOW
        facts.append("budget_low")

    if input("Will it be used for gaming? (y/n): ").lower().startswith("y"):                #GAMING
        facts.append("gaming")

    if input("Will you use it for creative works and arts? (y/n): ").lower().startswith("y"):   #CREATIVITY
        facts.append("creativity")

    if input("will it be used only for office work? (y/n): ").lower().startswith("y"):      #OFFICE-WORK
        facts.append("office_work")

    if input("Would a windows device be preferable? (y/n): ").lower().startswith("y"):      #WINDOWS
        facts.append("windows")

    if input("Would a Mac device be preferable? (y/n): ").lower().startswith("y"):          #MAC
        facts.append("mac")

    if input("Would a linux device be preferable? (y/n): ").lower().startswith("y"):        #LINUX
        facts.append("linux")

    if input("Is ai acceleration a desired feature? (y/n): ").lower().startswith("y"):      #AI-ACCELERATION
        facts.append("ai-acceleration")

    if input("Would a large screen be preferable? (y/n): ").lower().startswith("y"):        #LARGE_SCREEN
        facts.append("large-screen")

    if input("Will it be taken on trips and travels often? (y/n): ").lower().startswith("y"):   #TRAVELS
        facts.append("travels") 

    return facts

def main():
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)

    initial_facts = collect_initial_facts()

    engine.assert_facts(initial_facts)
    engine.run()

    result = engine.conclusions()

    print("\n    conclusion")

    if not result["recommendations"]:
        print("\nNo laptop recommended.")
    else:
        print("\n       Recommendations:\n")
        for r in result["recommendations"]:
            print(r)

    if not result["specifications"]:
        print("\nNo specification recommended.")
    else:
        print("\n       specifications:\n")
        for s in result["specifications"]:
            print(s)


    if not result["facts"]:
        print("N/A.")
    else:
        print ("\n      facts\n")
        for f in result["facts"]:
            print(f)


    for t in engine.trace:
        print(f"\n  Derived from: \n{t['rule']}\n")

if __name__ == "__main__":
    main()
