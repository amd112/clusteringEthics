# Motivation

# What is Clustering?

# Methods

## Data Scraping

In order to create a text corpus that best describes the motivations of NGOs in the global health and development realms, data was scraped from the GuideStar database, containing the self-reported mission statements for NGOs. 
Limited by the time it takes to scrape extensive data, as well as the scope of interest of this project, data was scraped for organizations that appeared under the search terms “international public health”, “global health”, or ‘“international development” and “health”’.

Consider scraping here if time runs out: “https://library.duke.edu/research/subject/guides/ngo_guide/ngo_database”

## Data Munging

The initial data corpus is sourced from a text file containing the names and missions of the organizations scraped. In order to analyze this text data, it must be converted to a high-dimensional numeric dataset. 

For this abstraction of the text, each dimension  represents a word that exists in the corpus, and each organization is assigned a value for that dimension depending on the word’s presence in that organization’s text. Choosing the method of conversion can inherently place value on different features in the text corpus. One common choice is a binary classifier: if that word appears in the text or not. A slightly more useful choice is a count: how many times that word appears in the text. Both those measures leave out significant and useful information. 

As humans investigating a text corpus, we look at more complex relationships between texts, and in computing the best representation of those relationships is known as the term-frequency-inverse document frequency. Term frequency refers to the number of times a feature appears in a text. Inverse document frequency refers to the inverse of the number of texts within the corpora that the feature appears in. This measure, the tf-idf, gives us an idea of not just how frequently a feature appears in a text, but also how rarely it occurs in the corpus. 

The tf-idf helps against weighting useless information too highly. In a long text, words like ‘and’, ‘but’, ‘if’ may appear many times, but by weighting by the number of texts they appear in (likely most, if not all) we areable to scale their weight. 
The text processing pipeline involves beginning with a complete corpus of texts:

- A: “The fox went over this hill and another hill.”
- B: “The hill had lemon trees on it!”
- C: “Lemons grow on the trees over there.”

All non-alphanumeric features are removed, along with punctuation, pluralization and capitalization. Additionally, stop words  are removed to reduce unnecessary dimensionality of the data. For large datasets, in order to further reduce dimensionality (implications of dimensionality are discussed later) words that appear in too few documents are removed, which also prevents overfitting. After text cleaning, the corpus may look like this:

- A: “fox hill hill”
- B: “hill lemon tree”
- C: “lemon grow tree”

By applying the tf-idf method, we can generate what the numeric abstraction of this data corpus would be:

|Text|fox|	hill|	lemon|	tree|	grow|
|----|---|---|---|---|---|
|A|1|1|0|0|0|
|B|0|0.5|0.5|0.5|0|
|C|0|0|0.5|0.5|1|


## The Curse of Dimensionality

The ‘curse of dimensionality,’ first introduced by Richard Bellman , is the idea that high dimensional datasets are commonly faced with sparse data. This curse is based on the idea that as dimensionality increases, the volume of space increases so fast that the data needed to address a problem grows exponentially with the number of dimensions. In data with a high number of dimensions, detecting similarities in data can be difficult, as all observations seem distinct due to the vastness of space they are distributed across.
For a simple example, let’s look at an example of a few data points in either one or two dimensions. In a single dimension, the red line is a very clear divisor between two groups of points. 
  
- insert picture here
  
Maintaining the same values on the first dimension, but adding data in a second, it’s less clear how these points are best divided. Without prior information on which points are truly grouped together, any of the red lines could be a good divisor. 
 
With more data, the number of dimensions can be compensated for. By adding data, there’s a clear separation between the two groups again. 

- insert picture here

As dimensions increase to the hundreds, or thousands, as tends to be common with text data, if additional texts aren’t available to add to the corpus, to search for ways of reducing dimensionality. 


## Clustering Methodology

Using this numeric abstraction of the text corpus, we are able to think of each row as a vector existing in a high dimensional space that represents a specific text within the corpus. Different metrics can provide measures of how different each vector is from the rest. 

## Clustering Interpretation

# Results

# Discussion

The limitations of n-gram based identification vs word type identification. Ie I am not showing any relationship between the words (Tanzania and Namibia) or (hiv and malaria) despite the fact that the first are both countries, and the second are both illnesses.
