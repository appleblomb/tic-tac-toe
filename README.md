# tic-tac-toe
## Running this project

Clone it like you would any other git repo

Make sure uv (python virtual environment manager) is installed on your system

cd to the project directory

```
uv run main.py
```

This takes no arguments and will prompt for any options

## The approach

I thought about this briefly as I try to plan things out a bit before just implementing, though the limited time did not allow for a full architecture design document.
So I started with the idea being able to simply start with a Gameboard class which would hold most of the data and game logic, then a Player class which would give us an interface
for any type of player if time allowed. Since a tic-tac-toe board looks a bit like a matrix, it gave me the idea to use numpy which is a common python library used in scientific
computing and is very lean and performant. With this it allowed me to focus on the higher level details rather than having to implement all the game logic myself. This gave me the benefit
of having the game scale to larger boards without having to re-design.

When developing I like to test incrementally and verify units are functioning. (If I were doing this for production this would mean writing unit tests and hacking on local dev or stage to test).
I also try to commit and someetimes even push incrementally as well so I have rollback points if ai goes off the rails or any other sort of unexpected disaster. Building isolated functionality
keeps things easier to test, allows for more rapid prototyping and pivoting (as seen when I realized I hadn't implemented the tie-breaker functionality and re-organized some code by hand).
I comment minimally usually, Brief summaries when necessary but otherwise try not to clutter the code unless I have to something complicated (and even then I try to de-complicate it and write
for maintainablity unless there is a strong performance indicator that would drive the solution). Then after the base functionality was implemented I jumped to ui improvements with the retry system.

## AI
For this exercise I chose to use Github Co-pilot with the GPT-5 mini model. It runs locally so it does not induce cloud costs (I have a pretty beefy machine that will run much larger models) and handles
next edit, auto-complete and conversation in one. Even though I could have run something bigger like gpt-oss-104b, configuring it with Continue and VS Code is quite tedious, and then would have to run a smaler model anyway
for auto complete and next edit. Playing around with with GPT-5 mini for a bash script I was writing for a personal project showed while it was not perfect, it was definitely good enough to converse with and generate code
for most things as was seen with the hallucinations. For this project I would scaffold code and have the agent show the syntax for features I had trouble remembering, make small edits, and would have it implement functions.
I would audit all of the code generated and more than once would fix errors as they came up, but I made sure to keep the scope small and manageable so that I could understand the output, and introduce minimal risk during development.
Given the small scope of this project, I did not find other AI tools necessary though I am always looking for new tools to increase velocity without sacrificing quality.

## Reflection
Overall I feel this implementation went pretty well. I had originally wanted to do this in a more web-server oriented format rather than the python cli since it would be more representative of my day-to-day but it was fun going back to
an older app style and I feel like I could implement a lot more with that choice. If I had spent more time thinking things through with the design I might have not got stuck when trying to decide where to handle some of the win/tie logic
and not had to refactor some of the ai generated logic to make the flow smoother. With the arbitrary board size I would have liked to add an arbitrary number of players as well to put another twist on the game but I was fairly certain I would
not have time to do it. I also would have liked to add unit testing given more time but making sure the game was working and sufficiently feature complete took priority. It was a fun little excercise, and I partially even surprised myself with
how much I got done. (AI is great isn't it?)


