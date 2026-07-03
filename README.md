# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

---

## Chunking Strategy

**Chunk size:** One complete written review record per chunk. This is not a fixed character limit: each chunk starts at `--- Review N ---` and ends immediately before the next review marker or the end of the source document.

**Overlap:** 0 characters. Reviews are independent records, so no information needs to carry across a boundary into the next review.

**Why these choices fit your documents:** Each review combines structured fields (course, date, rating, difficulty, grade) with one student's written explanation. Keeping the entire record together preserves that context for retrieval. Splitting a review could separate its rating or grade from its explanation, while combining adjacent reviews would mix unrelated student opinions. Before chunking, `ingest.py` ignores the document header, corpus note, and derived statistics above the first review marker, so those are not indexed as standalone chunks. Each chunk includes the professor name for standalone context and retains source filename, review position, and chunk ID as metadata.

**Final chunk count:** 141 review chunks from 12 local source documents.

---

## Sample Chunks

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 | `anahit_asadyan.txt` | Professor: Anahit Asadyan<br><br>--- Review 1 ---<br>Course: MATH5A<br>Review date: 2025-08-11<br>Rating: 3<br>Difficulty: 4<br>Would take again: Not provided<br>Grade: A<br><br>Review:<br>She is an extremely kind person and she really cares about you.<br>That being said her teaching is just okay, she also does everything on cengage which is an online textbook.<br>Most of the time you will probably be teaching yourself, I took her for summer, so idk how she is in the longer semesters.<br>But if you want to genuinely learn, look elsewhere. |
| 2 | `gonzaga_mendez.txt` | Professor: Gonzaga Mendez<br><br>--- Review 7 ---<br>Course: MATH005A<br>Review date: 2023-12-07<br>Rating: 4<br>Difficulty: 4<br>Would take again: Not provided<br>Grade: B<br><br>Review:<br>Took him for Math 8 and 5A.<br>Chillest professor at PCC but kind of lazy.<br>Takes forever to grade & post practice exams.<br>Material is hard but his lectures are great and he knows how to teach.<br>Pay attention during lectures & take notes!<br>If u don't understand the material, go to office hours or u won't pass.<br>Overall, try, listen, and you'll be alright. |
| 3 | `john_mathewson.txt` | Professor: John Mathewson<br><br>--- Review 1 ---<br>Course: MATH5A<br>Review date: 2026-06-30<br>Rating: 2<br>Difficulty: 4<br>Would take again: Not provided<br>Grade: B<br><br>Review:<br>He usually will give problems on the lecture and solve it by himself immediately, so you barely even have time to comprehend the questions.<br>He is nice and all, but you really have to know and prepare for the material to keep up with his pace. |
| 4 | `nerses_abramyan.txt` | Professor: Nerses Abramyan<br><br>--- Review 15 ---<br>Course: MATH5A<br>Review date: 2021-03-29<br>Rating: 5<br>Difficulty: 3<br>Would take again: Not provided<br>Grade: A+<br><br>Review:<br>His lectures are solid.<br>Do his homework assignments as if they were study guides for the exams!!<br>He is so sweet and caring do not be afraid to ask questions he will explain until you understand.<br>His grading is really fair.<br>Make sure to participate for points (even if it's just asking a Q).<br>Remember it's CALCULUS it's not supposed to be easy. |
| 5 | `thomas_kowalski.txt` | Professor: Thomas Kowalski<br><br>--- Review 7 ---<br>Course: MATH5A<br>Review date: 2016-04-12<br>Rating: 1<br>Difficulty: 5<br>Would take again: Not provided<br>Grade: Drop/Withdrawal<br><br>Review:<br>For starters his class was "flipped" meaning all the learning was done at home.<br>he sent videos but the videos are boring and unclear.<br>in class he did not lecture did not show any examples and hardly asked if any of us needed help.<br>his grading is confusing.<br>he'll take of points for ridiculous reasons. |
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 2:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 3:**

Top returned chunks:
-
-
-

Relevance explanation:

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query:

Response:

Source attribution:

---

**Grounded response 2**

Query:

Response:

Source attribution:

---

**Out-of-scope query**

Query:

System response (refusal):

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

**Output format:**

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** 

> **System:** 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
