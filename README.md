# NodeGainsDB v1.0 - Roid Rage Edition
### NodeGains is BULKING, NOT at its best physique. "Wait for the CUT"


Welcome to **NodeGainsDB**, a jacked-up Python graph database that pumps iron with nodes, edges, and queries. Built from the ground up to flex your data, this version—**Roid Rage Edition**—brings a stable, debugged core with a simple yet powerful GymQL syntax. Use it to `LIFT` bros, `SPOT` connections, and track those sweet `GAINS`. Stored in JSON, indexed for speed, and run via a terminal CLI, it’s time to build your data muscles!

## Features
- **Nodes**: Create bros with labels and properties (e.g., `name`, `gains`, `reps`).
- **Edges**: Connect bros with relationships like `FLEX` or `SPOT`.
- **Queries**: Retrieve nodes and traverse relationships with `SPOT`.
- **Persistence**: Save your graph to `gains_data.json` and reload it anytime.
- **Debugged**: No more dropped bars—stable and ready to lift!

## Repo
- **GitHub**: [https://github.com/Astrasv/NodeGainsDB](https://github.com/Astrasv/NodeGainsDB)
- **Version**: v1.0 - Roid Rage Edition
- **Author**: Astrasv

## Setup
Get your environment pumped and ready to lift:

1. **Prerequisites**:
   - Python 3.8 or higher
   - Git (optional, for cloning)

2. **Clone the Repo**:
   ```bash
   git clone https://github.com/Astrasv/NodeGainsDB.git
   cd NodeGainsDB
   ```

3. **(Optional) Virtual Environment**: Stay lean by isolating dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. **No Dependencies**: Pure Python, no pip install needed—just raw power!

## How to Run
Flex those gains in your terminal:

1. **Start Fresh (optional)**: Clear old data to reset the graph:
   ```bash
   rm gains_data.json  # Linux/Mac
   del gains_data.json # Windows
   ```

2. **Launch the CLI**:
   ```bash
   python main.py
   ```
   You’ll see:
   ```
   Graph initialized
   Index initialized
   No gains_data.json found, starting fresh
   Welcome to NodeGainsDB, bro! Time to flex some data gains—type 'help'!
   ```

3. **Interact**: Enter commands at the `>` prompt (see examples below).

4. **Exit**: Save your gains and bounce:
   ```
   > exit
   Saved data to gains_data.json
   Gains locked in, bro! See ya!
   ```
5. **Ask NodeGains for help**: See the list of working commands:
   ```
   > help

                GymQL Commands:
                - LIFT (n:Bro {name: 'Chad'}): Add a bro
                - LIFT (n:Bro)-[:FLEX]->(m:Bro): Connect bros
                - SPOT (n:Bro {name: 'Chad'}) GAINS n: Find a bro
                - SPOT (n:Bro)-[:FLEX]->(m) GAINS m: Spot connections
                - exit: Save and bounce
   ```
   

## GymQL Syntax
- **LIFT**: Add nodes or relationships.
  - **Node**: `LIFT (n:<label> {prop: 'value'});`
  - **Relationship**: `LIFT (n:<label> {prop: 'value'})-[:<type>]->(m:<label> {prop: 'value'});`
- **SPOT**: Query nodes or relationships.
  - **Node**: `SPOT (n:<label> {prop: 'value'}) GAINS n;`
  - **Relationship**: `SPOT (n:<label> {prop: 'value'})-[:<type>]->(m) GAINS m;`

## Example Command Sequence
Build and query a graph of bros with this sequence.

1. **Add Chad with Huge Gains**
   ```
   > LIFT (n:Bro {name: 'Chad', gains: 'huge'});
   ```

2. **Add Brad with Reps**
   ```
   > LIFT (n:Bro {name: 'Brad', reps: '20'});
   ```

3. **Connect Chad and Brad with FLEX**
   ```
   > LIFT (n:Bro {name: 'Chad'})-[:FLEX]->(m:Bro {name: 'Brad'});
   ```

4. **Add Tad and Connect to Chad**
   ```
   > LIFT (n:Bro {name: 'Tad', reps: '15'})-[:SPOT]->(m:Bro {name: 'Chad'});
   ```

5. **Spot All Bros Named Chad**
   ```
   > SPOT (n:Bro {name: 'Chad'}) GAINS n;
   ```

6. **Spot Chad’s FLEX Connections**
   ```
   > SPOT (n:Bro {name: 'Chad'})-[:FLEX]->(m) GAINS m;
   ```

7. **Spot Tad’s SPOT Connections**
   ```
   > SPOT (n:Bro {name: 'Tad'})-[:SPOT]->(m) GAINS m;
   ```

8. **Save and Exit**
   ```
   > exit
   ```

9. **Restart and Verify Persistence**
   ```bash
   python main.py
   ```
   ```
   > SPOT (n:Bro {name: 'Brad'}) GAINS n;
   ```
