init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_sweat_glitter_BELLA",
            category=["mas_compliment"],
            prompt="I bet you sweat glitter.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_sweat_glitter_BELLA:
    m 1rksdlb "That's a weird compliment... {w=0.3}{nw}"
    extend 3hua "But I'll accept it anyway! Ahaha!"
    m 1eka "You really are creative when it comes to complimenting me."
    m 1eua "I really like that about you, [player]."
    $ mas_gainAffection(2, bypass=False)
return
