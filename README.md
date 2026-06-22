# 🎓 Machine Learning Outreach Workshop Portal

Welcome to the **Machine Learning Outreach Workshop** repository! This project serves as a comprehensive, highly engaging, and interactive curriculum designed to introduce students to the core concepts of Machine Learning (ML), Natural Language Processing (NLP), and career paths in Artificial Intelligence.

This repository hosts both the **Student & Instructor Course Portal** and the individual presentation decks, fully optimized for modern classroom delivery and self-paced student learning.

🚀 **Live Deployment:** [https://drsnigdha.github.io/ml-outreach/](https://drsnigdha.github.io/ml-outreach/)

---

## 🏫 Workshop Curriculum

The workshop is divided into two high-impact, widescreen-optimized presentation sessions:

### 🌅 Session 1: AI Foundations & Real-World Impact

#### 🎓 [Module 1: AI Foundations](https://drsnigdha.github.io/ml-outreach/day1_session1_1.html)
Demystifies what AI is, how cognitive systems learn, and the conceptual boundaries of software.
* **Core Concepts:** Defining Intelligence (Human vs. Artificial), Traditional Coding Limits, the AI Learning Cycle (Data → Model → Training → Prediction).
* **Deep Concepts:** Hard vs. Soft Computing conceptual comparison (Calculator vs. ChatGPT).
* **Interactive Widgets:** AI or Not AI Card Quiz, Train an AI Classification Simulator.

#### 🚀 [Module 2: AI in the Real World](https://drsnigdha.github.io/ml-outreach/day1_session1_2.html)
Explores how AI operates in daily life, historical breakthroughs, and responsible usage.
* **Core Concepts:** A Typical Day with AI Timeline, Generative AI Revolution (2020-2026), Under the Hood of Recommendations (Netflix collaborative filtering) and Smart Assistants (voice vectors).
* **Interactive Widgets:** Daily AI Checklist, Image Generation Prompt Playground.
* **Ethics Checkpoint:** Responsible AI, Deepfakes, and Bias.

### 🌇 Session 2: Machine Learning Deep Dive & Careers

#### 📊 [Module 1: ML Foundations & Regressions](https://drsnigdha.github.io/ml-outreach/day1_session2_1.html)
Demystifies how computers learn from data without explicit programming.
* **Core Concepts:** Telemetry Data, Features vs. Labels, Training vs. Prediction loops.
* **Mathematical Intuition:** Continuous vs. Discrete predictions (Regression vs. Classification).
* **Interactive Widgets:** Training Ratio Slider (80/20 vs 50/50), Decision Boundary Coordinate Grid Adjuster.
* **Validation:** Train-Test Split and evaluating models on unseen data.

#### 🧠 [Module 2: NLP, Careers & Mindsets](https://drsnigdha.github.io/ml-outreach/day1_session2_2.html)
Explores how machines understand human text and guides students toward building a future in AI.
* **Natural Language Processing (NLP):** Bag-of-Words text representation, Tokenization, and Sentiment Classification.
* **Interactive Widgets:** Bag-of-Words Sentiment Classifier, AI Career Explorer Board.
* **Mindset & Recap:** The 3 Human ML Superpowers (Curiosity, Problem Solving, Creativity), Card-Flipping Classroom Quiz, Detective Challenge homework.

---

## 🛠️ Interactive Simulators & Widgets

To maximize student engagement, the presentation decks feature advanced, responsive interactive widgets built from scratch with pure client-side JavaScript:

1. **AI or Not AI Card Quiz (Session 1, Module 1):** A card-flipping conceptual review quiz evaluating if everyday products use AI.
2. **Train an AI Simulator (Session 1, Module 1):** An interactive playground simulating training a classification model by labeling items in real time.
3. **Daily AI Checklist (Session 1, Module 2):** An interactive checklist calculating the student's personal daily AI interaction score.
4. **Image Generation Prompt Playground (Session 1, Module 2):** A live visual simulator translating prompt descriptions into high-fidelity image outputs.
5. **Decision Boundary Adjuster (Session 2, Module 1):** A coordinate grid where students adjust a model's linear boundary line to classify orange and blue data points.
6. **Interactive Training Ratio Slider (Session 2, Module 1):** Simulates how altering the Train-Test Split ratio affects the training and testing records.
7. **Sentiment Analysis Classifier (Session 2, Module 2):** A live text mining widget where students watch the model tokenize text and classify sentiment using a Bag-of-Words dictionary.
8. **AI Career Explorer Board (Session 2, Module 2):** A dashboard displaying objectives, duties, and salaries for core AI professions.
9. **Interactive Classroom Quiz (Session 2, Module 2):** A card-flipping conceptual review quiz.

---

## 🧑‍🏫 Instructor & Presenter Guide

The presentations are designed with widescreen, cinematic keynote layouts, making them highly legible from the back of large classrooms. 

### ⌨️ Navigation Shortcuts
When presenting, use these keyboard shortcuts to navigate smoothly:
* **Next Slide:** Press `Right Arrow`, `Spacebar`, `Page Down`, or swipe left on mobile.
* **Previous Slide:** Press `Left Arrow`, `Page Up`, or swipe right on mobile.
* **🖥️ Projector Fullscreen Mode:** Double-click anywhere on the slide or press **`F`** to toggle full-screen classroom presentation mode.
* **🎯 Escape Projector Mode:** Press **`Esc`** to exit full-screen mode.

---

## 💻 Local Development & Setup

Since the entire portal and presentation decks are built as static, self-contained files, there are **zero server-side dependencies** or build steps! You can run the entire workshop locally without even needing an internet connection.

### 1. Clone the Repository
```bash
git clone https://github.com/drsnigdha/ml-outreach.git
cd ml-outreach
```

### 2. Run Locally
Simply double-click `index.html` to open the portal in any modern web browser, or serve it using a lightweight local server:
```bash
# Python 3
python3 -m http.server 8000

# Node.js
npx serve .
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

### 🛡️ 3. Activate Automated Slide Protection (Git Hooks)
To guarantee that you never accidentally break the HTML structure or introduce JavaScript syntax errors while editing the slides, this repository is equipped with an automated pre-commit validation suite.

To activate these hooks on your local machine, run the following one-click setup script:
```bash
chmod +x setup_hooks.sh && ./setup_hooks.sh
```

Once activated, Git will automatically run the structural and compilation validators every time you run `git commit`. If there are any errors, the commit will be blocked and you will receive a detailed report, ensuring the live website is always 100% stable and correct!

---

## 🌐 Technical Architecture

This project is built using modern web standards designed for speed, portability, and zero-maintenance hosting:
* **Frontend Structure:** Semantically structured HTML5.
* **Aesthetics & Styling:** Utility-first styling via Tailwind CSS (via CDN) combined with custom CSS animations.
* **Icons:** High-fidelity vector icons from FontAwesome 6.4.0.
* **Logic & Interactivity:** Compiler-verified Vanilla JavaScript (compiled and validated using Node.js syntax trees to guarantee zero runtime errors).
* **Deployment:** Hosted for free on **GitHub Pages** with automatic builds triggered on pushes to the `main` branch.
