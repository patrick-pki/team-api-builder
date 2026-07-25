# 🚀 Team API Builder - Class Collaboration Project

Welcome! This is a hands-on exercise to learn **Git** and **GitHub** collaboration.

---

## 🎯 Your Task

Add your personal profile to `team_data.json` using Git and GitHub.

---

## 📂 What Files Do You Edit?

| File | Do You Edit It? |
| :--- | :--- |
| `team_data.json` | ✅ YES - This is the ONLY file you edit |
| `app.py` | ❌ NO |
| `Dockerfile` | ❌ NO |
| `requirements.txt` | ❌ NO |
| `README.md` | ❌ NO - You're reading this right now! |

---

## 🔴 CRITICAL RULES

1. **Only edit `team_data.json`**
2. **Only edit YOUR placeholder** - Do not change other students' entries
3. **Keep the instructor's entry at the top**
4. **JSON must be valid** - Every comma, quote, and bracket matters
5. **Always `git pull` before `git push`**

---

## 📊 Your Student Assignment

Find your placeholder in `team_data.json` and replace it with your details!

## 📋 Step-by-Step Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_INSTRUCTORS_USERNAME/team-api-builder.git
cd team-api-builder

# Replace 'student1' with YOUR NAME (e.g., 'alice', 'bob')
git checkout -b feature/add-student1

{
    "name": "Student 1",        // CHANGE to your name
    "role": "Placeholder",      // CHANGE to your role
    "tech": "Placeholder"       // CHANGE to your favorite tech
}

{
    "name": "Alice",
    "role": "Frontend Developer",
    "tech": "React"
}

4. Commit and Push

5. Open a Pull Request
Go to the repository on GitHub.com

Click "Compare & pull request"

Title: Add profile for YOUR_NAME

Description: Include your name, role, and favorite tech

Click "Create Pull Request"

6. If You Get a Merge Conflict
If GitHub says there's a conflict:

bash
# Switch to main
git checkout main

# Pull the latest
git pull origin main

# Switch back to your branch
git checkout feature/add-student1

# Merge main into your branch
git merge main
Open team_data.json and:

Delete the <<<<<<<, =======, and >>>>>>> markers

Keep ALL student objects

Add commas between objects (except the last one)

Save the file

Then:

bash
git add team_data.json
git commit -m "resolve merge conflict in team_data.json"
git push origin feature/add-student1
7. Final Sync
Once your Pull Request is merged:

bash
git checkout main
git pull origin main
