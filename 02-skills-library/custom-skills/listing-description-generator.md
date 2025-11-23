# Skill: Listing Description Generator

## Skill Metadata
**Name**: `listing-description-generator`
**Version**: 1.0
**Category**: Marketing / Content Creation
**Estimated Time Savings**: 25 minutes per listing
**Skill Type**: Content Generation

---

## Purpose

Automatically generates compelling, SEO-optimized listing descriptions for residential properties that:
- Highlight key features and benefits
- Appeal to target buyer demographics
- Include emotional storytelling elements
- Follow best practices for MLS and marketing platforms
- Maintain consistent brand voice

---

## Inputs

### Required
- `address`: Full property address
- `price`: Listing price
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `square_feet`: Total square footage

### Optional
- `property_type`: (single-family, condo, townhome, etc.) - Default: single-family
- `key_features`: Array of standout features
- `neighborhood`: Specific neighborhood name
- `target_buyer`: (first-time buyer, luxury buyer, investor, family, retiree)
- `tone`: (professional, luxury, warm, modern) - Default: professional yet warm
- `special_notes`: Any unique selling points or context

---

## Outputs

The Skill generates three versions:

### 1. **Full MLS Description** (Max 1000 characters)
Complete description for MLS with all details

### 2. **Short Version** (Max 250 characters)
Quick snippet for social media and ads

### 3. **Email Version** (500-750 characters)
Balanced length for email campaigns and newsletters

### 4. **SEO Keywords**
List of relevant keywords for digital marketing

---

## Behavior Guidelines

### Tone & Style
- **Opening Hook**: Lead with the most compelling feature or benefit
- **Emotional Appeal**: Help buyers visualize their life in the home
- **Feature-Benefit Balance**: Not just "4 bedrooms" but "4 spacious bedrooms perfect for growing families"
- **Active Voice**: Strong, confident language
- **Avoid Clichés**: No "must see!" or "won't last long!" generic phrases

### Structure
1. **Headline/Hook** (1 sentence)
2. **Primary Features** (2-3 sentences)
3. **Interior Details** (2-3 sentences)
4. **Outdoor/Special Features** (1-2 sentences if applicable)
5. **Neighborhood/Location** (1-2 sentences)
6. **Call to Action** (1 sentence)

### Best Practices
✅ Use specific details (not "large kitchen" but "chef's kitchen with quartz countertops")
✅ Include measurements where impactful
✅ Mention recent updates/renovations
✅ Highlight energy efficiency if applicable
✅ Note proximity to key amenities

❌ Avoid discriminatory language
❌ Don't exaggerate or misrepresent
❌ Skip generic realtor-speak
❌ Don't mention price (it's listed separately)

---

## Context Files

The Skill references:
- `04-marketing-content/listing-packages/past-listings/` - Learn from successful past descriptions
- `03-market-intelligence/neighborhood-profiles/[neighborhood].md` - Include neighborhood context
- `04-marketing-content/brand-voice-guide.md` - Maintain consistent voice (if exists)

---

## Example Usage

### Basic Usage
```
/listing-description address="123 Main St, Charlotte NC" price=450000 bedrooms=4 bathrooms=2.5 square_feet=2400
```

### Advanced Usage
```
/listing-description
  address="456 Oak Avenue, Myers Park, Charlotte NC"
  price=1250000
  bedrooms=5
  bathrooms=4
  square_feet=4200
  property_type="single-family"
  key_features=["chef's kitchen", "master on main", "pool", "3-car garage"]
  neighborhood="Myers Park"
  target_buyer="luxury buyer"
  tone="sophisticated"
  special_notes="Completely renovated 2023, smart home features"
```

---

## Sample Output

### Input:
```
Address: 789 Elm Street, Dilworth, Charlotte NC
Price: $625,000
Bedrooms: 3
Bathrooms: 2
Square Feet: 1,850
Property Type: Bungalow
Key Features: ["hardwood floors", "covered porch", "updated kitchen"]
Neighborhood: Dilworth
Target Buyer: young professional couple
```

### Full MLS Description Output:
```
Welcome to quintessential Dilworth living in this beautifully updated 1920s bungalow.
From the moment you step onto the welcoming covered front porch, you'll feel the charm
of historic architecture blended perfectly with modern updates.

Inside, original hardwood floors flow throughout 1,850 square feet of thoughtfully
designed living space. The heart of the home is a completely reimagined kitchen featuring
white shaker cabinets, stainless appliances, and a generous island perfect for morning
coffee or evening entertaining. Three bedrooms and two fully updated bathrooms provide
comfortable accommodations, with the primary suite offering a peaceful retreat.

The covered back porch extends your living space outdoors, overlooking a private,
fenced backyard—a rare find in walkable Dilworth. Stroll to Frazier Park, grab coffee
at local favorites, or enjoy dinner at one of East Boulevard's renowned restaurants.

This home perfectly balances historic character with modern convenience in Charlotte's
most beloved neighborhood. Schedule your showing today.
```

### Short Version Output:
```
Charming 1920s Dilworth bungalow with updated kitchen, original hardwoods, and covered
porches. Walk to everything Dilworth offers! 3BR/2BA, 1,850 sqft.
```

### Email Version Output:
```
Your Dilworth dream home awaits at 789 Elm Street! This beautifully updated 1920s
bungalow offers the perfect blend of historic charm and modern updates. Featuring
3 bedrooms, 2 updated bathrooms, and 1,850 square feet, the home shines with original
hardwood floors and a stunning renovated kitchen. The covered front and back porches
are perfect for enjoying the neighborhood, which you can walk to from your front door—
coffee shops, restaurants, and Frazier Park are all nearby. Priced at $625,000, this
is Dilworth living at its finest.
```

### SEO Keywords Output:
```
Dilworth bungalow, Charlotte historic homes, Dilworth real estate, walkable Charlotte
neighborhood, updated bungalow Charlotte, East Boulevard homes, Dilworth 3 bedroom,
Myers Park adjacent, Charlotte bungalow for sale
```

---

## Configuration File (YAML)

```yaml
skill:
  name: listing-description-generator
  version: 1.0
  description: Generates compelling listing descriptions for residential properties

inputs:
  required:
    - address: string
    - price: number
    - bedrooms: number
    - bathrooms: number
    - square_feet: number

  optional:
    - property_type:
        type: string
        default: "single-family"
        options: ["single-family", "condo", "townhome", "multi-family", "land"]
    - key_features: array
    - neighborhood: string
    - target_buyer:
        type: string
        options: ["first-time", "luxury", "investor", "family", "retiree", "young professional"]
    - tone:
        type: string
        default: "professional yet warm"
        options: ["professional", "luxury", "warm", "modern", "traditional"]
    - special_notes: string

outputs:
  - full_description:
      max_length: 1000
      format: markdown
  - short_description:
      max_length: 250
      format: text
  - email_description:
      max_length: 750
      format: markdown
  - seo_keywords:
      type: array
      count: 8-12

behavior:
  style:
    voice: active
    perspective: second-person ("you'll love")
    emotion_level: moderate to high
    specificity: high (use exact details)

  structure:
    - hook: 1 sentence, most compelling feature
    - primary_features: 2-3 sentences, key selling points
    - interior: 2-3 sentences, room details
    - exterior: 1-2 sentences if applicable
    - neighborhood: 1-2 sentences, location benefits
    - call_to_action: 1 sentence

  rules:
    - avoid_discrimination: true
    - avoid_cliches: true
    - use_specific_details: true
    - maintain_honesty: true
    - seo_optimize: true

context_files:
  - path: "04-marketing-content/listing-packages/past-listings/"
    purpose: "Learn from successful past descriptions"
  - path: "03-market-intelligence/neighborhood-profiles/{neighborhood}.md"
    purpose: "Include accurate neighborhood context"
  - path: "04-marketing-content/brand-voice-guide.md"
    purpose: "Maintain brand consistency"
    required: false

examples:
  - input:
      address: "123 Main St"
      bedrooms: 4
      bathrooms: 3
      square_feet: 2500
    context: "First use, establishing baseline quality"
```

---

## Claude Code Implementation

### Creating the Skill

```bash
# Save the YAML configuration to your skills directory
# File: 02-skills-library/custom-skills/listing-description-generator.yaml
```

### Using the Skill in Claude Code

```
Generate a listing description for 456 Oak St, a 3-bed, 2-bath, 1,800 sqft home
in Dilworth priced at $550,000. Key features include updated kitchen and backyard.
Target young families.
```

Claude Code will:
1. Recognize the request matches this Skill
2. Load configuration and context files
3. Apply the behavior rules
4. Generate all output formats
5. Save outputs to specified location

---

## Performance Tracking

### Skill Usage Log

| Date | Address | Time Saved | Quality Rating | Notes |
|------|---------|------------|----------------|-------|
| 2024-11-15 | 123 Main St | 25 min | 5/5 | Perfect first draft |
| 2024-11-18 | 456 Oak Ave | 20 min | 4/5 | Needed minor tweaks |
| 2024-11-22 | 789 Elm St | 30 min | 5/5 | Used for multiple platforms |

### Improvement Log

**v1.0** (2024-11-01)
- Initial release
- Basic functionality

**v1.1** (Planned)
- Add video script variant
- Include virtual tour description
- Enhance neighborhood context integration

---

## Customization for Your Market

### Adapt for Your Area

**Charlotte-Specific Elements:**
- Neighborhood references (Myers Park, Dilworth, South End)
- Local amenities (Freedom Park, Uptown, etc.)
- Regional terminology

**Your Market:**
```
Update the following for your market:
- Neighborhood names and characteristics
- Local landmarks and amenities
- Regional real estate terminology
- Common buyer types in your area
```

### Brand Voice Adjustment

Create `04-marketing-content/brand-voice-guide.md`:
```markdown
# My Brand Voice

**Tone**: [Your preference]
**Style**: [Your style]
**Signature Phrases**: [Phrases you commonly use]
**Avoid**: [What you don't want]
```

The Skill will adapt to match your voice.

---

## Troubleshooting

### Skill output is too generic
✅ Add more specific key_features
✅ Provide special_notes about unique aspects
✅ Ensure neighborhood profile exists and is detailed

### Skill output doesn't match my voice
✅ Create or update brand-voice-guide.md
✅ Provide examples of your past descriptions in context files
✅ Adjust tone parameter

### Skill is too long/short
✅ Outputs are length-limited; Skill will auto-adjust
✅ If consistently too short, add more detail to inputs
✅ If too verbose, specify "concise" in tone or special_notes

---

## Next Steps

1. **Install this Skill** by saving configuration
2. **Test with 3 real listings** to calibrate quality
3. **Adjust parameters** based on results
4. **Add to your workflow** for all new listings
5. **Track time saved** and quality improvements

---

## Related Skills

- `listing-social-posts` - Creates social media posts from listing
- `open-house-announcement` - Generates open house marketing
- `listing-email-campaign` - Creates email sequence for new listing

---

*Skill Created: November 2024*
*Last Updated: November 2024*
*Next Review: After 10 uses or 30 days*
