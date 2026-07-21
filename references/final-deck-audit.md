# Final Deck Audit

Use this before handing a deck to the user. For decks over 20 slides, the audit is mandatory.

## Subagent Prompt

Use this prompt with a subagent:

```text
Audit the finished deck against the artful-deck-generator skill. Check whether the workflow was actually followed, not whether the deck merely looks acceptable. Review the source notes, generated deck, assets, QA screenshots/contact sheet, and PDF if present. Return PASS only if every required item is satisfied. For each failure, name the slide(s), evidence, and the smallest fix needed.
```

## Pass/Fail Checklist

- Source was read before outlining.
- Language was confirmed before outlining or deck generation, using the skill's four-option language choice when the user had not already stated it.
- Visible slide copy matches the confirmed language selection; no unrequested bilingual text was added.
- Flow summary exists: audience, time box, learning outcome, narrative arc, and slide count.
- Deck respects the requested slide count.
- For decks over 20 slides, `references/layout-variety-reference.md` was read and every screenshot in `references/style and layout/` was inspected before coding.
- For decks over 20 slides, a slide-format plan exists with slide number, slide purpose, layout family, density, image placement, interaction type, and reference inspiration.
- For decks over 20 slides, no more than two adjacent slides use the same layout family unless marked as an intentional motif.
- GenImage image brief exists before image generation.
- The brief separates slide claim, natural subject/metaphor, and style treatment; the reference image's scene was not cloned unless the slide required it.
- Every rendered image passes the content relevance gate: it communicates the slide's key idea rather than merely matching the deck style.
- The deck passes the scene-diversity check: meeting, workshop, presentation, office-review, and dashboard scenes are used only when the respective slide needs them.
- GenImage was used for new deck imagery unless the user explicitly approved placeholders or fewer images.
- `generated_or_selected_image_count == slide_count`, unless the user explicitly approved a different count.
- Every project-used image is saved in the deck workspace.
- Browser QA was run after the final edit.
- Contact sheet or equivalent all-slide overview was reviewed for decks over 10 slides.
- Large-deck contact sheet was checked for repeated silhouettes, repeated image placement, repeated density, and repeated diagram pattern.
- PDF/export was validated for visible content when a PDF was requested or produced.
- Temporary QA files were removed, leaving only final deck assets.

## Main Agent Rule

Fix audit failures before final delivery. If a failure cannot be fixed, report the blocker and the exact compromise instead of presenting the deck as complete.
