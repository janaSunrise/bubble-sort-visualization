# Bubble sort visualization

A simple pygame visualization, to visualize the working of the Bubble sort algorithm, 
in python.

## Running Demo

Here's a Demo on how it works

![alt text](https://github.com/janaSunrise/bubble-sort-visualization/blob/main/resources/sorting.gif)

## How to run it?

The project uses pipenv for dependencies.

### Install

To install the dependencies for the project, use this command

```sh
pipenv sync -d
```

### Usage

```sh
pipenv run start
```

Here are the controls!

- `Space` key press to start running the algorithm, and run it for the pre-added list.
- `R` Key press to generate a random array again, and sort it using the algorithm.

**Color Coding Syntax:**
        
- `TURQUOISE`: SWAP In progress
- `RED`: They're static, no swap
- `GREEN`: They're swapped
- `WHITE`: Reset Color

**Modifying the default list**

You can modify the default list, by changing the value of the variable `ARRAY` in `__init__.py`
And use the following controls as written above to visualize it's sorting.

## Show your support

We love people's support in growing and improving. Be sure to leave a ⭐️ if you like the project and 
also be sure to contribute, if you're interested!

<div align="center">
Made by janaSunrise with ❤
</div>
