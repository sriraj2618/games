import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Game Zone", page_icon="🎮", layout="wide")

st.title("🎮 Game Zone")

selected = option_menu(
    None,
    ["Home","Snake Game","Flappy Bird"],
    icons=["house","controller","controller"],
    orientation="horizontal"
)

# HOME PAGE
if selected == "Home":
    st.markdown("""
    ## Welcome to Game Zone

    Choose a game from above menu.

    🎮 Available Games  
    - Snake Game  
    - Flappy Bird
    """)

# ---------------- SNAKE GAME ----------------

elif selected == "Snake Game":

    snake = """
    <html>
    <body style="text-align:center;background:black;color:white">

    <h2>Snake Game</h2>
    <h3>Score: <span id="score">0</span></h3>

    <button onclick="startGame()">Start Game</button>

    <canvas id="game" width="400" height="400" style="background:#111;margin-top:20px"></canvas>

    <script>

    const canvas=document.getElementById("game");
    const ctx=canvas.getContext("2d");

    let snake;
    let food;
    let dx;
    let dy;
    let score;
    let gameRunning=false;

    function startGame(){

        snake=[{x:200,y:200}];
        food={x:100,y:100};
        dx=20;
        dy=0;
        score=0;
        gameRunning=true;

        document.getElementById("score").innerHTML=score;

    }

    document.addEventListener("keydown",e=>{

    if(!gameRunning) return;

    if(e.key=="ArrowUp" && dy==0){dx=0;dy=-20;}
    if(e.key=="ArrowDown" && dy==0){dx=0;dy=20;}
    if(e.key=="ArrowLeft" && dx==0){dx=-20;dy=0;}
    if(e.key=="ArrowRight" && dx==0){dx=20;dy=0;}

    });

    function draw(){

    if(!gameRunning){
        ctx.fillStyle="#111";
        ctx.fillRect(0,0,400,400);
        return;
    }

    ctx.fillStyle="#111";
    ctx.fillRect(0,0,400,400);

    ctx.fillStyle="red";
    ctx.fillRect(food.x,food.y,20,20);

    ctx.fillStyle="lime";

    snake.forEach(p=>ctx.fillRect(p.x,p.y,20,20));

    let head={x:snake[0].x+dx,y:snake[0].y+dy};

    if(head.x<0 || head.y<0 || head.x>=400 || head.y>=400){
        alert("Game Over! Score: "+score);
        gameRunning=false;
        return;
    }

    for(let i=1;i<snake.length;i++){
        if(head.x==snake[i].x && head.y==snake[i].y){
            alert("Game Over! Score: "+score);
            gameRunning=false;
            return;
        }
    }

    if(head.x==food.x && head.y==food.y){

        score++;

        document.getElementById("score").innerHTML=score;

        food={
            x:Math.floor(Math.random()*20)*20,
            y:Math.floor(Math.random()*20)*20
        }

    }else{
        snake.pop();
    }

    snake.unshift(head);

    }

    setInterval(draw,120);

    </script>
    </body>
    </html>
    """

    html(snake,height=520)

# ---------------- FLAPPY BIRD ----------------

elif selected == "Flappy Bird":

    bird = """
    <html>
    <body style="text-align:center;background:black;color:white">

    <h2>Flappy Bird</h2>
    <h3>Score: <span id="score">0</span></h3>

    <button onclick="startGame()">Start Game</button>

    <canvas id="game" width="400" height="500" style="background:skyblue;margin-top:20px"></canvas>

    <script>

    const canvas=document.getElementById("game");
    const ctx=canvas.getContext("2d");

    let birdY;
    let velocity;
    let pipes;
    let score;
    let gravity=0.6;
    let gameRunning=false;

    document.addEventListener("keydown",()=>{
        if(gameRunning) velocity=-8;
    });

    function startGame(){

        birdY=250;
        velocity=0;
        pipes=[];
        score=0;
        gameRunning=true;

        document.getElementById("score").innerHTML=score;

    }

    function createPipe(){

        if(!gameRunning) return;

        let gap=120;

        let topHeight=Math.random()*200+50;

        pipes.push({
            x:400,
            top:topHeight,
            bottom:topHeight+gap
        });

    }

    setInterval(createPipe,2000);

    function draw(){

    ctx.fillStyle="skyblue";
    ctx.fillRect(0,0,400,500);

    if(!gameRunning){
        requestAnimationFrame(draw);
        return;
    }

    velocity+=gravity;
    birdY+=velocity;

    ctx.fillStyle="yellow";
    ctx.beginPath();
    ctx.arc(100,birdY,15,0,Math.PI*2);
    ctx.fill();

    for(let i=0;i<pipes.length;i++){

        let p=pipes[i];
        p.x-=2;

        ctx.fillStyle="green";

        ctx.fillRect(p.x,0,40,p.top);
        ctx.fillRect(p.x,p.bottom,40,500);

        if(100+15>p.x && 100-15<p.x+40){

            if(birdY-15<p.top || birdY+15>p.bottom){
                alert("Game Over! Score: "+score);
                gameRunning=false;
            }

        }

        if(p.x==100){
            score++;
            document.getElementById("score").innerHTML=score;
        }

    }

    if(birdY>500){
        alert("Game Over! Score: "+score);
        gameRunning=false;
    }

    requestAnimationFrame(draw);

    }

    draw();

    </script>
    </body>
    </html>
    """

    html(bird,height=600)
