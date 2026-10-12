# Sahab V34 executed strengthening specification

Date: 2026-10-12
Baseline: V33 scientific manuscript. V34 adds executed analyses; it does not alter the locked historical source reconciliation or the V33 full-sample endpoint values.

## 1. Held-out target-weight stability
Primary design: 2,000 random two-thirds/one-third train-test splits per dataset/family.
- Sahab: 32 train / 16 held out.
- Amman-Airport: 29 / 15.
- Zagreb: 17 / 8.
For each split, the intercept/Fe adjustment and target weights are fitted on training rows only. Weights and adjustment coefficients are frozen before held-out evaluation. N4 is primary; N5 is sensitivity. Equal-coefficient targets are predeclared comparators. Random splitting is exploratory and nonspatial.
Seeds start at 2026101201 and are recorded in code.

## 2. Train-fraction sensitivity
N4 only, 1,000 splits at 60% and 75% training fractions. Primary 66.7% results remain from Section 1.

## 3. Common-target held-out transfer
For paired magnetic channels, minimum and maximum common-target witnesses are selected on training rows and frozen for held-out evaluation. 2,000 primary splits. This is a stability diagnostic, not a channel-performance test.

## 4. Environmental benchmark
Sahab N4 target uses a modified-contamination-degree-style positive reference scaling C_j/B_j with B_j equal to the mean among the six historically labelled Background rows. A median-background version is sensitivity only. No contamination class is assigned.

## 5. Alternative Fe adjustment
N4 bounds are recomputed with linear Fe (baseline), log Fe, and quadratic standardized Fe. These are descriptive sensitivities, not causal source-separation models.

## 6. Controlled simulation
1,000 replicates/scenario, n=48, 32/16 train-test split.
A: Fe-only magnetic signal; no independent non-Fe signal.
B: one genuine non-Fe signal.
C: several non-Fe signals.
D: scenario B plus 10% magnetic outliers and lower-20% censoring on Cu/Ni.
Simulation is a method stress test, not environmental evidence.

## 7. Verification
80 independently formulated SLSQP checks reproduce the active-face training maxima with maximum absolute difference 7.33e-15. Primary held-out result files reproduce byte-for-byte from a clean deterministic replay.
