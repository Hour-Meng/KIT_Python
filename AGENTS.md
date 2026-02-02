# AGENTS.md - Python Learning Repository Guide

## Overview

This is a Python learning repository containing educational materials and practice code from a first-semester Python course. The codebase includes:

- **19 Python files** organized by topic
- Basic syntax and fundamentals (variables, strings, functions, loops)
- Object-oriented programming with Turtle graphics
- Assignment projects (shape maker, ping pong game)
- Supporting documentation and notes

All code is for learning purposes - this is not a production application.

---

## Directory Structure

```
/python_semester1/
├── 0 Basic Syntax/           # Variables, strings, basic data types
├── 1.Intro_turtle/           # Introduction to turtle graphics library
├── 3.Function/               # Function definition and usage patterns
├── 4.Loop/                   # Loop constructs (while, for, nested)
├── 5.Programming_compare_operator/  # Conditionals and comparison operators
├── 6.PingPong_game/          # Game project using turtle graphics
├── Assignments/              # Course assignments and projects
└── hello_world.py            # Entry point - basic number guessing game
```

---

## Essential Commands

### Running Python Files

```bash
# Run any Python file directly
python python_semester1/hello_world.py
python python_semester1/6.PingPong_game/pingpong.py
python python_semester1/Assignments/Auto_shape_maker.py
```

### Running Turtle Graphics Projects

Files using `turtle` library (interactive window):
- `python_semester1/1.Intro_turtle/*.py`
- `python_semester1/6.PingPong_game/pingpong.py`
- `python_semester1/Assignments/Auto_shape_maker.py`

These will open graphical windows and accept user input.

### Checking Python Version

```bash
python --version
```

---

## Project-Specific Dependencies

### Required Library: `turtle`
Standard library - no installation needed.

### Optional Dependencies
- `numpy` - imported in `Auto_shape_maker.py` (for `power` function) but may not be used
- May be missing - install with: `pip install numpy`

### Interactive Input
Programs use `turtle.textinput()`, `turtle.numinput()`, and `input()` for user interaction.

---

## Code Organization & Patterns

### Naming Conventions

**Variables:**
- Snake case for most variables: `balance`, `game`, `ran`, `plate`
- ALL CAPS for global constants: `SCORE` (in pingpong.py)
- Abbreviated/cryptic names are common in learning code:
  - `dwr` = drawer (turtle instance)
  - `ustc` = user input shape choice
  - `usts` = user input size
  - `urng` = user input color range
  - `sqm()` = square maker function
  - `tm()` = triangle maker function
  - `crm()` = circle maker function

**Functions:**
- Use descriptive names with underscores: `move_plate_up()`, `screen_setup()`
- Some shortened names: `sqm()`, `tm()`, `crm()`
- Follow Python naming conventions even when abbreviated

### Type Hints

Modern files use type hints:
```python
def multiply(a: int | float, b: int | float):
    result = a * b
    return result
```

Older files may lack type hints - this is intentional as part of learning progression.

### Function Organization

Functions are typically:
- Defined before use
- Often nested within other functions for scope (see `plate_logic()` in pingpong.py)
- May have docstrings in comments above the function
- Use `if __name__ == "__main__":` guard for entry points

### Global Variables

Used in educational context:
- `SCORE` in pingpong.py is a global that tracks game state
- Modified with `global SCORE` keyword when needed
- Not best practice but acceptable for learning code

---

## Code Style & Patterns

### Comments
- Single-line: `# This is a comment`
- Multi-line: `''' docstring '''`
- Inline explanations common: `# all cap as it's a global value`
- Descriptive comments above complex logic

### Indentation
- Consistent 4-space indentation (no tabs)
- Python standard PEP 8 style

### String Formatting
- Modern: f-strings: `f"Current balance is ${balance}"`
- Used in `print()` and `turtle.write()`

### Comparison & Logic
```python
# Comparison operators
if game == ran:
if balance > 0:

# Boolean logic
if plate.ycor() > 220:
while balance > 0:
```

### Turtle Graphics Patterns

Classes/methods used:
```python
window = t.Screen()
window.setup(width=800, height=600)
window.title("Ping Pong Game")
window.listen()  # Enable keyboard listening
window.onkeypress(function, "key")  # Bind keys

turtle = t.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(x, y)
turtle.shape("square")
turtle.shapesize(width, height)
turtle.write(text, font=("Arial", size, "style"))
turtle.sety(value)  # Set Y coordinate
turtle.ycor()  # Get Y coordinate
```

---

## Testing & Validation

**No automated tests** - this is a learning repository.

**Manual testing:**
- Run Python files directly to verify functionality
- Interactive programs accept user input via turtle dialogs or terminal
- Visual verification through turtle graphics output

**Common Issues:**
- Turtle programs require a display/GUI environment
- Some files may have incomplete implementations (learning in progress)
- `tempCodeRunnerFile.py` is a scratch file (can be ignored)

---

## Important Gotchas & Non-Obvious Patterns

### 1. **Abbreviated Variable Names**
Learning code heavily uses 3-letter abbreviations. Always check the comments or surrounding code to understand what variables represent. This is intentional for learning but not production-quality.

### 2. **Global SCORE in Ping Pong**
The `SCORE` variable in pingpong.py uses `global` keyword. Understand this is a teaching example - production code would use a class instead.

### 3. **Turtle Graphics Blocking Behavior**
`turtle.done()` blocks execution and keeps the window open. Programs with `turtle` won't exit immediately.

### 4. **Screen Update Control**
The game files use `window.tracer(0)` to disable automatic updates and `window.update()` for manual refresh. This is important for animation performance.

### 5. **Incomplete Implementations**
Some files are works-in-progress (e.g., `score_update()` in pingpong.py is defined but may not integrate fully). Check for TODOs in comments.

### 6. **Function Return Values**
Functions like `ball_physics()` and `plate_logic()` in pingpong.py are generators or infinite loops - they don't cleanly return values. This is learning-stage code.

### 7. **Missing numpy Import**
`Auto_shape_maker.py` imports `from numpy import power` but never uses it. The import exists but is unused.

### 8. **Input Validation**
Some user inputs have validation (Auto_shape_maker checks color/choice), others don't. Be cautious when running user-input code.

---

## Project Context

### What This Repository Is
- A semester 1 Python course curriculum
- Contains progressively complex learning exercises
- Includes assignments demonstrating course concepts
- Educational/practice code, not production

### What This Repository Is NOT
- A complete, production-ready application
- A library to be imported elsewhere
- A project with tests, CI/CD, or deployment
- A finished product - actively being developed as coursework

---

## Adding New Code

When adding new Python files:
1. Place in appropriate topic folder (or create new one)
2. Use snake_case for filenames: `my_program.py`
3. Include comments explaining what the code demonstrates
4. Test by running: `python python_semester1/path/to/file.py`
5. Consider adding docstrings for functions
6. If adding dependencies, update this guide

---

## Key Files to Know

| File | Purpose |
|------|---------|
| `hello_world.py` | Number guessing game with balance tracking |
| `pingpong.py` | Turtle graphics game (incomplete but extensive) |
| `Auto_shape_maker.py` | Interactive shape drawing with user input |
| `Assignments/` | Course assignments demonstrating concepts |
| `0 Basic Syntax/` | Fundamental Python concepts |
| `3.Function/` | Function definition and usage |

---

## Quick Reference

**Run a Python file:**
```bash
python python_semester1/path/to/file.py
```

**Debug tips:**
- Add `print()` statements to trace execution
- Use turtle `hideturtle()` and `penup()` to avoid drawing artifacts
- Check indentation (Python is whitespace-sensitive)
- Watch for undefined variables or missing imports

**Common Python Concepts Used:**
- Variables and data types (int, float, str, bool)
- Functions with parameters and return values
- While loops and for loops
- Conditionals (if/elif/else)
- String formatting with f-strings
- Object-oriented turtle graphics
- User input/output
