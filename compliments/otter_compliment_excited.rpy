init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_excited_see",
            category=["mas_compliment"],
            prompt="I get so excited when I see you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_excited_see:
    m 1subfb "[player], me too!"
    m 2subfa "Even right now, I feel so excited I can't contain myself!"
    m 2hubfb "Ahahaha~!"
    m 2dsbfa "My heart feels like its gonna jump out of my chest!"
    m 5tsbfb "I really love you too much."
    m 5ksbfa "I'll feel this excitement forever!"
    return "love"
