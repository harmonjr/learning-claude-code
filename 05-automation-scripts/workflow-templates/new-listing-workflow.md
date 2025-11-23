# New Listing Workflow Template

## Overview
This workflow automates the complete process of taking a new listing from initial information to fully marketed property.

**Total Time**: ~30 minutes (vs 3-4 hours manual)
**Tools Required**: Claude Code, MLS access, photo editing software

---

## Phase 1: Property Information Gathering (5 min)

### Step 1: Collect Listing Details
Create a file: `99-sandbox/new-listing-[address].md`

```markdown
# New Listing Information

## Basic Details
- Address:
- Price:
- Bedrooms:
- Bathrooms:
- Square Feet:
- Lot Size:
- Year Built:
- Property Type:
- MLS#:

## Key Features
-
-
-

## Seller Goals
- Timeline:
- Motivation:
- Special Considerations:

## Target Buyer
-

## Photo Count:
## Notable Upgrades:
## Neighborhood:
```

### Step 2: Property Research
**Claude Code Prompt**:
```
Research [address] and provide:
- Recent comparable sales within 0.5 miles
- Current competitive listings
- Neighborhood highlights
- School information
- Market positioning recommendation

Save to 99-sandbox/new-listing-[address]-research.md
```

---

## Phase 2: Listing Description & Marketing Copy (10 min)

### Step 3: Generate Listing Description
**Claude Code Prompt**:
```
Using the listing-description-generator Skill, create a complete listing
description for [address] with these details: [paste from Step 1].

Generate:
1. Full MLS description (1000 chars)
2. Short version for social (250 chars)
3. Email version (500-750 chars)
4. SEO keywords

Tone: [professional/luxury/warm based on property]
Target Buyer: [from Step 1]

Save to 04-marketing-content/listing-packages/[address]/description.md
```

### Step 4: Create Property Feature Sheet
**Claude Code Prompt**:
```
Create a one-page property feature sheet for [address] with:
- Eye-catching headline
- Property highlights (bullets)
- Key statistics
- Neighborhood benefits
- Call to action

Format as markdown for easy PDF conversion.
Save to 04-marketing-content/listing-packages/[address]/feature-sheet.md
```

---

## Phase 3: Social Media & Email Content (10 min)

### Step 5: Social Media Posts
**Claude Code Prompt**:
```
Create a complete social media package for new listing at [address]:

1. Instagram carousel (5 slides):
   - Slide 1: Announcement with curb appeal
   - Slide 2: Key features
   - Slide 3: Best interior photo highlight
   - Slide 4: Neighborhood/lifestyle
   - Slide 5: CTA for showings

2. Facebook post (longer format with details)

3. Instagram Stories series (3-5 stories)

4. LinkedIn post (professional tone)

5. 5 different caption variations

Include relevant hashtags for each platform.
Save to 04-marketing-content/listing-packages/[address]/social-media.md
```

### Step 6: Email Campaign
**Claude Code Prompt**:
```
Create email announcements for new listing at [address]:

1. Email to existing client database (warm introduction)
2. Email to neighborhood residents (Just Listed in Your Area)
3. Email to buyer prospects (matching criteria)
4. Email to real estate agent network (co-op opportunity)

Each should have:
- Compelling subject line
- Engaging copy
- Clear CTA
- Property highlights

Save to 04-marketing-content/listing-packages/[address]/email-campaigns.md
```

---

## Phase 4: Open House & Showing Materials (5 min)

### Step 7: Open House Announcements
**Claude Code Prompt**:
```
Create open house marketing for [address] on [date] from [time]:

1. Facebook Event description
2. Instagram announcement post
3. Nextdoor post
4. Email invitation
5. Printable flyer copy
6. Directional sign text

Save to 04-marketing-content/listing-packages/[address]/open-house.md
```

### Step 8: Showing Instructions & Agent Remarks
**Claude Code Prompt**:
```
Create:
1. Showing instructions for other agents
2. Agent-only remarks highlighting investment value
3. Property highlights sheet for buyer agents
4. FAQ document anticipating agent questions

Save to 04-marketing-content/listing-packages/[address]/agent-materials.md
```

---

## Phase 5: Video & Advanced Marketing (Optional, 10 min)

### Step 9: Video Scripts
**Claude Code Prompt**:
```
Create video scripts for [address]:

1. 60-second property tour script
2. 15-second Instagram Reel script
3. Neighborhood spotlight script (2-3 minutes)
4. Agent introduction to property (for sending to prospects)

Include shot suggestions and talking points.
Save to 04-marketing-content/listing-packages/[address]/video-scripts.md
```

### Step 10: Blog Post / Long-Form Content
**Claude Code Prompt**:
```
Write a blog post: "Just Listed: [Compelling Headline for Address]"

Include:
- Why this property is special
- Neighborhood context
- Market opportunity
- Lifestyle description
- Visual storytelling

800-1200 words, SEO optimized.
Save to 04-marketing-content/listing-packages/[address]/blog-post.md
```

---

## Phase 6: Organization & Distribution (5 min)

### Step 11: Create Listing Package Folder Structure
```
04-marketing-content/listing-packages/[address]/
├── description.md
├── feature-sheet.md
├── social-media.md
├── email-campaigns.md
├── open-house.md
├── agent-materials.md
├── video-scripts.md
├── blog-post.md
├── photos/
└── final-exports/
```

### Step 12: Commit to Git
```bash
git add 04-marketing-content/listing-packages/[address]/
git commit -m "Add complete listing package for [address]"
git push origin main
```

---

## Phase 7: Deployment Checklist

### Immediate Actions (Day 1)
- [ ] Upload to MLS with full description
- [ ] Post to social media (all platforms)
- [ ] Send email to client database
- [ ] Create Facebook Event for open house
- [ ] Update personal website
- [ ] Send to agent network

### Week 1
- [ ] Post to Zillow, Trulia, Realtor.com
- [ ] Schedule Instagram Stories series
- [ ] Send neighborhood email blast
- [ ] Print feature sheets
- [ ] Create property-specific landing page
- [ ] Schedule social media posts for week

### Ongoing
- [ ] Share social posts 2-3x per week
- [ ] Send weekly updates to seller
- [ ] Adjust marketing based on feedback
- [ ] Track showing feedback
- [ ] Update pricing strategy as needed

---

## Automation Opportunities

### Python Script: Image Processor
```python
# Automatically resize and optimize listing photos
# Save to 05-automation-scripts/python-scripts/photo-processor.py

import os
from PIL import Image

def process_listing_photos(input_folder, output_folder):
    # Resize to standard MLS dimensions
    # Optimize file size
    # Create thumbnails
    # Watermark if needed
    pass
```

### Scheduled Task: Weekly Listing Report
Create a weekly automated report showing:
- Days on market
- Showing count
- Online engagement metrics
- Comparable sales updates
- Pricing recommendation

---

## Success Metrics

### Track for Each Listing:
- **Time to Market**: How long from info gathering to MLS
- **Engagement**: Social media impressions, clicks, shares
- **Showings**: Number of showings in first week
- **Quality**: Buyer agent feedback
- **Results**: Days on market, sale price vs list price

### Workflow Improvements:
- Document time saved per listing
- Note which marketing materials performed best
- Refine prompts based on results
- Update Skills with learnings

---

## Customization for Different Property Types

### Luxury Properties ($1M+)
- Emphasize: Sophisticated tone, lifestyle, exclusivity
- Additional content: Virtual tour script, luxury publication write-ups
- Extended description: More detail on high-end finishes

### First-Time Buyer Properties
- Emphasize: Affordability, neighborhood, starter home appeal
- Additional content: Buyer education materials, financing info
- Tone: Warm, accessible, encouraging

### Investment Properties
- Emphasize: ROI, cash flow, rental potential
- Additional content: Investment analysis, rental comps
- Tone: Data-driven, analytical

---

## Template Customization

### Adapt This Workflow:
1. Copy this file to create property-specific workflow
2. Replace [address] with actual address
3. Fill in property details
4. Adjust timeline based on urgency
5. Add/remove steps based on property type
6. Customize prompts for specific situation

---

## Troubleshooting

### Issue: Generic, template-sounding descriptions
**Fix**: Provide more specific details in prompts, include unique features

### Issue: Tone doesn't match property
**Fix**: Specify exact tone (luxury, warm, professional, modern, traditional)

### Issue: Missing key features
**Fix**: Create detailed property feature list before running prompts

### Issue: Social posts too long/short
**Fix**: Specify exact character counts and platform requirements

---

## Next-Level Enhancements

### Future Additions:
1. **Automated CMA**: Generate comparative market analysis
2. **Pricing Strategy**: AI-assisted pricing recommendation
3. **Staging Recommendations**: AI suggests staging based on photos
4. **Buyer Matching**: Auto-match to buyer prospects in database
5. **Performance Dashboard**: Real-time listing analytics

---

## Using This Workflow

### First Time:
1. Read through entire workflow
2. Adjust prompts for your market and style
3. Run through with a real listing
4. Time each phase
5. Note what works and what needs refinement

### Ongoing:
1. Copy this template for each new listing
2. Customize prompts with property specifics
3. Execute steps in order
4. Commit all files to Git
5. Track results and iterate

---

**Workflow Created**: November 2024
**Last Updated**: November 2024
**Time Savings**: ~2.5-3 hours per listing
**Quality Improvement**: Consistent, professional output every time

---

## Related Workflows

- `buyer-presentation-workflow.md` - Complete buyer consultation package
- `market-analysis-workflow.md` - Weekly market intelligence gathering
- `content-calendar-workflow.md` - Monthly content planning
