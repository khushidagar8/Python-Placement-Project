import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("PlacementPro AI - Career Matcher")
root.geometry("1000x700")
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

# Header
tk.Label(
    root, text="PlacementPro AI",
    font=("Arial", 25, "bold"),
    bg="#0f172a", fg="white"
).pack(pady=(15, 5))

tk.Label(
    root, text="Skill Assessment & Career Role Matcher",
    font=("Arial", 11),
    bg="#0f172a", fg="#94a3b8"
).pack()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=25, pady=20)

# Assessment tab
assessment_tab = tk.Frame(notebook, bg="#1e293b")
notebook.add(assessment_tab, text="Skill Assessment")

tk.Label(
    assessment_tab, text="Student Profile",
    font=("Arial", 18, "bold"),
    bg="#1e293b", fg="#38bdf8"
).pack(pady=10)

tk.Label(
    assessment_tab, text="Student Name:",
    bg="#1e293b", fg="white",
    font=("Arial", 12)
).pack()

name_entry = tk.Entry(assessment_tab, font=("Arial", 12), width=30)
name_entry.pack(pady=8)

tk.Label(
    assessment_tab,
    text="Rate your skills from 1 (Beginner) to 5 (Advanced)",
    bg="#1e293b", fg="white"
).pack(pady=10)

skill_frame = tk.Frame(assessment_tab, bg="#1e293b")
skill_frame.pack(pady=10)

for skill in skills:
    row = tk.Frame(skill_frame, bg="#1e293b")
    row.pack(pady=5)

    tk.Label(
        row, text=skill, width=20, anchor="w",
        bg="#1e293b", fg="white",
        font=("Arial", 11, "bold")
    ).pack(side="left")

    var = tk.IntVar(value=1)
    ratings[skill] = var

    tk.Scale(
        row, from_=1, to=5, orient="horizontal",
        variable=var, length=300,
        bg="#1e293b", fg="white",
        troughcolor="#334155",
        highlightthickness=0
    ).pack(side="left")

# Results tab
results_tab = tk.Frame(notebook, bg="#0f172a")
notebook.add(results_tab, text="Career Matcher")

tk.Label(
    results_tab, text="Career Match Results",
    font=("Arial", 20, "bold"),
    bg="#0f172a", fg="#38bdf8"
).pack(pady=20)

output = tk.Text(
    results_tab, height=22, width=95,
    font=("Consolas", 12),
    bg="#1e293b", fg="white",
    wrap="word", padx=15, pady=15
)
output.pack(padx=20, pady=10)

def find_careers():
    name = name_entry.get().strip()

    if not name:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Please enter your name in Skill Assessment tab.")
        notebook.select(assessment_tab)
        return

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"PLACEMENT REPORT FOR: {name.upper()}\n")
    output.insert(tk.END, "=" * 55 + "\n\n")

    # Overall skill score
    total = sum(v.get() for v in ratings.values())
    average = total / len(skills)

    output.insert(tk.END, f"Overall Skill Score: {total}/25\n")
    output.insert(tk.END, f"Average Rating: {average:.1f}/5\n\n")

    output.insert(tk.END, "CAREER ROLE MATCHING\n")
    output.insert(tk.END, "-" * 55 + "\n")

    role_scores = []

    for role, required_skills in roles.items():
        score = sum(ratings[s].get() for s in required_skills)
        max_score = len(required_skills) * 5
        percentage = (score / max_score) * 100

        role_scores.append((role, percentage, required_skills))

    role_scores.sort(key=lambda item: item[1], reverse=True)

    for role, percentage, required_skills in role_scores:
        output.insert(tk.END, f"{role}: {percentage:.1f}% match\n")

    best_role, best_score, best_skills = role_scores[0]

    output.insert(tk.END, "\nBEST MATCH\n")
    output.insert(tk.END, "-" * 55 + "\n")
    output.insert(tk.END, f"Recommended Career: {best_role}\n")
    output.insert(tk.END, f"Match Score: {best_score:.1f}%\n")
    output.insert(tk.END, "Required Skills: " + ", ".join(best_skills) + "\n\n")

    output.insert(tk.END, "SKILL IMPROVEMENT PLAN\n")
    output.insert(tk.END, "-" * 55 + "\n")

    for skill, var in ratings.items():
        rating = var.get()

        if rating <= 2:
            message = "Needs more practice"
        elif rating == 3:
            message = "Develop this skill further"
        else:
            message = "Good progress"

        output.insert(tk.END, f"{skill}: {rating}/5 - {message}\n")

    output.insert(
        tk.END,
        "\nNote: Match scores are based on your self-rated skills, "
        "not actual hiring probability."
    )

tk.Button(
    assessment_tab, text="FIND MY CAREER MATCH",
    font=("Arial", 12, "bold"),
    bg="#2563eb", fg="white",
    relief="flat", padx=20, pady=10,
    command=find_careers
).pack(pady=15)

root.mainloop()
