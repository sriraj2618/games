import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Game Zone", page_icon="🎮", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {
background: linear-gradient(to right,#141e30,#243b55);
color:white;
}
h1{
text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Welcome to Game Zone")

selected = option_menu(
    menu_title=None,
    options=["Home","Snake Game","Flappy Bird"],
    icons=["house","controller","controller"],
    orientation="horizontal"
)

# HOME PAGE
if selected == "Home":
    st.markdown("""
    ## 🕹️ Play Classic Games

    Welcome to **Game Zone**

    🎮 Available Games:
    - Snake Game
    - Flappy Bird

    Select a game from the menu and enjoy!
    """)

# SNAKE GAME
elif selected == "Snake Game":

    st.header("🐍 Snake Game")

    snake_html = """
    <html>
    <head>
    <style>
    canvas{
    background:black;
    display:block;
    margin:auto;
    }
    </style>
    </head>

    <body>

    <canvas id="game" width="400" height="400"></canvas>

    <script>

    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    let snake = [{x:200,y:200}];
    let food = {x:100,y:100};

    let dx = 20;
    let dy = 0;

    document.addEventListener("keydown", direction);

    function direction(event){

        if(event.key=="ArrowUp"){dx=0;dy=-20;}
        if(event.key=="ArrowDown"){dx=0;dy=20;}
        if(event.key=="ArrowLeft"){dx=-20;dy=0;}
        if(event.key=="ArrowRight"){dx=20;dy=0;}

    }

    function draw(){

        ctx.fillStyle="black";
        ctx.fillRect(0,0,400,400);

        ctx.fillStyle="red";
        ctx.fillRect(food.x,food.y,20,20);

        ctx.fillStyle="lime";

        snake.forEach(part=>{
            ctx.fillRect(part.x,part.y,20,20);
        });

        let head = {x:snake[0].x+dx,y:snake[0].y+dy};

        if(head.x==food.x && head.y==food.y){
            food.x=Math.floor(Math.random()*20)*20;
            food.y=Math.floor(Math.random()*20)*20;
        } else{
            snake.pop();
        }

        snake.unshift(head);

    }

    setInterval(draw,120)

    </script>

    </body>
    </html>
    """

    html(snake_html,height=450)

# FLAPPY BIRD
elif selected == "Flappy Bird":

    st.header("🐦 Flappy Bird")

    bird_html = """
    <html>
    <canvas id="game" width="400" height="500"></canvas>

    <script>

    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    let birdY = 200;
    let gravity = 2;
    let velocity = 0;

    document.addEventListener("keydown",()=>{
        velocity = -10;
    });

    function draw(){

        velocity += gravity;
        birdY += velocity;

        ctx.fillStyle="skyblue";
        ctx.fillRect(0,0,400,500);

        ctx.fillStyle="yellow";
        ctx.beginPath();
        ctx.arc(100,birdY,15,0,Math.PI*2);
        ctx.fill();

        requestAnimationFrame(draw);
    }

    draw();

    </script>
    </html>
    """

    html(bird_html,height=520)