Periodic **post-market surveillance / ISO 14971 §10** review (method: `docs/PMS.md`). Walk §10.2–§10.4:

### §10.2 Collect — review inputs since the last review
- [ ] New `field-feedback` issues (incidents / user-reported problems)
- [ ] New `soup-anomaly` issues + vulnerability→register issues (SBOM / CVE feed)
- [ ] Publicly available info on the product's technology
- [ ] `CONFORMANCE.md` `watch` rows — state-of-the-art / regulatory drift

### §10.3 Review — safety relevance
- [ ] Any previously **unrecognised** hazard or hazardous situation?
- [ ] Any risk **no longer acceptable** against its criteria?
- [ ] Is the **overall** residual risk still acceptable vs. benefit?
- [ ] **Trend** signal across incidents/complaints (MDR Art. 88)?

### §10.4 Act
- [ ] Update the harm-risk register / raise new `harm-risk` issues as needed
- [ ] Feed material changes into top-management process review (§4.2)
- [ ] At a release: roll the outcome into `HARM_RISK_REPORT.md` (§9)

**Outcome (summarise):** _&lt;what was reviewed, what changed, what actions were taken or none-needed&gt;_

_Auto-opened by `.github/workflows/pms-review.yml`. Close when the review is recorded._
