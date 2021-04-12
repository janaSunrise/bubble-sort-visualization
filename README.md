# Bubble sort visualization

A simple pygame visualization, to visualize the working of the Bubble sort algorithm, 
in python.

## Running Demo

Here's a Demo on how it works

![alt text](https://github.com/janaSunrise/bubble-sort-visualization/blob/main/resources/sorting.gif)

## How to run it?

The project uses pipenv for dependencies. You can install the dependencies by using `pipenv sync -d`. Then start the
app using `pipenv run start`.

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

<div align="center">
Made by janaSunrise with ❤
</div>
