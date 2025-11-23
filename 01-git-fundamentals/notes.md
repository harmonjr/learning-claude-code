# Git Fundamentals for Real Estate Agents

## What is Git?

Git is a **version control system** - software that tracks changes to files over time. Think of it like "Track Changes" in Microsoft Word, but much more powerful and for entire projects.

### Why Git Matters for Real Estate Agents

Without Git:
- ❌ Lost work if computer crashes
- ❌ No way to undo changes from last week
- ❌ "final_final_FINAL_v2" file naming chaos
- ❌ Can't collaborate without overwriting each other's work
- ❌ Claude Code forgets everything between sessions

With Git:
- ✅ Complete history of all changes
- ✅ Ability to go back to any previous version
- ✅ Organized, clean file system
- ✅ Team can work together smoothly
- ✅ Claude Code remembers everything forever
- ✅ Automatic backup to cloud (GitHub)

---

## Core Concepts

### Repository (Repo)
A folder that Git is tracking. Your `my-real-estate-ai` folder is a repository.

**Real Estate Analogy**: Think of it like an MLS listing folder, but instead of just holding the current listing info, it holds every version of the listing you've ever created.

### Commit
A saved snapshot of your project at a specific point in time.

**Real Estate Analogy**: Like taking a photo of a property at different stages of renovation. You can always look back at what it looked like at each stage.

### Branch
A separate version of your project where you can try new things without affecting the main version.

**Real Estate Analogy**: Like creating a "what if" scenario for a listing - test a luxury staging approach on one branch and a cozy staging approach on another, then keep whichever works better.

### Remote
A copy of your repository stored in the cloud (GitHub).

**Real Estate Analogy**: Like having your listing photos backed up to the cloud instead of just on your phone.

### Push
Sending your local commits to the remote repository (GitHub).

**Real Estate Analogy**: Uploading photos from your phone to the MLS.

### Pull
Downloading changes from the remote repository to your local computer.

**Real Estate Analogy**: Syncing the latest MLS updates to your computer.

---

## The 7 Essential Git Commands

### 1. `git status`
**What it does**: Shows what's changed in your repository

**When to use it**: All the time! Before committing, after making changes, when you're unsure what's happening.

**Example**:
```bash
git status
```

**Output**:
```
On branch main
Changes not staged for commit:
  modified:   03-market-intelligence/market-reports/weekly-report.md

Untracked files:
  04-marketing-content/social-media/new-post.md
```

**Translation**: "You modified the weekly report, and you have a new social media post that Git isn't tracking yet."

---

### 2. `git add`
**What it does**: Stages files for committing (tells Git which changes you want to save)

**When to use it**: After creating or modifying files, before committing

**Examples**:
```bash
# Add a specific file
git add 04-marketing-content/social-media/new-post.md

# Add all files in a folder
git add 03-market-intelligence/

# Add everything in the repository
git add .
```

**Real Estate Analogy**: Selecting which photos to upload to the MLS (not every photo makes the cut).

---

### 3. `git commit`
**What it does**: Saves a snapshot of your staged changes with a descriptive message

**When to use it**: After staging files with `git add`

**Examples**:
```bash
# Commit with a message
git commit -m "Add weekly market report for Nov 22"

# Commit with a detailed message
git commit -m "Create buyer presentation template

- Added slides for market overview
- Included neighborhood comparison
- Created buyer checklist section"
```

**Best Practices for Commit Messages**:
✅ **Good**:
- "Add listing description for 123 Main St"
- "Update market report with Q4 data"
- "Fix typo in email campaign template"
- "Create social media calendar for December"

❌ **Bad**:
- "stuff"
- "changes"
- "asdf"
- "final version"

**Pro Tip**: Write commit messages as if completing this sentence: "This commit will..."
- "This commit will... add listing description for 123 Main St"

---

### 4. `git push`
**What it does**: Uploads your local commits to GitHub (cloud backup)

**When to use it**: At least daily, or after completing a meaningful chunk of work

**Examples**:
```bash
# Push to main branch
git push origin main

# First time pushing a new branch
git push -u origin new-branch-name
```

**Why it matters**: Your work is only backed up after you push. If your computer crashes before you push, those commits are lost.

**Best Practice**: Push every evening before closing your computer.

---

### 5. `git pull`
**What it does**: Downloads changes from GitHub to your local computer

**When to use it**:
- When starting work for the day
- Before making new changes
- When working across multiple devices
- When collaborating with team members

**Example**:
```bash
git pull origin main
```

**Real Estate Scenario**:
- You make changes on your office computer and push
- That evening at home, you `git pull` to get those changes
- You make more changes at home and push
- Next morning at the office, you `git pull` to get last night's work

---

### 6. `git log`
**What it does**: Shows the history of commits

**When to use it**: When you want to see what's changed over time, or find a specific past version

**Examples**:
```bash
# Simple one-line format (easiest to read)
git log --oneline

# Detailed format
git log

# See last 5 commits
git log --oneline -5

# See commits from specific author
git log --author="Randy"
```

**Example Output**:
```
a1b2c3d Add weekly market report for Nov 22
e4f5g6h Create buyer email drip campaign
i7j8k9l Update listing description template
```

**Each line shows**:
- Commit ID (a1b2c3d)
- Commit message

---

### 7. `git diff`
**What it does**: Shows exactly what changed in files

**When to use it**: Before committing, to review what you're about to save

**Examples**:
```bash
# See all changes not yet staged
git diff

# See changes in a specific file
git diff weekly-report.md

# See changes staged for commit
git diff --staged
```

**Example Output**:
```diff
- Median Price: $450,000
+ Median Price: $475,000

- 15 new listings
+ 22 new listings
```

Lines starting with `-` were removed
Lines starting with `+` were added

**Pro Tip**: Always run `git diff` before committing to make sure you're saving what you think you are.

---

## Common Workflows

### Daily Workflow

**Morning**:
```bash
# Start your day
git pull origin main          # Get latest changes

# Work on your files
# (create reports, write content, etc.)

# Check what you changed
git status                    # See what's changed
git diff                      # Review the changes
```

**Evening**:
```bash
# Save your work
git add .                     # Stage all changes
git commit -m "Daily update: market reports and email campaigns"
git push origin main          # Backup to cloud

# Done! Your work is saved and backed up.
```

---

### Creating New Content Workflow

```bash
# Create or modify files using Claude Code
# Claude Code creates: 04-marketing-content/email-campaigns/new-campaign.md

# Stage the new file
git add 04-marketing-content/email-campaigns/new-campaign.md

# Commit it
git commit -m "Create new buyer email campaign"

# Push to cloud
git push origin main
```

---

### Checking Your Work Workflow

```bash
# Did I make changes I forgot about?
git status

# What exactly did I change?
git diff

# What have I been working on this week?
git log --oneline --since="1 week ago"

# Let me see that market report from 2 weeks ago
git log --oneline                    # Find the commit ID
git show a1b2c3d:path/to/file.md    # View that version
```

---

## Working with Branches

### What Are Branches For?

Branches let you experiment without breaking your main work.

**Real Estate Examples**:

**Scenario 1**: Testing two email campaign approaches
```bash
# Create a branch for approach A
git checkout -b email-campaign-personalized

# Create campaign
# Test it

# If it works, merge it back
git checkout main
git merge email-campaign-personalized

# If it doesn't work, just delete the branch
git branch -d email-campaign-personalized
```

**Scenario 2**: Redesigning your listing template
```bash
# Create experiment branch
git checkout -b listing-template-redesign

# Make changes
# Test with real listings

# If you like it, keep it
git checkout main
git merge listing-template-redesign

# If you don't, abandon it
git checkout main
git branch -D listing-template-redesign
```

### Branch Commands

```bash
# See all branches
git branch

# Create new branch
git branch new-branch-name

# Switch to a branch
git checkout branch-name

# Create and switch in one command
git checkout -b new-branch-name

# Merge branch into main
git checkout main
git merge branch-name

# Delete a branch
git branch -d branch-name

# Delete a branch (force, even if not merged)
git branch -D branch-name
```

---

## Collaborating with Team Members

### Setup
1. Invite collaborator to your GitHub repository
2. They clone the repository: `git clone [repository-url]`
3. Now you both have the same repository

### Workflow

**You**:
```bash
# Make changes
git add .
git commit -m "Update market report"
git push origin main
```

**Your Team Member**:
```bash
# Get your changes
git pull origin main

# Make their own changes
git add .
git commit -m "Add neighborhood profiles"
git push origin main
```

**You Again**:
```bash
# Get their changes
git pull origin main

# Now you have their neighborhood profiles!
```

### Avoiding Conflicts

**Best Practices**:
1. Always `git pull` before starting work
2. Communicate about which files you're working on
3. Push frequently so others can see your changes
4. Work in different files when possible

---

## Understanding Merge Conflicts

### What's a Merge Conflict?

When you and a teammate edit the same part of the same file differently, Git doesn't know which version to keep.

**Example Conflict**:

You wrote:
```
Median Price: $450,000
```

Your teammate wrote:
```
Median Price: $475,000
```

When you try to merge, Git shows:
```
<<<<<<< HEAD
Median Price: $450,000
=======
Median Price: $475,000
>>>>>>> their-branch
```

### How to Resolve

1. Open the file
2. Decide which version to keep (or combine them)
3. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Save the file
5. `git add` the file
6. `git commit` to complete the merge

**For our example**, maybe the correct answer is:
```
Median Price: $475,000
```

So you:
1. Delete the conflict markers
2. Keep the correct line
3. `git add weekly-report.md`
4. `git commit -m "Resolve market report price conflict"`

---

## Common Mistakes & How to Fix Them

### Mistake 1: Committed to wrong branch

```bash
# Oops, I committed to main but meant to use a branch
git branch new-feature-branch    # Create the branch (it includes the commit)
git reset --hard HEAD~1          # Remove commit from main
git checkout new-feature-branch  # Switch to the branch (commit is here)
```

### Mistake 2: Committed wrong files

```bash
# Undo last commit but keep the changes
git reset --soft HEAD~1

# Now re-stage only the files you want
git add correct-file.md
git commit -m "Correct commit"
```

### Mistake 3: Want to undo all local changes

```bash
# Discard all local changes (careful! This can't be undone)
git reset --hard HEAD

# Discard changes in one file
git checkout -- filename.md
```

### Mistake 4: Accidentally deleted a file

```bash
# Restore deleted file
git checkout HEAD filename.md
```

### Mistake 5: Need to go back to previous commit

```bash
# See history
git log --oneline

# Go back to specific commit (creates new commit)
git revert a1b2c3d

# Or reset to specific commit (destructive)
git reset --hard a1b2c3d
```

---

## Letting Claude Code Handle Git

### The Easy Way

Instead of memorizing all these commands, just ask Claude Code:

```
"Claude Code, commit my changes with an appropriate message"
"Claude Code, show me what's changed"
"Claude Code, push to GitHub"
"Claude Code, create a branch called test-new-template"
```

Claude Code will run the appropriate Git commands for you!

---

## Best Practices Summary

### Commit Often
✅ Commit after each meaningful change
✅ Better to have many small commits than one giant commit
✅ Think: "If I needed to undo this later, what would make sense as a unit?"

### Write Good Messages
✅ Be specific: "Add listing description for 123 Main St"
✅ Use present tense: "Add" not "Added"
✅ Start with a verb: "Create", "Update", "Fix", "Remove"

### Push Daily
✅ Push to GitHub at least once per day
✅ Your work is only backed up after pushing
✅ Makes collaboration smoother

### Pull Before Working
✅ Always `git pull` when starting work
✅ Prevents conflicts
✅ Ensures you have latest changes

### Keep Main Clean
✅ Main branch should always work
✅ Use branches for experiments
✅ Only merge when tested and ready

---

## Next Steps

1. **Practice**: Try all 7 commands with your repository
2. **Daily Habit**: Make Git part of your daily workflow
3. **Experiment**: Create a branch and try something new
4. **Collaborate**: If you have a team, start sharing the repository
5. **Trust the Process**: Git seems complicated at first, but becomes second nature

---

*Last Updated: November 2024*
*Next: Complete practice exercises*
