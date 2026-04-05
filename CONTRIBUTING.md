# Contributing to your learning journey

This repo follows a structured workflow powered by MeetaDev Momentum. Here's how to work on each assignment.

## Step-by-step workflow

1. **Get your assignment** from MeetaDev Momentum — it appears in your daily session
2. **Pull latest main:**
   ```bash
   git checkout main && git pull origin main
   ```
3. **Create your feature branch** using the naming convention:
   ```bash
   git checkout -b assignment/week-N-day-N-concept-name
   ```
4. **Write your code** — commit regularly with clear messages
5. **Push your branch:**
   ```bash
   git push -u origin assignment/week-N-day-N-concept-name
   ```
6. **Open a PR** from your branch to `main` on GitHub
7. **Request Alex review** from the MeetaDev platform
8. **Address feedback** if changes are requested — push to the same branch
9. **Alex auto-merges** on approval

## Commit message guidelines

- Use present tense: `Add function to handle errors`
- Not past tense: ~~`Added function to handle errors`~~
- Be specific: reference the concept you're implementing
- Example: `Add useEffect cleanup to prevent memory leaks`

## Need help?

Use the **Ask Alex** button in MeetaDev for hints, explanations, and guided support at any step. Alex knows your learning history and can tailor help to exactly where you are.