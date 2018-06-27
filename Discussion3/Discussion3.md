# Discriminatory Recommender Systems

There is a lot of warranted attention on bias in machine learning in general.
The canonical example of this is race's effect on loan applications and how zip
codes can act as a discriminatory variable. Cathy O'Neil's [Weapons of Math Distruction](http://www.nationalbook.org/nba2016_nf_oneil-weapons-of-math-destruction.html#.WzO5ZL392Aw)
does a great job investigating this.

There are several ways to fix this, one of which is represented in this weeks
[readings](https://arxiv.org/pdf/1610.02413.pdf)

In the [youtube video](https://www.youtube.com/watch?v=MqoRzNhrTnQ) on how some
recommenders can be biased, Evan Estola does a good job explaining some of
these.

Some examples that Evan brought up included the, over blown, recommender for
more expensive hotels for mac users, criminal defence ads for people with black
sounding names, and lower paying jobs for women. 

When I was an athlete I used to do a lot of google searches for diet related
articles and keto recipes. At the time keto was less main stream and google
started recommending me ads that appealed to presumably 40 year old women. This
was a bit disconcerting but by no means problematic. 

The main issue with these recommenders is that they ignore ethical constraints
that we have accepted as humans. For example, a recommender does not know that
it is OK to recommend bridal ads to women but not lower paying jobs because it
doesn't understand the difference. 


## Cause and Effect

Does a system cause discrimination, or does the system pick up on our embedded
biases already? 

I think that because this technology is so new, we are scared and wary of it. 
This is very reasonable, but I feel like we are putting too much blame on the
system. 

While recommending lower paying jobs to women is bad, blaming the algorithm
ignores that for a variety of reasons, women are in lower paying jobs. 

This problem existed before recommenders so I don't believe there is a causal
effect from them. While making the recommenders less biased will help a bit,
it is difficult to expect a few lines of code at google to fix the gender-wage
gap. 

Recommenders can help alleviate this like Evan suggested, however, I think the
effects will be minor. 

## Reinforcement

Whether these systems simply match the status quo or actually increase
discrimination is debatable, however, even if they simply maintain the status
it behooves data scientists to remedy this.

## Nudges

[Nudges](http://freakonomics.com/podcast-tag/behavioral-insights-team/) are a
way for policy makers to help people make good decisions. I think recommender
systems should act in the same way. 

Nudges, unfortunately, are not scaleable. Policy makers need to address
individual issues as the present themselves. The same holds true for
recommenders. 

For example, I am perfectly happy that google gives me ads that are tailored to
my gender. This only because an issue is a few rare cases. These should be met
with a tailored response. 

## Variance

Finally, I think that feed back loops should be addressed even if they do not
cover hot button topics like race or gender. Nobody wants a feedback loop that
only recommends the same thing to a certain demographic. Inserting random suggestions
can function as a great way to automatically test different suggestions without 
the need for a hypothesis to be formed.



<!-- LocalWords: Estola -->
