init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_better_if_like_you_BELLA",
            category=["mas_compliment"],
            prompt="Everything would be better if more people were like you!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_better_if_like_you_BELLA:
    if not renpy.seen_label("otter_better_if_like_you_BELLA_f"):
        call otter_better_if_like_you_BELLA_f from _call_otter_better_if_like_you_BELLA_f
    else:
        call otter_better_if_like_you_BELLA_s from _call_otter_better_if_like_you_BELLA_s
    return

label otter_better_if_like_you_BELLA_f:
    m 2subsb "Wow... thanks, [player]!"
    m 3hubsa "That means a lot to me!"
    m 1ekbsa "I could say the same to you, my love."
    m 5rua "You're so sweet, kind..."
    extend 3hubsb " perfect in every way, ahaha~!"
    m "I love you."
    $ mas_gainAffection(3, bypass=True)
return "love"

label otter_better_if_like_you_BELLA_s:
    m 1ekbsa "Thank you for reminding me this, [mas_get_player_nickname()]~"
    m "You are the best person I know."
    m "And my favorite, too! Ehehehe~"
    m 1hubsu "I love you!"
    $ mas_gainAffection(3, bypass=False)
return "love"