# Undergraduate coursework

Two directories with different provenance and different licences.

## `fmri_signal_analysis/`

Neuroimaging and signal processing coursework from a Dartmouth psychology
course, covering the general linear model, group analysis, multiple comparison
correction and Fourier methods.

Each notebook has been trimmed to my own exercise solutions, keeping the minimal
setup code they depend on. `fMRI_Project.ipynb` is my own analysis rather than a
course exercise.

These notebooks are adaptations of [DartBrains](https://dartbrains.org/) by Luke
Chang, used under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). ShareAlike
requires adaptations to carry the same licence, so this directory is CC BY-SA
4.0 rather than MIT. Each notebook records the changes made.

The notebooks reference a course data path and will not run without it.

## `general_programming/`

Four self-contained projects from an introductory computer science course.
Entirely my own work, MIT licensed.

| Project | What it does |
|---|---|
| `nbody_simulation/` | Pairwise gravitational simulation with solar system and earth-moon scenarios |
| `city_sorting/` | Quicksort parameterised by a comparator function, sorting 47,913 world cities three ways, then plotting the largest on a world map |
| `campus_pathfinding/` | Graph loader, vertex class and breadth-first search behind an interactive click-to-route campus map |

`cs1lib.py` is the course teaching library, not my code. See `NOTICE`.

The city sorting pipeline runs from `cities_out.txt` onward. `city.py` parses the
original `world_cities.txt`, which I no longer have, so that first step cannot be
re-executed.

## Licences

- `fmri_signal_analysis/` is CC BY-SA 4.0, required by the licence on the
  original material
- `general_programming/` is MIT

There is deliberately no repository-wide licence, because a single one would
misstate the terms on one half.
