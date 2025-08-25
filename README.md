# Blackjack Strategy CLI 🃏

A command-line tool for practicing and using **Basic Blackjack strategy**. Enter the dealer’s up-card and your hand, and the program will suggest the optimal move (Hit, Stand, Double, etc.). Perfect for learning or sharpening your skills at the table!

## Features 📊

* Validates player and dealer card input
* Suggests optimal Blackjack actions based on strategy rules
* Supports repeated **Hit** cycles, recalculating the best move each time
* Continuous rounds until you choose to quit
* Clean and colorful CLI interface using `colorama`

## Installation 📦

This project uses [uv](https://docs.astral.sh/uv/) as its package manager.
If you don’t already have it, install `uv` by following the [official instructions](https://docs.astral.sh/uv/getting-started/).

Clone the repository and install dependencies:

```bash
git clone https://github.com/jerryshum/blackjack-cli.git
cd blackjack-cli
uv sync
```

This will create and manage a virtual environment for you and install all dependencies declared in `pyproject.toml`.

## Usage

Run the app with:

```bash
uv run python main.py
```

Example interaction:

```
Dealer Card (The card that the dealer shows): K
Player Cards (The cards that the player has): 10 2
-------------------------------------------------------------------------
Suggested Action: Hit
🤔 Since we suggested you to hit again, would you like to input your new card? (y/n)
```

## Roadmap 🗺

* Add automated unit tests
* Expand support for special rules (e.g., Splits)
* Improve error handling for unexpected input
* Add strategy table reference in documentation


## License

This project is open-source under the MIT License.

