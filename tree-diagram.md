flowchart TD
    START([Start]) --> OPEN_WORD[How would you describe today overall?]
    OPEN_WORD --> OPEN_ROUTE{Productive/Mixed or Heavy/Frustrating?}
    OPEN_ROUTE -->|Productive/Mixed| A1_Q1_HIGH[Axis 1 Question Path A]
    OPEN_ROUTE -->|Heavy/Frustrating| A1_Q1_LOW[Axis 1 Question Path B]
    A1_Q1_HIGH --> A1_D1{Agency leaning?}
    A1_Q1_LOW --> A1_D1B{Agency leaning?}
    A1_D1 --> A1_Q2_INT[Follow-up: internal agency]
    A1_D1 --> A1_Q2_MIX[Follow-up: shared influence]
    A1_D1B --> A1_Q2_INT
    A1_D1B --> A1_Q2_EXT[Follow-up: external locus]
    A1_Q2_INT --> A1_R_INT[Reflection: agency]
    A1_Q2_MIX --> A1_R_MIX[Reflection: shared agency]
    A1_Q2_EXT --> A1_R_EXT[Reflection: lost control]
    A1_R_INT --> B12[Bridge 1→2]
    A1_R_MIX --> B12
    A1_R_EXT --> B12
    B12 --> A2_OPEN[Axis 2 opening question]
    A2_OPEN --> A2_ROUTE{Giving or expecting?}
    A2_ROUTE -->|Giving| A2_Q1_CONTRIB --> A2_Q2_CONTRIB --> A2_R_CONTRIB
    A2_ROUTE -->|Expecting| A2_Q1_ENT --> A2_Q2_ENT --> A2_R_ENT
    A2_R_CONTRIB --> B23[Bridge 2→3]
    A2_R_ENT --> B23
    B23 --> A3_OPEN[Axis 3 opening question]
    A3_OPEN --> A3_ROUTE{Narrow or wide radius?}
    A3_ROUTE -->|Self| A3_Q1_SELF --> A3_Q2_SELF --> A3_R_SELF
    A3_ROUTE -->|Wide| A3_Q1_WIDE --> A3_Q2_WIDE --> A3_R_ALTRO
    A3_R_SELF --> SUMMARY[Summary]
    A3_R_ALTRO --> SUMMARYB[Summary]
    SUMMARY --> END([End])
    SUMMARYB --> END
