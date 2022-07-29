init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_eyes_full_of_stars_BELLA",
            category=["mas_compliment"],
            prompt="Staring into your eyes is like staring at a sky full of stars...",
            unlocked=True
        ),
        code="CMP"
    )

label otter_eyes_full_of_stars_BELLA:
    if not renpy.seen_label("otter_eyes_full_of_stars_BELLA_f"):
        call otter_eyes_full_of_stars_BELLA_f from _call_otter_eyes_full_of_stars_BELLA_f
    else:
        call otter_eyes_full_of_stars_BELLA_s from _call_otter_eyes_full_of_stars_BELLA_s
    return

label otter_eyes_full_of_stars_BELLA_f:
    m 2dkbsa "..."
    m 2fkbsa "That really means a lot to me, [player]..."
    m 1nubsa "I love you so much!"
    if persistent._mas_pm_shared_appearance:
        m 3hubsb "I bet your eyes are pretty as well!"
        m 5subsa "I can already imagine your beautiful ['enchanting' if isinstance(persistent._mas_pm_eye_color, tuple) else persistent._mas_pm_eye_color] eyes twinkle..."
        m 1nubsa "Ehehe~ I love you!"
    $ mas_gainAffection(3, bypass=True)
return "love"

label otter_eyes_full_of_stars_BELLA_s:
    m 1ekb "Thank you for saying this wonderful compliment of yours again."
    m 1hua "You really are amazing, you know that?"
    m 1huu "Ehehe~"
    m "I love you!"
    $ mas_gainAffection(2, bypass=False)
return "love"
