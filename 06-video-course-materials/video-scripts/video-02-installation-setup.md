# Video 2: Installing Claude Code 2.0 + GitHub - Your AI Command Center

**Duration**: 15-18 minutes
**Target Audience**: Real estate agents ready to install Claude Code
**Goal**: Get agents fully installed and ready to use Claude Code by end of video

---

## Script Structure

### HOOK (0:00-0:30) - 30 seconds

**[Visual: Clean desktop transforming to AI command center]**

**OPENING LINE:**
"In the next 15 minutes, you're going to transform your computer into an AI-powered real estate command center. By the end of this video, you'll have Claude Code installed, GitHub connected, and you'll run your first command. Let's do this."

**[Title Card: "Installing Claude Code 2.0 + GitHub Setup"]**

---

### SECTION 1: Pre-Installation Checklist (0:30-2:00) - 1.5 minutes

**[Screen recording: Checklist appearing]**

**NARRATION:**
"Before we start, let's make sure you have everything you need. Don't worry, this is all free and straightforward."

**[Checklist on screen]**

**Requirements:**
1. ✅ Computer running Windows 10+, macOS 10.15+, or Linux
2. ✅ Internet connection
3. ✅ About 500MB of free disk space
4. ✅ 30 minutes of focused time
5. ✅ An email address

**[Speaking to camera]**

"That's it. If you have a computer from the last 5 years, you're good to go. We're installing two things today: Claude Code itself, and GitHub Desktop. Both are free."

**[Show browser]**

"Have these websites open:
1. claude.ai/code (for Claude Code)
2. github.com (for GitHub)
3. desktop.github.com (for GitHub Desktop)"

**[Reassuring tone]**

"I'm going to show every click, every step. Pause the video anytime you need to. There's no rush. Let's get started."

---

### SECTION 2: Installing Claude Code - Step by Step (2:00-7:00) - 5 minutes

**[Screen recording: Entire installation process]**

#### Step 1: Download Claude Code

**NARRATION:**
"First, go to claude.ai/code. You'll see the download page."

**[Show website]**

"The website automatically detects your operating system. For me, it's showing macOS. If you're on Windows or Linux, it'll show that instead."

**[Click download button]**

"Click 'Download Claude Code.' The file will start downloading. It's about 200MB, so it might take a minute or two depending on your internet speed."

**[While downloading]**

"While that downloads, let's talk about what Claude Code is actually doing. It's installing a local application that can read and write files on your computer, integrate with Git and GitHub, and communicate with Claude's AI through Anthropic's secure servers."

#### Step 2: Run the Installer

**[Download completes]**

"Okay, download is complete. Let's run the installer."

**[For macOS]**
"On Mac, you'll see a .dmg file. Double-click it. Drag Claude Code to your Applications folder. That's it."

**[Show Windows alternative]**
"On Windows, you'll have a .exe file. Double-click it. Click 'Next' through the installation wizard. Use the default settings—they're perfect."

**[Installation running]**

"The installer is copying files, setting up permissions, adding Claude Code to your system path. This takes about 2 minutes."

#### Step 3: First Launch

**[Installation complete]**

"Installation complete! Let's launch Claude Code for the first time."

**[Open Applications/Start Menu]**

"On Mac, go to Applications and double-click Claude Code. On Windows, search for 'Claude Code' in the Start menu."

**[First launch screen]**

"The first time you launch it, you might see a security prompt. On Mac, go to System Preferences > Security & Privacy and click 'Open Anyway.' On Windows, click 'More Info' then 'Run Anyway.'"

**[Claude Code welcome screen]**

"And here we are! Claude Code welcome screen."

#### Step 4: Authentication

**[Login prompt]**

"Claude Code will ask you to sign in with your Anthropic account. If you use Claude.ai, you already have one. Click 'Sign In.'"

**[Browser opens]**

"Your browser will open to authenticate. Enter your email and password. If you don't have an account, click 'Sign Up'—it's free."

**[Authorization screen]**

"Click 'Authorize Claude Code' to give it permission. This allows Claude Code to use Claude's AI while keeping your data secure."

**[Returns to Claude Code]**

"And we're authenticated! You should see 'Logged in as [your email]' in Claude Code."

#### Step 5: Verify Installation

**[Terminal/Command line in Claude Code]**

"Let's verify everything is working. Open Claude Code's terminal. There's a terminal built right into Claude Code."

**[Type command]**

```bash
claude --version
```

**[Output shows]**

"You should see the version number. Mine shows 'Claude Code version 2.0.1.' If you see this, congratulations—Claude Code is installed!"

**[First interaction]**

"Now let's have your first interaction with Claude Code. Type:"

```
Hello Claude Code! What can you help me with?
```

**[Claude responds]**

"And Claude Code responds! We're in business."

---

### SECTION 3: Installing GitHub Desktop (7:00-10:30) - 3.5 minutes

**[Navigate to desktop.github.com]**

**NARRATION:**
"Now let's install GitHub Desktop. This makes working with GitHub super easy—no command line memorization required."

#### Step 1: Download GitHub Desktop

**[Show website]**

"Go to desktop.github.com. Click 'Download for [Your OS].'"

**[Download starts]**

"Another quick download. While it downloads, quick overview: GitHub Desktop is a visual interface for Git and GitHub. You'll use it to save your work, backup to the cloud, and track changes over time."

#### Step 2: Install GitHub Desktop

**[Run installer]**

"Run the installer. On Mac, drag to Applications. On Windows, run the .exe. Same process as before."

**[Launch GitHub Desktop]**

"Launch GitHub Desktop. First time you open it, you'll see a welcome screen."

#### Step 3: Sign in to GitHub

**[Sign in screen]**

"Click 'Sign in to GitHub.com.' If you don't have a GitHub account yet, click 'Create your free account.'"

**[Show sign-up process]**

"For new accounts:
1. Enter your email
2. Create a password
3. Choose a username
4. Verify your email
5. Done!"

**[Sign in complete]**

"Once you're signed in, GitHub Desktop will say 'Welcome [your name]!'"

#### Step 4: Configure Git

**[Configuration screen]**

"GitHub Desktop will ask you to configure Git. It auto-fills your name and email from your GitHub account. These will appear in your commit history. Click 'Continue.'"

**[Settings confirmation]**

"Perfect. GitHub Desktop is now installed and configured."

---

### SECTION 4: Creating Your First Repository (10:30-14:00) - 3.5 minutes

**[GitHub Desktop main screen]**

**NARRATION:**
"Now for the magic: creating your real estate AI repository. This is where all your work will live."

#### Step 1: Create New Repository

**[Click "Create a New Repository"]**

"In GitHub Desktop, click 'Create a New Repository on your hard drive.'"

**[Form appears]**

**Fill out the form:**
- **Name:** `my-real-estate-ai`
- **Description:** `AI-powered system for real estate intelligence and marketing`
- **Local Path:** Keep the default (usually Documents/GitHub/)
- **Initialize with README:** ✅ Check this
- **Git Ignore:** None for now
- **License:** None

**[Click Create Repository]**

"Click 'Create Repository.' GitHub Desktop creates the folder and initializes Git."

#### Step 2: Publish to GitHub

**[Publish button appears]**

"Now let's backup this repository to GitHub's cloud. Click 'Publish repository.'"

**[Publish dialog]**

"Important: Check 'Keep this code private' unless you specifically want it public. Your business data should be private."

**[Click Publish]**

"Click 'Publish repository.' GitHub Desktop pushes it to GitHub.com."

**[Success message]**

"Success! Your repository is now local and on GitHub.com."

#### Step 3: Open in Claude Code

**[Repository menu]**

"In GitHub Desktop, go to Repository > Open in Terminal (or Open in Visual Studio Code if you have that)."

**[Or manually navigate]**

"Or manually navigate: Open Claude Code, click 'Open Folder,' navigate to Documents/GitHub/my-real-estate-ai, click 'Open.'"

**[Claude Code shows repository]**

"Claude Code now sees your repository! Look at the file explorer on the left—you see your README.md file."

#### Step 4: Your First Command to Claude Code

**[Claude Code interface]**

"Let's have Claude Code do something useful. In the Claude Code terminal or chat, type:"

```
Create a well-organized folder structure for a real estate agent's AI system. Include folders for market intelligence, marketing content, client presentations, and automation scripts. Add a brief README.md explaining the structure.
```

**[Claude Code works]**

"Watch Claude Code work. It's creating folders, writing a README, organizing everything."

**[Shows result]**

"Look at that! Folders created, README updated. Click on the files to see what it wrote."

#### Step 5: Your First Commit

**[GitHub Desktop shows changes]**

"Switch back to GitHub Desktop. See those changes? Claude Code created files, and GitHub Desktop detected them."

**[Commit interface]**

"At the bottom, there's a 'Summary' field. Type:"
```
Initial repository structure
```

"Click 'Commit to main.'"

**[Changes committed]**

"Your first commit! Now click 'Push origin' at the top."

**[Pushed to GitHub]**

"Your changes are now backed up on GitHub.com. You can verify by going to github.com and viewing your repository."

---

### SECTION 5: Verification & Next Steps (14:00-15:30) - 1.5 minutes

**[Checklist appearing]**

**NARRATION:**
"Let's verify everything is set up correctly."

**Verification Checklist:**
- [x] Claude Code installed and running
- [x] Authenticated with Anthropic account
- [x] GitHub account created
- [x] GitHub Desktop installed
- [x] Repository created locally
- [x] Repository published to GitHub
- [x] Claude Code can access repository
- [x] First commit made
- [x] Changes pushed to cloud

**[All checkmarks appear]**

"If you've got checkmarks on all of these, you are ready to go! You now have a fully functional AI-powered real estate system."

**[Show the three components]**

"Here's what you have:
1. **Claude Code**: Your AI assistant that never forgets
2. **Local Repository**: Organized file system for all your work
3. **GitHub Cloud**: Automatic backup accessible anywhere"

**[Encouraging tone]**

"I know that might have felt like a lot, but look what you just did! You set up enterprise-level AI infrastructure. Real estate teams paying thousands per month for CRM systems don't have what you just built."

---

### CALL TO ACTION (15:30-16:00) - 30 seconds

**[Speak directly to camera]**

**NARRATION:**
"In Video 3, we're diving into why GitHub changes everything. You're going to see how persistent context transforms you from a casual AI user into a genuine market expert. This is where it gets really exciting."

**[Subscribe animation]**

"Subscribe and hit the notification bell. Drop a comment: How did the installation go? Any issues? I'll respond to every single one."

**[Download link appears]**

"Download the 'First Commands Cheat Sheet' in the description. It's got 20 useful commands you can run right now."

**[End screen]**

"See you in Video 3!"

---

## Screen Recordings Needed

- [ ] Complete Claude Code installation (macOS)
- [ ] Complete Claude Code installation (Windows)
- [ ] GitHub.com account signup
- [ ] GitHub Desktop installation
- [ ] Repository creation in GitHub Desktop
- [ ] Claude Code opening repository
- [ ] First commands in Claude Code
- [ ] First commit and push workflow

## Graphics Needed

- [ ] Title card
- [ ] Pre-installation checklist
- [ ] Three components diagram (Claude Code + Local + GitHub)
- [ ] Verification checklist
- [ ] Step numbers overlays (Step 1, Step 2, etc.)

## Common Issues & Solutions (Pin in Comments)

**Issue: "Can't install on Mac - Security warning"**
Solution: System Preferences > Security & Privacy > Open Anyway

**Issue: "GitHub Desktop won't sign in"**
Solution: Try signing in through browser first, then retry

**Issue: "Claude Code can't see my repository"**
Solution: File > Open Folder > Navigate to repository location

**Issue: "Command not found: claude"**
Solution: Restart terminal or computer after installation

## Downloadable Resource

**"First Commands Cheat Sheet"** - PDF with:
- 20 useful first commands
- Repository structure examples
- GitHub Desktop shortcuts
- Troubleshooting guide

## YouTube Description Template

```
Installing Claude Code 2.0 + GitHub - Complete Setup Guide for Real Estate Agents

Step-by-step installation of Claude Code and GitHub Desktop. By the end of this video, you'll have a fully functional AI-powered real estate system ready to use!

⏱️ TIMESTAMPS
0:00 - Intro
0:30 - Pre-Installation Checklist
2:00 - Installing Claude Code (Step-by-Step)
7:00 - Installing GitHub Desktop
10:30 - Creating Your First Repository
14:00 - Verification & Next Steps

💻 INSTALLATION LINKS
- Claude Code: https://claude.ai/code
- GitHub Desktop: https://desktop.github.com
- GitHub.com: https://github.com

🎁 FREE DOWNLOAD: First Commands Cheat Sheet
[Link]

📋 REQUIREMENTS
- Windows 10+, macOS 10.15+, or Linux
- 500MB free space
- Internet connection
- 30 minutes

🎬 NEXT VIDEO: Understanding Context - Why GitHub Changes Everything

❓ QUESTIONS?
Comment below! I respond to every question.

---

#ClaudeCode #RealEstateAI #InstallGuide #AIForRealtors #GettingStarted
```

---

*Last Updated: November 2024*
*Video 2 of 20-part series*
