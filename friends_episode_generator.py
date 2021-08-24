from random import choice

def title():
    
    male_char = ["Ross", "Chandler", "Joey", "Gunther", "Rachel's dad", "Monica's dad"]
    female_char = ["Monica", "Rachel", "Phoebe", "Rachel's mom", "Joey sister's"]
    operator = ["and", "but", "meanwhile"]
    situation = ["fall in love with", "want a child from", "doesn't bear anymore", "had a fight with", "dreamed of", "stolen a job from", "said bad things about", "will share a flat with", "is going to move with", "would like to spend more time with", "did a bad joke to"]
    situation_post = ["would like to change job", "would like to move from NYC", "has some problems paying the rent", "is getting addicted to alchool", "discover to like women","discover to like men", "want to get a dog", "is stucked in traffic since hours", "find a new addicted friend", "is in love with the new tv", "is upset by constat disorder in the flat"]

    
    first_char = choice(male_char)
    second_char = choice(female_char)
    situation_pick = choice(situation)
    interruption = choice (operator)
    situation_last = choice(situation_post)
    male_char.remove(first_char)
    female_char.remove(second_char)
    all_together = male_char + female_char 
    third_char = choice(all_together)
    episode_title = f"{first_char} {situation_pick} {second_char}, {interruption} {third_char} {situation_last}"
    return (episode_title)
    
    
    
count = 1
while count < 50:
    print(title())
    count += 1
    
