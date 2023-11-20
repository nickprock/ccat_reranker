# Cheshire Cat ReRanker
 
[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

Cheshire Cat ReRanker apply a rearrangement at each memory with different criteria:
* the [*episodic memory*](https://cheshire-cat-ai.github.io/docs/conceptual/memory/episodic_memory/) is reordered according to a temporal criteria, from the newest to the oldest.
* the [*declarative memory*](https://cheshire-cat-ai.github.io/docs/conceptual/memory/declarative_memory/) is reordered according the [**lost in the middle** paper](https://arxiv.org/abs/2307.03172) method
* the [*procedural memory*](https://cheshire-cat-ai.github.io/docs/conceptual/memory/procedural_memory/) isn't reordered but filtered using a threshold, the default value is 0.5 but you can set it.

The ReRanker can be enabled and disabled for each memory independently using the "Settings".

## Installation

1. Navigate to the `Plugins` page;
2. Scroll until you find the "Cheshire Cat ReRanker" plugin;
3. Click on `Install

## Usage

1. Navigate to the `Plugins` page;
2. Scroll until you find the "Cheshire Cat ReRanker" plugin;
3. Click on the "Settings" icon on the bottom right of the plugin card;
4. Edit the available settings and save.

> **Important**

> ReRankers (in particular Lost In The Middle) are very useful if you get at least more than 10 documents returned from the memories.
> Before using it download and enable the [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools) from the Plugins store, [follow the instructions](https://github.com/Furrmidable-Crew/cat_advanced_tools#usage) to increase the k parameter of the memories.