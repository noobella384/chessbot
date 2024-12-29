# Queen's Gambit: Python-Based Chess Engine

## Project Overview
This project was undertaken as part of the Seasons of Code (Jun '24 - Jul '24) organized by the Web and Coding Club at IIT Bombay. The objective was to design and develop a Python-based chess engine capable of analyzing and optimizing chess gameplay. By implementing advanced algorithms and improving computational efficiency, the engine supports Universal Chess Interface (UCI) compatibility and provides robust move analysis.

## Key Features
- **Minimax Algorithm**: Evaluates possible moves and their consequences to make optimal decisions in adversarial conditions.
- **Alpha-Beta Pruning**: Reduces the number of nodes evaluated by the Minimax algorithm, improving efficiency by up to 25%.
- **Iterative Deepening**: Ensures efficient exploration of chess puzzles, including complex mate-in-2, 3, and 4 scenarios.
- **Hans-Berliner’s System**: Structures and organizes move evaluation for better decision-making.
- **Universal Chess Interface (UCI)**: Ensures compatibility with popular chess platforms.

## Repository Contents
| File/Directory              | Description                                                  |
|------------------------------|--------------------------------------------------------------|
| **Give_Optimal_Move.py**      | Implements the Minimax algorithm and Alpha-Beta Pruning for decision-making. |
| **Greedy_Or_Not.py**          | Contains a simpler greedy algorithm for evaluating moves, contrasting it with the Minimax approach. |
| **helper.cpp**                | Provides utility functions in C++ for performance-critical tasks such as board evaluations. |
| **reading1.pdf**              | Reference material explaining Hans-Berliner’s system and its application in the project. |
| **reading2.pdf**              | A theoretical overview of the Minimax and Alpha-Beta Pruning algorithms. |
| **reading3.pdf**              | Documentation on UCI integration and its usage with the chess engine. |
| **Final_Attempt/chessbot.py** | An initial version of the chess engine with basic move evaluation capabilities. |
| **Final_Attempt/chessbot_v2.py** | Enhanced move evaluation featuring a move ordering function for better Alpha-Beta Pruning. |
| **Final_Attempt/final_engine.py** | The finalized chess engine integrating iterative deepening and UCI compatibility. |
| **Final_Attempt/uci.py**      | Enables UCI support for interaction with external chess platforms. |
| **Final_Attempt/a**           | Auxiliary file used during the engine's development, potentially for debugging or testing purposes. |

### Note:
The **Final_Attempt** directory contains the final code for Chessbot, showcasing all the advanced features, optimizations, and UCI compatibility.

---

## Workflow
The Chessbot project was developed through several key steps:

1. We began by studying chess rules, move mechanics, and board representation to build a solid foundation for the engine's logic.
2. A simple greedy algorithm was implemented to evaluate basic board states and suggest moves.
3. The Minimax algorithm was developed to simulate future board states and evaluate moves more comprehensively.
4. To optimize performance, Alpha-Beta Pruning was introduced, reducing unnecessary computations and improving efficiency.
5. Additional enhancements, like move ordering and iterative deepening, were added to improve decision-making and puzzle-solving capabilities.
6. Hans-Berliner’s evaluation system was implemented to prioritize factors such as piece positioning and control.
7. UCI (Universal Chess Interface) support was integrated, enabling the Chessbot to interact with external chess platforms seamlessly.
8. Finally, all components were integrated into the final version, followed by rigorous testing to refine its performance.

---

## Installation and Usage
No installation and usage details have been provided as per your request. Ensure Python 3 is installed on your system to run the provided scripts.

---

## Acknowledgments
This project was undertaken as part of the Seasons of Code (Jun '24 - Jul '24) by the Web and Coding Club at IIT Bombay. Special thanks to mentors and peers who provided guidance and support throughout the development process.

---


