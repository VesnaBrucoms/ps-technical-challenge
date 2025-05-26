# Tech choices

**Note to reduce repitition:** I have selected a lot of the technology on the basis of familiarity, and with
that familiarity comes speed. Though there are differing levels of familiarity from tech to tech.

#### Python

Not only am I familiar with it, but it's the language I have the most experience with. I find that it's also
a language that's very well suited to a project like this, in two different ways:

1. The speed on writing enables me to go further with this week long interview tech test.
2. For an equivalent real project, the API does not require raw speed. As such Python is an equally good choice
alongside Java or C#. So speed of development comes more into play, plus the less noisy code allows for better
readability (though this part I do realise is subjective).

#### Flask

I'm familiar with it, it's lightweight and thus very fast to get up and running.

#### Swagger UI

Again, I'm familiar with it. Plus as the test API also uses Swagger docs, choosing it for this API brings
consistency, which in turn improves developer/maintainer/user experience.

#### Black Formatter

Very opinionated formatter that very closely follows Python's [PEP8](https://peps.python.org/pep-0008/) style
guidelines. It has a VSCode extension to enable formatting when saving, which I have enabled in the workspace
settings. Having Black format every time I save, saves me the effort and time to think about and fuss with
the style of the code. It also saves a step during the build process.