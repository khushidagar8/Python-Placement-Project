import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ================= DATABASE =================

conn = sqlite3.connect("placementpro.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    python INTEGER,
    java INTEGER,
    sql INTEGER,
    dsa INTEGER,
    ml INTEGER,
    average REAL,
    best_role TEXT
)
""")
conn.commit()

# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("PlacementPro AI")
root.geometry("1050x720")
root.configure(bg="#0f172a")

skills = ["Python", "Java", "SQL", "DSA", "Machine Learning"]
ratings = {}

roles = {
    "Python Developer": ["Python", "SQL", "DSA"],
    "Java Developer": ["Java", "DSA", "SQL"],
    "Data Analyst": ["Python", "SQL", "Machine Learning"],
    "AI/ML Engineer": ["Python", "Machine Learning", "DSA"],
    "Software Developer": ["Java", "Python", "DSA"]
}

learning_topics = {
    "Python": [
        "Python fundamentals and data types",
        "Loops, conditions and functions",
        "Object-oriented programming",
        "Build a Python mini project"
    ],
    "Java": [
        "Java basics and syntax",
        "Classes and objects",
        "Inheritance and polymorphism",
        "Collections and practice programs"
    ],
    "SQL": [
        "SELECT, WHERE and filtering",
        "ORDER BY and GROUP BY",
        "Joins and subqueries",
        "Practice database queries"
    ],
    "DSA": [
        "Arrays and strings",
        "Searching and sorting",
        "Stacks and queues",
        "Linked lists and trees"
    ],
    "Machine Learning": [
        "NumPy and Pandas basics",
        "Data cleaning and preprocessing",
        "Regression and classification",
        "Build an ML mini project"
    ]
}

# ================= HEADER =================

tk.Label(
    root,
    text="PlacementPro AI",
    font=("Arial", 26, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=(18, 5))

tk.Label(
    root,
    text="Smart Placement Preparation & Career Guidance System",
    font=("Arial", 11),
    bg="#0f172a",
    fg="#94a3b8"
).pack(pady=(0, 15))

# ================= TABS =================

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#0f172a", borderwidth=0)
style.configure("TNotebook.Tab", padding=[15, 8])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=25, pady=10)

profile_tab = tk.Frame(notebook, bg="#1e293b")
assessment_tab = tk.Frame(notebook, bg="#1e293b")
career_tab = tk.Frame(notebook, bg="#1e293b")
roadmap_tab = tk.Frame(notebook, bg="#1e293b")

notebook.add(profile_tab, text="Student Profile")
notebook.add(assessment_tab, text="Skill Assessment")
notebook.add(career_tab, text="Career Matcher")
notebook.add(roadmap_tab, text="Learning Roadmap")

# ================= PROFILE TAB =================

tk.Label(
    profile_tab,
    text="Student Profile",
    font=("Arial", 22, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
).pack(pady=30)

tk.Label(
    profile_tab,
    text="Enter your name to begin your placement assessment",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
).pack(pady=10)

name_entry = tk.Entry(
    profile_tab,
    font=("Arial", 14),
    width=35
)
name_entry.pack(pady=15)

profile_status = tk.Label(
    profile_tab,
    text="Your assessment data will be saved locally.",
    font=("Arial", 11),
    bg="#1e293b",
    fg="#94a3b8"
)
profile_status.pack(pady=10)

# ================= ASSESSMENT TAB =================

tk.Label(
    assessment_tab,
    text="Skill Assessment",
    font=("Arial", 21, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
).pack(pady=20)

tk.Label(
    assessment_tab,
    text="Rate your skills from 1 (Beginner) to 5 (Advanced)",
    font=("Arial", 11),
    bg="#1e293b",
    fg="white"
).pack(pady=10)

skill_frame = tk.Frame(assessment_tab, bg="#1e293b")
skill_frame.pack(pady=15)

for skill in skills:
    row = tk.Frame(skill_frame, bg="#1e293b")
    row.pack(pady=7)

    tk.Label(
        row,
        text=skill,
        font=("Arial", 12, "bold"),
        width=22,
        anchor="w",
        bg="#1e293b",
        fg="white"
    ).pack(side="left")

    var = tk.IntVar(value=1)
    ratings[skill] = var

    tk.Scale(
        row,
        from_=1,
        to=5,
        orient="horizontal",
        variable=var,
        length=300,
        bg="#1e293b",
        fg="white",
        troughcolor="#334155",
        highlightthickness=0
    ).pack(side="left")

tk.Label(
    assessment_tab,
    text="1 = Beginner     2 = Basic     3 = Intermediate     4 = Good     5 = Advanced",
    font=("Arial", 9),
    bg="#1e293b",
    fg="#94a3b8"
).pack(pady=5)

# ================= CAREER TAB =================

tk.Label(
    career_tab,
    text="Career Role Matcher",
    font=("Arial", 22, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
).pack(pady=20)

career_output = tk.Text(
    career_tab,
    height=23,
    font=("Consolas", 12),
    bg="#0f172a",
    fg="white",
    wrap="word",
    padx=15,
    pady=15
)
career_output.pack(fill="both", expand=True, padx=20, pady=10)

# ================= ROADMAP TAB =================

tk.Label(
    roadmap_tab,
    text="Personalized Learning Roadmap",
    font=("Arial", 21, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
).pack(pady=20)

roadmap_output = tk.Text(
    roadmap_tab,
    height=23,
    font=("Consolas", 11),
    bg="#0f172a",
    fg="white",
    wrap="word",
    padx=15,
    pady=15
)
roadmap_output.pack(fill="both", expand=True, padx=20, pady=10)

# ================= ANALYSIS FUNCTION =================

def analyze():

    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "Missing Name",
            "Please enter your name in Student Profile."
        )
        notebook.select(profile_tab)
        return

    # Calculate average
    total = sum(var.get() for var in ratings.values())
    average = total / len(skills)

    # Career role matching
    role_scores = []

    for role, required in roles.items():
        score = sum(ratings[s].get() for s in required)
        max_score = len(required) * 5
        percent = (score / max_score) * 100
        role_scores.append((role, percent, required))

    role_scores.sort(key=lambda x: x[1], reverse=True)

    best_role = role_scores[0][0]

    # Save to database
    cursor.execute("""
    INSERT INTO students
    (name, python, java, sql, dsa, ml, average, best_role)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        ratings["Python"].get(),
        ratings["Java"].get(),
        ratings["SQL"].get(),
        ratings["DSA"].get(),
        ratings["Machine Learning"].get(),
        average,
        best_role
    ))

    conn.commit()

    profile_status.config(
        text=f"Assessment saved successfully for {name}!",
        fg="#4ade80"
    )

    # ================= CAREER REPORT =================

    career_output.delete("1.0", tk.END)

    career_output.insert(tk.END, "PLACEMENT ANALYSIS REPORT\n")
    career_output.insert(tk.END, "=" * 45 + "\n")
    career_output.insert(tk.END, f"Student: {name}\n")
    career_output.insert(tk.END, f"Total Score: {total}/25\n")
    career_output.insert(tk.END, f"Average Skill Rating: {average:.2f}/5\n\n")

    career_output.insert(tk.END, "CAREER ROLE MATCHES\n")
    career_output.insert(tk.END, "-" * 45 + "\n")

    for role, percent, required in role_scores:
        career_output.insert(
            tk.END,
            f"{role}: {percent:.1f}%\n"
        )

    career_output.insert(tk.END, "\nBEST MATCH\n")
    career_output.insert(tk.END, "-" * 45 + "\n")
    career_output.insert(tk.END, f"Recommended Role: {best_role}\n")
    career_output.insert(
        tk.END,
        f"Match Score: {role_scores[0][1]:.1f}%\n"
    )
    career_output.insert(
        tk.END,
        "Skills: " + ", ".join(role_scores[0][2]) + "\n\n"
    )

    career_output.insert(tk.END, "SKILL REPORT\n")
    career_output.insert(tk.END, "-" * 45 + "\n")

    for skill, var in ratings.items():
        rating = var.get()

        if rating <= 2:
            level = "Needs Improvement"
        elif rating == 3:
            level = "Intermediate"
        else:
            level = "Strong"

        career_output.insert(
            tk.END,
            f"{skill}: {rating}/5 - {level}\n"
        )

    career_output.insert(
        tk.END,
        "\nNote: Career matches are based on self-reported ratings."
    )

    # ================= LEARNING ROADMAP =================

    roadmap_output.delete("1.0", tk.END)

    roadmap_output.insert(
        tk.END,
        f"PERSONALIZED ROADMAP FOR {name.upper()}\n"
    )
    roadmap_output.insert(tk.END, "=" * 45 + "\n\n")

    weak_skills = [
        skill for skill, var in ratings.items()
        if var.get() <= 3
    ]

    if not weak_skills:
        roadmap_output.insert(
            tk.END,
            "Your self-ratings are strong in all listed skills!\n"
            "Focus on advanced topics and project building.\n\n"
        )
        weak_skills = skills.copy()

    for skill in weak_skills:

        roadmap_output.insert(tk.END, f"\n{skill.upper()}\n")
        roadmap_output.insert(tk.END, "-" * 35 + "\n")

        for number, topic in enumerate(
            learning_topics[skill], start=1
        ):
            roadmap_output.insert(
                tk.END, f"{number}. {topic}\n"
            )

    roadmap_output.insert(
        tk.END,
        "\nSuggested strategy: Study one topic, practice it, "
        "and build a small project."
    )

    messagebox.showinfo(
        "Success",
        "Assessment complete!\nYour results have been saved."
    )

# ================= BUTTON =================

tk.Button(
    root,
    text="ANALYZE SKILLS & SAVE REPORT",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=12,
    relief="flat",
    command=analyze
).pack(pady=15)

root.mainloop()
