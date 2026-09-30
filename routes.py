from pathlib import Path

from fastapi import APIRouter, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent

TEMPLATE_DIR = BASE_DIR / "templates"

templates = Jinja2Templates(
    directory=TEMPLATE_DIR
)
users_data = []


@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
@router.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    fitness_goal: str = Form(...),
    workout_intensity: str = Form(...)
):
    users_data.append({
        "user_id": user_id,
        "name": name,
        "age": age,
        "weight": weight,
        "goal": fitness_goal,
        "intensity": workout_intensity,
        "original_plan": "Squats - 3 sets × 12 reps\nPush-ups - 3 sets × 10 reps\nLunges - 3 sets × 10 reps\nPlank - 3 sets × 30 seconds",
        "updated_plan": ""
    })

    return f"""
    <html>
    <head>
        <title>FitBuddy Workout Plan</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f7f8;
                padding: 40px;
            }}
            .card {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }}
            h1 {{
                color: #222;
            }}
            .info {{
                margin: 12px 0;
                font-size: 17px;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>💪 Your Workout Plan</h1>

            <div class="info"><b>Name:</b> {name}</div>
            <div class="info"><b>User ID:</b> {user_id}</div>
            <div class="info"><b>Age:</b> {age}</div>
            <div class="info"><b>Weight:</b> {weight} kg</div>
            <div class="info"><b>Fitness Goal:</b> {fitness_goal}</div>
            <div class="info"><b>Workout Intensity:</b> {workout_intensity}</div>

            <hr>

            <h2>Workout Plan</h2>

            <p>🏋️ Squats - 3 sets × 12 reps</p>
            <p>💪 Push-ups - 3 sets × 10 reps</p>
            <p>🏋️ Lunges - 3 sets × 10 reps</p>
            <p>💪 Plank - 3 sets × 30 seconds</p>

            <h3>Good luck with your workout! 🔥</h3>
            <hr>

<a href="/workout-details"
   style="
   display:inline-block;
   padding:12px 25px;
   background:#2196f3;
   color:white;
   text-decoration:none;
   border-radius:8px;
   font-weight:bold;
   margin-top:15px;">
   View Detailed 7-Day Workout Plan
</a>
        </div>
    </body>
    </html>
    """
@router.get("/workout-details", response_class=HTMLResponse)
def workout_details():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FitBuddy - 7 Day Workout Plan</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5f9;
                margin: 0;
                padding: 30px;
            }

            .container {
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }

            h1 {
                text-align: center;
                color: #1e3a5f;
            }

            h2 {
                color: #2196f3;
            }

            .day {
                background: #f8fafc;
                padding: 18px;
                margin: 15px 0;
                border-radius: 10px;
                border-left: 5px solid #2196f3;
            }

            li {
                margin: 8px 0;
            }

            .back {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 25px;
                background: #2196f3;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

    <div class="container">

        <h1>💪 7-Day Workout Plan</h1>

        <p>
            Your personalized weekly workout schedule.
        </p>

        <div class="day">
            <h2>Day 1 - Upper Body 💪</h2>
            <ul>
                <li>Push-ups - 3 sets × 10 reps</li>
                <li>Shoulder Press - 3 sets × 10 reps</li>
                <li>Arm Circles - 2 sets × 30 seconds</li>
                <li>Triceps Dips - 3 sets × 10 reps</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 2 - Lower Body 🦵</h2>
            <ul>
                <li>Squats - 3 sets × 12 reps</li>
                <li>Lunges - 3 sets × 10 reps</li>
                <li>Glute Bridges - 3 sets × 12 reps</li>
                <li>Calf Raises - 3 sets × 15 reps</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 3 - Cardio ❤️</h2>
            <ul>
                <li>Jumping Jacks - 3 sets × 30 seconds</li>
                <li>High Knees - 3 sets × 30 seconds</li>
                <li>Mountain Climbers - 3 sets × 20 seconds</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 4 - Rest & Recovery 🧘</h2>
            <ul>
                <li>Light Walking - 20 minutes</li>
                <li>Stretching - 10 minutes</li>
                <li>Deep Breathing</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 5 - Full Body 🔥</h2>
            <ul>
                <li>Squats - 3 sets × 12 reps</li>
                <li>Push-ups - 3 sets × 10 reps</li>
                <li>Lunges - 3 sets × 10 reps</li>
                <li>Plank - 3 sets × 30 seconds</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 6 - Core Workout 🔥</h2>
            <ul>
                <li>Plank - 3 sets × 30 seconds</li>
                <li>Crunches - 3 sets × 15 reps</li>
                <li>Leg Raises - 3 sets × 10 reps</li>
            </ul>
        </div>

        <div class="day">
            <h2>Day 7 - Active Recovery 🌿</h2>
            <ul>
                <li>Light Walking - 20 minutes</li>
                <li>Full Body Stretching</li>
                <li>Relaxation</li>
            </ul>
        </div>

        <a class="back" href="/">
            ← Back to FitBuddy
        </a>
        <br><br>

<a class="back" href="/feedback">
    💬 Give Feedback
</a>

</div>

    </body>
    </html>
    """
@router.get("/feedback", response_class=HTMLResponse)
def feedback():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FitBuddy - Share Your Feedback</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f5f9;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }

            h1 {
                text-align: center;
                color: #2196f3;
            }

            label {
                font-weight: bold;
                display: block;
                margin-top: 18px;
            }

            input, textarea {
                width: 100%;
                padding: 12px;
                margin-top: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
                box-sizing: border-box;
                font-size: 15px;
            }

            textarea {
                height: 120px;
                resize: vertical;
            }

            button {
                width: 100%;
                padding: 13px;
                margin-top: 20px;
                background: #2196f3;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background: #1976d2;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>📝 Share Your Feedback</h1>

            <label>Your Unique User ID:</label>

            <input
                type="text"
                placeholder="Enter the same User ID used to generate your plan"
            >

            <label>Your Feedback:</label>

            <textarea
                placeholder="Let us know how we can improve your plan..."
            ></textarea>

            <button onclick="window.location.href='/all-users'">
    Submit Feedback
</button>

        </div>

    </body>
    </html>
    """
@router.get("/all-users", response_class=HTMLResponse)
def all_users():

    rows = ""

    for user in users_data:
        rows += f"""
        <tr>
            <td>{user["user_id"]}</td>
            <td>{user["name"]}</td>
            <td>{user["age"]}</td>
            <td>{user["weight"]}</td>
            <td>{user["goal"]}</td>
            <td>{user["intensity"]}</td>
            <td style="text-align:left; vertical-align:top; min-width:350px;">
    <strong>7-Day Workout Plan</strong><br><br>

    <strong>Day 1 - Upper Body</strong><br>
    Push-ups - 3 sets × 10 reps<br>
    Shoulder Press - 3 sets × 10 reps<br>
    Bicep Curls - 3 sets × 12 reps<br>
    Triceps Dips - 3 sets × 10 reps<br><br>

    <strong>Day 2 - Lower Body</strong><br>
    Squats - 3 sets × 12 reps<br>
    Lunges - 3 sets × 10 reps<br>
    Glute Bridges - 3 sets × 12 reps<br>
    Calf Raises - 3 sets × 15 reps<br><br>

    <strong>Day 3 - Cardio & Core</strong><br>
    Jumping Jacks - 3 × 30 sec<br>
    Mountain Climbers - 3 × 20 reps<br>
    High Knees - 3 × 30 sec<br>
    Plank - 3 × 30 sec<br><br>

    <strong>Day 4 - Active Recovery</strong><br>
    Walking - 20 minutes<br>
    Light Stretching - 10 minutes<br>
    Yoga - 10 minutes<br>
</td>

<td style="text-align:left; vertical-align:top; min-width:350px;">
    <strong>Updated 7-Day Workout Plan</strong><br><br>

    <strong>Day 1 - Upper Body</strong><br>
    Bench Press - 3 sets × 12 reps<br>
    Push-ups - 3 sets × 12 reps<br>
    Shoulder Press - 3 sets × 12 reps<br>
    Lateral Raises - 3 sets × 15 reps<br><br>

    <strong>Day 2 - Lower Body</strong><br>
    Squats - 3 sets × 15 reps<br>
    Lunges - 3 sets × 12 reps<br>
    Glute Bridges - 3 sets × 15 reps<br>
    Calf Raises - 3 sets × 20 reps<br><br>

    <strong>Day 3 - Cardio & Core</strong><br>
    Jumping Jacks - 3 × 40 sec<br>
    Mountain Climbers - 3 × 25 reps<br>
    High Knees - 3 × 40 sec<br>
    Plank - 3 × 45 sec<br><br>

    <strong>Day 4 - Active Recovery</strong><br>
    Walking - 30 minutes<br>
    Stretching - 15 minutes<br>
    Yoga - 15 minutes<br>
</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>FitBuddy - All Users & Workout Plans</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f7f8;
                padding: 30px;
            }}

            .container {{
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                overflow-x: auto;
            }}

            h1 {{
                text-align: center;
                color: #2196f3;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th {{
                background: #2196f3;
                color: white;
                padding: 12px;
            }}

            td {{
                padding: 10px;
                border: 1px solid #ddd;
                text-align: center;
            }}

            tr:nth-child(even) {{
                background: #f2f2f2;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>💪 FitBuddy - All Users & Workout Plans</h1>

            <table>

                <tr>
                    <th>User ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Weight (kg)</th>
                    <th>Goal</th>
                    <th>Intensity</th>
                    <th>Original Plan</th>
                    <th>Updated Plan</th>
                </tr>

                {rows}

            </table>

        </div>

    </body>
    </html>
    """