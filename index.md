# Contents

- [Background](#background)

- [Goals](#goals)

- [Methods](#methods)

- [Results](#results)

- [Discussion](#discussion)


# Background <a name="background"></a>

## Approaches to Humanitarianism

Within the set of prevalent humanitarian organizations there's debate on how to effectively approach humanitarianism. Groups like Medecins Sans Frontieres (MSF) and the International Committee of the Red Cross (ICRC) place significant value on principles of neutrality. Other groups hold the fundamentally contrary belief that change can best be made through political action.

Humanitarianism fundamentally aims to promote human welfare. The debate lies primarily in how to best achieve that goal. Though differences in values seem vast small tweaks in our how we individually value things can result in extreme differences in approach. In many ways  groups on opposite ends of neutrality hold many of the same ideals.

These organizations will likely all agree that humanitarian work is good, and are trying to do as much as they can with the limited resources they have. In a world that has finite resources and allocates a very small portion of those resources towards humanitarian work the goal is to do the most good possible with the fewest resources. 

## Cause-Prioritization

In order to use resources more effectively many groups have devoted themselves to the idea of optimizing humanitarianism. Research organizations, think tanks, and social movements like The Center for Effective Altruism, 80,000 Hours, Charity Science, The Future of Humanity Institute, and giveWell have done research on which humanitarian groups are most effective, what careers contribute the most to humanitarian goals, and what realms of humanitarianism would benefit the most from further work. 

These groups hope that 'cause-prioritization' research will help lead to more effective long term humanitarian work. 

Within the umbrella of humanitarianism an incredible diversity of approaches exist, from groups dedicated to creating art in war zones to groups distributing eye wear in the global south. This reflects the diversity in thought of how to best improve lives globally. Unfortunately, the conclusions of cause-prioritization research is as varied as the organization they investigate. 

The reasons for differing opinion among cause prioritization organizations isn't often discussed. Given all groups tend to focus on quantifying three areas of each cause area (importance, tractability, and uncrowdedness) shouldn't they all reach the same conclusions?

## Quantifying Values

The most difficult problem in quantifying distinctly human ideas is explicitly defining the tremendous amount of data that humans subconsciously consider when thinking about abstract ideas. When we think about our values, we rely on past experience, set beliefs, and may not even consciously realize it. When quantifying any abstract value, there are unfathomable numbers of variables that *could* be included. The conscious choices researchers make on which values to include in their analysis creates an approximation of human value based on their beliefs. The choices they make may not be appropriate for people with different sets of values. 

To create a measure of how much value an idea holds for a given individual, a near infinite set of knobs defining how we personally value things relative to each other would need to be defined and tweaked. For any given issue many small definitions of value are involved, as well as the relationships those value systems have. Do we value a life today the same as a life in 100 years? Do we value reducing pain of a terminal patient equally to healing a patient who wasn't in pain? Does intervening in disease through preventative care carry the same value as curing a patient who already has the disease? Is a human life worth the same amount as an animal's life? It is questions like this, and the relative value we place on different aspects of human life that lead to the large differences in humanitarian approaches, the best example being the deeply felt convictions on both sides of the neutrality debate. 

Given the ability to estimate the value of a given outcome, the value of a given action is a function of the value of the potential outcomes, as weighted by the probability of them occurring. Expected value is a simple measure, despite the complexities of calculating its inputs. 

Nonetheless, expected value is the measure used by most cause-prioritization groups to investigate cause importance and the potential for improvement in a cause area. Despite the validity of the measure, it is entirely dependent on what is chosen for inputs. 

The Center for Effective Altruism recently ranked artificial intelligence safety research as a top cause area. Artificial intelligence was ranked as one of the most likely existential risks. Given that the number of potential humans that could exist in the future far outnumbers the number people currently alive, along with the premise that there is no "moral difference between .. a life today and one in a hundred years", the magnitude of the moral implications is enormous. Even with a minuscule probability of extinction, enormity of the implications warrant putting significant funding towards this are. 

Though these conclusions are logical, they are dependent on the value system placing equal moral importance on life today and the far future. Humans tend to value future rewards at a high discount rate, and some may not even put stock in the inherent value of long term survival of humanity. Either of these differences in value would significantly alter the conclusion, despite the consistency and validity of their methods. 

In the context of humanitarian work, we have the goal of optimizing work in the context of our value 'knob' settings. Do we value focusing on a specific location? Do we focus on number of lives saved? Do we focus on dignity in aid? But most of all, how do we find a way to quantify those differences? What can those differences reveal to us about the way groups differentiate themselves?

## Dangers of Dependence on Quantifications

In the expanding space of big data, it's becoming increasingly attractive to generate auto-quantifying practices that streamline decision making and the need for human value judgments. These tools are extremely useful, both for the time they can save and the theoretical benefit of an even playing field where models treat all data the same. 

The danger in using data to make judgments lies in how we are able to interpret and contextualize data. Fundamentally all computational predictive and explanatory models, from a simple linear regression to complex black box machine learning models, are trained to mimic the data they are fed with. Models find patterns in the data they've been given, but also only look for patterns in the data in the specific form they've been asked to find. These dangers have already played out in the real world with models reinforcing selective policing, recommending inequitable jail time, and inaccurately identifying minority faces. These models are not inherently biased - they've been trained to follow the biases that currently play out in society. Models can be tools for equity, or the justification and formalization of human bias.  

In the words of statistician George Box, "all models are wrong, but some are useful." Care needs to be taken in interpreting the blind spots and useful aspects of all models. 

# Goals <a name="goals"></a>

Clustering and classification, sometimes called unsupervised and supervised classification, are modeling methods that specifically aim to find divisions in data. Classification is generally focused on modeling the relationships between traits and a known classification scheme. This form of model is predicated on a knowledge of what class past data falls in to, and uses other factors to try to predict what class future data will fall in to. Predicting recidivism is a common classification problem, and past models have been shown to be inequitable in how they classify probability of recidivism for different race groups. 

Clustering is a similar problem, but is based on data that has no data on which class each data point falls in to. Clustering problems are more focused on building hyperplanes that divide high dimensional spaces in to discrete spaces in which data naturally groups. These hyperplanes don't necessarily have an obvious meaning, but the clusters built can be informative specifically in understanding how the clusters have been chosen. 

The goal of this project is to scrape and cluster data on the mission statements of NGOs. The language used by NGOs in their mission statements, and even the communication intent of mission statements, is not uniform, so this classification cannot be directly framed as a classification of the values of NGOs. 

However, clustering the missions of NGOs may give insight in to the language used in different fields of humanitarianism. Additionally, that language may give insight to the specific goals and intents of organizations. 

Ideally, this classification would divide organizations by their values, revealing the small but deep seated differences in how these groups approach humanitarianism. Given the high dimensional and noisy nature of the data, this is an incredibly unrealistic goal. Nonetheless, this acts as a proof of concept of the possibility of quantifying value choices and invites use of more consistent data that would provide a better analysis.

# Methods <a name="methods"></a>

## Data Scraping

In order to create a text corpus that best describes the motivations of NGOs in the global health and development realms, data was scraped containing the self-reported mission statements for NGOs. 

To create a defined corpus, missions were scraped for NGOs holding General Consultative Status with the United Nations Economic and Social Council, as well as for NGOs mentioned on the pages of those holding General Consultative Status. 

Scraping was done through Wikipedia. By first collecting the organization names from the UNESC website, it was possible to automatically paginate through the respective pages on Wikipedia. In order to approximate similar categories of statements for each group, only sections titled 'Purpose', 'Mission', 'Founding', 'Principles', or 'Philosophy' were scraped. Section titles were fuzzy matched, meaning that sections could be identified that had similar but not exact titles. The fuzzy matching algorithm used prioritizes sequence of lettering, and secondarily the set and number of letters. This means that 'Mission Statement', a phrase adding text at the end, would likely be considered a close match for 'Mission', while '**Miss**ing Opin**ion**', a phrase adding text in the middle, and 'I miss gin', an anagram, would be considered poor matches. 

## Data Munging

The initial data corpus is sourced from a text file containing the names and missions of the organizations scraped, taking the following form:

|Name			|Mission							|
|-----------------------|---------------------------------------------------------------|
|Human Rights Education Institutions|Educational institutions that are concerned with human rights.|
|Agua Bolivia|An organization made up of private and public institutions that manage water consumption in Bolivia.|
|Preservador del Medi Ambiente|Founded in 1990, its purpose preserve and study the environment.|

In order to analyze this text data, it must be converted to a high-dimensional numeric dataset that acts as an abstraction of the text. To this end, a dataset is created where each row represents a text, and each dimension represents a word that exists in the corpus. For each word in the corpus, we assign a value representing its commonality in each organization's text. After calculation the data takes the form shown below, where features X<sub>1</sub> through X<sub>n</sub> (n being the number of unique words in the full corpus) each represent a word.

|Name|educational|institution|...|environment|
|----|--|--|---|--|
|Human Rights Education Institutions|1|1|...|0|
|Agua Bolivia|0|1|...|0|
|Preservador del Medi Ambiente|0|0|...|1|

Generating a numeric representation of the text is a step towards formalizing a human decision process, and different methods of conversion place value differently on traits of the text corpus. One common choice is a binary classifier: assign 1 if the word appears in the text, and 0 otherwise. A slightly more useful choice is a count: how many times that word appears in the text. Both those measures leave out significant and useful information. 

As humans investigating a corpus we look at more complex relationships between texts than just the number of times a word appears. Mimicking that process is difficult, but a good representation of the relationship between texts and the words they contain is known as the term frequency-inverse document frequency. Term frequency refers to the number of times a feature appears in a text. Inverse document frequency refers to the inverse of the number of texts within the corpora that the feature appears in. This measure, the tf-idf, gives us an idea of not just how frequently a feature appears in a text, but also deflates the value if the word occurs in many or most texts. 

The tf-idf helps against weighting useless information too highly. For a corpus centered around a specific idea, eg. humanitarianism, words related to the main concept may appear many times without providing information specific to the text. Dividing the count of appearances of the word by the number of texts the word appears in (likely most, if not all) we are able to reduce the value we place on the word.
 
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

The ‘curse of dimensionality,’ first introduced by Richard Bellman, is the idea that high dimensional datasets are commonly faced with the problem of sparse data. As dimensionality increases, the volume of space increases so fast that the data needed to find patterns grows exponentially. In data with a high number of dimensions detecting similarities in data can be difficult, as all observations seem distinct due to the vastness of space they are distributed across. This means that an incredible amount of data is needed to detect grouping in high dimensional data. 

For a simple example, let’s look at a few data points in one and two dimensions. In a single dimension, the red line is a very clear divisor between two groups of points. 

![1 dimension](https://github.com/amd112/clusteringEthics/blob/master/images/1_dim.jpg?raw=true "One Dimensional Division")

Maintaining the same values on the first dimension, but adding data in a second, it’s less clear how these points are best divided. Without prior information on which points are truly grouped together, any of the red lines could be a good divisor. 

![2 dimensions](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim.jpg?raw=true "Two Dimensional Unclear Division")
 
By adding more data the number of dimensions can be compensated for. With the new data there’s a clear separation between the two groups again. 

![2 dimensions full](https://github.com/amd112/clusteringEthics/blob/master/images/2_dim_full.jpg?raw=true "Two Dimensional Clear Division")

As dimensions increase to the hundreds or thousands (as can happen with text data) methods of reducing dimensionality must be used. 

## Clustering Methodology

Using this numeric abstraction of the text corpus, we are able to think of each row as a vector existing in a high dimensional space that represents a specific text within the corpus. So how does clustering find different groupings of data? 'Bag-of-words' models treat any text corpus as just the composition of words it contains - regardless of order or meaning. There are many methods to do clustering, even within the space of 'bag-of-words' models. 

Here I will focus on the method implemented here: Hierarchical clustering using Ward's minimum variance method. All hierarchical clustering methods used in this context follow a similar algorithm, outlined below. 

For a cluster *i*, containing *n<sub>i</sub>* objects, let the distance to cluster *j*, where *i* and *j* are arbitrary, be *d<sub>ij</sub>*. *D* represents the set of distances between all *ij* pairs, and *N* the number of objects to cluster. 

The basic algorithm for hierarchical clustering is:

1. Start with *N* clusters, one for each initial observation.

2. Find *d<sub>ij</sub>* for all *ij* combos of clusters, computing the set *D*.

3. Merge the clusters *i* and *j* that have the smallest *d<sub>ij</sub>* in *D*. The merged cluster will be called cluster *k*.

4. Recalculate the values in *D* that reference the recently merged cluster *i* and *j*. Calculate each new distance (*d<sub>kl</sub>*) through a weighted sum of *d<sub>il</sub>*, *d<sub>jl</sub>*, *d<sub>ij</sub>* and (*d<sub>il</sub>* - *d<sub>jl</sub>*).

5. Repeat steps 3 and 4 until *N* = 1, meaning that only one cluster is left, and there is nothing remaining to merge.

Ward's minimum variance method defines the distance function between two points (or clusters) as the pooled within-group sum of squares. This means that at each merge, the clusters chosen to merge are those that create the smallest jump in the pooled within-group sum of squares. 

## Salient Features

In text analysis, salient features refers to the words (aka tokens or features) that are most distinctive to a text. Using data on how common a word is across the corpus, we calculate the tf-idf value for each word in the corpus for a given text. This value gives us an idea of how prevalent the word is in a given text as compared to texts in the corpus as a whole. 

Features with high tf-idf values are those that are common in a text or most distinctively part of that text. These salient features can give us an idea of what's unique about a text. In this case, salient features are used to give an idea of what is distinctive about a group of organizations. 

To find the salient features of a group, all texts that are categorized in that group are combined to be treated as one text. Then, the texts of each group are combined to create a new corpus, and salient features are found for each group. 


# Results <a name="results"></a>

Below is the dendogram generated through clustering. As discussed in methods, the dendogram is generated bottom up, starting with each organization as its own cluster and merging the clusters that increase the pooled within-group sum of squares least. On the x-axis we see each of the organizations. On the y-axis is the cumulative within-group sum of squares. The level at which two clusters merge represents the increase in within-group sum of squares at that merge. This visual representation of the clustering process is similar to an evolutionary tree, with higher level merges representing more 'evolutionary' distinct groups. 

Switching the framework to a top down approach, initially all organizations are in one large cluster. At each of the splits salient words are annotated at each of the splits. These salient words don't represent the decision factors used by the model, or what is the ultimate unique identifier for a group. Rather, the salient words indicate at each split which words are the most distinctly relevant to each of the groups in the split. These words can give us an idea of what the split represents.

![dendogram](https://github.com/amd112/clusteringEthics/blob/master/images/labeled_clusters_un.png?raw=true "Ward Dendogram")



For a larger view of the dendogram, with text on salient characteristics and organization names, click [here](https://github.com/amd112/clusteringEthics/blob/master/images/labeled_clusters_un.png?raw=true).




# Discussion <a name="discussion"></a>

## Findings

The clustering method used resulted in 7 groups of organizations. A subset of organizations in each cluster is shown below. The descriptors in the first column are approximated guesses at what the commonalities between organizations the clustering algorithm is finding. 

|Potential Group|Organizations|Identifiers|
|---------|-------------|-----------|
|1 - Human Rights and Liberties|Defense for Children International, Arab Association for Human Rights, Minority Rights Group, Human Rights in China, Human Rights Advocates, Inc, Equality Now, Archaeologists for Human Rights, Refugee Law Project, People's Union for Civil Liberties, Doctors of the World|worldwide, services, promoting, society, institutions, developing|
|2 - Social Justice and Accountability|MacArthur Foundation, Womankind Worldwide, International Council of Women, Social Justice Committee, Anti-Slavery International, Rights and Accountability in Development, First Nations Development Institute, Church World Service, Centre for Democracy and Development|worldwide, services, promotions, civil, discrimination, principles|
|3 - Equity and Health|We the Peoples Initiative, Partner's In Health, Operation Smile, International Federation of Fertility Societies, Hunger Project, Greenpeace, Environmental Defense, Earth Society Foundation, American Civil Liberties Union, European Public Law Center|experience, equity, programmes, people, health|
|4 - Research/Computation for Policy|Human Sciences Research Council, Global Vision, Institute of Development Studies, International Development Research Centre, International Statistical Institute, Centre for Science and Environment, Development Group for Alternative Policies|experience, equity, sector, scientific, policy, development|
|5 - Resource Provision/Health|Canadian Research Institute for the Advancement of Women, Asia Crime Prevention Foundation, Indigenous Environmental Network, Population Services International, International Institute for Sustainable Development, Stop Hunger Now, Solar Cookers, ICRC, Family Health International, Doctors Without Borders, AmeriCares, Peace Corps, Americorps, CARE International|experience, equity, sector, scientific, awareness, resources, families|
|6 - International Network Building|International Community of Women Living with HIV/Aids, Social Watch, Relief International, CropLife International, Green Cross International, Salvation Army, ReliefWeb, International Immigrants Foundation, HelpAge International, Gifts in Kind International, Center for International Policy, International Social Service|experience, equity, sector, scientific, awareness, worldwide, network, information|
|7 - Awareness and Public Involvement|United States Fund for UNICEF, Global Health Council, Mercy Corps, Oxfam, Citizens for Global Solutions, Lutheran World Service, Medecins Sans Frontieres (MSF), War Child, Association for the Prevention of Torture, Save the Children, Refugees International|experience, equity, sector, scientific, awareness, ensure, united|

A case study in how the classifier is operating in the case of Medecins Sans Frontieres and Doctors Without Borders. Scraping was automated, so pages aren't manually inspected and overlap like this is not unusual. These two data points refer to the same group, yet they've been grouped separately, so let's take a glimpse at how the two descriptions compare, and how they fit in to their larger groups. 

Medecins Sans Frontieres scraped mission:
> Medecins Sans Frontieres (MSF) is an international humanitarian aid organisation that provides emergency medical assistance to populations in danger in more than 70 countries. MSF works in rehabilitation of hospitals and dispensaries, vaccination programmes and water and sanitation projects. MSF also works in remote health care centres, slum areas and provides training of local personnel.

Doctors Without Borders scraped mission: 
> Doctors Without Borders/Médecins Sans Frontières (MSF) is an independent international medical humanitarian organization that delivers emergency aid to people affected by armed conflict, epidemics, natural or man-made disasters, or exclusion from health care in more than 70 countries.

The tokens in the description for Medecins Sans Frontiers but not in the description for Doctors Without Borders are: 
> training, sanitation, dispensaries, assistance, slum, local, water, rehabilitation, vaccination, danger, hospitals, populations. 

These tokens line up fairly well with the salient tokens of the group MSF has been allocated to. The cluster has a much higher prevalence of the words training, local, and rehabilitation, and contains many similar words, like national, education and improve. 

The tokens in the description for Doctors Without Borders but not in the description for Medecins Sans Frontiers are: 
> epidemics, exclusion, man-made, independent, conflict, disasters, natural, people, armed, doctors. 

The cluster has a high prevalence of the words independent, conflict, disaster, and armed, as well as similar words like emergency, alarm, and associated.

Despite the differences between the two texts, they share many similarities, both featuring the words 'care', 'health', 'aid', 'medical', 'humanitarian', 'international', and 'emergency'. This is a good example of the strengths and limitations of this process. The similarities of their text places them relatively close to each other on the evolutionary tree, but their phrasing actually separated them significantly. Looking only at the words contained and their prevalence, this seems like a reasonable allocation. Even on first glance, the MSF description appears more focused on the types of work they do, indicating value placed specifically on "remote health care centers" and "slum areas." Comparatively the DWB description is more focused on on what causes the need for emergency aid, focusing on "armed conflict, epidemics, and ... disasters". This may be an indication of different approaches in the American and Swiss approaches to the group or the intent of the unknown author of the article. 

With that context, let's look at the salient features at each division of a cluster. These features represent the words that are most distinctive to the new split clusters. The first cluster split has the groups represented by "worldwide, services, promoting" and "experience, equity, programmes". The first group features words that focus more on the corporate aspect of humanitarianism, while the second group features words that focus more on the ideals of humanitarianism. 

Other splits seem to mimic this trend, with a split between "people, mission, health" and "sector, scientific", again showing a difference between goals and methods. Splits further down the tree tend to focus on differences in method, "policy, development" versus "awareness" or the field that the group focuses on "community, people" versus "medical, programs". Within the group defined by "civil, discrimination, principles" we see a split between groups that focus on "partners, members", work by the people affected, or "assistance, alliance", work on capacity building to help those affected. 

The splits that are found by this clustering method are discovering differences in the language used to describe the goals of organizations more than they are discovering the ethical choices of those organizations. Nonetheless, differences in language surrounding ethical values are important distinctions, and illuminate how groups focus on different aspects of humanitarianism, but also different aspects of their work. 

Unexpectedly, the first split of clusters reduces the within group sum of squares by over 30%, and that split appears to be separating predominantly by whether the language is describing the actions ("services, promote") or the goals ("experience, equity") of the organization. The large drop in within group sum of squares from that one split indicates that this is a broad and common distinction between the texts of these organizations.

These distinctions may not shed light on the intricate ethical work involved in making decisions on the most important aspects of humanitarianism, but they do give information on how groups choose to frame the work they do. It seems that the how organizations frame their work doesn't appear to be related to success, with famous groups like MSF, the ICRC, and Partners in Health all categorized separately. 

Despite the inability of the model to discover delicate separations in the way humanitarian organizations operate and build value systems, this form of classifications bring up interesting questions in the way that we choose to talk about our work. Regardless of the actual field of work, we see a glimmer of the drivers of each organization through their classification. Despite being a medical organization, Doctors of the World is classified in the 'Human Rights and Liberties' group due to their belief that access to health care is a right, and their mission to address 'violations of human rights and civil liberties'. Despite being a religious organization, the Church World Service falls in the 'Social Justice and Accountability' group due to their focus on 'self-reliance', 'human needs', 'partnership', and 
'fairness'. 

With data from a more consistent source and more data on each organization it may be possible to expand on this model to create more precise comparisons of these groups and others. There is potential for these 

## Limitations

The model used here is called a 'bag-of-words' model, treating text as just the composition of the words it contains. This allows us to operate in the very simple framework of a collection of high-dimensional points, but doesn't address many of the complexities of language. 

Other frameworks for text analysis can involve sentiment analysis, structural analysis, concept mining, extraction and abstraction, etc. Collectively, these methods broach all the ways humans interpret data, but computationally they are each complex problems in their own right. Not using these other text analysis methods means that there are likely many similarities in the text that won't be recognized. Bag-of-words models don't recognize relationships in words across texts, meaning texts that commonly use 'Tanzania' and 'Nigeria' won't be registered as similar, despite the fact that both words represent a country. Similarly, bag-of-words models are unable to recognize structural similarities in writing like passive or active voice. 

Despite the drawbacks, bag-of-words models are extremely useful for their quick ability to turn text in to data that can be used for analysis. 

The data used in this analysis is inconsistent in many ways. As data comes from Wikipedia, each mission statement is placed within the page differently, and the surrounding text is written by different people. Even for organizations who have similar goals and similar approaches, the text style is equally dependent on the viewpoint of the open source author. This results in a corpus with extreme variation in length, scope, style, and phrasing. Ideally, the data would be uniform across groups. This data could be obtained through a survey, with a representative filling out answers to a specific set of questions in an allotted space. Even just mission statements themselves, without the inconsistencies created by scraping through Wikipedia, would be a significant improvement. 

A different set of organizations may also reveal more useful, or at least different, insights. The list of organizations holding General Consultative status with UNESC is very varied. It might reveal very different things to focus on a more specific group of organizations, like emergency aid groups, long term focused health groups, dignity focused groups, etc. More focused analysis would likely reveal more about specifics of methods, rather than how organizations frame their goals.