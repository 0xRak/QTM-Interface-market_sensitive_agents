# Quantitative Token Model radCAD Integration

! This repository is a work in progress !

## Background

The [Quantitative Token Model (QTM)](https://outlierventures.io/quantitative-token-model-a-data-driven-approach-to-stay-ahead-of-the-game/) is an open source spreadsheet model developed by [Outlier Ventures](https://outlierventures.io/). It's purpose is to forecast key metrics of different token economies on a higher level by abstracting a set of often leveraged token utilities. It should be used for educational purposes only and not to derive any financial advise. The market making for the token is approximated by a DEX liquidity pool with [constant product relationship](https://balancer.fi/whitepaper.pdf).

## QTM Structure

![Quantitative Token Model](https://github.com/BlockBoy32/QTM-Interface/blob/main/images/Quantitative_Token_Model_Abstraction.jpeg?raw=true)

## Motivation for the radCAD Extension

The goal of the QTM radCAD integration is to extend and to improve the static high-level approach of the QTM spreadsheet model to a more flexible and dynamic one. With the radCad integration one should be able to perform parameter sweeps and optimizations. Furthermore it opens up the capabilities for more dynamic agent behaviors, Monte Carlo runs, and Markov decision trees, which reflect a more realistic approximation of a highly non-linear web3 token ecosystem. At a later stage there should also be a more accessible (web-based) UI.

## Development Roadmap

- Update the postprocessing in the `post_processing.py` with respect to the new streamlined adoption of the QTM parameters and conventions
- Update the plot functionallities in the `plots.py` with respect to the new parameter conventions
- Build the utility policies
- Build the trading policies (interactions with the liquidity pool)
- Build the user adoption policies
- Build the business policies
- Update the postprocessing w.r.t. the new implemented policies and corresponding state variables
- Add all remaining plot functionallities
- Web based UI for outputs
- Develop risk analysis procedures
- Test and improve the robustness of all functions -> unit tests
- Staging tests of the whole model
- Test parameter sweep capabilities
- Case studies & publishing first results in an article
- Add more dynamic agent (behavior) policies
- Add advanced optimization procedures
- Build a web-based UI to create another input option for users that don't want to use the initial spreadsheet model as input --> Increase accessibility

## Installation

Python 3.9 is recommended!

- Clone this repository to your local machine by `git clone https://github.com/BlockBoy32/QTM-Interface.git`
- Create a new Python environment in the projects directory by `python venv venv`
- Activate the new environment by `venv\scripts\activate`
- Install all required packages by `pip3 install -r requirements.txt`

## Usage

### Parameters

Most of the input parameters are contained in the `./data/Quantitative_Token_Model_V1.87 - cadCAD_inputs.csv` file. It can be generated by saving the `cadCAD_integration` tab of the [QTM spreadsheet model](https://drive.google.com/drive/folders/1mKZVGR5_qsrbP9mVkMddLrB791NPeOHP?usp=sharing) as `.csv` file and to replace it for the default parameter set `./data/Quantitative_Token_Model_V1.87 - cadCAD_inputs.csv`.

Note that at the current development stage some aspects are still hard coded, such as some agents behaviors. This will become more flexible in future versions.

### Simulation Settings

The prescribed simulation timestep is fixed to 1 month.
The user can adjust the length of the simulation by changing the `TIMESTEPS` parameter in the `./Model/simulation.py` file.

### Run Simulations

- Go with your terminal to the `./Model/` directory.
- Run `python simulation.py` within the environment.
