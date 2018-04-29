# Contents

- [Background](#background)

- [Defining Value](#value)

- [Goals](#goals)

- [Methods](#methods)

- [Results](#results)

- [Discussion](#discussion)


# Background <a name="background"></a>

## Approaches to Humanitarianism

Even within the set of prevalent humanitarian organizations, there's debate on how to effectively approach humanitarianism. Groups like Medecins Sans Frontieres (MSF) and the International Committee of the Red Cross (ICRC) place significant value on their principles of neutrality. Other groups hold fundamentally contrary beliefs that to make change humanitarian organizations need to act humanitarian-political organizations.

Fundamentally, all humanitarian groups lie under an umbrella of groups who intend to promote human welfare. The debate lies in how to categorize within that umbrella, with divisions created due to differences in belief of how to best embody the goal of promoting human welfare. 

Though the differences in values seem vast - how can groups on opposite ends of neutrality be promoting the same ideals? - small tweaks in our how we individually value things can result in extreme differences in approach.

These organizations will likely all agree that humanitarian work is good, and are trying to do as much as they can with the limited resources they have. In a world that collectively has finite resources (and allocates a very small portion of those resources towards humanitarian work) the goal should be to focus on work that does the most good possible with the resources available. 

## Cause-Prioritization

Many groups have devoted themselves entirely to the idea of optimizing humanitarianism. Research organizations, think tanks, and social movements like The Center for Effective Altruism, 80,000 Hours, Charity Science, the Future of Humanity Institute, and giveWell have done research on which humanitarian groups are most effective, what careers contribute the most to humanitarian goals, and what realms of humanitarianism would benefit the most from further work. 

This work exists under the term 'cause-prioritization' and is thought to be important due to its ability to uncover differences in how effective different causes are, therefore leading to much more effective long term humanitarian work. 

Within the large umbrella of humanitarianism an incredible diversity of approaches exist, from groups dedicated to creating art in war zones to groups distributing eye wear in the global south. This reflects the diversity in thought of how to best improve lives globally. Even within the group of cause-prioritization organizations, many different conclusions are reached on which approaches best execute humanitarianism. 

The reasons for differing opinion among cause prioritization organizations isn't often discussed. Given all groups tend to focus on quantifying three areas of each cause area (importance, tractability, and uncrowdedness) shouldn't they all reach the same conclusions?

## Quantifying Values

The most difficult problem in quantifying ideas that are distinctly human is incorporating, and explicitly defining, the tremendous amount of data that humans subconciously consider when thinking about abstract ideas. When we think about our values, we rely on past experience, set beliefs, things that we may not even conciously realize are important until pointed out. When quantifying value, there are unfathomable numbers of variables that *could* be included, and the concious choices researchers make on which ideas to include create an approximation of human value that may leave out crucial factors, and may not be appropriate for people with different sets of values. 

An example of a polarizing cause is artificial intelligence safety research. Currently ranked as The Center for Effective Altriusim's top cause area, as it is considered one of the more likely existential risks. Given the number of potential humans that could exist in the future far outnumbers the number people currently alive, and the belief that there is no "moral difference between .. a life today and one in a hundred years", even a very low probability of extinction would warrant putting significant funding towards this work, due to the magnitude of the potential effect. The conclusion, though sound, doesn't acknowledge that humans tend to value in the future under a significant discount rate, or that some may not put a strong inherent value on the long term survival of humanity, especially when comparing it to the suffering currently ongoing. 

To accurately measure value for individuals, a near infinite set of knobs defining how we value things relative to each other would need to be defined. Do we value a life today the same as a life in 100 years? Do we value reducing pain of a terminal patient equally to healing a patient who wasn't in pain? Does intervineing in disease through proventative care carry the same value as curing a patient who already has the disease? Is a human life worth the same amount as an animal's life?

In the context of contributing to humanitarian work, we have the goal of optimizing our donations by considering how to optimize improvement in the context of our  value 'knob' settings. Do we value focusing on a specific location? Do we focus on number of lives saved? Do we focus on dignity in aid?

But most of all, how do we find a way to quantify those differences? Once those differences are found how can we use that information to classify people's opinions in order to better find who to donate to?


# Defining Value <a name="value"></a>

## Past Methods and Contexts

## Clustering

# Goals <a name="goals"></a>

# Methods <a name="methods"></a>

## Data Scraping

In order to create a text corpus that best describes the motivations of NGOs in the global health and development realms, data was scraped from the GuideStar database, containing the self-reported mission statements for NGOs. 
Limited by the time it takes to scrape extensive data, as well as the scope of interest of this project, data was scraped for organizations that appeared under the search terms “international public health”, “global health”, or ‘“international development” and “health”’.

Consider scraping here if time runs out: “https://library.duke.edu/research/subject/guides/ngo_guide/ngo_database”

## Data Munging

The initial data corpus is sourced from a text file containing the names and missions of the organizations scraped, taking the following form:

|Name			|Mission							|
|-----------------------|---------------------------------------------------------------|
|Human Rights Education Institutions|Educational institutions that are concerned with human rights.|
|Agua Bolivia|An organization made up of private and public institutions that manage water consumption in Bolivia.|
|Preservador del Medi Ambiente|Founded in 1990, its purpose preserve and study the environment.|

In order to analyze this text data, it must be converted to a high-dimensional numeric dataset that acts as an abstraction of the text. To this end, a dataset is created where each row represents a text, and each dimension represents a word that exists in the corpus. For each word in the corpus, we find a value representing its commonality in each organization's text. After calculation the data takes the form shown below, where features X<sub>1</sub> through X<sub>n</sub> (n being the number of unique words in the corpus) each represent a word.

|Name|educational|institution|...|environment|
|----|--|--|---|--|
|Human Rights Education Institutions|1|1|...|0|
|Agua Bolivia|0|1|...|0|
|Preservador del Medi Ambiente|0|0|...|1|

Generating a numeric representation of the text is just a method of formalizing a human decision process, and different methods of conversion can inherently place value differently on the text corpus. One common choice is a binary classifier: assign 1 if the word appears in the text, and 0 otherwise. A slightly more useful choice is a count: how many times that word appears in the text. Both those measures leave out significant and useful information. 

As humans investigating a corpus we look at more complex relationships between texts than just the number of times a word appears. Mimicking that process is difficult, but a good representation of the relationship between texts and the words they contain is known as the term-frequency-inverse document frequency. Term frequency refers to the number of times a feature appears in a text. Inverse document frequency refers to the inverse of the number of texts within the corpora that the feature appears in. This measure, the tf-idf, gives us an idea of not just how frequently a feature appears in a text, but also weights it by how rarely it occurs in the corpus. 

The tf-idf helps against weighting useless information too highly. In a long text, words like ‘and’, ‘but’, or ‘if’ may appear many times, but by dividing the count of appearances by the number of texts the word appears in (likely most, if not all) we are able to reduce the value we place on the word.
 
The text processing pipeline begins with a complete corpus of texts, for example:

- A: “The fox went over this hill and another hill.”
- B: “The hill had lemon trees on it!”
- C: “Lemons grow on the trees over there.”

All non-alphanumeric features are removed, along with punctuation, pluralization and capitalization. Additionally, stop words are removed to reduce unnecessary dimensionality of the data. For large datasets, in order to further reduce dimensionality (implications of dimensionality are discussed later) words that appear in too few or too many documents are removed. After text cleaning, the corpus may look like this:

- A: “fox hill hill”
- B: “hill lemon tree”
- C: “lemon grow tree”

By applying the tf-idf method, the numeric abstraction of this data corpus would be:

|Text|fox|hill|lemon|tree|grow|
|----|---|----|-----|----|----|
|A   |1  |1   |0    |0   |0   |
|B   |0  |0.5 |0.5  |0.5 |0   |
|C   |0  |0   |0.5  |0.5 |1   |

## The Curse of Dimensionality

The ‘curse of dimensionality,’ first introduced by Richard Bellman, is the idea that high dimensional datasets are commonly faced with sparse data. This curse is based on the idea that as dimensionality increases, the volume of space increases so fast that the data needed to address a problem grows exponentially. In data with a high number of dimensions, detecting similarities in data can be difficult, as all observations seem distinct due to the vastness of space they are distributed across. This means that an incredible amount of data is needed to detect grouping in high dimensional data. 

For a simple example, let’s look at an example of a few data points in one and two dimensions. In a single dimension, the red line is a very clear divisor between two groups of points. 

![1 dimension](https://github.com/amd112/clusteringEthics/blob/master/images/1_dim.jpg?raw=true "One Dimensional Division")

Maintaining the same values on the first dimension, but adding data in a second, it’s less clear how these points are best divided. Without prior information on which points are truly grouped together, any of the red lines could be a good divisor. 

![2 dimensions](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim.jpg?raw=true "Two Dimensional Unclear Division")
 
By adding more data the number of dimensions, and therefore the increasing space, can be compensated for. With the new data there’s a clear separation between the two groups again. 

![2 dimensions full](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim_full.jpg?raw=true "Two Dimensional Clear Division")

As dimensions increase to the hundreds or thousands (as can happen with text data) methods of reducing dimensionality must be used. 

## Clustering Methodology

Using this numeric abstraction of the text corpus, we are able to think of each row as a vector existing in a high dimensional space that represents a specific text within the corpus. The question broached next is how to find

## Clustering Interpretation

# Results <a name="results"></a>

# Discussion <a name="discussion"></a>

## Limitations

The model used in this form text cleaning and parsing is called a 'bag-of-words' model. This treats any text as just the composition of the words it contains. This allows us to operate in the very simple framework of a collection of high-dimensional points, but doesn't address many of the complexities of language. 

Other frameworks for text analysis can involve sentiment analysis, structural analayis, concept mining, extraction and abstraction, etc. Collectively, these methods broach all the ways humans interpret data, but computationally they are each complex problems in their own right. Not using these other text analysis methods means that there are likely many similarities in the text that won't be recognized. Bag-of-words models don't recognize relationships in words across texts, meaning texts that commonly use 'Tanzania' and 'Nigeria' won't be registered as containing similarities, despite the fact that both words represent the concept of a country. Similarly, bag-of-words is unable to recognize structural similarities in writing, such as grouping texts that all use passive voice. 

Despite the drawbacks, bag-of-words models are extremely useful for their quick ability to turn text in to data that can be used for analysis. 

## Future Work
