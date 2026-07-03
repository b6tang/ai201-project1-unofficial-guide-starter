# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

This project is an unofficial guide to selected Pasadena City College MATH 005A (Single Variable Calculus I) instructors, based on collected student reviews for those instructors.

The guide is valuable because students choosing a Calculus I section may want to compare how reviewers describe lecture clarity, homework workload, exam style, grading concerns, study advice, and online or recorded-course experiences. PCC's official course catalog explains the course content, prerequisites, and units, but it does not collect instructor-specific
student experiences in one searchable place. These reviews are scattered across individual professor pages, making recurring feedback across multiple Calculus I instructors difficult to compare.

---

## Documents

The 12 RMP profiles below are the documents that will be ingested. Each profile represents a different PCC MATH 005A instructor perspective. Only MATH 005A / Calculus I reviews with written comments will be included in the corpus. The official PCC Fall 2026 schedule was used only to select instructors who currently teach regular MATH 005A; it is not itself an ingested document.

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Gonzaga Mendez — RMP profile | PCC MATH 005A instructor reviews. The verification run found 9 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/2609879 |
| 2 | John Mathewson — RMP profile | PCC MATH 005A instructor reviews. The verification run found 17 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/1179033 |
| 3 | Roger Yang — RMP profile | PCC MATH 005A instructor reviews. The verification run found 3 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/195939 |
| 4 | Erlend Weydahl — RMP profile | PCC MATH 005A instructor reviews. The verification run found 4 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/284762 |
| 5 | Frank Bermudez — RMP profile | PCC MATH 005A instructor reviews. The verification run found 15 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/1700371 |
| 6 | Jay Cho — RMP profile | PCC MATH 005A instructor reviews. The verification run found 5 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/205605 |
| 7 | Thomas Kowalski — RMP profile | PCC MATH 005A instructor reviews. The verification run found 7 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/2119025 |
| 8 | Nerses Abramyan — RMP profile | PCC MATH 005A instructor reviews. The verification run found 18 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/226835 |
| 9 | Irina Badalyan — RMP profile | PCC MATH 005A instructor reviews. The verification run found 27 labeled MATH 005A text reviews. | https://www.ratemyprofessors.com/professor/347864 |
| 10 | Mark Pavitch — RMP profile | PCC MATH 005A instructor reviews. The verification run found 4 labeled MATH 005A text reviews. His Fall 2026 sections include DE Online Lecture. | https://www.ratemyprofessors.com/professor/1661072 |
| 11 | Sandra Vazquez-Celaya — RMP profile | PCC MATH 005A instructor reviews. The verification run found 22 labeled MATH 005A text reviews. Her Fall 2026 section includes DE Online Lecture. | https://www.ratemyprofessors.com/professor/2255988 |
| 12 | Anahit Asadyan — RMP profile | PCC MATH 005A instructor reviews. The verification run found 10 labeled MATH 005A text reviews. Her Fall 2026 section includes DE Online Lecture. | https://www.ratemyprofessors.com/professor/2167794 |

---

## Chunking Strategy

Derived Rating, Difficulty, and self-reported grade GPA statistics are stored in each local document header for transparency. They are calculated only from the included written MATH 005A reviews.

For the required RAG pipeline, only complete individual review records will be embedded as chunks. The derived header statistics will not be indexed as separate chunks in the initial version.

**Chunk size:** One complete review record per chunk. Chunk length is variable because each review is kept intact rather than split by a fixed character limit.

**Overlap:** 0 characters for normal review chunks. If an unusually long review must be split, use 150 characters of overlap between its parts.

**Reasoning:** After reviewing the collected documents, the student reviews are short and self-contained, and no review record is long enough to require additional splitting. Each review is therefore kept as one chunk so that its course label, date, rating fields, and written opinion remain together. This prevents feedback from different instructors or reviews from being mixed in the same chunk. Each chunk will retain professor and source metadata for citation.

## Retrieval Approach

**Embedding model:** I will use `all-MiniLM-L6-v2` through `sentence-transformers` to embed the review chunks and user queries. This is a lightweight local embedding model and appropriate for an initial semantic-search system with a small corpus of short review records.

**Top-k:** 5 chunks per query. Because the corpus contains short, opinion-based reviews, the fifth-ranked result may still contain useful evidence that would be missed with a smaller retrieval set. Retrieving too few chunks could omit the review that contains the needed evidence; retrieving too many could introduce weakly related opinions and pull the generated answer away from the user's question. I will start with five and adjust it only after reviewing real retrieval results from the evaluation queries.

**Production tradeoff reflection:** Even if cost were not a constraint, I would compare retrieval quality against latency, multilingual support, model input length, domain-specific accuracy, and whether embeddings should run locally or through an API.  Since the review chunks are short, I do not need a model with a very large context window. A larger model could be slower, so I would only use one if it gave noticeably better retrieval results in my evaluation tests.

---

## Evaluation Plan

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Are Asadyan's quizzes and tests like the homework? | Multiple collected reviews said that quizzes were based on homework and that tests or exams were similar to, or primarily taken from, homework. |
| 2 | Does Asadyan give extra credit? | Reviews conflict across terms. Some 2019 reviews described extra-credit opportunities, while 2025 reviews reported no extra credit. The system should not present either as a current policy. |
| 3 | How many tests does Gonzaga Mendez give? | Two collected reviews described three tests plus a final, for four major exams total. One review also reported that students could retake two exams. These are past reviewer reports, not current policy. |
| 4 | Was Jay Cho's MATH 005A class ever hybrid or online? | Yes. Past reviews described Jay Cho's MATH 005A class as hybrid, and one review said that lectures were mostly online and asynchronous. |
| 5 | Are any MATH 005A tests open book? | The collected written reviews do not provide enough information to answer this. The system should state that it does not have enough information in the retrieved reviews and should not guess or use outside sources. |

---
## Anticipated Challenges

1. **Conflicting and time-dependent reviewer reports.** 
   Reviews in the corpus come from different terms and describe individual student experiences. A practice reported in an older review may conflict with a later review, such as reports about extra credit. The system could incorrectly present one reviewer's experience as a current course policy. To reduce this risk, each review chunk will retain its review date and professor metadata, and the generation prompt will require answers to describe these as past reviewer reports. When retrieved reviews conflict, the response should state that the reports differ instead of choosing one as definitive.

2. **Ambiguous retrieval for broad terms.** 
   Terms such as "online," "grading," or "tests" can refer to different things across the corpus. For example, "online" may refer to online homework, an online textbook, Zoom support, or a hybrid course. Semantic retrieval could return a chunk that shares words with the question but does not directly answer it, or it could mix feedback from different instructors. To reduce this risk, the system will preserve source and professor metadata, show source attribution in every answer, and instruct the LLM to answer only when the retrieved chunks directly support the claim. Otherwise, it must say that the collected reviews do not provide enough information.

---

## Architecture

```text
documents/*.txt
      │
      ▼
[Document Ingestion]
Python
      │
      ▼
[Chunking]
Python
1 complete review = 1 chunk
0 overlap
      │
      ▼
[Embedding + Vector Store]
sentence-transformers
all-MiniLM-L6-v2 
ChromaDB
      │
      ▼
[Retrieval]
Python + ChromaDB
top-5 similarity search
      │
      ▼
[Generation]
Python + Groq SDK
llama-3.3-70b-versatile
      │
      ▼
Response + source citations or “not enough information”
```
---

## AI Tool Plan

**Milestone 3 — Ingestion and chunking:**

- **AI tool:** I will use ChatGPT to clarify the parsing and chunking logic and to review terminal output. I will use Claude to generate the ingestion and chunking code and suggest checks for it.

- **Input provided to AI:** I will give Claude my `Chunking Strategy` section, my Architecture diagram, and one real file from `documents/` so the code can match the actual review-record format. I will specify that each complete review record should remain one chunk with zero overlap.

- **Expected output:** I expect Python code that loads the local documents and turns the complete review records into chunks according to my Chunking Strategy.

- **Verification:** I will read the generated code before running it. I will run it on the real corpus, confirm that it produces 141 review chunks, print and inspect five random chunks, and check that they are complete, self-contained reviews rather than fragments, empty strings, or document headers.

**Milestone 4 — Embedding and retrieval:**

- **AI tool:** I will use ChatGPT to clarify embedding, ChromaDB, and distance score behavior and to review retrieval output. I will use Claude to generate the embedding and retrieval code.

- **Input provided to AI:** I will give Claude my `Retrieval Approach` section, my Architecture diagram, and the chunk output from Milestone 3. I will specify `all-MiniLM-L6-v2`, ChromaDB, source metadata, and `top_k = 5`.

- **Expected output:** I expect code that loads chunks from the ingestion pipeline, embeds them with `all-MiniLM-L6-v2`, stores them in ChromaDB with source document name and chunk-position metadata, and provides a retrieval function that returns the top five relevant chunks with source information and distance scores.

- **Verification:** I will read the generated code and ask for an explanation of any ChromaDB code I do not understand. I will run retrieval on three questions from my Evaluation Plan, print the returned chunks and distance scores, and check whether the chunks visibly and directly relate to each question before moving to generation.

**Milestone 5 — Generation and interface:**

- **AI tool:** I will use ChatGPT to clarify grounded-generation behavior and review actual responses. I will use Claude to generate the generation and interface code.

- **Input provided to AI:** I will give Claude my Architecture diagram and the relevant parts of `planning.md`, including the Evaluation Plan and Anticipated Challenges. I will specify that answers must use retrieved
  context only, that the output must include an answer and source list, and that source attribution must be added programmatically rather than relying only on the LLM to remember citations.

- **Expected output:** I expect code that sends the user question and retrieved chunks to Groq's `llama-3.3-70b-versatile`, returns an answer grounded only in that context, displays the source documents used, and provides a usable query interface.

- **Verification:** I will read the generated code before running it and check that the system prompt explicitly restricts answers to retrieved context. I will test the full pipeline with covered questions and with my open-book question, confirming that covered answers cite local sources and that the unsupported question returns an information-insufficient response instead of guessing.
