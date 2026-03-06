import streamlit as st
import random
import time

st.set_page_config(page_title="Snake Game", page_icon="🐍")

st.title("🐍 Snake Game (Python Version)")

# -------- INITIALIZE SESSION --------

if "snake" not in st.session_state:
    st.session_state.snake = [(5,5)]
    st.session_state.food = (10,10)
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.running = False

# -------- START BUTTON --------

if st.button("Start Game"):
    st.session_state.snake = [(5,5)]
    st.session_state.food = (random.randint(0,19), random.randint(0,19))
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.running = True

# -------- SCORE --------

st.subheader(f"Score: {st.session_state.score}")

# -------- CONTROLS --------

col1,col2,col3,col4 = st.columns(4)

if col1.button("⬅"):
    st.session_state.direction="LEFT"

if col2.button("⬆"):
    st.session_state.direction="UP"

if col3.button("⬇"):
    st.session_state.direction="DOWN"

if col4.button("➡"):
    st.session_state.direction="RIGHT"

# -------- GAME LOOP --------

grid_size = 20

def move_snake():

    head = st.session_state.snake[0]

    if st.session_state.direction=="RIGHT":
        new_head = (head[0], head[1]+1)

    elif st.session_state.direction=="LEFT":
        new_head = (head[0], head[1]-1)

    elif st.session_state.direction=="UP":
        new_head = (head[0]-1, head[1])

    elif st.session_state.direction=="DOWN":
        new_head = (head[0]+1, head[1])

    st.session_state.snake.insert(0,new_head)

    if new_head == st.session_state.food:

        st.session_state.score +=1

        st.session_state.food = (
            random.randint(0,grid_size-1),
            random.randint(0,grid_size-1)
        )

    else:
        st.session_state.snake.pop()

    # collision

    if (
        new_head[0] <0 or new_head[0]>=grid_size
        or new_head[1]<0 or new_head[1]>=grid_size
        or new_head in st.session_state.snake[1:]
    ):
        st.session_state.running=False
        st.error("Game Over!")

# -------- GAME DISPLAY --------

grid = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]

for s in st.session_state.snake:
    grid[s[0]][s[1]]="🟩"

food = st.session_state.food
grid[food[0]][food[1]]="🍎"

for row in grid:
    st.write("".join(row))

# -------- RUN GAME --------

if st.session_state.running:

    move_snake()

    time.sleep(0.3)

    st.rerun()
