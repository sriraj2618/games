import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Game Zone", page_icon="🎮", layout="wide")

st.markdown("""
<style>
body{
background: linear-gradient(135deg,#1e3c72,#2a5298);
color:white;
}
h1,h2{
text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Game Zone")

selected = option_menu(
    None,
    ["Home","Snake Game","Flappy Bird"],
    icons=["house","controller","controller"],
    orientation="horizontal"
)

# HOME
if selected == "Home":
    st.markdown("""
    ## Welcome 🎮

    Play classic arcade games directly in your browser.

    **Available Games**
    - 🐍 Snake Game
    - 🐦 Flappy Bird

    Select a game above to start playing!
    """)

# ------------------ SNAKE GAME ------------------

elif selected == "Snake Game":

    snake_game = """
    <html>
    <body style="text-align:center;background:black;color:white">

    <h2>Snake Game</h2>
    <h3>Score: <span id="score">0</span></h3>

    <canvas id="game" width="400" height="400" style="background:#111"></canvas>
    <br><br>
    <button onclick="location.reload()">Restart</button>

    <script>

    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    let snake=[{x:200,y:200}];
    let food={x:100,y:100};
    let dx=20;
    let dy=0;
    let score=0;

    document.addEventListener("keydown",changeDir);

    function changeDir(e){

    if(e.key=="ArrowUp" && dy==0){dx=0;dy=-20;}
    if(e.key=="ArrowDown" && dy==0){dx=0;dy=20;}
    if(e.key=="ArrowLeft" && dx==0){dx=-20;dy=0;}
    if(e.key=="ArrowRight" && dx==0){dx=20;dy=0;}

    }

    function draw(){

    ctx.fillStyle="#111";
    ctx.fillRect(0,0,400,400);

    ctx.fillStyle="red";
    ctx.fillRect(food.x,food.y,20,20);

    ctx.fillStyle="lime";

    snake.forEach(p=>{
        ctx.fillRect(p.x,p.y,20,20);
    });

    let head={x:snake[0].x+dx,y:snake[0].y+dy};

    if(head.x<0 || head.y<0 || head.x>=400 || head.y>=400){
        alert("Game Over! Score: "+score);
        location.reload();
    }

    for(let i=1;i<snake.length;i++){
        if(head.x==snake[i].x && head.y==snake[i].y){
            alert("Game Over! Score: "+score);
            location.reload();
        }
    }

    if(head.x==food.x && head.y==food.y){
        score++;
        document.getElementById("score").innerHTML=score;

        food={
            x:Math.floor(Math.random()*20)*20,
            y:Math.floor(Math.random()*20)*20
        };

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

    html(snake_game,height=500)


# ------------------ FLAPPY BIRD ------------------

elif selected == "Flappy Bird":

    bird_game = """
    <html>
    <body style="text-align:center;background:black;color:white">

    <h2>Flappy Bird</h2>
    <h3>Score: <span id="score">0</span></h3>

    <canvas id="game" width="400" height="500" style="background:skyblue"></canvas>
    <br><br>
    <button onclick="location.reload()">Restart</button>

    <script>

    const canvas=document.getElementById("game");
    const ctx=canvas.getContext("2d");

    let birdY=250;
    let velocity=0;
    let gravity=0.6;
    let pipes=[];
    let score=0;

    document.addEventListener("keydown",()=>velocity=-8);

    function createPipe(){

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

    velocity+=gravity;
    birdY+=velocity;

    ctx.fillStyle="skyblue";
    ctx.fillRect(0,0,400,500);

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
                location.reload();
            }

        }

        if(p.x==100){
            score++;
            document.getElementById("score").innerHTML=score;
        }

    }

    if(birdY>500){
        alert("Game Over! Score: "+score);
        location.reload();
    }

    requestAnimationFrame(draw);

    }

    draw();

    </script>

    </body>
    </html>
    """

    html(bird_game,height=600)
