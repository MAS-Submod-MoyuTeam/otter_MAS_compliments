init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_colors_brighter_when_youre_around_BELLA",
            category=["mas_compliment"],
            prompt="Colors are brighter when you're around.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_colors_brighter_when_youre_around_BELLA:
    m 1hubsa "You're so creative on your compliments!"
    m "Thank you, [player]."
    m 1eubsa "I really like it when you say things like that."
    m 1ekbsa "It makes me feel special."
    m 4hubsb "I could say the same to you, ehehe~"
    m "I love you~"
    $ mas_gainAffection(2, bypass=False)
return "love"
