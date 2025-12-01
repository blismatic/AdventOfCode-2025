# AdventOfCode-2025
Make sure your Advent of Code session token is stored in a `.env` file

This project uses `uv`, the [extremely fast Python package and project manager](https://docs.astral.sh/uv/).

*Note: last line of input file does **not** end with a newline character*

## Helpful Commands
`Set-ExecutionPolicy Unrestricted -Scope Process` if you are getting a "*\\AdventOfCode-2025\\.venv\\scripts\\Activate.ps1 cannot be loaded because running scripts is disabled on this system.*" error

`uv self update` to update the UV tool

`uv add X` to install dependency X

`uv remove X` to remove dependecy X

`uv run 01/main.py` to run a file

`uv cache clear` for when you get hardlink errors when trying to add dependencies
