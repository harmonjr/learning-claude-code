# Claude Code Skills: Complete Guide

## What Are Skills?

Skills are specialized capabilities you can add to Claude Code to perform specific tasks efficiently. Think of them as expert assistants for particular jobs—instead of writing detailed prompts every time, you activate a Skill that already knows how to do the task.

## Why Skills Matter for Real Estate Agents

### Without Skills:
```
Every time you need a listing description, you write:
"Create a compelling listing description for a 4-bedroom house at 123 Main St.
Include features like hardwood floors, updated kitchen, large backyard.
Use professional but warm tone. Highlight neighborhood amenities.
Format with bullet points..."
```

### With Skills:
```
/listing-description 123 Main St
```

The Skill already knows:
- Your preferred tone and style
- Standard format and structure
- What features to highlight
- Local neighborhood context
- SEO best practices

## Types of Skills

### 1. Content Generation Skills
Create marketing materials, descriptions, and content

**Examples:**
- **Listing Description Generator**: Creates compelling property descriptions
- **Email Campaign Writer**: Generates drip campaign sequences
- **Social Media Scheduler**: Plans and writes social posts
- **Blog Post Creator**: Writes neighborhood guides and market updates

### 2. Research Skills
Gather and analyze information

**Examples:**
- **Market Research Assistant**: Compiles market statistics and trends
- **Neighborhood Profiler**: Researches area demographics, schools, amenities
- **Competitive Analyzer**: Tracks competitor strategies and performance
- **Property Investigator**: Due diligence research on properties

### 3. Data Processing Skills
Transform and analyze data

**Examples:**
- **CMA Generator**: Comparative Market Analysis creation
- **Investment Analyzer**: ROI and cash flow calculations
- **Price Trend Tracker**: Historical price analysis and predictions
- **Lead Scorer**: Prioritizes leads based on criteria

### 4. Workflow Skills
Automate multi-step processes

**Examples:**
- **New Listing Workflow**: From photos to MLS to marketing
- **Client Onboarding**: Complete buyer/seller setup process
- **Transaction Checklist**: Step-by-step transaction management
- **Morning Briefing**: Daily market and task summary

## Skill Structure

### Basic Skill Anatomy

```yaml
name: listing-description-generator
version: 1.0
description: Creates compelling listing descriptions for residential properties

inputs:
  - address: string (required)
  - property_type: string (optional, default: single-family)
  - key_features: list (optional)
  - target_buyer: string (optional)

outputs:
  - description: markdown formatted listing description
  - headline: catchy headline for ads
  - social_snippet: short version for social media

behavior:
  tone: professional yet warm
  style: benefit-focused, emotionally engaging
  format: headline + paragraph + bullet points + call-to-action

context_files:
  - 04-marketing-content/listing-packages/template.md
  - 03-market-intelligence/neighborhood-profiles/
```

### Skill Components

1. **Metadata**: Name, version, description
2. **Inputs**: What information the Skill needs
3. **Outputs**: What the Skill produces
4. **Behavior**: How the Skill should act
5. **Context**: What repository files it should reference

## Creating Your First Custom Skill

### Step 1: Identify a Repeated Task

Look for tasks you do frequently with similar patterns:
- ✅ Writing listing descriptions
- ✅ Creating market reports
- ✅ Drafting client emails
- ✅ Researching neighborhoods

### Step 2: Document Your Best Example

Take your best version of this task:
- Save it as a template
- Note what makes it effective
- Identify the variables that change
- Document your decision-making process

### Step 3: Create the Skill File

```yaml
# 02-skills-library/custom-skills/market-report-generator.yaml

name: weekly-market-report
version: 1.0
description: Generates comprehensive weekly market report for your territory

inputs:
  - week_ending: date (required)
  - neighborhoods: list (optional, default: all tracked)
  - include_graphs: boolean (optional, default: true)

outputs:
  - report: markdown formatted report
  - summary: email-ready summary
  - social_posts: 3 social media posts highlighting key insights

behavior:
  analyze:
    - new listings count and average price
    - sales volume and median price
    - days on market trends
    - inventory levels
    - price per square foot changes

  compare:
    - week over week
    - month over month
    - year over year

  highlight:
    - significant changes (>10%)
    - emerging trends
    - buyer/seller opportunities

  tone: authoritative expert, accessible to consumers

context_files:
  - 03-market-intelligence/market-reports/
  - 03-market-intelligence/neighborhood-profiles/

template: |
  # Market Report - Week Ending {week_ending}

  ## Executive Summary
  {Generate 3-4 sentence overview of key trends}

  ## New Listings
  {Analyze new inventory}

  ## Sales Activity
  {Analyze closed sales}

  ## Market Trends
  {Identify and explain trends}

  ## Opportunities
  {Highlight actionable insights for buyers/sellers}

  ## Forecast
  {Brief outlook for next 30 days}
```

### Step 4: Test and Refine

```
# Test the Skill
/weekly-market-report week_ending="2024-11-22"

# Review output
# Adjust parameters
# Refine template
# Test again
```

### Step 5: Document and Share

Create documentation:
```markdown
# Weekly Market Report Skill

## Purpose
Generates comprehensive weekly market analysis

## How to Use
`/weekly-market-report week_ending="YYYY-MM-DD"`

## Inputs
- week_ending: Required. Format: YYYY-MM-DD
- neighborhoods: Optional. Comma-separated list
- include_graphs: Optional. true/false

## Outputs
- Full markdown report
- Email summary version
- Social media posts

## Examples
`/weekly-market-report week_ending="2024-11-22" neighborhoods="Downtown,Myers Park"`

## Tips
- Run every Monday for previous week
- Commit report to market-reports/ folder
- Use email summary for newsletter
- Post social snippets throughout the week
```

## Pre-Built Skills for Real Estate

### Must-Have Skills to Install

#### 1. Market Analysis Suite
- **Market Report Generator**: Weekly/monthly market summaries
- **CMA Creator**: Comparative Market Analysis
- **Price Trend Analyzer**: Historical price analysis
- **Inventory Tracker**: Supply and demand monitoring

#### 2. Marketing Content Suite
- **Listing Package Creator**: Complete listing marketing
- **Social Media Planner**: Content calendar generation
- **Email Sequence Builder**: Drip campaign creation
- **Blog Post Writer**: SEO-optimized articles

#### 3. Client Service Suite
- **Buyer Consultation Package**: Complete buyer presentation
- **Seller Consultation Package**: Complete seller presentation
- **Property Research Report**: Due diligence automation
- **Transaction Checklist**: Step-by-step task management

#### 4. Business Operations Suite
- **Meeting Prep Assistant**: Client meeting preparation
- **Follow-up Manager**: Client communication tracking
- **Team Training Creator**: Process documentation
- **Performance Dashboard**: Business metrics tracking

## Advanced Skill Techniques

### Chaining Skills

Run multiple Skills in sequence:
```
1. /property-research address="123 Main St"
2. /listing-description address="123 Main St" features={from step 1}
3. /marketing-plan listing={from step 2}
```

### Conditional Logic

Skills can make decisions:
```yaml
behavior:
  if property_price > 1000000:
    tone: sophisticated, luxury-focused
    platforms: ["Instagram", "Facebook", "Luxury Website"]
  else if property_price > 500000:
    tone: professional, upscale
    platforms: ["Instagram", "Facebook", "Zillow"]
  else:
    tone: warm, accessible, first-time-buyer friendly
    platforms: ["Facebook", "Zillow", "Community Groups"]
```

### Context-Aware Skills

Skills that learn from your repository:
```yaml
behavior:
  analyze_past_successes:
    - review past listing descriptions in 04-marketing-content/
    - identify highest-performing language patterns
    - note which features generated most interest
    - replicate successful approaches

  maintain_brand_voice:
    - read all previous content
    - extract tone and style patterns
    - ensure consistency
```

## Skill Management Best Practices

### Organization
```
02-skills-library/
├── installed-skills/        # Community/marketplace Skills
│   ├── README.md           # Index of installed Skills
│   └── {skill-files}
├── custom-skills/          # Your custom Skills
│   ├── README.md           # Documentation
│   ├── marketing/          # Marketing Skills
│   ├── research/           # Research Skills
│   └── workflows/          # Multi-step Skills
└── skills-analysis.md      # Performance tracking
```

### Version Control
- Commit Skills to Git
- Track changes over time
- Branch for testing new versions
- Tag stable releases
- Document improvements

### Documentation
Each Skill should have:
- Purpose and use case
- Input parameters
- Output format
- Usage examples
- Performance notes
- Version history

### Performance Tracking
```markdown
# skills-analysis.md

## Skill Performance Log

### Listing Description Generator
- **Created**: 2024-10-15
- **Times Used**: 47
- **Avg Time Saved**: 25 minutes
- **Total Time Saved**: 19.6 hours
- **Quality Rating**: 4.8/5
- **Notes**: Excellent for traditional homes, needs refinement for luxury properties

### Weekly Market Report
- **Created**: 2024-10-20
- **Times Used**: 8 (weekly)
- **Avg Time Saved**: 1.5 hours
- **Total Time Saved**: 12 hours
- **Quality Rating**: 5/5
- **Notes**: Consistent, reliable, clients love the format
```

## Common Skill Patterns

### Template Pattern
```yaml
# Skill fills in a template with variable data
template: |
  # {Title}
  {Body}
  {Call-to-Action}
```

### Research Pattern
```yaml
# Skill gathers information from multiple sources
sources:
  - web_search
  - repository_files
  - context_data
analyze: synthesize and summarize
output: structured report
```

### Generation Pattern
```yaml
# Skill creates new content from scratch
inputs: parameters
process: creative generation
output: original content
```

### Analysis Pattern
```yaml
# Skill examines data and provides insights
inputs: data or files
process: pattern recognition, trend analysis
output: insights and recommendations
```

## Skill Development Workflow

### 1. Identify Need
- Notice repeated tasks
- Time task to measure savings potential
- Document current manual process

### 2. Design Skill
- Define inputs needed
- Specify desired outputs
- Determine behavior requirements
- Identify context files needed

### 3. Build Prototype
- Create basic Skill file
- Test with simple example
- Iterate on outputs

### 4. Refine
- Test with edge cases
- Adjust parameters
- Improve prompts
- Optimize context

### 5. Document
- Write usage guide
- Create examples
- Note limitations
- Track performance

### 6. Share (Optional)
- Clean up for others
- Add comprehensive docs
- Share with team
- Contribute to community

## Troubleshooting Skills

### Skill Doesn't Produce Expected Output
- ✅ Check input parameters are correct
- ✅ Verify context files exist and are accessible
- ✅ Review Skill configuration for errors
- ✅ Test with simpler example
- ✅ Check Claude Code version compatibility

### Skill Is Too Slow
- ✅ Reduce context files loaded
- ✅ Simplify processing logic
- ✅ Cache frequently used data
- ✅ Split into smaller Skills

### Skill Output Quality Is Poor
- ✅ Improve prompt engineering
- ✅ Add better examples
- ✅ Provide more context
- ✅ Refine behavior parameters

### Skill Conflicts with Others
- ✅ Check for naming conflicts
- ✅ Review context file overlaps
- ✅ Ensure clear Skill boundaries
- ✅ Rename if necessary

## Learning Path: Skills Mastery

### Week 1: Understanding Skills
- Install 3-5 pre-built Skills
- Use them for real tasks
- Observe how they work
- Document results

### Week 2: Customizing Skills
- Modify existing Skill parameters
- Adjust for your specific needs
- Test different configurations
- Track improvements

### Week 3: Building Simple Skills
- Create your first custom Skill
- Start with template pattern
- Test and refine
- Document thoroughly

### Week 4: Advanced Skills
- Build research or analysis Skill
- Implement conditional logic
- Chain multiple Skills
- Optimize performance

### Week 5: Skill Library
- Create 5+ custom Skills
- Organize systematically
- Document comprehensively
- Share with team

## Real Estate Agent Skill Starter Pack

### Essential 10 Skills to Create First

1. **Listing Description Generator**: Save 25 min per listing
2. **Weekly Market Report**: Save 1.5 hours per week
3. **Social Media Calendar**: Save 3 hours per month
4. **Email Drip Campaign**: Save 4 hours per campaign
5. **Buyer Presentation**: Save 1 hour per buyer
6. **Seller Presentation**: Save 1 hour per seller
7. **Property Research**: Save 45 min per property
8. **Open House Promotion**: Save 30 min per open house
9. **Client Follow-up**: Save 15 min per client
10. **Morning Briefing**: Save 30 min per day

**Total Time Savings**: 20+ hours per week

## Next Steps

1. **Explore**: Review Skills in `02-skills-library/`
2. **Install**: Add 3 pre-built Skills relevant to your work
3. **Practice**: Use installed Skills for real tasks this week
4. **Create**: Build your first custom Skill by end of week
5. **Document**: Track time saved and quality improvements

---

*Last Updated: November 2024*
*Next: Start creating your first custom Skill!*
