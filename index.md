# Contents

- [Motivation](#motivation)

- [What is Clustering?](#clustering)

- [Methods](#methods)

- [Results](#results)

- [Discussion](#discussion)


# Motivation <a name="motivation"></a>

ideas of how we differently value different things. 
there are many things we all agree are good, but in a world of limited resources we need to focus on the actions that do the most good
organizations entirely devoted to this idea - EA, 80k hours, center for effective action, charity science, giveDirectly, giveWell, etc
their conclusions aren't the same and the reasons aren't discussed (https://80000hours.org/problem-profiles/positively-shaping-artificial-intelligence/) 
80k prioritieses ai bcsz long term future, subconciously we all devalue future ppl. 
that needs to either be addressed or accounted for

So then as we make decisions about charity what do we do?
We need to consider the categorizations of the ethics of charity. 
do we focus on deworming? do we focus on a specific location? do we care about art and dignity?

What is a quantifiable way of finding those differences?
Once those differences are found how can we use that information to classify people's opinions?

# What is Clustering? <a name="clustering"></a>

# Methods <a name="methods"></a>

## Data Scraping

In order to create a text corpus that best describes the motivations of NGOs in the global health and development realms, data was scraped from the GuideStar database, containing the self-reported mission statements for NGOs. 
Limited by the time it takes to scrape extensive data, as well as the scope of interest of this project, data was scraped for organizations that appeared under the search terms “international public health”, “global health”, or ‘“international development” and “health”’.

Consider scraping here if time runs out: “https://library.duke.edu/research/subject/guides/ngo_guide/ngo_database”

## Data Munging

The initial data corpus is sourced from a text file containing the names and missions of the organizations scraped. In order to analyze this text data, it must be converted to a high-dimensional numeric dataset. 

In order to create an abstraction of the text, a dataset is created where each row represents a text, and each dimension represents a word that exists in the corpus. We calculate a value for each word for all organizations that is dependent on the word’s presence in that organization’s text. 

- insert picture of data here

This process is just a method of formalizing a human decision process, and different methods of conversion can inherently place value on different forms of differentiation within the text corpus. One common choice is a binary classifier: if that word appears in the text or not. A slightly more useful choice is a count: how many times that word appears in the text. Both those measures leave out significant and useful information. 

As humans investigating a corpus, we look at more complex relationships between texts than just the number of times a word appears. Mimicking that process is difficult, but the best representation of the relationship between words and their texts is known as the term-frequency-inverse document frequency. Term frequency refers to the number of times a feature appears in a text. Inverse document frequency refers to the inverse of the number of texts within the corpora that the feature appears in. This measure, the tf-idf, gives us an idea of not just how frequently a feature appears in a text, but also weights it by how rarely it occurs in the corpus. 

The tf-idf helps against weighting useless information too highly. In a long text, words like ‘and’, ‘but’, ‘if’ may appear many times, but by dividing that count by the number of texts the word appears in (likely most, if not all) we are able to reduce the value we place on the word.
 
The text processing pipeline involves beginning with a complete corpus of texts, for example:

- A: “The fox went over this hill and another hill.”
- B: “The hill had lemon trees on it!”
- C: “Lemons grow on the trees over there.”

All non-alphanumeric features are removed, along with punctuation, pluralization and capitalization. Additionally, stop words are removed to reduce unnecessary dimensionality of the data. For large datasets, in order to further reduce dimensionality (implications of dimensionality are discussed later) words that appear in too few documents are removed, which also prevents overfitting. After text cleaning, the corpus may look like this:

- A: “fox hill hill”
- B: “hill lemon tree”
- C: “lemon grow tree”

By applying the tf-idf method, we can generate what the numeric abstraction of this data corpus would be:

|Text|fox|hill|lemon|tree|grow|
|----|---|----|-----|----|----|
|A   |1  |1   |0    |0   |0   |
|B   |0  |0.5 |0.5  |0.5 |0   |
|C   |0  |0   |0.5  |0.5 |1   |

## The Curse of Dimensionality

The ‘curse of dimensionality,’ first introduced by Richard Bellman , is the idea that high dimensional datasets are commonly faced with sparse data. This curse is based on the idea that as dimensionality increases, the volume of space increases so fast that the data needed to address a problem grows exponentially with the number of dimensions. In data with a high number of dimensions, detecting similarities in data can be difficult, as all observations seem distinct due to the vastness of space they are distributed across.
For a simple example, let’s look at an example of a few data points in either one or two dimensions. In a single dimension, the red line is a very clear divisor between two groups of points. 

![1 dimension](https://github.com/amd112/clusteringEthics/blob/master/images/1_dim.jpg "One Dimensional Division")

Maintaining the same values on the first dimension, but adding data in a second, it’s less clear how these points are best divided. Without prior information on which points are truly grouped together, any of the red lines could be a good divisor. 

![2 dimensions](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim.jpg "Two Dimensional Unclear Division")
 
With more data, the number of dimensions can be compensated for. By adding data, there’s a clear separation between the two groups again. 

![2 dimensions full](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim_full.jpg "Two Dimensional Clear Division")

As dimensions increase to the hundreds, or thousands, as tends to be common with text data, if additional texts aren’t available to add to the corpus, to search for ways of reducing dimensionality. 

## Clustering Methodology

Using this numeric abstraction of the text corpus, we are able to think of each row as a vector existing in a high dimensional space that represents a specific text within the corpus. Different metrics can provide measures of how different each vector is from the rest. 

## Clustering Interpretation

# Results <a name="results"></a>

# Discussion <a name="discussion"></a>

## Limitations

The limitations of n-gram based identification vs word type identification. Ie I am not showing any relationship between the words (Tanzania and Namibia) or (hiv and malaria) despite the fact that the first are both countries, and the second are both illnesses.

## Future Work
