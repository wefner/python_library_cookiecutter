#!/usr/bin/env bash

# Needs to be sourced
# Sets up alias functions for the interface while keeping backwards compatibility with the old bash type

for command in bootstrap lint test build tag upload document graph
do
    eval "_$command() { if [ -f _CI/scripts/$command.py ]; then ./_CI/scripts/$command.py; else ./_CI/scripts/$command || echo "Command $command not found."; fi }"
done

alias _activate='source .venv/bin/activate'
