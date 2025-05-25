# Key Assumptions

This page documents important assumptions that I have made regarding the given dataset.

## Inclusive vs Exclusive Thresholds

For me I found the achievement level criteria to have a level of ambiguity to them regarding whether the
number thresholds as given were inclusive or exclusive.

The `Bronze` level criteria is stated as "*Owns more than 10 games*", which clearly states that a user with
10 games would **not** be eligible for a `Bronze` account wide achievement and thus the minimum would be 11.
However, the higher levels are phrased as "*Owns 10+ games and has 75%+ achievements in each*" where the
usage of `10+` and `75%+` reads as an inclusive (to my mind) "*Owns 10 ***or more*** games and has 75%
***or more*** achievements in each*".

I sent a clarification email at noon on Friday, however it was late in the week and I anticipated that I very
understandably would not receive a response in time.

As such I have proceeded with the assumption that all thresholds are exclusive, to be in line with the clear
exclusive `Bronze` level criteria.

If I have time I will implement a simple switch to allow running the API in inclusive or exlusive modes, with
the default setting being exclusive.

## Non PlayStation Games

During my run through to understand the API I spotted that the dataset user libraries contain Nintendo and
Microsoft developed/published games as well as PC or mobile only titles that are most certainly not available
on a PS console. These are:

* The Legend of Zelda: Breath of the Wild (was particularly easy to pick out as a Zelda girl!)
* Animal Crossing: New Horizons
* Gears of War 4
* Gears Tactics
* Gears 5
* Total War Three Kingdoms
* Minecraft Earth
* The Witcher 2: Assassins of Kings

A handful of others are ambiguous. For example, is The Elder Scrolls V: Skyrim referencing the versions
available to the PS4 and PS5, or the original PS3 version (honestly can't remember if the PS4 is BC with
PS3 games (IIRC not due to the widely differing CPU architectures))?

I asked in the same email mentioned in the [Inclusive vs Exclusive Thresholds](./key-assumptions.md#inclusive-vs-exclusive-thresholds) section. Largely around if extra handling needs to be performed, or if this is simply a case of engineers
filling out example datasets with their favourite games (I've inputted many a *John 117* in my time!).

I've proceeded with the assumption that these are simply there to fill out the dataset.

**Previous page:** [Data](./data.md)

**Next page:** [Key Assumptions](./key-assumptions.md)