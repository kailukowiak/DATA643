# Recommender Systems Suffer from Serial Auto Correlation 

A hot dog is a hot dog. In fact, it is trivial to make a machine learning system
that can accurately classify cancers, had written letters, hot dogs, types of
cat, or anything else. 

Further, a hot dog is a hot dog whether or not an algorithm says it is or not.
The same cannot be said for recommender systems. On the surface recommender
systems have a close similarity to other ML programs. They both use linear
algebra and a training/test set or cross validation to minimize a cost function.

However, recommender systems, in the real world have the problem of influencing
their future results with current recommendations. In econometrics, when a past
event influences a future event, it is called auto-correlation. 

This is most simply seen as a feed back loop. If I watch a video of cats the
recommender system will recommend more. I will then watch/rate these movies and
the system will be re-enforced. This is fine for cat videos but less so when it
comes to deplorable content such as racist/incel material.

## How can we combat this?

First of all, the vast majority of recommender systems are guilty of this. Just
because the worst thing that happens is that I get recommended a ton of cat
videos in most cases doesn't mean there isn't a methodological problem with the
system. I don't have a solution to this other than introducing more random
variation to systems. This would reduce their short term profitability but
could, in the long run increase over all satisfaction.

The second problem is that deplorable content is normative in nature. Machine
learning algorithms are good at identifying positive attributes, but it is hard
to identify value judgments. Thus, the solution for most novel problems is a 
human initiated algorithm change. For example, google recommending suicide help
lines for people googling how to kill themselves or dissuading potential ISIS
recruits from joining.

## Current Solution

Realistically, there is not an AI solution to this. As data scientists, we must
remain vigil about potential abuses, unintended consequences and abhorrent
results and combat them.
