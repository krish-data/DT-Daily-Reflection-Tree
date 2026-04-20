# DeepThought Fellowship Assignment — The Daily Reflection Tree

## 1) Why I chose these questions
I designed the tree to feel like a guided evening reflection rather than a survey. Each axis starts with a broad prompt and then narrows into a follow-up that clarifies the employee’s underlying orientation.

- **Axis 1 (Locus: Victim vs Victor):** The questions focus on reaction under pressure, perceived choice, and whether the employee sees themselves as an active navigator or a passive recipient of events.
- **Axis 2 (Orientation: Contribution vs Entitlement):** The questions are framed around interaction, motivation, and what the employee tracked mentally — contribution to the whole versus what they felt owed.
- **Axis 3 (Radius: Self-Centrism vs Altrocentrism):** The questions widen the frame from “me” to “team / colleague / customer,” which helps surface whether the employee stayed self-referential or connected their work to a broader system.

I deliberately used realistic and slightly uncomfortable options. If all “good” answers look obviously virtuous, the tree becomes moralizing and employees will game it.

## 2) Branching design and trade-offs
I used a deterministic tree with a small number of meaningful splits rather than an overly deep tree with dozens of fragile branches.

### Design principles
1. **Readable as data:** Every node is traceable in TSV without running code.
2. **Fixed options only:** No free-text input, no classification, no runtime LLM.
3. **Conversation flow over raw coverage:** I prioritized a coherent employee experience over maximum combinatorial branching.
4. **Signals + summaries:** Each axis records simple tallies (`axis1:internal`, `axis2:contribution`, etc.), which makes the final summary auditable.

### Trade-offs
- I chose **clarity over complexity**. A more sophisticated version could branch on cumulative state earlier and produce finer-grained summaries, but that would make the tree harder to audit quickly.
- I used **two broad end summaries** rather than many micro-summaries. With more time, I would add summary variants for mixed profiles.
- I kept **3–4 options per question** to reduce cognitive load. More options might increase nuance, but also increase friction and ambiguity.

## 3) Psychological sources informing the design
The design is based on the psychological framing described in the assignment:

- **Axis 1:** Locus of Control (Rotter, 1954) and Growth Mindset (Dweck, 2006)
- **Axis 2:** Psychological Entitlement (Campbell et al., 2004) and Organizational Citizenship Behavior (Organ, 1988)
- **Axis 3:** Self-Transcendence (Maslow, 1969) and Perspective-Taking / Empathic Concern (Batson, 2011)

I used these theories as design scaffolding, not as labels exposed to the employee. The product should feel like reflection, not diagnosis.

## 4) Guardrails against AI hallucination
I used AI only as a design accelerator, not as the runtime product. My guardrails were:

- No LLM calls at runtime
- No generated reflections in the live product
- Fixed options for every question
- Deterministic branching only
- Summaries built from stored answers and tally state
- Human review of all prompts to avoid vague or generic psychology language

## 5) What I would improve with more time
With more time, I would improve this in five ways:

1. Add more **mixed-state summaries**, especially for people who show agency on Axis 1 but entitlement on Axis 2.
2. Create **role-specific variants** (sales, operations, engineering) while preserving the same core axes.
3. Add a **reflection history view** so employees can compare patterns across days.
4. Introduce **safety checks** for repeated “external / entitlement / self” patterns across many sessions, without moralizing.
5. Build a **web UI** with progress indicators and sample explanation tooltips for better usability.
