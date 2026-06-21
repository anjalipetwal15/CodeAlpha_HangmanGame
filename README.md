# 🎮 CodeAlpha Hangman Game - Task 1

**Internship Domain:** Python Programming  
**Submitted By:** Anjali Petwal  
**Organization:** CodeAlpha  

## 📝 Project Overview
This is a command-line based Hangman game developed as Task 1 for the CodeAlpha Python Programming Internship. The game challenges users to guess a hidden word letter by letter before running out of attempts. 

To make it more engaging, I've added a **category-based hint system** that gives players clues about the word type instead of revealing letters directly.

## ✨ Key Features
- **25+ Unique Words** across 5 categories: Technology, Career Opportunity, Nature, Daily Use, and Abstract
- **Smart Hint System**: Type `hint` to reveal the word's category. Max 2 hints per game to keep it challenging
- **Score Tracking**: Get +10 points for correct guess, -5 for wrong guess. Final score shown on win/loss
- **Dynamic Feedback**: Shows remaining attempts, guessed letters, and win/loss messages with emojis
- **Input Validation**: Handles duplicate guesses, numbers, special characters, and multi-letter inputs
- **Clean Terminal UI**: Easy to read interface with clear instructions

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries Used:** `random` module only - no external dependencies

## 🚀 How to Run This Project
1. **Clone the repository:**
   ```bash
   git clone https://github.com/anjalipetwal15/CodeAlpha_HangmanGame.git
