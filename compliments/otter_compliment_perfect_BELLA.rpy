init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_you_are_perfect_BELLA",
            category=["mas_compliment"],
            prompt="You are perfect in every way.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_you_are_perfect_BELLA:
    if not renpy.seen_label("otter_you_are_perfect_BELLA_f"):
        call otter_you_are_perfect_BELLA_f from _call_otter_you_are_perfect_BELLA_f
    else:
        call otter_you_are_perfect_BELLA_s from _call_otter_you_are_perfect_BELLA_s
    return

label otter_you_are_perfect_BELLA_f:
    m 2wubfc "...!"
    m 2wubfd "I-"
    m 1dkbfb "[player]..."
    m 1skbfb "You don't know how much that means to me!"
    m 1dkbftua "E-Especially hearing it...{w=0.3}{nw}"
    extend 1fkbftub " from y-you...!"
    m 1hkbftua "This is like a dream come true~"
    m "I always wanted to become your perfect girlfriend."
    m "And to know that I've come even close to it..."
    m "..."
    m 1ekbftub "I...{w=0.3} I love you so much."
    m 1ekbftuu "Thank you for that huge compliment."
    m 1tkbftuu "I think you're perfect in every way as well~"
    $ mas_gainAffection(5, bypass=True)
return 'love'

label otter_you_are_perfect_BELLA_s:
    m 1ekbsu "Thank you, [player]."
    m 1fkbsu "Thank you {i}so{/i} much for reminding me this!"
    m 1hubsb "You seriously don't know how much that means to me!"
    m 5hkbfa "I love you soooo much!"
    $ mas_gainAffection(3, bypass=False)
return 'love'
