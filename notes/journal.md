# Ellie's Adventure Project Journal

## Initial Thoughts 
I want to create a game for my daughter Ellie, who is currently 2. I would like to use this to help encourage her imagination and creativity. The game will start as a text based adventure (like Zork) and will morph into a graphical game as she gets older. Initially I will come up with the story, but as she gets older, I would start to use some stories that she comes up with as "quests", and use her artwork to inspire the graphical components of the game as it grows. When she was older, if she was interested in continuing to grow the project, or learning programming, I would pass the project off to her. 

As she is still young, the initial story....maybe Chapters?...will be very guided, more like adlibs where she will have the ability to interact with the story in limited ways, by providing names, or having to answer simple riddles, (If you knock twice, then knock three times, how many times will you have to knock?). Each chapter should have some sort of lesson to it. 

I am open sourcing the project for other people who may want to do something similiar. So I will need to think of this as creating a game engine of sorts that other people could use. 

A text based adventure is going to need a text parser to interpret responses. Initially the commands will be easy, and she would be playing with someone, so the commands will be in the realm of "Go Left", "Open the door", "Look out the window". I'm really not sure how to set that up initially. Zork had a pretty indepth text parser, hopefully I can find some pseudo code on that.

I will also need to come up with a way to create "maps". There was a guy ([javidx9](https://www.youtube.com/c/javidx9)) on Youtube who had a series on creating a 3D game engine from scratch in C++, I remember he had a creative way of "generating" maps with a textual representation in the code. That may be a good area to look at. 

There will also need to be a library of stories that can be pulled from. I may ask my wife to start coming up with some....Or maybe enlist the help of someone who is really good at DnD to give me some pointers? 


## References
* [Zork the Great Inner Workings](https://medium.com/swlh/zork-the-great-inner-workings-b68012952bdc) - Analysis of the Zork Text Parser
* [How to Write a Text Adventure in Python Part 2: The World Space](https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/)
