# Exam scheduling

This repository includes implementation of several algorithms for scheduling exams at schools according to time and room capacity constraints.

## Problem description

There are $N$ exams, denoted by $1$, $2$, ..., $N$, which need to be scheduled. Each exam $i$ is to be sat by $d_i$ students.

$M$ exam rooms denoted by $1$, $2$, ..., $M$ can be used. Each room $i$ can accomodate at most $c_i$ students at a time.

Every exam must be held in exactly one exam period (or time slot), of which there are four on every exam day. In addition, two exams must not be held in the same room at the same time.

There are $K$ pairs of exams where the exams cannot be held in the same exam period because some students want to sit both of them.

Given these constraints, one needs to work out an exam plan allocating each exam to an exam period and exam room minimizing the number of exam days needed.

## Input format

Each problem instance is described by a text file formatted as follows:
* Line $1$: $N$
* Line $2$: $d_1$, $d_2$, ..., $d_N$ (separated by a space)
* Line $3$: $M$
* Line $4$: $c_1$, $c_2$, ..., $c_M$ (separated by a space)
* Line $5$: $K$
* Line $5 + k$ for $k \in \{1, 2, ..., K\}$: $i$ and $j$ separated by a space, indicating exams $i$ and $j$ cannot be held in the same exam period.

## Algorithms

* Integer linear programming (Google OR-Tools's Linear Solver)
* Constraint programming (Google OR-Tools's CP-SAT solver)
* Greedy algorithms

## Testing

A script for generating random problem instances and a test sample has been provided in this repository.

## Acknowledgements

This project was done as part of my Fundamentals of Optimization class at Hanoi University of Science and Technology from Dec 2021 to Jan 2022. The team members are Nguyễn Trung Hiếu, Hoàng Xuân Việt, Đỗ Tuấn Đức, and Nguyễn Phương Uyên. I appreciate their collaboration in completing the project.

I would like to express my gratitude to Dr. Phạm Quang Dũng, the instructor of my Fundamentals of Optimization class, for his valuable guidance on and evaluation of this project.
