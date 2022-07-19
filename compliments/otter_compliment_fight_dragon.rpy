#If we were in the Middle Ages, I’d fight a dragon for you, compliment submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_compliment_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_otter_compliment_fight_dragon",
            category =["mas_compliment"],
            prompt="If we were in the Middle Ages, I’d fight a dragon for you.",
            unlocked=True
        ),
        code="CMP"
    )

label monika_otter_compliment_fight_dragon:
    m 1tsbfb "Aww, is that right, my dragon slayer?"
    m 2hsbfu "I love you so much!"
    m 4ksbfu "No creature would scare me if you were in danger!"
    m 4tsbfb "I would fight basilisks, manticores, cerberus..."
    m 3ssbfu "If that would mean being by your side!"
    m 5fkbfa "My medieval hero."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
