# slamresearch: A Comparative Study on Slam Algorithms

## Introduction

### What is this repository?

This repository provides a comparative study on various SLAM algorithms in terms of performance and accuracy.

### System

All the algorithms are tested under Ubuntu 18.04 LTS. Computer specifications are:

Graphics: GTX860M

Processor: Intel Core i7 4700HQ

Storage: Toshiba 1TB 5400 RPM HDD

### Algorithms

Algorithms used for this research are currently:

ORB_SLAM2: https://github.com/raulmur/ORB_SLAM2

ORB_SLAM3: https://github.com/UZ-SLAMLab/ORB_SLAM3

DSO: https://github.com/JakobEngel/dso

LDSO: https://github.com/tum-vision/LDSO

OKVIS: https://github.com/ethz-asl/okvis

BASALT: https://github.com/VladyslavUsenko/basalt-mirror

## Folders

### scripts

This folder consists of scripts that are used to refine the output files created from the algorithms, since not all algorithms provide an output that would work on evaluation tool.

### output

This folder consists of all the output data created from algorithms. 

### graphs

This folder consists of drawn graphs of the outputs, relative to the ground truth.
