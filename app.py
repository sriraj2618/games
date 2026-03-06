import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Game Hub", page_icon="🎮")

st.title("🎮 Game Hub")

game = st.selectbox("Choose Game", ["Snake Game"])

if game == "Snake Game":

    st.subheader("Snake Game")

    game_html = """
    <!DOCTYPE html>
    <html>
    <body style="background:#111;text-align:center;color:white">

    <h2>Snake Game</h2>
    <p>Score: <span id="score">0</span></p>
    <canvas id="game" width="400" height="400" style="background:black"></canvas>

    <script>

    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    let snake = [{x:200,y:200}];
    let dx = 20;
    let dy = 0;
    let food = {x:100,y:100};
    let score = 0;

    document.addEventListener("keydown",dir);

    function dir(e){

        if(e.key=="ArrowUp" && dy==0){dx=0;dy=-20;}
        if(e.key=="ArrowDown" && dy==0){dx=0;dy=20;}
        if(e.key=="ArrowLeft" && dx==0){dx=-20;dy=0;}
        if(e.key=="ArrowRight" && dx==0){dx=20;dy=0;}

    }

    function draw(){

    ctx.fillStyle="black";
    ctx.fillRect(0,0,400,400);

    ctx.fillStyle="red";
    ctx.fillRect(food.x,food.y,20,20);

    ctx.fillStyle="lime";

    snake.forEach(s=>{
        ctx.fillRect(s.x,s.y,20,20);
    });

    let head = {x:snake[0].x+dx,y:snake[0].y+dy};

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

    if(head.x<0||head.y<0||head.x>=400||head.y>=400){
        alert("Game Over! Score:"+score);
        location.reload();
    }

    setTimeout(draw,120);

    }

    draw();

    </script>
    </body>
    </html>
    """

    components.html(game_html,height=500)
