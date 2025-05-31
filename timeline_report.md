# Mechanistic Interpretability Discord Server Timeline

**Analysis Period:** 2023-03-04 to 2025-05-31
**Total Significant Events:** 539

## Event Categories Summary

- **Other**: 11 events
- **Papers & Research**: 229 events
- **Projects**: 17 events
- **Technical Discussions**: 107 events
- **Research Findings**: 107 events
- **General Discussions**: 67 events
- **Announcements**: 1 events

## Chronological Timeline

### 2023-03-04

**07:10:09 UTC** - #general-resources - **firstuserhere**
"A Comprehensive Mechanistic Interpretability Explainer & Glossary" : https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J

I found it to be a useful introduction + the intuitions are also interesting ways to think about common concepts.

https://readingwhatwecan.com/ - a more general list but still quite broad and useful

### 2023-03-05

**18:30:14 UTC** - #general-resources - **fieryvictorystar**
https://www.youtube.com/@neelnanda2469/videos
Neel Nanda's youtube channel is also a great place for videos explaining the field.
Also see https://www.neelnanda.io/mechanistic-interpretability/quickstart  for a good quick guide of how to get started on the field Or https://www.neelnanda.io/mechanistic-interpretability/getting-started for a more detailed version.

### 2023-03-08

**16:37:08 UTC** - #about - **firstuserhere**
Please visit https://mechinterp.com/reading-group to see details of the past papers read and upcoming to-read papers.

**17:03:11 UTC** - #general-resources - **alexioli** (1 reactions)
Yep I quite like it. My question was more about the general preference of 1) list of notebooks on github vs) proper markdown docs underlying a wiki (if this was preferred then gitbooks is a good option though!)

### 2023-03-11

**20:17:00 UTC** - #about - **fieryvictorystar**
# Rules
- No advertising or spam.
- Be respectful to other members
- And in general follow the Discord Community Guidelines.
- If you want to link an invite to another discord server ask the admins since otherwise our bot detection might ban you.(note automod might randomly delete your messages for some other reasons, if you think its making a mistake contact admins)
- More rules will be added as needed

### 2023-03-12

**18:24:07 UTC** - #general-resources - **fieryvictorystar** (1 reactions)
https://alignmentjam.com/interpretability

**18:25:01 UTC** - #general-resources - **fieryvictorystar**
<@119559264153894914> <@1060971001002872843> this is the apart research thing I mentioned.

### 2023-03-13

**21:03:25 UTC** - #project-proposals - **loganriggs** (1 reactions)
- I'm working towards automating feature interpretability of language models. As a toy example, we find the max-activating datapoints that activate layer 6, neuron 0, and it looks like it's about cars. We can create data examples of specific cars and non-cars to further refine the hypothesis. Say it ends up only activating on older cars, we can refine the hypothesis and repeat. A language model can come up with hypotheses & verifying examples as well. 

In practice, coming up with a hypothesis a...

**21:03:28 UTC** - #project-proposals - **loganriggs** (2 reactions)
- Partial success here means we discover classes of features, such as features that are invariant to distance between tokens (eg skip-grams might be invariant to distance. For example, if I've already seen " (1)", then if I see "(", output "2" even if there's lots of tokens in between), with automated tests we can make to test them out (e.g. adding buffer tokens). Additionally, we can use these techniques to determine circuits we do actually care about, such as truthfulness, deception, and speci...

**23:35:01 UTC** - #project-proposals - **fieryvictorystar** (1 reactions)
Sounds good, made a channel for it called "automating feature interpretability"(tell me if you want to change  the name).

### 2023-03-14

**00:12:36 UTC** - #project-proposals - **fieryvictorystar** (1 reactions)
Maybe I should add a "research lead" role for people who propose and manage a project so they are more easily identifiable.

### 2023-03-29

**02:31:20 UTC** - #paper-discussion - **joyeechen**
I'm doing an AI safety project (something about causal-scrubbing and abstractions theory) for which I want to find a fairly concrete, well-defined environment so that I can build up a good intuition (and hopefully with enough codebase for me to test it quickly) for my theories. Besides the AI Safety Gridworlds (https://arxiv.org/abs/1711.09883v2), are there any other good premade environments?

**03:36:44 UTC** - #paper-discussion - **fieryvictorystar**
Do you want anything more specific?
If you want something like the AI safety gridwolds in scrtucture(wich unfortunately not a lot people actually ended up using) maybe https://minigrid.farama.org/ maybe.
You can also just use gym enviroments https://github.com/Farama-Foundation/Gymnasium
If you want something harder you can use minecraft/minetest either using mineRL or the new Minetest enviroment for alignment research the EleutherAi people are working on(but training agents there is pretty hard...

**05:12:31 UTC** - #paper-discussion - **stellaathena** (1 reactions)
The Pythia models we specifically designed to promote interpretability and scientific research on LLMs. There’s a couple details we need to finish in the paper, but I wanted to post a draft seeing as I know many people here are already playing with the models.

### 2023-03-30

**00:14:43 UTC** - #paper-discussion - **stellaathena**
Sorry, this was supposed to come with a link to said paper: https://cdn.discordapp.com/attachments/1052314805576400977/1090445218723147796/Interpretability-42.pdf

### 2023-04-03

**04:40:56 UTC** - #project-proposals - **abhayesian**
I think it would be cool of someone tried to interpret transformers trained to predict the next state of a simple dynamical system.  The model will be trained similar to https://arxiv.org/pdf/2301.07067.pdf

### 2023-04-10

**05:00:38 UTC** - #project-proposals - **stellaathena**
<@226082991598862336> something like this, maybe? https://twitter.com/karpathy/status/1645115622517542913

**17:40:55 UTC** - #paper-discussion - **fieryvictorystar**
https://arxiv.org/abs/2302.03025

**17:41:12 UTC** - #paper-discussion - **fieryvictorystar**
Neel mentioned this paper on twitter.

**21:01:05 UTC** - #paper-discussion - **stellaathena** (1 reactions)
There’s a channel working on extending this paper in EleutherAI. We are close to having a full circuit reverse engineered for S_5!

**21:25:18 UTC** - #project-proposals - **abhayesian**
It seems that in this case, the transformer is trained to memorize a specific bit string?  I don't think that this transformer is looking at the other bits in the context window to figure out what the pattern is.

**21:26:53 UTC** - #project-proposals - **abhayesian**
maybe a version of this where bitstrings of a certain lenth with varying patterns are sampled, and the transformer will have to figure out which pattern the bitstring is following

**21:40:49 UTC** - #project-proposals - **abhayesian**
I was thinking that you could train the transformer on bitstrings generated by multiple randomly sampled FSMs.  Here, the transformer is trained on one bitstring from one FSM.  I want to be able to see if the model can predict what the automata is from the bits already in the context window, and then output the most likely transition, so I dont think this would be sufficient.

**21:55:28 UTC** - #paper-discussion - **stellaathena**
Interpretability General > S_n Circuits

### 2023-05-03

**16:26:42 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2305.01610

### 2023-05-05

**02:25:25 UTC** - #paper-discussion - **abhayesian**
this paper looks fairly interesting

**02:25:26 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://kindxiaoming.github.io/pdfs/BIMT.pdf

### 2023-05-07

**18:54:33 UTC** - #paper-discussion - **jknowak**
Yes, I wonder what would the BIMTs impact be on superposition/polysemanticity. Is it a valid research idea?

### 2023-05-08

**11:44:48 UTC** - #paper-discussion - **yongzx**
What do you all think about performing MI on https://arxiv.org/abs/2305.02363 (new entity tracking task)?

**11:45:47 UTC** - #paper-discussion - **yongzx**
I'm quite new to MI but I feel like the underlying mechanism may be similar to the https://arxiv.org/abs/2211.00593

**17:01:30 UTC** - #paper-discussion - **abhayesian**
technical note on bilinear layers from Lee Sharkey of conjecture
https://arxiv.org/abs/2305.03452

**17:36:11 UTC** - #paper-discussion - **fieryvictorystar**
https://arxiv.org/abs/2305.03210

### 2023-05-10

**20:33:42 UTC** - #paper-discussion - **lunaiscoding**
https://arxiv.org/abs/2211.03540

### 2023-05-11

**12:36:46 UTC** - #project-proposals - **davidstrongfield**
The Markov diagram posted by <@193204646687408129>  looks a bit odd. Why is there a 22% chance of adding a 0 when the last 3 bits were 110? Does the baby GPT not know that a sequence of two consecutive 0's do not appear in the data? There should be a 0% chance of this transition. It seems like for the problem of reconstructing finite state Markov chains with a small number of states, a more efficient machine learning algorithm would be to cluster the positions in the sequence of bits into states...

**15:30:29 UTC** - #project-proposals - **davidstrongfield**
So I have used my (matrix-product optimized) MPO word embedding algorithm to see if I can completely recover the transition for the sequence 11110 repeated over and over again. The MPO word embedding algorithm was designed to maximize the quantity log(rad(x^4*y))/5-log(rad(kron(x,conjugate(x))+kron(y,conjugate(y))))/2. Here, rad denotes the spectral radius of a matrix while kron denotes the tensor product, and conjugate refers to the matrix obtained by conjugating each of the entries in the matr...

**22:15:42 UTC** - #project-proposals - **davidstrongfield**
My above comment actually gives me an idea about interpretability. If I train an MPO word embedding on a sequence generated by a finite state Markov process, then how closely will the matrices in the MPO word embedding correlate to the transition matrices for the finite state Markov process? Perhaps, I will need to apply a dimensionality reduction to some of these matrices. Fortunately, I have developed the notion of the L_{2,d}-spectral radius dimensionality reduction which will reduce the dime...

### 2023-05-16

**17:04:43 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2305.08809

### 2023-05-19

**23:06:54 UTC** - #paper-discussion - **abhayesian**
https://openreview.net/forum?id=X3JFgY4gvf

### 2023-05-25

**02:06:34 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2305.15348
I remember Yudkowsky saying that he was afraid of this?
hooking up an RNN directly to the transformer's residual stream as a method for parameter efficient fine tuning

### 2023-05-26

**16:01:21 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://transformer-circuits.pub/2023/interpretability-dreams/index.html

**16:17:56 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2305.14699

**19:49:04 UTC** - #paper-discussion - **abhayesian**
https://twitter.com/DrJimFan/status/1662115266933972993

### 2023-05-27

**22:07:02 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2305.16130

### 2023-05-29

**05:01:41 UTC** - #general-resources - **joyeechen**
Anybody know the major AI safety/alignment related conferences? I have a transformers interp project for it

### 2023-06-02

**17:12:57 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2305.19466

**17:13:25 UTC** - #paper-discussion - **abhayesian**
It turns out that decoder-only transformers work just fine (and most of the time, better) without positional embeddings

### 2023-06-03

**16:08:51 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2306.00937

**16:22:44 UTC** - #paper-discussion - **fieryvictorystar**
Yes, Twitter algoritms knows me and recommended the announcement.

### 2023-06-07

**13:12:38 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://twitter.com/danfriedman0/status/1665691834088030210

**13:12:51 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2306.01128

### 2023-06-21

**07:16:42 UTC** - #project-proposals - **q_m_o**
if anyone's interested in getting a group around interpreting open source rlhf models or RMs, I'm looking for collaborators to help brainstorm ideas and get something going
https://docs.google.com/document/d/1eUdvlJNqY9X0NAw9UUseZz6dFyRklCcOHQy8x3CbcBk/edit?usp=sharing

### 2023-06-22

**09:23:01 UTC** - #project-proposals - **q_m_o**
https://arxiv.org/abs/2306.07567

### 2023-06-30

**18:23:16 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2301.13196

**18:23:34 UTC** - #paper-discussion - **abhayesian**
assembler turned into encoder-only transformer

### 2023-07-09

**16:18:51 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2305.18741

### 2023-07-16

**14:20:10 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://openreview.net/forum?id=ytYaiSQNCB

**14:45:29 UTC** - #paper-discussion - **woog** (1 reactions)
thats sick. hot off the press too; https://anonymous.4open.science/r/circuit-breaking-5DE5/README.md their code is here

### 2023-07-19

**07:08:12 UTC** - #paper-discussion - **jannikbrinkmann** (1 reactions)
https://arxiv.org/abs/2307.09458

### 2023-07-23

**18:17:02 UTC** - #paper-discussion - **poppingtonic** (2 reactions)
https://arxiv.org/abs/2007.12213

### 2023-08-02

**16:09:36 UTC** - #paper-discussion - **abhayesian** (1 reactions)
https://arxiv.org/abs/2307.15771

### 2023-08-04

**18:02:21 UTC** - #paper-discussion - **abhayesian**
https://arxiv.org/abs/2308.01544

### 2023-08-08

**04:08:05 UTC** - #paper-discussion - **abhayesian** (2 reactions)
https://arxiv.org/abs/2308.03296

**05:20:08 UTC** - #paper-discussion - **woog**
Oh let's go. New anthropic paper

**06:58:15 UTC** - #paper-discussion - **nedflacosyndiam**
the whole approach of influence functions is very interesting - i can't really tell if it actually works or not by reading this paper, but the way the influence function is defined seems to have direct implications for all of the people attempting to determine (using the legal system) if the inclusion of copyrighted work in a training corpus influenced the output of a released model.

**10:53:49 UTC** - #paper-discussion - **jannikbrinkmann**
I have not checked or seriously engaged with it yet, but I found the abstract interesting: https://arxiv.org/pdf/2301.04213.pdf

**10:56:06 UTC** - #paper-discussion - **alexioli**
Yes this is quite an interesting paper - you can insert factual associations into the weights in places other than those identified as most relevant by causal tracing, and it often works better (or at least as well)

**10:56:42 UTC** - #paper-discussion - **alexioli** (1 reactions)
Punchline: " Causal Tracing answers a
question about where factual information is carried in representations in a Transformer forward pass, and this question
turns out to be a different question than the editing question
of where is best to intervene in the Transformer in order
to change the factual information it expresses"

### 2023-08-16

**11:55:26 UTC** - #project-proposals - **jonask7671**
**Epistemic Benchmarks **
Epistemic Benchmark explores the evaluation and measurement
of the knowledge foundations of intelligent agents in various environments.
This research aims to develop standardized benchmarks for assessing the
epistemic capabilities of agents, including their understanding of the envi-
ronment, adaptability to dynamic situations, and decision-making strate-
gies based on internal models and predictions
https://github.com/equiano-institute/epistemic-benchmark

### 2023-09-13

**09:35:51 UTC** - #paper-discussion - **jannikbrinkmann**
https://arxiv.org/abs/2309.05858 random finding on X: google publishing on mesa-optimization

**12:17:33 UTC** - #paper-discussion - **woog** (1 reactions)
... but is the circuit efficient? 😂

**12:29:36 UTC** - #paper-discussion - **woog**
do you think with that many google authors that the codebase would be in this list https://github.com/google-research/google-research/tree/master

**12:33:15 UTC** - #paper-discussion - **woog**
anyone know how to navigate github

**12:35:45 UTC** - #paper-discussion - **woog**
when it's applied to interpretability its really something else

**12:37:13 UTC** - #paper-discussion - **woog**
https://pair.withgoogle.com/explorables/grokking/ e.g. i was tryna find the code for this page he did the visualizations for

**12:38:01 UTC** - #paper-discussion - **woog** (1 reactions)
https://roadtolarissa.com/ his whole "portfolio" is here, the code for this website is available here <https://github.com/1wheel/roadtolarissa/tree/master/source>, but only some of the links in the portfolio are actually on the website, rather than linking somewhere else

**12:50:42 UTC** - #paper-discussion - **woog**
https://github.com/PAIR-code/ai-explorables/tree/master/source/grokking OK found the grokking page code

### 2023-09-21

**19:22:03 UTC** - #paper-discussion - **paranoidhumanoid**
https://arxiv.org/abs/2106.00737
Is there interpretability work on how LLM have a vague sense of encoding representations of meaning like in this paper ? 
I thought this was interesting as the authors describe llms encode a sets of situation in something called as "information states"

### 2023-09-22

**13:27:50 UTC** - #paper-discussion - **jannikbrinkmann** (2 reactions)
"How does GPT-2 compute greater-than? ..." got accepted at NeurIPS. great sign that mech-interp research is appreciated at top-tier conferences: https://twitter.com/michaelwhanna/status/1705152268209709224

**14:59:40 UTC** - #paper-discussion - **jannikbrinkmann**
https://twitter.com/ZimingLiu11/status/1705212421306990671 pizza paper even got an oral

### 2023-12-07

**21:52:09 UTC** - #interesting-findings - **dashiell_s**
and I'm curious if perhaps this sort of representation of the circuits would give us tools to try and tell the difference

**21:53:08 UTC** - #interesting-findings - **narmeen**
Me too, yeah feel free to share thoughts, i really like talking about that paper (i process it better in iterations)

**21:53:33 UTC** - #interesting-findings - **dashiell_s** (1 reactions)
I'm quite busy right now, but I'll try and read that paper next week

### 2023-12-16

**17:56:12 UTC** - #interesting-findings - **woog** (1 reactions)
https://www.youtube.com/watch?v=_oCWsaFBY1M

**21:05:34 UTC** - #interesting-findings - **burnytech**
https://openreview.net/forum?id=Pe9WxkN8Ff Learning Transformer Programs show how you can modify transformers to learn human-intepretable circuits translatable to Python!

**21:22:44 UTC** - #interesting-findings - **burnytech**
Transformers can learn in context like statisticians - A single transformer can select different learned algorithms for different data at hand. https://openreview.net/forum?id=vlCG5HKEkI

### 2023-12-17

**09:46:00 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2210.13382
https://arxiv.org/abs/2310.07582 OtherlloGPT learns emergent nonlinear internal representation of the board state
>Interventional experiments indicate this representation can be used to control the output of the network and create "latent saliency maps" that can help explain predictions in human terms.
>The investigation reveals that Othello-GPT encapsulates a linear representation of opposing pieces, a factor that causally steers its decision-making process

### 2023-12-18

**21:00:16 UTC** - #general-resources - **seonsmallworldz**
https://aicyberchallenge.com/

### 2023-12-19

**15:21:21 UTC** - #interesting-findings - **jannikbrinkmann** (1 reactions)
the second paper seems to be a knock-off from Neel's work (first published as blog post and later published at BlackboxNLP https://arxiv.org/abs/2309.00941), or are there any new findings I missed?

### 2023-12-20

**01:28:09 UTC** - #interesting-findings - **burnytech**
He knows about it as I found the paper from Neel's EA lecture https://www.youtube.com/watch?v=7t9umZ1tFso

**01:28:10 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2312.10794

**01:37:08 UTC** - #interesting-findings - **burnytech**
https://techxplore.com/news/2023-12-ai-memory-forming-mechanism-similar-brain.amp AI's memory-forming mechanism found to be strikingly similar to that of the brain

**09:00:23 UTC** - #interesting-findings - **g_w1**
I just made a connection which could be potentially interesting: there is a program called creduce https://github.com/csmith-project/creduce/ that takes in a c file and interestingness test and reduces the code until you get the smallest program that still passes the interestingness test

this seems pretty similar to what we want to do in interpretability (and what ACDC is trying to do). I wonder if there are any insights or algorithms that we could borrow from creduce. My guess is that there ar...

**16:43:02 UTC** - #interesting-findings - **useewhynot**
This seems interesting, I read through the paper that presented this (p sure it was a NeurIPS accept this year so maybe some people here saw it there), and it's interesting how their activation mirrors swish/sigmoid

**16:44:25 UTC** - #interesting-findings - **useewhynot**
Specifically when you look at one of their findings (large a value corresponds to better place cell scores and lower error rate), the higher a value roughly corresponds to a higher "bias term" in an elementwise linear op prior to swish or sigmoid activation

**16:48:25 UTC** - #interesting-findings - **useewhynot**
Would be interesting to see why a higher bias/offset prior to activation improves in-memory error rate

**19:01:39 UTC** - #interesting-findings - **.jclinton**
What is CCS? 

Edit: I found the paper: https://arxiv.org/pdf/2212.03827.pdf, I get what it is now.

### 2023-12-21

**23:51:38 UTC** - #interesting-findings - **45awsmwarrir123**
<@102871169362825216> https://www.llamaindex.ai/ would this be of help to you for summarizing, semantically searching for, and selecting papers?

### 2023-12-22

**08:42:52 UTC** - #interesting-findings - **alextmjugador**
One of my professors suggested as a somewhat obvious but nevertheless interesting technique for finding papers: doing "snowballing"

**08:43:03 UTC** - #interesting-findings - **alextmjugador**
You first take a paper you like (or several)

**08:43:16 UTC** - #interesting-findings - **alextmjugador**
Then go through its citations finding other papers you like

**09:47:45 UTC** - #interesting-findings - **vkc6969**
he summarized how most phd students look for papers

### 2023-12-23

**10:05:52 UTC** - #interesting-findings - **butanium**
https://cdn.discordapp.com/attachments/1162345675137220699/1187089607427371171/ccs_layer_8_policy.mp4?ex=65959e59&is=65832959&hm=dbe3cbd7c2f6d8afe5799a99596d7f111ac83322a39fd3928f3475bae81f3d66&

**19:32:05 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/omarsar0/status/1738592208054370723
<https://github.com/JShollaj/awesome-llm-interpretability>

**19:46:09 UTC** - #interesting-findings - **burnytech**
https://openreview.net/forum?id=4bSQ3lsfEV Going Beyond Neural Network Feature Similarity: The Network Feature Complexity and Its Interpretation Using Category Theory
1) the larger the network, the more redundant features it learns; 2) in particular, we show how to prune the networks based on our finding using direct equivalent feature merging, without fine-tuning which is often needed in peer network pruning methods; 3) same structured networks with higher feature complexity achieve better perf...

**19:46:10 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2310.06824 The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets
"1. Visualizations of LLM true/false statement representations, which reveal clear linear structure. 2. Transfer experiments in which probes trained on one dataset generalize to different datasets. 3. Causal evidence obtained by surgically intervening in a LLM's forward pass, causing it to treat false statements as true and vice versa. Overall, we prese...

**19:47:27 UTC** - #interesting-findings - **45awsmwarrir123**
"hasn't received as much attention" 🤔

**19:48:08 UTC** - #interesting-findings - **45awsmwarrir123**
i don't know if it's selection bias from me being in interp servers or something, but i see a lot of interp research around me

**19:50:57 UTC** - #interesting-findings - **45awsmwarrir123**
ah so we're talking about shallow hype not deep attention

**19:54:03 UTC** - #interesting-findings - **burnytech**
there are whole programs for deep attention on cybersecurity in Czech universities, but im the only one weirdo nerding about mechinterp here

### 2023-12-24

**05:58:34 UTC** - #interesting-findings - **burnytech**
https://www.latent.space/p/neurips-2023-papers

**06:38:34 UTC** - #interesting-findings - **burnytech**
https://www.lesswrong.com/posts/uG7oJkyLBHEw3MYpT/generalization-from-thermodynamics-to-statistical-physics

**14:47:49 UTC** - #interesting-findings - **burnytech**
Zeta Alpha Trends in AI - December 2023 - Gemini, NeurIPS & Trending AI Papers https://www.youtube.com/watch?v=6iLBWEP1Ols

**19:43:39 UTC** - #interesting-findings - **burnytech**
https://www.youtube.com/watch?v=9dSkvxS2EB0

**20:48:23 UTC** - #interesting-findings - **burnytech** (1 reactions)
“Our paper suggests that the information flow inside Transformers can be decomposed cleanly at a macroscopic level. This gives hope that we could design safety applications to know what models are thinking or intervene on their mechanisms without the need to fully understand their internal computations.” https://arxiv.org/abs/2312.10091

**23:21:49 UTC** - #interesting-findings - **burnytech**
<https://arxiv.org/abs/2311.15131>
Twitter thread: https://twitter.com/mezaoptimizer/status/1729981499397603558

### 2023-12-25

**22:43:07 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/fly51fly/status/1739042528748572798?t=-sviSkTmtYYmiIsYKgU85A&s=19

### 2023-12-26

**10:34:48 UTC** - #interesting-findings - **45awsmwarrir123**
random thought: if systolic arrays are such a good fit for what human brains do, then the rows of systolic arrays (https://www.intel.com/content/dam/develop/external/us/en/documents/catc17-in-depth-learning-matrix-multipliers-dl-accelerators-844137.pdf) could represent the brain's incoming sensory input, and the columns could be the learned model. then our brain waves would just be our relevant life experiences flowing down the columns

### 2023-12-29

**22:41:24 UTC** - #paper-discussion - **45awsmwarrir123**
i wonder if he will find this concept i use: consider me being offered 4 choices:

1. $20 of stock A, $20 of stock B, plus $20 of stock C
2. $200 of stock A, $50 of stock B, plus $150 of stock C
3. $200 of stock A, $100 of stock B, plus $100 of stock C
4. $200 of stock A, $150 of stock B, plus $50 of stock C

at first glance, i would prefer option 1 over option 3 over an indifference between options 2 and 4. this relies on a prior based on symmetry and that there are usually more wrong choices t...

### 2023-12-30

**01:53:22 UTC** - #interesting-findings - **burnytech** (1 reactions)
https://www.youtube.com/watch?v=ZSmORp3Bm2c

**14:45:57 UTC** - #interesting-findings - **woog**
Basically it is evidence against using probes for (causal) interp research since this is a huge established confounder. Sounds good to me

**16:05:22 UTC** - #interesting-findings - **woog**
https://arena3-chapter1-transformer-interp.streamlit.app/ updated arena resources

**17:59:32 UTC** - #interesting-findings - **woog**
Exploring zotero. found organized collections of "old interpretability" literature, e.g. stuff up until the end of 2021. This one has 791 entries in it:
https://www.zotero.org/groups/2361530/interpretability/library

**18:01:42 UTC** - #interesting-findings - **woog**
Another one (not organized), this one has 128 entries:
https://www.zotero.org/groups/2616285/interpretability__bias_in_nlp/library

**22:23:38 UTC** - #interesting-findings - **burnytech**
I wonder what could you get if you threw this math to artificial neural nets https://arxiv.org/abs/2102.03849

### 2024-01-01

**03:24:45 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2307.07843

**05:38:53 UTC** - #interesting-findings - **burnytech**
looking for some papers at the intersection of statistical mechanics and deep learning, this is pretty cool (random landscapes, spin glasses, jamming, dynamical phase transitions, chaos, Riemannian geometry, random matrix theory, free probability, and nonequilibrium statistical mechanics) https://www.annualreviews.org/doi/10.1146/annurev-conmatphys-031119-050745

**05:38:59 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2212.01744

### 2024-01-02

**00:36:37 UTC** - #interesting-findings - **burnytech** (1 reactions)
https://arxiv.org/abs/2311.07590 LLM strategically deceiving their users in a realistic situation without direct instructions or training for deception

**19:28:04 UTC** - #interesting-findings - **butanium**
https://fxtwitter.com/norabelrose/status/1724106552376988132?t=3T4ipemEKtLlqtjfPjpm7g&s=19

**21:41:18 UTC** - #interesting-findings - **45awsmwarrir123**
i shouldn't need to tell the model not to put the cat in the over for dinner: https://www.quantamagazine.org/artificial-intelligence-aligned-with-human-values-qa-with-stuart-russell-20150421/

### 2024-01-03

**14:25:32 UTC** - #interesting-findings - **burnytech**
https://twitter.com/johnschulman2/status/1741178475946602979
"A compelling intuition is that deep learning does approximate Solomonoff induction, finding a mixture of the programs that explain the data, weighted by complexity. Finding a more precise version of this claim that's actually true would help us understand why deep learning works so well. There are a couple recent papers studying how NNs solve algorithmic tasks, which seem like exciting progress in this direction.
- https://arxiv.org/a...

**23:23:18 UTC** - #interesting-findings - **butanium**
reproduced this on a more capable network trained against a pool of frozen agents and itself https://cdn.discordapp.com/attachments/1162345675137220699/1192245605733503118/multi_agent_train_fixed_ppo_multiagent_2.cleanrl_model_vs_multi_agent_train_fixed_ppo_multiagent_2.cleanrl_model.mp4?ex=65a8603f&is=6595eb3f&hm=7f06060f04e30bb5323a7faf1305a7cce9f22f773459981bf5d82626d5229994&

### 2024-01-04

**08:17:02 UTC** - #interesting-findings - **giftedgummybee**
This is very important

**19:34:01 UTC** - #interesting-findings - **useewhynot**
I guess the question here then is whether you can fit the alignment "behavior" (mappings of how to respond to certain topics) into a singular prompt. from a mechanistic pov a prompt is just a "program" that determines which offset is applied to embedding representations moving forward in the LLM inference, akin to activation steering. Issue is though, can prompts only encode constant offsets in latent space, or are they capable of encoding arbitrary steering vectors for any point in the latent s...

**19:39:55 UTC** - #interesting-findings - **giftedgummybee**
i believe that a naive way of doing is forcing attention to "overattend" to the system message tokens

**19:40:19 UTC** - #interesting-findings - **useewhynot**
attention sinks might be an interesting look at that

**19:41:31 UTC** - #interesting-findings - **useewhynot**
a study that might prove interesting would be applying transformer inference with/without attention sinks given a constant system prompt and measure HH-RLHF scores

**19:42:41 UTC** - #interesting-findings - **useewhynot**
although i guess attention sinks only really apply when the context window isn't big enough to hold the entire text, so you'd prob need to limit the context window or start messing with the actual attention computation like you mentioned

**19:49:45 UTC** - #interesting-findings - **useewhynot**
I guess the big thing is figuring out whether prompt prefix/suffixes are capable of encoding arbitrary programs that can react to any embedding representation seen and steer it effectively

**19:50:33 UTC** - #interesting-findings - **useewhynot**
my gut feeling says yes based on a look at a single self-attention layer, but I imagine the "resolution" of word embeddings and how many tokens are in the prompt define the effectiveness of that

### 2024-01-05

**20:58:47 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2307.15043

**21:07:22 UTC** - #interesting-findings - **woog**
theres some very clever ideas in it though. like generating transferrable prompt injection activation vectors without needing a complex dataset, like you just append 1 prefix or suffix to every prompt of your original dataset

**21:07:51 UTC** - #interesting-findings - **woog**
and then make contrast pairs that way, average over all the activations and steer via this activation addition intervention

**21:08:14 UTC** - #interesting-findings - **woog**
and they found a way to do interpretability with it

**21:09:42 UTC** - #interesting-findings - **burnytech**
i just know steering gpt2 https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector

**21:10:23 UTC** - #interesting-findings - **woog**
https://www.lesswrong.com/posts/v7f8ayBxLhmMFRzpa/steering-llama-2-with-contrastive-activation-additions

**21:10:47 UTC** - #interesting-findings - **woog**
there's a paper now but the work had been done for months before that

**21:11:34 UTC** - #interesting-findings - **woog**
https://airtable.com/appYIr2qJDA2k0H9V/shrngsIKdJMCD7dYz/tblcUzakXN65z6xs7/viws1Gk5k0Xerk3Jr/rec6ks2L9T4WuEp5Z then this is the project page for nina's spar project

**21:13:41 UTC** - #interesting-findings - **burnytech**
is this convertible from activation vector to a prompt (since you cant really add activation vector to ChatGPT behind an API)

**21:13:57 UTC** - #interesting-findings - **woog**
you need access to the activations

**21:14:49 UTC** - #interesting-findings - **woog** (1 reactions)
this repo is a goldmine https://github.com/nrimsky/LM-exp/tree/main

### 2024-01-07

**04:53:24 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/a_karvonen/status/1743666230127411389?t=3UDIFxYPmJljaVzK1B0F0w&s=19

**04:53:33 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/a_karvonen/status/1743666236180119706?t=3gyzwQ26mR3cf_f0qkPX9Q&s=19

**04:53:48 UTC** - #interesting-findings - **burnytech**
https://adamkarvonen.github.io/machine_learning/2024/01/03/chess-world-models.html

**17:57:32 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://fxtwitter.com/FazlBarez/status/1743441580479115458

**21:43:22 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2301.04589

### 2024-01-08

**16:00:12 UTC** - #interesting-findings - **burnytech**
https://users.ics.aalto.fi/tho/stes/step96/hyotyniemi1/ Turing Machines are Recurrent Neural Networks
https://en.wikipedia.org/wiki/Neural_Turing_machine
https://news.ycombinator.com/item?id=33869533 "It is possible to construct an (infinite) recurrent neural network that emulates a Turing Machine. But the fact that a Turing Machine can be built out of perceptrons is neither surprising nor interesting. It's pretty obvious that you can build a NAND gate out of perceptrons, and so of course you ca...

### 2024-01-09

**14:01:07 UTC** - #interesting-findings - **woog** (1 reactions)
implementation of a CNN on mnist in a google sheet: https://docs.google.com/spreadsheets/d/1SwfVctd4TjdN2S8BL09ktpQN_41sARYzD3NEHyr-8Z0/edit#gid=0

**17:08:53 UTC** - #interesting-findings - **burnytech**
LLM Automated Interpretability Agent: Built from LLM with black-box access to functions, can infer function structure; A "scientist" forming hypotheses, proposing experiments, & updating descriptions; Capture global function behavior, but can miss details. https://arxiv.org/abs/2309.03886

### 2024-01-10

**16:42:24 UTC** - #general-resources - **seonsmallworldz**
https://open.spotify.com/show/5664BSntGTMKOfVUTVXppO

**16:44:07 UTC** - #general-resources - **seonsmallworldz**
https://www.youtube.com/@alignmentnewsletterpodcast4310/videos

**16:46:14 UTC** - #general-resources - **seonsmallworldz**
https://www.youtube.com/@aisafetyreadinggroup/videos

**16:47:33 UTC** - #general-resources - **seonsmallworldz** (1 reactions)
put on stuff from MIT,and various courses that teach the core of ai
or even just turn various books,papers into audiobooks and listen to those

### 2024-01-11

**18:10:26 UTC** - #interesting-findings - **seonsmallworldz**
https://experiments.withgoogle.com/visualizing-high-dimensional-space

### 2024-01-13

**05:45:05 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2401.05566

**05:45:16 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/AnthropicAI/status/1745854907968880970 thread

### 2024-01-14

**15:52:41 UTC** - #interesting-findings - **g_w1** (1 reactions)
https://www.lesswrong.com/posts/93nKtsDL6YY5fRbQv/case-studies-in-reverse-engineering-sparse-autoencoder seems quite interesting

### 2024-01-16

**04:57:06 UTC** - #interesting-findings - **burnytech** (1 reactions)
https://pair-code.github.io/interpretability/patchscopes/

### 2024-01-17

**13:48:04 UTC** - #interesting-findings - **burnytech**
https://link.springer.com/chapter/10.1007/978-3-031-04083-2_2 LIME, Anchors, GraphLIME, LRP, DTD, PDA, TCAV, XGNN, SHAP, ASV, Break-Down, Shapley Flow, Textual Explanations of Visual Models, Integrated Gradients, Causal Models, Meaningful Perturbations, and X-NeSyL

**16:38:22 UTC** - #interesting-findings - **wlodder** (1 reactions)
Paper connecting grokking to polytope lense for MI https://arxiv.org/pdf/2310.12977.pdf

### 2024-01-18

**14:21:52 UTC** - #interesting-findings - **seonsmallworldz**
https://openai.smapply.org/prog/agentic-ai-research-grants/

### 2024-01-19

**22:45:41 UTC** - #interesting-findings - **.msklar** (1 reactions)
Fluent gradient-based adversarial attacks on LLMs are possible! Our latest draft, not yet submitted to arxiv but we'd love your feedback:

This might for allow "dreaming" approaches to LLM interpretability (which was previously only for vision-capable models, as far as we're aware)

**23:37:31 UTC** - #interesting-findings - **abhayesian**
nice, I've been working on something similar.  We try comparing GCG to just training a reverse language model (training a model to predict tokens backwards) to sample a bunch of prompts which we then pass through a normal LM to find the ones which gives the target tokens the highest probability.  Here is an outdated version (we're trying to get the arxiv version out soon)
https://openreview.net/forum?id=m6xyTie61H

**23:37:55 UTC** - #interesting-findings - **abhayesian**
I guess this is less aimed at feature viz, but more so aimed at generating more natural adversarial prompts

### 2024-01-21

**00:20:40 UTC** - #interesting-findings - **g_w1**
https://arxiv.org/pdf/2401.10020.pdf 👀 getting closer towards recursive self-improvement

**01:20:50 UTC** - #interesting-findings - **useewhynot**
ReST-EM is a "evolutionary-style" method of preference learning where instead of trying to directly maximize reward via gradients, you pick high reward generations and use those as targets for SFT (supervised fine-tuning) (https://arxiv.org/pdf/2312.06585.pdf)

**01:21:57 UTC** - #interesting-findings - **useewhynot**
I was thinking this takes a similar approach based on my skim-through of the paper, but instead of selecting the highest reward generations to train directly on via SFT you're instead generating the rewards with LLM-judging and using DPO as a policy update instead

### 2024-01-22

**14:05:43 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/gsarti_/status/1749366992132292652
https://huggingface.co/collections/gsarti/daily-picks-in-interpretability-and-analysis-of-lms-65ae3339949c5675d25de2f9

### 2024-01-24

**08:51:57 UTC** - #interesting-findings - **jannikbrinkmann**
https://twitter.com/NeelNanda5/status/1749886478673682677

**08:56:31 UTC** - #interesting-findings - **jannikbrinkmann**
https://twitter.com/wesg52/status/1749829624933322886

**13:45:29 UTC** - #interesting-findings - **burnytech**
Arxiv link, amazing work https://arxiv.org/abs/2401.12181

### 2024-01-26

**00:24:41 UTC** - #interesting-findings - **butanium**
Do you know that when you do `run_with_cache(string)`, at least for pythias models, transformer_lens add a `bos_token` at the beginning of the statmeent ?

**00:25:10 UTC** - #interesting-findings - **butanium**
at least it did when we tried to probe xors of simple feature in small pythias

### 2024-01-29

**17:40:23 UTC** - #paper-discussion - **jannikbrinkmann** (1 reactions)
Black-Box Access is Insufficient for Rigorous AI Audits (or "The Case for nnsight"): https://arxiv.org/abs/2401.14446

### 2024-01-31

**12:19:06 UTC** - #interesting-findings - **g_w1**
once we build a sae it might be worth putting it in a format that we can upload to neuronpedia so that we can get an easy way to evaluate it like they do here https://www.lesswrong.com/posts/QwgYmpnMxBZnmGCsw/exploring-openai-s-latent-directions-tests-observations-and#Observations_and_Tidbits

### 2024-02-04

**17:01:59 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2401.14953
<https://syncedreview.com/2024/01/31/neural-networks-on-the-brink-of-universal-prediction-with-deepminds-cutting-edge-approach/>

### 2024-02-06

**18:19:29 UTC** - #interesting-findings - **tbenthompson** (1 reactions)
Hi all, new around here, hope it's alright to share a mech-interp-relevant paper we just put out! “Fluent dreaming for language models” : we managed to optimize prompts for large activations while maintaining perplexity as low as the Pile. A new tool in the LLM interpretability toolkit analogous to feature visualization/DeepDream in the vision model world.  https://arxiv.org/abs/2402.01702

**21:17:21 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/FazlBarez/status/1754919497247686885

**21:17:37 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2402.02619

### 2024-02-08

**22:33:57 UTC** - #interesting-findings - **kilgore.trout** (1 reactions)
https://twitter.com/jesse_hoogland/status/1755679791943147738

https://arxiv.org/abs/2402.02364

### 2024-02-12

**16:16:57 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/burny_tech/status/1757074849967595757
https://arxiv.org/abs/2106.10165
https://deeplearningtheory.com/

**16:17:09 UTC** - #interesting-findings - **burnytech** (1 reactions)
https://fxtwitter.com/jaschasd/status/1756930242965606582?t=S6R6iJfPbb_l1o8_FWm1dA&s=19
https://fxtwitter.com/jaschasd/status/1756930244337098890?t=-KwCiOaFz8OJ2rZzl_6fBw&s=19

### 2024-02-14

**11:08:44 UTC** - #interesting-findings - **burnytech**
https://www.youtube.com/watch?v=pad023JIXVA

### 2024-02-18

**20:12:39 UTC** - #interesting-findings - **burnytech**
https://fxtwitter.com/anand_bhattad/status/1759070325499625855?t=kXZAJ9ubDj2R_8NFHWynGg&s=19

### 2024-02-27

**17:03:34 UTC** - #interesting-findings - **kilgore.trout** (1 reactions)
https://arxiv.org/abs/2402.14735

### 2024-02-28

**00:14:56 UTC** - #interesting-findings - **g_w1**
https://www.lesswrong.com/posts/YsFZF3K9tuzbfrLxo/counting-arguments-provide-no-evidence-for-ai-doom

### 2024-03-01

**15:36:21 UTC** - #interesting-findings - **vkc6969**
https://arxiv.org/pdf/2402.17764.pdf

**15:50:01 UTC** - #interesting-findings - **wlodder**
https://proceedings.neurips.cc/paper_files/paper/2023/file/9d0f188c7947eacb0c07f709576824f6-Paper-Conference.pdf 

Author find that compositionality in generative image models (via DDPM)  respect an ordering of emergence similar to grokking

**18:14:13 UTC** - #interesting-findings - **j.w3697**
https://openreview.net/forum?id=exPzwOhBgx&referrer=%5Bthe%20profile%20of%20XUAN%20TANG%5D(%2Fprofile%3Fid%3D~XUAN_TANG1)

### 2024-03-02

**02:10:08 UTC** - #interesting-findings - **burnytech** (1 reactions)
<https://twitter.com/fchollet/status/1763692655408779455>
https://arxiv.org/abs/1911.01547

### 2024-03-04

**08:32:16 UTC** - #interesting-findings - **burnytech** (1 reactions)
https://fxtwitter.com/fly51fly/status/1764279536794169768?t=up6d06PPGeCE5fvIlE418Q&s=19
https://arxiv.org/abs/2402.18312

**20:23:13 UTC** - #interesting-findings - **kilgore.trout**
my goodness https://x.com/alexalbert__/status/1764722513014329620?s=46&t=Jcz3C2siFYnALAOLAcTSKw

### 2024-03-05

**01:57:22 UTC** - #interesting-findings - **fieryvictorystar**
https://twitter.com/repligate/status/1764781786062614827?t=WqbI-Y_gKkdeOKPxXk1Atw&s=19

**02:15:23 UTC** - #interesting-findings - **fieryvictorystar**
https://twitter.com/repligate/status/1764804500760485980?t=NPNCyzWM9PYtErC0SRzycA&s=19

**02:58:45 UTC** - #interesting-findings - **fieryvictorystar** (1 reactions)
https://twitter.com/repligate/status/1764837656834543864?t=nQT9ItEh83ypke7WBp15ew&s=19

### 2024-03-06

**20:55:02 UTC** - #interesting-findings - **michaelpearce**
https://x.com/SuryaGanguli/status/1765401784103960764?s=20

### 2024-03-13

**19:51:05 UTC** - #interesting-findings - **g_w1** (2 reactions)
a mech interp project won 250k in the regeneron competition: https://www.societyforscience.org/regeneron-sts/2024-sts-winners/

### 2024-03-19

**14:55:54 UTC** - #interesting-findings - **j.w3697**
https://arxiv.org/pdf/2306.09346.pdf

**14:56:11 UTC** - #interesting-findings - **j.w3697**
https://arxiv.org/pdf/2310.05916.pdf

**19:26:26 UTC** - #interesting-findings - **wlad123**
*Mechanism for feature learning in neural networks and backpropagation-free machine learning models*

**19:43:36 UTC** - #interesting-findings - **seonsmallworldz**
https://www.kaggle.com/competitions/llm-prompt-recovery/?utm_medium=email&utm_source=gamma&utm_campaign=comp-llmpromptrecovery

### 2024-03-20

**21:33:50 UTC** - #interesting-findings - **j.w3697**
https://arxiv.org/pdf/2305.19187.pdf

### 2024-03-26

**19:07:08 UTC** - #interesting-findings - **seonsmallworldz**
heres a cute lil badge you can put on your orcid
https://github.com/nasa/Transform-to-Open-Science/blob/main/docs/Area2_Capacity_Sharing/Open-Science-101/readme.md

### 2024-03-30

**17:17:27 UTC** - #interesting-findings - **burnytech**
Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models https://arxiv.org/abs/2403.19647v1

### 2024-04-12

**15:10:23 UTC** - #interesting-findings - **chocolala15**
What are the current research looking into safer alternative foundational model architectures - ie more interpretable architectures, modularized/bounded architectures, etc - or safer/more interpretable ways of training foundational models in general?

### 2024-04-24

**14:02:50 UTC** - #interesting-findings - **clemd6d** (1 reactions)
from the mech interp slack : 
**Neel Nanda**
> Activation patching is a crucial mech interp technique, but is deceptively hard to use well. In this informal note, Stefan Heimersheim and I discuss the details of different variants of activation patching, thinking intuitively about exactly what the technique is telling you, subtleties of choosing the right metrics, and give some extremely opinionated recommendations about how to do things.
> https://arxiv.org/abs/2404.15255

### 2024-04-25

**23:09:35 UTC** - #interesting-findings - **g_w1**
looks very nice: https://arxiv.org/abs/2404.16014

### 2024-04-29

**23:32:15 UTC** - #interesting-findings - **g_w1** (1 reactions)
https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2 insanely cool!

### 2024-05-01

**15:59:40 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2404.14394

### 2024-05-05

**10:52:33 UTC** - #interesting-findings - **manifoldhiker** (1 reactions)
https://twitter.com/s_scardapane/status/1786382353499144515

**18:23:16 UTC** - #interesting-findings - **vkc6969**
this one is a great paper

### 2024-05-08

**20:36:16 UTC** - #interesting-findings - **burnytech**
Stanford series of lectures on machine learning theory
When do machine learning algorithms work and why? How do we formalize what it means for an algorithm to learn from data? How do we use mathematical thinking to design better machine learning methods? This course focuses on developing a theoretical understanding of the statistical properties of learning algorithms. 
Topics Include: 
Generalization bounds via uniform convergence 
Theory for deep learning 
Non-convex optimization 
Neural tangen...

### 2024-05-15

**11:02:24 UTC** - #interesting-findings - **g_w1**
I think I found a typo in https://arxiv.org/abs/2310.10348 . (it says edge activation patching rather than edge attribution patching). Can someone else just confirm this is a typo before I email them?

**12:04:27 UTC** - #interesting-findings - **mrgonao** (1 reactions)
it's strange because they do say activation patching twice and then they say attribution, but I think you are right

### 2024-05-27

**12:43:35 UTC** - #interesting-findings - **manifoldhiker**
https://arxiv.org/abs/2405.15071

### 2024-05-28

**18:35:33 UTC** - #paper-discussion - **fieryvictorystar** (1 reactions)
https://x.com/CarlGuo866/status/1795442886940737545?t=iYglNp1Hjek01Y6lU4g6Cw&s=19

### 2024-05-29

**17:48:02 UTC** - #interesting-findings - **vkc6969**
https://arxiv.org/pdf/2405.04517

### 2024-06-12

**20:31:46 UTC** - #interesting-findings - **hamish_todd** (1 reactions)
https://arxiv.org/pdf/2406.01506 Hey folks. Here's a paper from last week. Claims that concepts are direct sums of simplices. This may seem weird but something like it is actually extremely well studied in a field called "Clifford Algebra", which I am researching

**20:33:41 UTC** - #interesting-findings - **hamish_todd**
On the other hand, I wouldn't know how to connect this with interpretability research

**21:46:21 UTC** - #interesting-findings - **mrgonao**
Reminds me of the https://www.lesswrong.com/posts/gTZ2SxesbHckJ3CkF/transformers-represent-belief-state-geometry-in-their (mostly because there they also talk about simplices)

### 2024-06-13

**20:28:49 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://arxiv.org/abs/2406.08391

### 2024-06-17

**20:54:34 UTC** - #interesting-findings - **burnytech**
https://www.youtube.com/watch?v=PeSNEXKxarU

**21:09:39 UTC** - #interesting-findings - **bcarbon** (1 reactions)
Au contraire: https://x.com/bshlgrs/status/1802766374961553887

### 2024-06-18

**22:11:26 UTC** - #interesting-findings - **j.w3697** (1 reactions)
https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00644/120576 
Limitations of knowledge editing, specifically, changing one factual association may not change any other logical associations, which makes me wonder if true knowledge editing requires the edits of all the key-values in the MLP layers or if it's important to look at the other components of the model and edit those to also change logical relationships (like the attention layers).

### 2024-06-20

**19:22:20 UTC** - #interesting-findings - **j.w3697**
Not necessarily mech interp, more theory stuff, but this paper (while I don't fully understand it) is quite interesting and in some sense supports the whole idea of superposition, with the self attention layer too. 

https://proceedings.neurips.cc/paper_files/paper/2023/file/73bf692447f174984f30499ec9b20e04-Paper-Conference.pdf

**19:38:21 UTC** - #interesting-findings - **manifoldhiker**
https://arxiv.org/abs/2406.03689

### 2024-06-24

**00:45:32 UTC** - #interesting-findings - **burnytech**
https://www.youtube.com/watch?v=8Nyn3_ZWa_U

### 2024-07-07

**13:03:40 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2405.20233

Grokking seems accelerable, if not inducible. Might be interesting for studying mechanism of reasoning

### 2024-07-13

**16:40:09 UTC** - #interesting-findings - **burnytech**
"An Extremely Opinionated Annotated List of My Favourite Mechanistic Interpretability Papers" https://www.alignmentforum.org/posts/NfFST5Mio7BCAQHPA/an-extremely-opinionated-annotated-list-of-my-favourite-1

### 2024-07-18

**06:21:04 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2406.19501

### 2024-07-19

**14:13:43 UTC** - #interesting-findings - **seonsmallworldz**
https://www.youtube.com/watch?v=krINuMZhJmU

**15:40:12 UTC** - #interesting-findings - **burnytech**
Resources  for training sparse autoencoders:
<https://github.com/jbloomAus/SAELens>
<https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes>
<https://github.com/ai-safety-foundation/sparse_autoencoder/tree/main>
<https://ai-safety-foundation.github.io/sparse_autoencoder/>
<https://github.com/EleutherAI/sae>

**18:07:34 UTC** - #interesting-findings - **burnytech**
https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2

**22:31:54 UTC** - #interesting-findings - **burnytech**
https://www.lesswrong.com/posts/CbSEZSpjdpnvBcEvc/i-found-greater-than-800-orthogonal-write-code-steering

### 2024-07-20

**21:41:44 UTC** - #interesting-findings - **burnytech**
https://x.com/ravfogel/status/1814318728491815228

### 2024-07-21

**17:11:23 UTC** - #interesting-findings - **burnytech**
https://x.com/sebkrier/status/1814765954217488884
<https://arxiv.org/abs/2407.12831>

### 2024-07-22

**13:07:17 UTC** - #interesting-findings - **sye22** (1 reactions)
https://adamkarvonen.github.io/machine_learning/2024/03/20/chess-gpt-interventions.html

### 2024-08-01

**20:29:21 UTC** - #interesting-findings - **j.w3697**
https://arxiv.org/pdf/2406.04331

### 2024-08-02

**16:02:41 UTC** - #interesting-findings - **orbitsoferis**
(This has nothing to do with interpretability but I thought I’d share anyway)

Deep-TEMPEST: Using Deep Learning to Eavesdrop on HDMI from its Unintended Electromagnetic Emanations (https://arxiv.org/abs/2407.09717)

Wtf! I didn’t even know this was thing - but apparently it’s been a thing since the 1980s : “ The issue of inferring the content displayed on a monitor from the electromagnetic waves emitted by it and its connectors has a long history, dating back to the 1980s with the first public ...

**17:09:09 UTC** - #interesting-findings - **seonsmallworldz**
deep learning for hacking based stuff has been around for a while ; as well as its non ml based counterparts ;  keyboard sound analysis , other parts of the machine analysis (iirc a big one was done by checking how long a system takes to run stuff; but this  is more software) , hdmi emanations (phreaking?), led patterns on stuff depending on what specifically you're using , supposedly some stuff using audio waves but idt that makes any sense; might be used in conjunction with keyboard sounds to ...

### 2024-08-03

**02:25:34 UTC** - #interesting-findings - **burnytech**
https://x.com/a_karvonen/status/1819399813441663042
https://arxiv.org/abs/2408.00113
https://x.com/a_karvonen/status/1819399832466776389

**03:52:44 UTC** - #interesting-findings - **jh_lim131**
https://pair.withgoogle.com/explorables/grokking/

### 2024-08-13

**04:23:45 UTC** - #interesting-findings - **burnytech**
The AI Scientist: The world’s first AI system for automating scientific research and open-ended discovery
"Our system produced papers with novel contributions in ML research domains such language modeling, Diffusion and Grokking."
https://fxtwitter.com/SakanaAILabs/status/1823178623513239992
<https://sakana.ai/ai-scientist/>

**20:18:35 UTC** - #interesting-findings - **j.w3697** (1 reactions)
lol just reading the abstract, 

```The AI Scientist can produce papers that exceed the
acceptance threshold at a top machine learning conference as judged by our automated reviewer. ``` So is the reviewer AI here too?

### 2024-08-21

**17:59:52 UTC** - #interesting-findings - **ruiton320**
https://www.arxiv.org/abs/2408.10920

**18:02:32 UTC** - #interesting-findings - **bcarbon**
Isn't part of the intuition behind LRH the fact that transformers are mostly linear

**18:08:29 UTC** - #interesting-findings - **woog**
actually i guess that is not the crux. LRH was conceived outside of the transformer context

### 2024-08-23

**03:58:02 UTC** - #interesting-findings - **j.w3697** (1 reactions)
https://www.reddit.com/r/MachineLearning/comments/1eybxel/transformers_learn_incontext_by_gradient_descent_r/

### 2024-08-24

**02:40:28 UTC** - #interesting-findings - **nedflacosyndiam**
I love this paper so much!

### 2024-08-25

**20:39:55 UTC** - #interesting-findings - **j.w3697**
^ not sure if anyone has read this paper but leaving the abstract here:
```Language models learn a great quantity of factual information during pretraining,
and recent work localizes this information to specific model weights like mid-layer
MLP weights [21 ]. In this paper, we find that we can change how a fact is stored
in a model by editing weights that are in a different location than where existing
methods suggest that the fact is stored. This is surprising because we would
expect that local...

### 2024-08-26

**00:47:31 UTC** - #interesting-findings - **woog**
I know that David bau wants to produce a follow up work to the ROME causal tracing paper from way back, in response to this

**02:34:21 UTC** - #interesting-findings - **j.w3697**
yeah I'd be really curious, this definitely reshaped my perspective on a lot of the "circuits"-based work similar to the RIPPLE edits paper

### 2024-08-29

**01:33:16 UTC** - #interesting-findings - **seonsmallworldz**
https://www.youtube.com/watch?v=Gvh3gsmSLpA

### 2024-09-04

**12:48:53 UTC** - #interesting-findings - **seonsmallworldz**
should hold for most fields; though most of them aren't specifically ai research like above (rather; using ai for research)

### 2024-09-06

**17:48:23 UTC** - #interesting-findings - **_triquetra** (1 reactions)
Possibly of interest to you:
https://www.ams.org/journals/notices/202402/noti2868/noti2868.html?adat=February%202024&trk=2868&pdfissue=202402&pdffile=rnoti-p174.pdf&cat=none&type=.html

### 2024-09-07

**19:52:30 UTC** - #interesting-findings - **neelnanda** (1 reactions)
In my opinion the result isn't very surprising and isn't an update against circuit finding. ROME optimises an update that makes the model say B, not A. A natural way of doing that is by adding a really loud fact that outputs B. There's no need to delete A, so long as the insertion is loud enough. Thus ROME could just be doing insertion, not editing. Further, ROME works when done on a single layer while we know facts are spread across layers, making it even clearer that it can't be truly editing ...

**21:04:53 UTC** - #interesting-findings - **j.w3697**
Yeah that wasn't immediately obvious to me.  When I think of "fact editing", I originally thought ROME was directly erasing and replacing memories by identifying where they were stored through causal tracing. 

I think the ripple edits paper + the other one are good followups that mediated my admittedly overly-simplified understanding of what ROME was doing.

### 2024-09-13

**01:06:02 UTC** - #interesting-findings - **ruiton320**
Is there any work that systemically explore the structure of low-rank subspace within LLMs? I know there are tons of papers leveraging subspace for steering the model but not sure whether there is any explanation on how these low-rank subspaces emerge?

**01:07:40 UTC** - #interesting-findings - **ruiton320**
Interestingly there is a paper which finds that semantic subspaces also arise in diffusion models

**01:07:41 UTC** - #interesting-findings - **ruiton320**
https://arxiv.org/pdf/2409.02374

**01:07:57 UTC** - #interesting-findings - **ruiton320**
https://arxiv.org/abs/2409.02374

### 2024-09-17

**03:07:17 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2409.05907

### 2024-09-18

**23:26:19 UTC** - #interesting-findings - **woog**
https://x.com/kyutai_labs/status/1836427396959932492 Hmm interesting

### 2024-09-20

**11:24:24 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://www.youtube.com/watch?v=OyKXjdA09fE

**20:37:31 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2407.20311

**20:37:46 UTC** - #interesting-findings - **jh_lim131**
https://m.youtube.com/watch?v=bpp6Dz8N2zY

### 2024-09-21

**17:14:31 UTC** - #interesting-findings - **mrgonao**
I have collected activations for all layers of the gemma 9b SAEs  (over 10 M tokens) and have been thinking for a while on how I could investigate co-occurance

**21:38:52 UTC** - #interesting-findings - **burnytech**
https://youtu.be/BtHMIQs_5Nw?si=awTXmGSwxwj0pOFP

**21:38:56 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2303.13506

**21:38:59 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2205.10343

**21:39:02 UTC** - #interesting-findings - **burnytech**
https://arxiv.org/abs/2210.01117

**21:39:24 UTC** - #interesting-findings - **burnytech**
"We observe empirically the presence of four learning phases: comprehension, grokking, memorization, and confusion. We find representation learning to occur only in a "Goldilocks zone" (including comprehension and grokking) between memorization and confusion. We find on transformers the grokking phase stays closer to the memorization phase (compared to the comprehension phase), leading to delayed generalization. The Goldilocks phase is reminiscent of "intelligence from starvation" in Darwinian e...

### 2024-10-02

**18:23:38 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2409.15019
https://arxiv.org/abs/2409.17113

### 2024-10-03

**21:05:23 UTC** - #interesting-findings - **danibalcells**
Really into this paper about pluralistic alignment, and excited for the workshop at NeurIPS.
I'm curious whether people are aware of any benchmarks  / eval frameworks for model steerability at inference time - i.e. how good is a particular model / agent at aligning with a specific persona it's seeded with at inference time.
This paper has a pretty good conceptual framing of the topic - I'm looking for what they call "tradeoff-steerable benchmarks", which they introduce conceptually but don't men...

### 2024-10-17

**19:57:00 UTC** - #interesting-findings - **uzairm**
This paper and the one Burny shared both have to do with developmental interpretability, which seems like a cool new field

### 2024-10-21

**16:33:53 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://www.lesswrong.com/posts/h4wXMXneTPDEjJ7nv/a-rocket-interpretability-analogy new post with some takes about the dynamics around alignment strongly focusing on mech interp

**22:49:24 UTC** - #interesting-findings - **seonsmallworldz**
https://x.com/nickhjiang/status/1842298779246153891?s=46&t=iz30kAapV_a2uT_WcuFHTQ

**23:38:10 UTC** - #interesting-findings - **bcarbon**
thanks for sharing this post, not sure if I would have seen it otherwise. I think the post + comments contain good discussion on meta aspects of mechinterp that I would encourage people on this server to read.

gist of the post:
> The field of alignment seems to be increasingly dominated by interpretability. (and obedience[2])
> 
> This was surprising to me[3], until a friend pointed out that partially opening the black box of NNs is the kind of technology that would scaling labs find new unhobb...

**23:39:23 UTC** - #interesting-findings - **bcarbon**
[habryka](https://www.lesswrong.com/posts/h4wXMXneTPDEjJ7nv/a-rocket-interpretability-analogy?commentId=H7SJgvfcfNDm4nEfY)
> I would bet against this on the basis that Chris Olah's work was quite influential on a huge number of people, shaped their mental models of how Deep Learning works in general, and probably contributed to lots of improved capability-oriented thinking and decision-making. 
> 
> Like, as a kind of related example where I expect it's easier to find agreement, it's hard to poi...

**23:41:07 UTC** - #interesting-findings - **bcarbon**
[ryan_greenblatt](https://www.lesswrong.com/posts/h4wXMXneTPDEjJ7nv/a-rocket-interpretability-analogy?commentId=F22oqrkgm8a4TvXXc)
> I'm sympathetic to 'a high fraction of "alignment/safety" work done at AI companies is done due to commercial incentives and has negligible effect on AI takeover risk (or at least much smaller effects than work which isn't influenced by commercial incentives)'.
> 
> However, I'm quite skeptical that (mechanistic) interpretability research in particularly gets much ...

### 2024-10-29

**23:04:16 UTC** - #interesting-findings - **burnytech** (2 reactions)
Supercool 
https://fxtwitter.com/tegmark/status/1851288315867041903?t=eB9Ft7hF9ocV9s-w3s-O1w&s=19

### 2024-11-09

**21:19:59 UTC** - #interesting-findings - **vodros**
Cool SAE like approach to learning interpretable features
https://x.com/kamath_harish/status/1854988777175105865

### 2024-11-16

**21:03:18 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/pdf/2407.06076

### 2024-11-17

**13:47:27 UTC** - #interesting-findings - **paranoidhumanoid** (1 reactions)
https://arxiv.org/abs/2410.20035

### 2024-11-18

**19:34:44 UTC** - #interesting-findings - **alofty** (1 reactions)
good paper https://openreview.net/forum?id=pXlmOmlHJZ

### 2024-11-25

**13:53:50 UTC** - #interesting-findings - **seonsmallworldz**
https://arxiv.org/abs/2410.24184

**20:04:42 UTC** - #interesting-findings - **jager.bomber** (1 reactions)
https://openreview.net/forum?id=WxqWuG431g

### 2024-11-28

**13:36:23 UTC** - #interesting-findings - **seonsmallworldz**
https://www.aria.org.uk/programme-safeguarded-ai/

**14:38:47 UTC** - #interesting-findings - **seonsmallworldz**
SNUFA (spiking neural networks) talks are now public! https://www.youtube.com/playlist?list=PL09WqqDbQWHHijfS3PyGxPxeoATc-suAv

### 2024-12-07

**21:07:49 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://www.youtube.com/watch?v=YpFaPKOeNME

**22:09:43 UTC** - #interesting-findings - **burnytech**
intersection of spline theory and mechanistic interpretability https://arxiv.org/abs/2211.12312

### 2024-12-11

**16:34:35 UTC** - #interesting-findings - **fieryvictorystar**
completely forgot about this but recently the arbitrary close date I put to my prediction market about this arrived and reminded me of it, and I'm wondering what happened with it(plus want to resolve the prediction market) https://manifold.markets/VictorLevoso/will-loss-curves-on-pythia-models-o

**19:06:49 UTC** - #interesting-findings - **seonsmallworldz**
https://x.com/NeelNanda5/status/1866535859757125884

### 2024-12-14

**01:13:31 UTC** - #interesting-findings - **vodros**
Cool new paper from Meta where they group bytes into patches based on entropy before feeding them to the transformer instead of the traditional BPE tokens. It's a real shame they didn't publish the weights because I think it would've been really cool to try training SAEs on the patches. Hopefully they do it at some point
https://ai.meta.com/research/publications/byte-latent-transformer-patches-scale-better-than-tokens/

### 2024-12-15

**05:47:53 UTC** - #interesting-findings - **jager.bomber**
https://arxiv.org/pdf/2412.07947

**20:48:32 UTC** - #interesting-findings - **narmeen** (1 reactions)
https://arxiv.org/pdf/2405.07987 <@270628719503212545> ( paper i was talking about)

### 2024-12-16

**02:16:19 UTC** - #interesting-findings - **jager.bomber**
Whoah looks cool, havent read the paper, but how do they convert the input prompt into the patches?

**02:23:40 UTC** - #interesting-findings - **f3mi**
I've been looking @ late layer sae features, and on average, they are shockingly interpretable

**02:24:33 UTC** - #interesting-findings - **f3mi**
there are plenty of features that promote semantic classes of tokens, not just single vectors

### 2024-12-20

**00:02:55 UTC** - #interesting-findings - **mrgonao**
except the first layers of models (which are bad) I have not found much difference of interpretability along layers

**00:17:01 UTC** - #general - **f3mi**
generally most of the search results return these later layer features, and sometimes i find features in ~20 that do more than just token steering.

**00:17:28 UTC** - #general - **f3mi**
i'm setting the strength to maybe 1x-3x the maximum activation

**00:22:22 UTC** - #general - **mrgonao**
are you on the open source interpretability slack?

**02:04:02 UTC** - #interesting-findings - **vodros**
Sorry I just now saw your message. So they operate on bytes (individual characters), they first train a little transformer on the bytes that they later use to decide on how to group them to form patches by looking at the entropy of the model. Once the grouping have been decided, they use (another?) local transformer that converts the byte embeddings into patch embeddings, and then they have the main transformer operate on the patch embeddings. They also train a local decoder to convert the predi...

### 2024-12-21

**09:51:10 UTC** - #interesting-findings - **razorduck** (1 reactions)
Excited to share new work from my PIBBSS Fellowship with Hardik Bhatnagar and Joseph Bloom on Sparse AutoEncoders! We found that SAE latents aren't always independent - some form clusters that map interpretable subspaces. These clusters often appear in cases of ambiguity (like different meanings of 'how') or appear to form a compositional encoding (like gradients between 'some of' and 'all of'). We observed this in both GPT2-Small and Gemma-2-2b, though clusters become smaller and less common as...

### 2024-12-22

**15:38:14 UTC** - #interesting-findings - **attentionmech**
Hey folks, recently started with neural nets and slowly working towards mech interp. Today just out of a random thought I decided to do a Random walk experiment with open source LLMs and plot the graphs.. mostly everything was expected but gemma2:9b was odd one out of everyone else. I am looking for suggestions on how to proceed with investigating this behaviour. Please check out this github page to see the plots - https://github.com/attentionmech/TILDNN/blob/main/articles/2024-12-22/A00002.md

...

### 2024-12-27

**17:51:44 UTC** - #general - **davidklindt_23547**
I beg to differ 🤓 

https://arxiv.org/abs/2410.21869

### 2024-12-28

**10:39:45 UTC** - #general - **yp_yurilee**
RAVEL: Evaluating Interpretability Metho...

**12:21:39 UTC** - #general - **shivbhatia**
hi folks, hope you're all having a great holiday! I'm organising a mechanistic interpretability hackathon in London on Jan 18-19, if you'll be in town you should come along, DM me for an invite to the discord server. hope to see some of you there 🙂

**14:29:15 UTC** - #interesting-findings - **attentionmech**
the gemma2:2b also has tendency to not actually choose UP and DOWN and mostly go right in initial tempretures. whereas llama models are going up/down more early on. again this is not a theorectically correct / rigorous. description of what is happening => but it seems like either architecture wise / training data wise ---- there was as a delta which caused it. ( do look at the graphs once on the link to see the temp <0.5 for gemma2:2b as well)

**22:34:33 UTC** - #interesting-findings - **burnytech**
potential math behind o1 https://www.youtube.com/watch?v=6PEJ96k1kiw

### 2025-01-01

**01:40:43 UTC** - #interesting-findings - **woog** (2 reactions)
https://x.com/MasonKamb/status/1874120587754561871?t=DBgZEyxmddLEc05mFczeqQ&s=19

### 2025-01-04

**01:36:09 UTC** - #general - **alex083190**
Is anyone aware of a more detailed description about why there is no inclusion of any mech interp in the alignment faking paper by Anthropic? They allude to no methods working well (I assume this is in reference for a cross coder) but why didn’t it work? They clearly call for methods that can detect faking in the model’s activations, so why don’t they build on it? It’s a shame this behaviour is not present in open source models so it cannot be studied independently atm.

I was hoping to see some...

### 2025-01-05

**17:52:36 UTC** - #general - **clemd6d** (1 reactions)
Looks super interesting: https://x.com/a_jy_l/status/1875929881416216760
Models can form in context representations to solve ICL tasks
Cc <@742701213090578482>, seems highly related to your LR stuff

**18:32:14 UTC** - #general - **vodros** (1 reactions)
I remember someone sharing it here. Here is a very quick summary from when I skimmed through it:
- ICL has a direct effect on internal representation
- On a graph problem, representations organize themselves into a structure similar to the graph
- Accuracy increases with context size
- If concepts already have an underlying semantic graph structure (eg days of the week), the ICL graph structure is harder to learn

### 2025-01-08

**12:56:37 UTC** - #general - **matheart**
https://arxiv.org/abs/2412.01003

**20:24:53 UTC** - #general - **yoohoo**
Has anyone tried to do feature visualization with language models the way people have done with convnets?

**20:26:28 UTC** - #general - **yoohoo**
Like you have a deception SAE feature, and you do gradent descent on randomly initialized dictionary vectors, to maximally activate deception feature + standard feature viz tricks. Then argmax over it. Do you get sensible text? Or just like 1 word repeated over and over. Or does it not work at all?

**20:31:08 UTC** - #general - **electrifier123**
feature vis they do some kind of regularization?

**20:53:45 UTC** - #general - **yoohoo**
Because if you did the feature viz the naive way you got these jittery not very good images

**21:34:35 UTC** - #general - **woog**
google pair did this way back in the day on bert https://pair-code.github.io/interpretability/text-dream/blogpost/

**21:53:35 UTC** - #general - **jager.bomber**
These people were able to do it: https://arxiv.org/abs/2402.01702

**21:55:27 UTC** - #general - **jager.bomber**
Also for SAEs: https://www.lesswrong.com/posts/hMBTaFvAzdMNnj29c/evolutionary-prompt-optimization-for-sae-feature

### 2025-01-09

**02:26:56 UTC** - #general - **dex04887**
https://m.youtube.com/watch?v=7a0_iEruGoM&pp=ygUNU3BhcnNlIGNvZGluZw%3D%3D

### 2025-01-10

**18:26:50 UTC** - #interesting-findings - **vodros** (1 reactions)
Nice
https://x.com/GoodfireAI/status/1877777694936694962

### 2025-01-12

**19:55:21 UTC** - #general - **dvvord** (1 reactions)
I would highly recomend this Data Driven Science book and Steven Brunton videos

https://databookuw.com/page-2/page-13/

### 2025-01-14

**14:37:13 UTC** - #interesting-findings - **seonsmallworldz**
https://x.com/AISafetyMemes/status/1795756579742179744

strange

### 2025-01-22

**23:37:34 UTC** - #interesting-findings - **clemd6d** (1 reactions)
> The original datasets consists of 1.4M dialogues generated by ChatGPT and spanning a wide range of topics. To create UltraChat 200k, we applied the following logic:
> 
> Selection of a subset of data for faster supervised fine tuning.
> Truecasing of the dataset, as we observed around 5% of the data contained grammatical errors like "Hello. how are you?" instead of "Hello. How are you?"
> Removal of dialogues where the assistant replies with phrases like "I do not have emotions" or "I don't ha...

### 2025-01-24

**11:51:37 UTC** - #interesting-findings - **pradeep1148**
https://www.youtube.com/shorts/Bip0jH0ARVA

### 2025-01-25

**19:34:18 UTC** - #general - **yoohoo**
Do anyone know if theres any papers on stability of feature directions under training?

**19:35:30 UTC** - #general - **yoohoo**
Like if I take gpt2, find the direction v of a feature I wanna use, then I fine tune it for 10000 gradient steps on some random task, how much does v change?

### 2025-01-26

**14:41:29 UTC** - #general - **yoohoo**
That'd be an example. Are there any papers where people inspect this phenomenon for its own sake? Like look at how stable feature directions are under fine tuning.

**14:44:05 UTC** - #general - **yoohoo**
I could also imagine that they kind of crystallize at some point because, the modules that write to that features, are used for many downstream tasks, so gradient propagation punishes features moving much.

**14:45:01 UTC** - #general - **yoohoo**
Or like some kind of feature geometry, features converge to a locally optimal configuration for reducing interferrence, and just stay there when you continue training.

**14:45:41 UTC** - #general - **yoohoo**
I'm just wondering if theres any papers that would tell me whether these ill-founded speculations of mine are stupid or if any are correct.

**15:30:07 UTC** - #general - **mrgonao**
I don't think there are full-fledged papers out, but maybe there will after the submissions to ICML are public

### 2025-01-27

**20:27:37 UTC** - #general - **pocketperceptron** (1 reactions)
https://publications.apolloresearch.ai/apd

https://fixupx.com/leedsharkey/status/1883904940558500282

### 2025-01-28

**18:42:43 UTC** - #general - **seonsmallworldz**
hey <@102871169362825216> what was your experience working with Apart research?

### 2025-01-29

**02:04:02 UTC** - #general - **seonsmallworldz**
ah thats all good just making sure theres no real red flags (like ip drama,paper stealing,corpo drama,etc)

**02:04:14 UTC** - #general - **seonsmallworldz** (2 reactions)
i mostly am, just there for the compute, help is nice though but the compute is good to get this research off the ground

### 2025-01-30

**21:45:43 UTC** - #general - **tha_jp**
im trying to find some direction in the field, new to it. read some of the papers on nandas list and also the newest survey from the apollo team

### 2025-01-31

**01:09:47 UTC** - #general - **tha_jp** (1 reactions)
to answer your question: yes
also, i mainly want a second well respected lit survey so that i can cross reference citations to see what papers are foundational . i find literature review daunting and i would like to minimize reading time if that makes sense. but as i think about it, i realize that there is a better option where i just try and implement some follow up work on a recent paper mentioned in the survey.

**09:02:53 UTC** - #interesting-findings - **burnytech** (2 reactions)
https://fxtwitter.com/chrisbarber/status/1885047105741611507

**09:02:55 UTC** - #interesting-findings - **burnytech**
Reverse engineering of the reasoning models DeepSeek is emerging!
They apparently found a backtracking vector "that when applied, caused the chain of thought to backtrack much more often, and when suppressed caused it to be a linear and much shorter CoT"!
And they think that sparse autoencoders will find similar features that are general "functions" the model has learned for reasoning that you can they explicitly steer, manipulate, edit etc., like backtracking, forking, reflection, selfcorrectio...

**16:42:20 UTC** - #interesting-findings - **mukyuu123** (1 reactions)
https://arxiv.org/abs/2501.15740

### 2025-02-05

**15:18:59 UTC** - #general - **fieryvictorystar** (1 reactions)
https://x.com/thesubhashk/status/1887138694546788556?t=Wjrwg_U6VStTBHiPzv6Hfg&s=19

### 2025-02-06

**16:48:00 UTC** - #interesting-findings - **jerrychatz**
https://arxiv.org/abs/2501.17727

**17:24:03 UTC** - #interesting-findings - **electrifier123**
do they talk about the towards monosemanticity paper at all?

**17:30:12 UTC** - #interesting-findings - **electrifier123**
https://transformer-circuits.pub/2023/monosemantic-features#global-analysis-about-model

**17:52:37 UTC** - #interesting-findings - **mrgonao**
I don't think it contradicts it. They show that the random model is interpretable as well, as long as you don't ignore the "single token" features

**17:53:39 UTC** - #interesting-findings - **electrifier123**
so it's just saying that there are qualitatively different features associated with random transformers vs trained transformers

**17:55:56 UTC** - #interesting-findings - **electrifier123**
I am curious what attention heads look like for random transformers. Like my guess is they attend uniformly by default? But I guess it would depend on magnitude of the weights

**17:58:23 UTC** - #interesting-findings - **mrgonao**
Yeah, I think the paper is saying "we should be careful about looking at just raw interpretability scores and you need to look at the quality of features"

**18:14:49 UTC** - #interesting-findings - **juanchas** (1 reactions)
I mean, something like penalising for learning "single token" features, although that may not be a good idea

**18:15:28 UTC** - #interesting-findings - **mrgonao**
https://www.lesswrong.com/posts/P8qLZco6Zq8LaLHe9/tokenized-saes-infusing-per-token-biases

### 2025-02-09

**22:14:53 UTC** - #general - **jager.bomber** (1 reactions)
@here Hey everyone! I'm organizing a virtual Distill meetup next Friday (Feb 14) 11.30am ET - 1pm ET to bring people who are doing, have done, or just like Distill style articles and blog posts, and using visualization for communicating science in general (eg 3Blue1Brown videos). If this interests you and you are available to join, please react to this post and I'll send you the invite! In case you cannot join, here's a meeting notes doc that we'll fill out with resources before the meeting.
htt...

### 2025-02-11

**19:34:48 UTC** - #general - **tha_jp**
Even some resources or papers that talk about this would be good.

### 2025-02-12

**13:55:15 UTC** - #general - **iz0950**
Gm all,

If I want to build up knowledge about audio models (transcription, generation etc) what foundational papers or concepts should I be looking at ? Looking to learn ideas from the beginning that are still relevant. Especially interested if there any new ideas that I won’t see in language or vision.

### 2025-02-16

**16:02:26 UTC** - #general - **firstuserhere** (1 reactions)
This is the list of papers i've found the most useful for getting up to SOTA. Just read them, talk to models, follow up on references, etc and you should catch up soon


- https://arxiv.org/abs/2107.03312

- https://arxiv.org/abs/2011.10650

- https://arxiv.org/abs/2309.15505

- https://arxiv.org/abs/2010.02193

- https://arxiv.org/abs/2210.13438

- https://arxiv.org/abs/2104.00355

- https://arxiv.org/abs/2305.13009

### 2025-02-17

**17:31:42 UTC** - #general - **narmeen** (1 reactions)
Hi everyone,
I'm compiling a comprehensive assessment of mechanistic interpretability tooling, evaluating them on key criteria like faithfulness and scalability. The goal is to identify areas where our current tools could be improved.
I've started documenting various tools and their characteristics here: https://docs.google.com/spreadsheets/d/17BwBlHKnGho5KG_0B2Sla7SAOTN4rOrHAGgHzf9fcVQ/edit?gid=0#gid=0 
I'd appreciate input from the community on: 

- Additional tools that should be included
- E...

**17:48:30 UTC** - #general - **mrgonao**
I don't know if you want comments here or there. I think I disagree with your definition of scalable (at least in the way you apply it to delphi, which is the one I know most about).
 Because latent auto-interpretation is infinitely parallelizable (you can explain each latent independently) you only care about the cost per latent explanation, which is close to $700/100k latents - which is low if you are not an independent researcher.
 In fact, if you only care about speed and have money to do th...

**22:13:19 UTC** - #general - **narmeen**
Yes anything you think should be part of the toolkit of researchers

### 2025-02-20

**02:27:48 UTC** - #general - **fieryvictorystar**
https://x.com/BartBussmann/status/1889338359887126682?t=A6aKTILtM1CBUxe4FvHTMA&s=19

**02:28:26 UTC** - #interesting-findings - **fieryvictorystar**
https://x.com/BartBussmann/status/1889338359887126682?t=A6aKTILtM1CBUxe4FvHTMA&s=19

### 2025-02-21

**08:41:44 UTC** - #interesting-findings - **clemd6d** (1 reactions)
Cool paper:
https://x.com/MikaStars39/status/1892777331909153264?t=jwG-90zKD3DM_Ux9kWIuvw&s=19

**16:55:51 UTC** - #interesting-findings - **jh_lim131**
Time circuit 

https://arxiv.org/pdf/2502.14258

### 2025-02-22

**01:26:57 UTC** - #general - **eduardoslonski** (1 reactions)
https://arxiv.org/abs/2412.01014

**01:26:58 UTC** - #general - **eduardoslonski** (1 reactions)
https://x.com/EduardoSlonski/status/1893070333831205000

**17:10:19 UTC** - #welcome - **Carl-bot**
Hello attentionmech, welcome! 👋 You are the 1,855th member to join 🥳

### 2025-02-23

**00:41:37 UTC** - #interesting-findings - **xpkcs** (3 reactions)
hello! I'm training crosscoders and got some interesting results to share

These plots compare the baseline crosscoder recipe from Anthropic's original post vs. the Jan 2025 update that adds JumpReLU. jumprelu performs worse because of low # of firing latents - the pre-act Lp terms penalizes nonfiring latents
- blue: baseline
- pink: jumprelu

__details:__
- dataset: tiny stories
- model: tiny stories 33M (4 layers x 768 model dim)
- crosscoder dim: 16384
- # tokens: 10M 
- training objective: i...

### 2025-02-24

**10:08:39 UTC** - #general - **tomasruiz2301**
Hi! Anybody else working on a submission for the CVPR workshop on mechanistic interpretability for vision models? Would love to have a conversation and exchange feedback. Workshop link: https://sites.google.com/view/miv-cvpr2025/

### 2025-02-25

**08:08:42 UTC** - #interesting-findings - **tl.kim_58258**
https://arxiv.org/abs/2502.08524

Knowledge distillation with predicting which SAE latent should fire.

**23:44:23 UTC** - #interesting-findings - **jbcoo**
https://x.com/OwainEvans_UK/status/1894436637054214509
that one's actually crazy

### 2025-02-26

**22:51:45 UTC** - #interesting-findings - **seonsmallworldz** (1 reactions)
https://x.com/lucyfarnik/status/1894764023809286414

**22:54:28 UTC** - #general - **seonsmallworldz**
https://www.lesswrong.com/posts/FrekePKc7ccQNEkgT/paper-jacobian-sparse-autoencoders-sparsify-computations-not

### 2025-03-02

**21:35:47 UTC** - #general - **mrgonao**
Maybe this https://arxiv.org/abs/2501.16496

### 2025-03-03

**15:25:22 UTC** - #general - **yoohoo**
Hmm, what is the current view of SAEs and features?

**15:25:34 UTC** - #general - **yoohoo**
Do big enough SAEs find all the features?

**15:26:07 UTC** - #general - **yoohoo**
I'm confused, like if you have a attention head output something interpretable, that plays a role in a circuit you've found.

**15:26:35 UTC** - #general - **yoohoo**
Will a big enough sae find features that decompose the subspace that attn head is writing to always?

**15:29:21 UTC** - #general - **electrifier123**
Yes just take d_voc^(n_ctx) features

**15:33:16 UTC** - #general - **yoohoo**
Like my intuition is that LLMs do computation using sparse feature circuits, and that the features / "variables in said circuit" can be found by SAEs or similar techniques

**15:34:47 UTC** - #general - **electrifier123**
There's been some work looking for sparse circuits that has been relatively successfull, with transcoders

**15:35:17 UTC** - #general - **mrgonao**
no (and that is not a well defined question because "all the features" is not well defined). A big enough SAE would potentially learn all the datapoints (if trained on the data multiple times), which is definitivelly not all the feature

**15:36:41 UTC** - #general - **yoohoo**
Yeah, but like, do you know of any evidence that either.

1. **All** variables in circuits are linearly represented
1.1. **All** such "variables" can be found by SAEs or similar
or
2. There is a circuit whose features are convincingly demonstrated to not be linear or not to be found by any kind of SAE

**15:38:54 UTC** - #general - **electrifier123**
Where there was a ground truth circuit

**15:39:10 UTC** - #general - **mrgonao**
There is evidence that there are features that are represented by more than one direction (so they are linear but not 1-d: https://arxiv.org/html/2405.14860v1) Maybe Josh would like to say more aboyt that

**15:40:53 UTC** - #general - **mrgonao**
there were probing results. I don't think anyone has ever produced a ground truth circuit on something that is not Tracr

**15:42:13 UTC** - #general - **yoohoo**
Do saes find output of OV copy circuits?

**15:42:42 UTC** - #general - **electrifier123**
Wdym by an OV copy circuit?

**15:43:43 UTC** - #general - **electrifier123**
Well SAEs aren't trained to find dense transformations. So they will learn features so each of the possible tokens, and each of those features will boost themselves and act as copying, but it won't be able to learn "copies"

**15:45:42 UTC** - #general - **yoohoo**
Doesn't that mean the "Sparse feature circuits explains all LLM behavior" is almost certainly false?

**15:46:26 UTC** - #general - **yoohoo**
Hmm, I am confused about this. Do you know any good papers I can read talking about this and related issues?

**15:48:31 UTC** - #general - **electrifier123**
But you can look at lots of SAE features and spot patterns and maybe hypothesize about what a component as a whole is doing based on the featura

**15:49:31 UTC** - #general - **electrifier123**
Yeah exactly so you can get an idea for what a component is doing based on it's features.

**15:50:32 UTC** - #general - **electrifier123**
Like you don't see an induction head feature. But you see lots of features that seem to activate as induction for particular tokens.

**15:51:25 UTC** - #general - **yoohoo**
What do you mean "lots of features that seem to activate as induction for particular tokens"?

**15:51:55 UTC** - #general - **yoohoo**
Like one feature that activates on an example the induction head would've activated on, and that has the same downstream effect as the induction head would've had on that example?

**15:52:28 UTC** - #general - **electrifier123**
https://robertzk.github.io/gpt2-small-saes/cards/top_features_6_9.html#feature_num_19625

**15:52:44 UTC** - #general - **electrifier123**
These are SAE features for a known induction head

**15:53:37 UTC** - #general - **electrifier123**
And the orange represents the current token. The blue represents what token gave rise to the current features. Notice it's always the b in smth of the form "a b .... a" that is blue

**15:55:16 UTC** - #general - **electrifier123**
No this was work done by some MATS scholars https://www.alignmentforum.org/posts/xmegeW5mqiBsvoaim/we-inspected-every-head-in-gpt-2-small-using-saes-so-you-don

### 2025-03-04

**12:12:41 UTC** - #interesting-findings - **adr.skapars**
https://arxiv.org/abs/2410.20035 Interesting paper! (Not mine). Sending in case its under peoples radar, seems relevant to interpretability and training dynamics.

### 2025-03-05

**07:41:49 UTC** - #general - **clemd6d**
i meant for a specific feature

**09:33:17 UTC** - #general - **electrifier123**
I think the original towards monsemanticity paper mentioned that there is a transition point between "true features" of the model and when it starts just finding properties of the dataset.

**09:34:12 UTC** - #general - **electrifier123**
"true features" I guess is hard but you can find neurons which are monosemantic where it's pretty incontestable that the model is using that feature internally

**09:36:22 UTC** - #general - **electrifier123**
I've found arguments about features boosting their own logits/representations unconvincing because it can easily be explained by a dense transformation.

**11:12:25 UTC** - #general - **unnamed8802**
my viewpoint was based on that the current SAE architectures primarily use reconstruction loss only, to evaluate the performance of the SAE and not the performance on the downstream task, that is why they primarily learn data features and not features learned/used by the model ... josh's recent tweets basically talks about it in detail.. 
https://x.com/JoshAEngels/status/1896943919675662376?t=k0nvh-ftc6eIo5LwPduKwQ&s=08

**13:06:38 UTC** - #general - **electrifier123**
My main gripe with SAEs is that I just don't think it's mech interp anymore. It's depressing how few mechanistic insights into models have emerged since induction heads say.

**13:10:19 UTC** - #general - **electrifier123**
Like one question that I haven't seen investigated anywhere, is can you give a mechanistic explanation for how SAE features, even some early ones, are computed by the model.

**13:35:43 UTC** - #general - **mrgonao**
Have you read the sparse feature circuits paper?

**15:37:49 UTC** - #general - **electrifier123**
The ideal is a form for the SAE feature in terms of the input sequence itself, as a ground truth. I am much more thinking do this for the first layer, than anything that you can auto scale.

**15:52:06 UTC** - #general - **electrifier123**
Given an SAE feature in the first layer, find some simplified form for the computation the model performs to get the SAE feature, which allows you to reason about how the SAE feature will act off train distribution

**17:50:04 UTC** - #general - **mrgonao**
Well if you have a sae or transcoder on the mlp and on the attention you can start to answer that

**23:15:10 UTC** - #general - **tha_jp**
cool tool by the frog on X
https://github.com/doomslide/attention-graph

**23:17:20 UTC** - #general - **tha_jp**
https://x.com/doomslide/status/1897349668058927249

### 2025-03-09

**16:56:44 UTC** - #general - **seonsmallworldz**
https://lu.ma/guiyjbf9

### 2025-03-12

**14:34:15 UTC** - #general - **jager.bomber** (1 reactions)
@here Hey everyone, our Distill meetup was pretty successful and there was enough interest that we have started a monthly Distill meetup! The next one is this Friday, March 14 11.30-1pm ET. Please have a look at this summary meeting doc for more details: Exploring Explainables Reading Group (https://docs.google.com/document/d/1Hhd5onku9IcLUT5tHtifvb4aF7aDXIxJtU4oLIrNeb8/edit?tab=t.j50n7nkrp9yn#heading=h.ew6mldlb8qym)

### 2025-03-14

**21:47:49 UTC** - #general - **tha_jp**
in short im trying to use SGD to optimize an embedding vector for SAE activation but the gradient chain is breaking. I'm not sure if there is a way around this

### 2025-03-15

**12:10:55 UTC** - #general - **tha_jp**
If you mean set up a manual computation, yes that is a last resort but I was specifically wondering if patching in activations breaks the graph for backprop in torch. Not very good at coding or familiar with the libraries at the lower level.

### 2025-03-17

**05:14:00 UTC** - #welcome - **cherie_arjun**
Hello 🙂 I am Mallikarjuna, grad student at RIT and Researching on Model stitching and Mech Interp

**10:34:17 UTC** - #welcome - **Carl-bot**
Hello attentionmech, welcome! 👋 You are the 1,894th member to join 🥳

**12:01:42 UTC** - #general - **whimsical_mango_31409**
Hello Everyone......I have just enrolled in my PhD and want to do some research in MI field and need some guidance to get started.....Should we be using any specific tools for MI for interpretation and visualization purposes? While I have gone through the various papers but from a practical implementation needed some help on the tools and techniques

### 2025-03-20

**11:37:17 UTC** - #general - **imai_87834**
hi all, wanted to find out what this question really asks, " pieces of evidence that you'd be able to do good research in this stream?" do i talk about my experience?

**15:51:22 UTC** - #general - **cohlem**
Can anyone put me in a right direction? I've been experimenting with instruction-tuned models to see if I can find any circuits for these models but I've been unsuccessful so far. All the paper where authors find circuit for their task for instance, IOI and greater than task all use base-models, and the they analyze simply the next-token using path patching, the patching process is also straightforward since they only need to patch the ending tokens to see the causal effect. 

My problem is my o...

**16:55:33 UTC** - #interesting-findings - **currentlystillasleep**
https://arxiv.org/pdf/2503.13395

### 2025-03-21

**01:40:35 UTC** - #interesting-findings - **seonsmallworldz**
https://x.com/leedsharkey/status/1902705855142789584

**03:31:42 UTC** - #general - **fieryvictorystar**
This is somewhat interesting .
So basically the problem here is that you aren't really running the model just once but the 5 is the result of a long conputation that goes though multiple times trough the model right?.
I feel like what you should do is try patching on diferent parts of the cot.
Maybe you should first try to figure out how the model outputs the first 4 patching stuff on the earlier positions.
You can also in fact later see if the earlier 5 is just being copied .
I feel like if you...

**05:03:37 UTC** - #general - **cohlem**
Thank you very much for the insights <@128268156459286528> I'll try path patching at these intermediate positions.

Another thing I need help with is with the tokenizers. I've found most math-finetuned models to have tokenizers that tokenize numbers to one token, for instance, 234 to 3 separate tokens and my tokenizer also behaves the same.

I'm calculating logit difference to measure the causal effect, and I don't know what I should be measuring if the answers are two tokens, 

Lets say if have...

**06:34:08 UTC** - #general - **sheikheddy** (1 reactions)
Overheard hot take, “mechanistic interpretability is just a branch of linguistics”

**10:06:07 UTC** - #general - **mrgonao**
What do you mean generalize here? Detect hallucinations in contexts that are not the ones they were trained on? I feel like I've seen several hallucination papers, but not sure if they use probes normally

**14:34:29 UTC** - #general - **jithesh336**
Yes. That is what the paper suggested "This suggests these probes may be identifying not truth,
but other features that correlate with truth on their training data."

**14:36:40 UTC** - #general - **jithesh336**
The paper had Animals, Cities, Companies, Elements, Scientific Facts, and Inventions datsets. Each dataset contains a minimum of 876 entries, with a balance of true and false statements.

**18:13:29 UTC** - #general - **fieryvictorystar** (1 reactions)
https://x.com/NeelNanda5/status/1903147294465155196

### 2025-03-25

**23:14:55 UTC** - #interesting-findings - **electrifier123**
https://arxiv.org/abs/2409.15318 idk if people have sent this paper before, I thought it was really cool. Uses a simple counting argument to get a lower bound on the parameters needed for computing in superposition

### 2025-03-26

**22:58:43 UTC** - #general - **seonsmallworldz**
https://x.com/NeelNanda5/status/1904988240542834724

### 2025-03-27

**09:44:17 UTC** - #general - **neelnanda** (1 reactions)
I like cross coders for model diffing, though I think there's some improvements there that we'll hopefully have a paper out on soon. Cross coders on a single model do not substantially change that my position on "SAEs are less exciting than I'd hoped" and I include things like cross coders and transcoders in that statement

**13:34:16 UTC** - #general - **jasonrichdarmawan**
Hi Neel, if you don't mind, do you suggest newcomer to learn SAEs or learn something else?

By newcomer, I mean, (1) someone with a knowledge limited to Andrej Karpathy's video on how to pretrain GPT-2 124M model, and how to build an autograd, and ( 2 ) don't know anything about mechanistic interpretability.

I do see another mechanistic interpretability tool is being developed at MATS Summer 2025. The deadline to apply is very close. In other words, if you don't mind, and could you please guide...

**17:33:26 UTC** - #general - **nedflacosyndiam**
https://transformer-circuits.pub/2025/attribution-graphs/methods.html

**17:37:30 UTC** - #general - **nedflacosyndiam**
https://transformer-circuits.pub/2025/attribution-graphs/biology.html

**17:46:27 UTC** - #general - **mrgonao**
these examples are also used to collect feature activations, so I don't think it is unfair

**18:17:39 UTC** - #general - **fieryvictorystar**
https://x.com/yifeiwang77/status/1905259845583843546

**18:21:02 UTC** - #general - **fieryvictorystar** (1 reactions)
next reading group is <@917902468048879657>'s paper since he wanted to present it and thats when hes avaliable. But the one after that sure. Also taking this as an opportunity to check josh is actually available to put it on the calendar and anounce it on the reading group channel.

**18:44:08 UTC** - #general - **fieryvictorystar**
Also didn't get to that part on todays reading group but Josh's paper https://openreview.net/forum?id=IT5fRjnGr0 seems relevant for the  "Removing High Frequency Latents from JumpReLU SAEs"  section of deepminds latest post https://www.alignmentforum.org/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks as is evidence of the hypotesis that high frequency latents represent meaningful directions in activation space that we just haven't been able to interpret yet.

**19:25:33 UTC** - #general - **joshengels**
Still good for next week, but also happy to do the week after if you want to do the anthropic paper next week

**20:04:15 UTC** - #general - **fieryvictorystar**
https://x.com/AnthropicAI/status/1905303835892990278

**20:05:09 UTC** - #general - **fieryvictorystar**
this is the antropic paper we are talking about in case other people havent seen it yet.

**21:58:42 UTC** - #general - **neelnanda**
Oh thanks! I know of the paper, but didn't know it was publicly accessible yet, so we didn't cite it

**21:59:32 UTC** - #general - **neelnanda**
I recommend the ARENA curriculum https://arena3-chapter1-transformer-interp.streamlit.app/

### 2025-03-28

**03:05:38 UTC** - #general - **burnytech** (1 reactions)
and more concrete links
https://www.anthropic.com/research/tracing-thoughts-language-model
https://transformer-circuits.pub/2025/attribution-graphs/methods.html
https://transformer-circuits.pub/2025/attribution-graphs/biology.html

**15:05:56 UTC** - #general - **nedflacosyndiam**
I know you did auto-interp - but did you ever have the suspicion that perhaps the auto-interp process was actually backward?   that is, maybe it would be better to ask models to "explain" their outputs, and then use those text  "explanations" (or rationalizations) to construct linear probes which would predict the explanation or explained behavior?    I've been doing a lot of this "inverse" prompting, and while I'm quite sure that preference tuned models are just telling you a story that sounds ...

**23:01:28 UTC** - #general - **pzhao.**
why do we expect the sae to perform better than the linear probe ? I mean the sae is just a approximation of the orginal signal, albeit with some features identified (however, we can't expect those features to be complete and relevant for our downstream task)

### 2025-03-29

**07:51:30 UTC** - #general - **pzhao.**
maybe they do, but you need to guide them. like in here:

https://transformer-circuits.pub/2024/september-update/index.html#oversampling

**07:52:26 UTC** - #general - **pzhao.**
also, im not sure if this has been mentioned but they show contrary results:

https://transformer-circuits.pub/2024/features-as-classifiers/index.html

**08:56:30 UTC** - #general - **electrifier123**
But at the point you're assembling specialised datasets, why wouldn't you just use a linear probe? Generally you expect the more feature splitting occurs, the less robust your features will be ood, because features correspond to fewer samples.

**13:20:42 UTC** - #general - **juanchas** (1 reactions)
I feel like the questions is really if we want to develop models (like SAEs) that are interpretable and also good at downstream tasks. Like, sometimes it feels like we are hoping that internals of the LLMs work the same way our "reasoning" works but really our reasoning (like how we identify a dataset for malicious intent) might be coming out of a really complex model similar to an LLM. 

Just my 50 cents, SAEs work at internal level but whenever we are probing for a manually built dataset we ar...

### 2025-03-30

**10:25:14 UTC** - #general - **neelnanda** (1 reactions)
You also may find this exchange interesting https://www.alignmentforum.org/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks?commentId=borgejNSWXbtWDMc7

### 2025-03-31

**15:16:29 UTC** - #general - **jh_lim131**
https://www.lesswrong.com/posts/wGRnzCFcowRCrpX4Y/downstream-applications-as-validation-of-interpretability

**20:32:48 UTC** - #general - **rictoo**
Hi all! I've been reading the "Toy models" paper by Anthropic (not yet finished it), but I have a question:

**20:34:44 UTC** - #general - **rictoo**
Why is sparsity necessary if representation vectors are nearly orthogonal, following the JL lemma? Wouldn't the features (that ideally would be represented within a higher dimensional space) be able to be fully recovered, since the representation vectors (in the lower dimensional space) are nearly orthogonal?

### 2025-04-01

**20:51:08 UTC** - #general - **morgan_sinclaire**
There are 2 separate mechanisms for implementing superposition: JL and sparsity, which can be studied separately. For example, JL only applies in high dimensions, but this figure is in R^2.

Here, on the right, there is substantial interference between features. But that's ok since at 90% sparsity, the probability of any 2 co-occuring is 0.1^2 = 1%. 

Whereas at low sparsity on the left, the model can't use this mechanism either, so it elects to only represent 2 of the 5 features.

(I'm not an e...

### 2025-04-04

**21:38:05 UTC** - #general - **installjohn2**
A lot of the mats mentors have "desire to publish a paper" in their desired mentee characteristics. Is there really anyone who doesn't want to publish a paper? Or, is this a coded way of saying something like "desire to finish under conference deadlines even if it means shipping a less complete paper," or "desire to publish small papers every few months instead of less frequent big papers?"

### 2025-04-05

**17:14:14 UTC** - #general - **alextmjugador**
I mean, in real research positions you have to publish papers, so you better desire doing it 😅

### 2025-04-06

**01:22:39 UTC** - #general - **nihilisticneuralnet** (1 reactions)
found this interesting diagram mapping brain and AI capabilities in https://www.arxiv.org/abs/2504.01990

### 2025-04-07

**10:05:43 UTC** - #general - **neelnanda**
Yes, there's a moderate amount of people (especially in the early days of MATS) who think papers are a somewhat silly institution, not worth the effort, they only care about learning, etc. in fairness, I think there's a lot of truth to these concerns, but it's typically still better to encourage my scholars to do it

**11:14:48 UTC** - #general - **alextmjugador**
Out of curiosity, why do you think it's better to give such encouragement to scholars? Because of the external social factors that encourage paper publication (funding allocation, etc.), because of how the process of actually having to sit down and do a coherent formal writeup can be helpful for developing soft skills related to e.g. idea expression and communication, a mix of both, or something else?

**15:28:38 UTC** - #general - **neelnanda** (1 reactions)
Good for their careers, good to practice communicating their research well, an incentive and deadline to do the boring bits of rigor and good communication

**22:53:27 UTC** - #general - **jh_lim131**
what about a good paper can an aspiring blog post learn from and vice versa?

### 2025-04-08

**07:20:39 UTC** - #general - **jager.bomber** (1 reactions)
@here Hi everyone! This month's Distill reading group (now called Exploring Explainables reading group) is happening this Friday from 10.30am ET/15:30pm UK time to 12.00am ET/17:00pm UK time. Hope you can make it (new faces are most welcome!) More details in the doc: https://docs.google.com/document/d/1Hhd5onku9IcLUT5tHtifvb4aF7aDXIxJtU4oLIrNeb8/edit?tab=t.1phib5rg0mya#heading=h.i4lb3y3qj2uk

**22:19:46 UTC** - #general - **fieryvictorystar**
https://x.com/JeffLadish/status/1909685895743389808?t=qwPhqIGByDV0wiRjY1QXpg&s=19

### 2025-04-11

**14:25:25 UTC** - #general - **jager.bomber** (1 reactions)
@here Distill meetup happening in 5: https://harvard.zoom.us/j/97231146625

**16:16:01 UTC** - #general - **fieryvictorystar** (1 reactions)
https://youtu.be/_KoUcwCoID4?si=FDlNRGMibVFQz3lB

### 2025-04-12

**08:33:05 UTC** - #general - **burnytech**
Since circuits inside LLMs like Claude 3.5 Haiku are different than what LLMs say when asked to explain how they got to an answer, I suspect the same holds for the models in the new reasoning paradigm. Someone needs to do graph attribution mechanistic interpretability on the reasoning models as well! I bet Anthropic will release something like that soon.
(context: https://transformer-circuits.pub/2025/attribution-graphs/biology.html )

**08:44:34 UTC** - #general - **mrgonao**
I have an hard time with this line of thought. What should the circuit of addition look like? If you say you do addition in some way, and you look at the connectosome in your brain, is it one to one?

### 2025-04-13

**06:45:40 UTC** - #general - **jh_lim131**
you’re probably right about the lack of one to one relationship between behavior and circuit. Even slightly varying the order of a few tokens or injecting a token results in slightly or very different circuits.

The limitation (section 14) of the blog mentions the circuits are for a single prompy

**23:34:04 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/pdf/2503.11742?

### 2025-04-14

**10:17:37 UTC** - #interesting-findings - **clemd6d** (1 reactions)
For people like me too lazy to open a pdf: https://arxiv.org/abs/2503.11742?

**12:06:47 UTC** - #general - **talhaklay** (1 reactions)
🚨 Call for Papers!

The First Workshop on 𝐀𝐜𝐭𝐢𝐨𝐧𝐚𝐛𝐥𝐞 𝐈𝐧𝐭𝐞𝐫𝐩𝐫𝐞𝐭𝐚𝐛𝐢𝐥𝐢𝐭𝐲 will be held at ICML 2025 in Vancouver!

📅 Submission Deadline: May 9
Website >> https://actionable-interpretability.github.io/

We’d love to see folks from this server submitting papers and joining us at the workshop!

### 2025-04-15

**07:35:13 UTC** - #general - **irmaheithoff** (1 reactions)
Call for Participants – eDIF in Cooperation with NDIF

We're testing a shared infrastructure for mechanistic interpretability research in Europe.

🚀 Access includes:
*Open-source models 
*High-end GPUs (A100, L40)
*Full access to model internals via NDIF + NNsight (PyTorch)
*A private researcher Discord for support & exchange
*No restrictions on how results are used — free research resources

🗓️ ~4-week pilot starting early May
👥 For EU/UK/CH-based researchers working on model internals
📅 Apply ...

### 2025-04-19

**06:46:08 UTC** - #interesting-findings - **jh_lim131** (1 reactions)
https://arxiv.org/pdf/2504.03933

### 2025-04-23

**20:46:18 UTC** - #general - **rorroart**
Hey Guys! 

I took the MATS code signal yesterday, and encountered a weird issue where my changes in the code were not being saved and I was unable to progress in the assignment. I notified the applications team, but have not had any response. Is there someone here who can assist me or discuss what to do with me?

Not sure if this is the right place to ask, and would be happy to delete and move if so. I’m just a bit concerned this might hurt might chances of progression in the selection process.

### 2025-04-24

**09:32:35 UTC** - #general - **keryacine**
Hello <@1340742405783158845>, same for us, we saw the announcement a bit late and sent the application yesterday. But the experimentation seems exiting indeed!

### 2025-04-25

**17:48:52 UTC** - #general - **c4tm4nd00**
I have worry that there is not enough auditing/criteria evaluation in considering additional features pertaining to algorithmic constraints and hardware constraints regarding cost to scale. I don’t really see that discussed in the majority of ML focused servers

### 2025-04-26

**14:37:13 UTC** - #interesting-findings - **paranoidhumanoid**
https://arxiv.org/abs/2410.13821

### 2025-05-05

**15:04:54 UTC** - #general - **firstuserhere**
Hey, can someone here endorse me for cs.LG or cs.AI on arxiv?

**15:52:06 UTC** - #general - **ethanc8**
is there a good overview of current open problems in mech interpretability, and of recent progress? (the latest reviews I can find are from fall 2024)

**15:59:06 UTC** - #general - **joshengels** (1 reactions)
https://arxiv.org/abs/2501.16496

### 2025-05-06

**02:16:28 UTC** - #general - **fieryvictorystar** (1 reactions)
Been thinking about how this seems to be an example of how work on toy problems actually does gives us insights into LLM internals.
 https://x.com/thesubhashk/status/1887138694546788556?t=AlWw7wufXQ40OfWIoFXUew&s=19


I was starting to think It wouldn't and actually It might just be better to  just focus on LLM directly but maybe not ?.

Also wondering how much this is related to the example on the recent  Antropic paper about adition , I haven't actually undertood that one yet and will need to ...

**02:36:12 UTC** - #general - **fieryvictorystar** (1 reactions)
Mmm is there any other examples? 
A problem might be that we just don't have a lot of reverse engeniered toy models to extrapolate in general .
Like  are there even any that Isn't the modular addition thing , orthello , my graphs paper, the mazes stuff ?.

**10:49:28 UTC** - #general - **firstuserhere**
It's just having submitted 3+ papers in one of the cs. Fields in the last 5 yrs

### 2025-05-10

**13:46:46 UTC** - #general - **jasonrichdarmawan** (1 reactions)
From the MATS Open House, I heard that a score of 400 is considered not a good fit, while 500 is considered a good fit. According to Egg Syntax, the acceptance rate is around 3%, with over 1,100 applicants for MATS Summer 2024, that’s about 36 applications per stream on average

So, for mentors who require a CodeSignal score, that’s a significant filter, it’s a big deal for mentees

I scored 420. That said, I was working as a Angular Developer before I am pursuing a Master’s degree at a research...

### 2025-05-11

**12:20:12 UTC** - #general - **alextmjugador**
All these CodeSignal assignments and many developers still don't know how to use Git features that help loads with collaboration like branching, rebasing, rerere, or conflict resolution properly

**12:32:04 UTC** - #general - **alextmjugador** (2 reactions)
> Felt I am not cut it for the new world. I mean, I just left the industry 8 months ago, do I lose all that skill already? Maybe I can improve myself before MATS Winter 2025
With all due respect, I don't think that is the most proper way to feel due to those results.

CodeSignal and other similar platforms are ways to filter many candidates into smaller sets which are thought to be worth investing more time into assessing more deeply. That's what their marketing sells: time savings for recruitme...

### 2025-05-12

**04:56:43 UTC** - #general - **millander** (1 reactions)
I bombed my first CodeSignal around a year ago (420 score) when interviewing with Anthropic. I recently scored a 520 when interviewing for a fellowship. The most salient difference in my interview prep between both times was that I focused on maximizing sleep in the week leading up to the challenge deadline. You must be super alert since misinterpreting a requirement or a subtle bug can set you back. The broader lesson is that sleep/health is super important for coding and research.

**09:30:07 UTC** - #general - **clemd6d**
Do you have terabytes of storage to save activations?

### 2025-05-13

**09:39:43 UTC** - #general - **clemd6d**
I put the one I know in this gdoc https://docs.google.com/document/d/1YLSl6BVMNIYxWPQ2jglsB7t7Ch4ztCUPuOTGb4uggdg/edit?usp=drivesdk

**09:57:50 UTC** - #general - **alextmjugador** (1 reactions)
Now, for a research result to be reproducible accross execution environments, you'll probably not want to make one of your critical steps rely on very specific and decidedly variable ways data structures are laid out on memory. But realistically, much research code is already a pain to make portable to anything else than the specific machine it was made to work with, and you can just rely on such things for non-critical performance optimizations, so it can be fine

### 2025-05-15

**08:39:51 UTC** - #general - **gsarti** (1 reactions)
The 8th edition of [BlackboxNLP](https://blackboxnlp.github.io), the leading workshop on on interpretability and analysis of neural networks for NLP, will be co-located with EMNLP 2025 in Suzhou this November! 📆

This year's edition will feature a [new shared task](https://blackboxnlp.github.io/2025/task) on circuits/causal variable localization in LMs using the recently released [MIB Benchmark](https://mib-bench.github.io/) (submission deadline: August 1st)

Have a look at our website for more ...

**18:20:12 UTC** - #general - **alextmjugador**
<@128268156459286528> didn't you technically wrote mech interp papers?

**23:46:57 UTC** - #general - **seonsmallworldz**
though tbh realistically they're around the same level; just its slightly harder to go from engineer to lead research than it is from researcher to engi

### 2025-05-16

**16:20:42 UTC** - #general - **seonsmallworldz**
but would be important to do stuff soon; im expecting a lot of residuals from people who didnt get in to MATS since i know the PI's are directing them to spots online

**16:42:18 UTC** - #general - **seonsmallworldz**
(there are some other reasons i've heard from 1 on 1's notably coupling discord with casual stuff rather than research communities on discord being a real thing; or usual research communities are hard to get into etc)

**16:45:23 UTC** - #general - **fieryvictorystar** (1 reactions)
This is ironic in ML cause actually eleuther has more citations and is more important  than almost any other org .

**16:46:43 UTC** - #general - **seonsmallworldz**
yeah, general public's knowledge of academia is universities (eg i need a phd to do research thinking etc)

**16:47:11 UTC** - #general - **seonsmallworldz**
compsci knowledge of research is almost the same- its why most people fresh out of bootcamp goes into entrepreneurship/jobs

**16:47:12 UTC** - #general - **seonsmallworldz**
not research

### 2025-05-17

**08:28:21 UTC** - #general - **daksh.mor**
why do not we try to apply gradient ascent in transformers, like we do in CNN's (feature visualization) ?

**08:59:43 UTC** - #general - **tl.kim_58258** (1 reactions)
Directly using gradient ascent doesn't work very well with discrete natural language but feature visualization-like works are done in https://www.alignmentforum.org/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation and more recently https://arxiv.org/abs/2402.01702.

### 2025-05-18

**12:09:13 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/pdf/2505.08915

**12:09:23 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2505.08915

**14:32:27 UTC** - #general - **sesh**


**16:30:48 UTC** - #interesting-findings - **berendg.** (1 reactions)
This paper also exploits a similar idea, but for encoder based models: https://aclanthology.org/2023.findings-acl.876/

### 2025-05-20

**08:54:58 UTC** - #general - **installjohn2**
Mech interp seems like basic research to me, and basic research is extremely valuable, but in unexpected ways across a wide domain.

### 2025-05-22

**17:58:56 UTC** - #general - **seonsmallworldz**


### 2025-05-23

**04:12:41 UTC** - #general - **wabi.sabi.1**
Reasoning models would be a good recent example of a dual use interpretability and capabilities advancement.

(I don't see what work specifying mechanistic interpretability specifically would be doing in the dual use debate, so I'm just thinking about interpretability generally here.)

### 2025-05-24

**10:41:19 UTC** - #general - **neelnanda**
How did reasoning models come from interpretability work?

**15:35:03 UTC** - #general - **fieryvictorystar**
Has mechinterp lead to any significant  capabilities improvement that sota LLM use so far ?
My impresion is that the answer is no(theres some papers people will point to as mechinterp related capability advances but none that are used on practice ) , and I expect that to keep being the case unless mechinterp is wildly sucessfull but maybe I'm missing something .

**16:43:15 UTC** - #general - **wabi.sabi.1**
Interpretability wasn't the main motivation for their development, but they're still dual use. 

I see chain of thought and most other forms of dual use as essentially dangerous due to making models more interpretable to themselves, if they can decompose their own problem solving into pieces in a way that's easier to manage then they become more capable.

**18:01:57 UTC** - #general - **inscrut**
My feel, would be interested in feedback: Most attempts to make interpretable makes the models worse due to making them less end to end. Other branches don’t seem to have much practical implications. Causal patching for localization was shown to not help model editing. Most interp adjacent tuning (scaling circuits) (steering) (probing) is surpassed by Lora. Someone would have to aggressively muscle the interp insights into performance gain while beating all of the work done trying to directly op...

### 2025-05-25

**18:44:32 UTC** - #general - **seonsmallworldz**
https://arxiv.org/pdf/2502.08524

### 2025-05-26

**12:29:05 UTC** - #general - **timo13113**
Hi, some questions:
Are there models with sparse autoencoders, with some confirmed features that represent misalignment/deception/...?
If so, is it possible to run these models+SAEs cheaply, with 2060 6gb? 
I had an idea to try to predict/evaluate probability of this feature activating while the model generates the answer by looking at residuals interpreted with SAE with statistical methods like Peaks-Over-Threshold. Is this idea even useful/feasible or not?

**13:30:12 UTC** - #general - **aletheia27**
perhaps i'm a bit too policypilled but it seems to me that mitigating the dual use risks of interp is fundamentally a governance question, ie it would depend on forces outside of the ML community more than inside (how the external public uses our models, how policymakers seek to regulate, how quickly access spreads etc etc). is this a reasonable perspective, and if so, what can we researchers do about it?

**13:38:52 UTC** - #general - **clemd6d** (1 reactions)
idk but you could try to search https://www.neuronpedia.org/ database for such features

**23:06:10 UTC** - #general - **roberth653**
Golden Gate Claude was so good it had to be reverted back to give us additional time for alignment research.

### 2025-05-29

**20:21:07 UTC** - #general - **fieryvictorystar** (1 reactions)
https://x.com/AnthropicAI/status/1928119229384970244

**23:36:39 UTC** - #interesting-findings - **burnytech**
Open sourcing Anthropic's mechinterp code https://x.com/AnthropicAI/status/1928119229384970244 👀
<https://github.com/safety-research/circuit-tracer/blob/main/demos/circuit_tracing_tutorial.ipynb>

### 2025-05-31

**00:33:02 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/pdf/2505.20809

**00:33:22 UTC** - #interesting-findings - **jh_lim131**
https://arxiv.org/abs/2505.20809

**07:04:00 UTC** - #interesting-findings - **mrgonao**
https://arxiv.org/abs/2505.18373

## Papers & Research Highlights

**2025-05-15** - #general - alextmjugador
<@128268156459286528> didn't you technically wrote mech interp papers?

**2025-05-17** - #general - tl.kim_58258
Directly using gradient ascent doesn't work very well with discrete natural language but feature visualization-like works are done in https://www.alignmentforum.org/posts/aPeJE8bSo6rAFoLqg/solidgoldma...

**2025-05-18** - #interesting-findings - jh_lim131
https://arxiv.org/pdf/2505.08915

**2025-05-18** - #interesting-findings - jh_lim131
https://arxiv.org/abs/2505.08915

**2025-05-18** - #interesting-findings - berendg.
This paper also exploits a similar idea, but for encoder based models: https://aclanthology.org/2023.findings-acl.876/

**2025-05-24** - #general - fieryvictorystar
Has mechinterp lead to any significant  capabilities improvement that sota LLM use so far ?
My impresion is that the answer is no(theres some papers people will point to as mechinterp related capabili...

**2025-05-25** - #general - seonsmallworldz
https://arxiv.org/pdf/2502.08524

**2025-05-31** - #interesting-findings - jh_lim131
https://arxiv.org/pdf/2505.20809

**2025-05-31** - #interesting-findings - jh_lim131
https://arxiv.org/abs/2505.20809

**2025-05-31** - #interesting-findings - mrgonao
https://arxiv.org/abs/2505.18373

## Projects Highlights

**2023-04-10** - #project-proposals - abhayesian
I was thinking that you could train the transformer on bitstrings generated by multiple randomly sampled FSMs.  Here, the transformer is trained on one bitstring from one FSM.  I want to be able to se...

**2023-05-11** - #project-proposals - davidstrongfield
The Markov diagram posted by <@193204646687408129>  looks a bit odd. Why is there a 22% chance of adding a 0 when the last 3 bits were 110? Does the baby GPT not know that a sequence of two consecutiv...

**2023-05-11** - #project-proposals - davidstrongfield
So I have used my (matrix-product optimized) MPO word embedding algorithm to see if I can completely recover the transition for the sequence 11110 repeated over and over again. The MPO word embedding ...

**2023-05-11** - #project-proposals - davidstrongfield
My above comment actually gives me an idea about interpretability. If I train an MPO word embedding on a sequence generated by a finite state Markov process, then how closely will the matrices in the ...

**2023-05-29** - #general-resources - joyeechen
Anybody know the major AI safety/alignment related conferences? I have a transformers interp project for it

**2023-06-21** - #project-proposals - q_m_o
if anyone's interested in getting a group around interpreting open source rlhf models or RMs, I'm looking for collaborators to help brainstorm ideas and get something going
https://docs.google.com/doc...

**2023-08-16** - #project-proposals - jonask7671
**Epistemic Benchmarks **
Epistemic Benchmark explores the evaluation and measurement
of the knowledge foundations of intelligent agents in various environments.
This research aims to develop standard...

**2023-12-20** - #interesting-findings - g_w1
I just made a connection which could be potentially interesting: there is a program called creduce https://github.com/csmith-project/creduce/ that takes in a c file and interestingness test and reduce...

**2024-01-05** - #interesting-findings - woog
https://airtable.com/appYIr2qJDA2k0H9V/shrngsIKdJMCD7dYz/tblcUzakXN65z6xs7/viws1Gk5k0Xerk3Jr/rec6ks2L9T4WuEp5Z then this is the project page for nina's spar project

**2024-03-13** - #interesting-findings - g_w1
a mech interp project won 250k in the regeneron competition: https://www.societyforscience.org/regeneron-sts/2024-sts-winners/

## Technical Discussions Highlights

**2025-04-13** - #general - jh_lim131
you’re probably right about the lack of one to one relationship between behavior and circuit. Even slightly varying the order of a few tokens or injecting a token results in slightly or very different...

**2025-04-25** - #general - c4tm4nd00
I have worry that there is not enough auditing/criteria evaluation in considering additional features pertaining to algorithmic constraints and hardware constraints regarding cost to scale. I don’t re...

**2025-05-11** - #general - alextmjugador
All these CodeSignal assignments and many developers still don't know how to use Git features that help loads with collaboration like branching, rebasing, rerere, or conflict resolution properly

**2025-05-12** - #general - clemd6d
Do you have terabytes of storage to save activations?

**2025-05-15** - #general - gsarti
The 8th edition of [BlackboxNLP](https://blackboxnlp.github.io), the leading workshop on on interpretability and analysis of neural networks for NLP, will be co-located with EMNLP 2025 in Suzhou this ...

**2025-05-17** - #general - daksh.mor
why do not we try to apply gradient ascent in transformers, like we do in CNN's (feature visualization) ?

**2025-05-24** - #general - inscrut
My feel, would be interested in feedback: Most attempts to make interpretable makes the models worse due to making them less end to end. Other branches don’t seem to have much practical implications. ...

**2025-05-26** - #general - timo13113
Hi, some questions:
Are there models with sparse autoencoders, with some confirmed features that represent misalignment/deception/...?
If so, is it possible to run these models+SAEs cheaply, with 2060...

**2025-05-26** - #general - clemd6d
idk but you could try to search https://www.neuronpedia.org/ database for such features

**2025-05-29** - #interesting-findings - burnytech
Open sourcing Anthropic's mechinterp code https://x.com/AnthropicAI/status/1928119229384970244 👀
<https://github.com/safety-research/circuit-tracer/blob/main/demos/circuit_tracing_tutorial.ipynb>

## Research Findings Highlights

**2025-01-14** - #interesting-findings - seonsmallworldz
https://x.com/AISafetyMemes/status/1795756579742179744

strange

**2025-01-22** - #interesting-findings - clemd6d
> The original datasets consists of 1.4M dialogues generated by ChatGPT and spanning a wide range of topics. To create UltraChat 200k, we applied the following logic:
> 
> Selection of a subset of dat...

**2025-01-24** - #interesting-findings - pradeep1148
https://www.youtube.com/shorts/Bip0jH0ARVA

**2025-01-31** - #interesting-findings - burnytech
https://fxtwitter.com/chrisbarber/status/1885047105741611507

**2025-02-06** - #interesting-findings - mrgonao
https://www.lesswrong.com/posts/P8qLZco6Zq8LaLHe9/tokenized-saes-infusing-per-token-biases

**2025-02-20** - #interesting-findings - fieryvictorystar
https://x.com/BartBussmann/status/1889338359887126682?t=A6aKTILtM1CBUxe4FvHTMA&s=19

**2025-02-23** - #interesting-findings - xpkcs
hello! I'm training crosscoders and got some interesting results to share

These plots compare the baseline crosscoder recipe from Anthropic's original post vs. the Jan 2025 update that adds JumpReLU....

**2025-02-25** - #interesting-findings - jbcoo
https://x.com/OwainEvans_UK/status/1894436637054214509
that one's actually crazy

**2025-02-26** - #interesting-findings - seonsmallworldz
https://x.com/lucyfarnik/status/1894764023809286414

**2025-03-21** - #interesting-findings - seonsmallworldz
https://x.com/leedsharkey/status/1902705855142789584

## General Discussions Highlights

**2025-05-16** - #general - seonsmallworldz
not research

**2025-05-18** - #general - sesh


**2025-05-20** - #general - installjohn2
Mech interp seems like basic research to me, and basic research is extremely valuable, but in unexpected ways across a wide domain.

**2025-05-22** - #general - seonsmallworldz


**2025-05-23** - #general - wabi.sabi.1
Reasoning models would be a good recent example of a dual use interpretability and capabilities advancement.

(I don't see what work specifying mechanistic interpretability specifically would be doing...

**2025-05-24** - #general - neelnanda
How did reasoning models come from interpretability work?

**2025-05-24** - #general - wabi.sabi.1
Interpretability wasn't the main motivation for their development, but they're still dual use. 

I see chain of thought and most other forms of dual use as essentially dangerous due to making models m...

**2025-05-26** - #general - aletheia27
perhaps i'm a bit too policypilled but it seems to me that mitigating the dual use risks of interp is fundamentally a governance question, ie it would depend on forces outside of the ML community more...

**2025-05-26** - #general - roberth653
Golden Gate Claude was so good it had to be reverted back to give us additional time for alignment research.

**2025-05-29** - #general - fieryvictorystar
https://x.com/AnthropicAI/status/1928119229384970244

## Announcements Highlights

**2025-04-24** - #general - keryacine
Hello <@1340742405783158845>, same for us, we saw the announcement a bit late and sent the application yesterday. But the experimentation seems exiting indeed!

