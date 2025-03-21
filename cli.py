from graph_db import Graph, Storage, GymQLParser

def run_cli():
    graph = Graph()
    storage = Storage()
    parser = GymQLParser(graph)
    storage.load(graph)
    print("Welcome to NodeGainsDB, bro! Time to flex some data gains—type 'help'!")

    while True:
        command = input("> ").strip()
        if not command:
            continue
        try:
            if command.lower() == "exit":
                storage.save(graph)
                print("Gains locked in, bro! See ya!")
                break
            elif command.lower() == "help":
                print("""
                GymQL Commands:
                - LIFT (n:Bro {name: 'Chad'}): Add a bro
                - LIFT (n:Bro)-[:FLEX]->(m:Bro): Connect bros
                - SPOT (n:Bro {name: 'Chad'}) GAINS n: Find a bro
                - SPOT (n:Bro)-[:FLEX]->(m) GAINS m: Spot connections
                - exit: Save and bounce
                """)
            elif command.upper().startswith(("LIFT", "SPOT")):
                results = parser.parse(command)
                for result in results:
                    print(result if isinstance(result, dict) else str(result))
            else:
                print("No gains here, bro! Type 'help'!")
        except Exception as e:
            print(f"Dropped the bar, bro! Error: {e}")