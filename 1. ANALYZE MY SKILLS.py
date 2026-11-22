import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("PlacementPro AI")
root.geometry("1000x700")
root.configure(bg="#0f172a")

skills = ["Python", "Java", "SQL", "DSA", "Machine Learning"]
ratings = {}

# Heading
tk.Label(
    root, text="PlacementPro AI",
    font=("Arial", 25, "bold"),
    bg="#0f172a", fg="white"
).pack(pady=(15, 5))

tk.Label(
    root, text="Student Placement & Skill Analysis System",
    font=("Arial", 11),
    bg="#0f172a", fg="#94a3b8"
).pack()

# Main content
main = tk.Frame(root, bg="#1e293b")
main.pack(fill="both", expand=True, padx=30, pady=20)

tk.Label(
    main, text="Skill Assessment",
    font=("Arial", 20, "bold"),
    bg="#1e293b", fg="#38bdf8"
).pack(pady=15)

tk.Label(
    main,
    text="Rate your current skills from 1 to 5",
    font=("Arial", 11),
    bg="#1e293b", fg="white"
).pack()

# Skill ratings
skill_frame = tk.Frame(main, bg="#1e293b")
skill_frame.pack(pady=15)

for skill in skills:
    row = tk.Frame(skill_frame, bg="#1e293b")
    row.pack(fill="x", pady=8)

    tk.Label(
        row, text=skill, width=20, anchor="w",
        font=("Arial", 12, "bold"),
        bg="#1e293b", fg="white"
    ).pack(side="left", padx=10)

    var = tk.IntVar(value=1)
    ratings[skill] = var

    scale = tk.Scale(
        row, from_=1, to=5, orient="horizontal",
        variable=var, length=300,
        bg="#1e293b", fg="white",
        highlightthickness=0,
        troughcolor="#334155"
    )
    scale.pack(side="left")

    tk.Label(
        row, text="1 = Beginner    5 = Advanced",
        bg="#1e293b", fg="#94a3b8",
        font=("Arial", 9)
    ).pack(side="left", padx=10)

# Result section
result_frame = tk.Frame(main, bg="#0f172a")
result_frame.pack(fill="x", padx=20, pady=15)

result = tk.Label(
    result_frame,
    text="Your assessment result will appear here.",
    font=("Arial", 12),
    bg="#0f172a", fg="white",
    justify="left", wraplength=800
)
result.pack(pady=15)

def analyze_skills():
    total = sum(var.get() for var in ratings.values())
    average = total / len(skills)

    if average < 2:
        level = "Beginner"
        advice = "Start with Python fundamentals and basic problem-solving."
    elif average < 3:
        level = "Developing"
        advice = "Practice coding regularly and work on small projects."
    elif average < 4:
        level = "Intermediate"
        advice = "Build projects and practice technical interview questions."
    else:
        level = "Strong"
        advice = "Focus on projects, DSA practice and mock interviews."

    strong = [s for s, v in ratings.items() if v.get() >= 4]
    weak = [s for s, v in ratings.items() if v.get() <= 2]

    result.config(
        text=f"Total Score: {total}/25\n"
             f"Average Skill: {average:.1f}/5\n"
             f"Skill Level: {level}\n"
             f"Strong Skills: {', '.join(strong) if strong else 'None yet'}\n"
             f"Needs Practice: {', '.join(weak) if weak else 'None'}\n\n"
             f"Recommendation: {advice}"
    )

tk.Button(
    main, text="ANALYZE MY SKILLS",
    font=("Arial", 12, "bold"),
    bg="#2563eb", fg="white",
    relief="flat", padx=25, pady=12,
    command=analyze_skills
).pack(pady=10)

root.mainloop()
