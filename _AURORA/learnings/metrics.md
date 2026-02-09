# AURORA UX Metrics

Tracking UX quality and AURORA effectiveness across the GAIA ecosystem.

---

## Dashboard

| Metric | Target | Current | Measured By |
|--------|--------|---------|-------------|
| Design system coverage | Brand kits for all 8 products | 0/8 | `brand_tokens.json` exists per product |
| Pattern library size | 10+ reusable patterns | 0 | File count in `patterns/` |
| Anti-patterns documented | Ongoing | 1 | Entry count in `anti_patterns.md` |
| Design decisions logged | Ongoing | 2 | Entry count in `decisions.md` |
| Time to prototype | Hours, not days | Unmeasured | Phase 5 start-to-approval duration |
| Accessibility compliance | WCAG 2.1 AA | Untested | Axe DevTools audit results |
| User satisfaction | Positive feedback | Unmeasured | Sentiment in `feedback_log.md` |
| Design reuse rate | 30%+ shared components | 0% | Components from `patterns/` used in 2+ projects |

---

## Measurement Schedule

- **After each project engagement:** Update coverage, pattern count, reuse rate
- **Monthly:** Review feedback log for satisfaction trends
- **Quarterly:** Run accessibility audits on all active products

---

## Notes

Metrics are tracked manually for now. Future integration with ARGUS could automate telemetry-based UX metrics (page load times, interaction rates, error frequencies).
