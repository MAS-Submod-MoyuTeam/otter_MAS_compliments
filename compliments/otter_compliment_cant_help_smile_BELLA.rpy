init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_cant_help_but_smile_BELLA",
            category=["mas_compliment"],
            prompt="Whenever I see you, I can't help but smile!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_cant_help_but_smile_BELLA:
    m 1eka "Thank you, [mas_get_player_nickname()]. I appreciate you~"
    m 3hua "I could say the same to you!"
    m "Look! I can't stop smiling! Ehehehe~"
    m 7ekb "Thank you for being there for me, [player].{nw}"
    $ _history_list.pop()
    menu:
        m "Thanks for being there for me, [player].{fast}"
        
        "Anything for you.":
            jump monika_expression_end
        "You're welcome.":
            jump monika_expression_end

label monika_expression_end:
    $ mas_gainAffection(2, bypass=False)
    show monika 5hubsu
    pause 2.0
    window auto
return