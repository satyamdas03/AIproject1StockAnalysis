# Stock Analysis Project

## Overview

This project aims to develop a comprehensive stock analysis report that includes trend analysis, predictions, and investment recommendations.

## Setting Up the Environment

### Step 1: Setting Up `pyproject.toml`

The `pyproject.toml` file turns all the requirements of our project into code, so we can run an install script to package and build all the necessary dependencies.

1. **Install Poetry**:
    ```sh
    pipx install poetry
    ```

2. **Install pipx**:
    ```sh
    py -m pip install --user pipx
    ```

3. **Create `pyproject.toml`**:
    - Define core components under `[tool.poetry]` such as `name` and `description`.
    - Specify dependencies required for the project.
    - Use `tool.pyright` to check Python codes for type errors.
    - Use `tool.ruff` to check for errors and styling issues.
    - Define `build-system` to use Poetry version.

### Step 2: Install Dependencies

Open the terminal and run:
```sh
poetry install --no-root
```

### Step 3: Check Python Version

Check the currently used Python version for your Poetry environment:
```sh
poetry env list
```

### Step 4: Enter Poetry Environment

Enter into the Poetry environment:
```sh
poetry shell
```

After this, you will have a Python environment in which you can work.


## Cheat Sheet to Make a Good Agent
### General Guidelines
-**Begin with the end in mind**:  Identify the specific outcome your tasks are aiming to achieve.
-**Break down the outcome into actionable tasks**:  Assign each task to the appropriate agent.
-**Ensure the tasks are descriptive**: Provide clear instructions and expected deliverables.

### Project Goal
Develop a comprehensive stock analysis report that includes trend analysis, predictions, and investment recommendations.

### Key Roles
**Captain/Manager/Boss**
**Role**: Expert Stock Analyst
-**Responsibilities**: Oversees the entire stock analysis project.
-**Goal**: Ensure the final report is accurate, comprehensive, and actionable.
-**Backstory**: Experienced stock analyst with a background in financial markets and data analysis.





