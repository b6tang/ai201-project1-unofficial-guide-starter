# The Unofficial Guide — Project 1
---

## Domain

This project is an unofficial course-selection guide for Pasadena City College students choosing among regular MATH 005A (Single Variable Calculus I) instructors. 

It is based on student reviews with written comments and helps students understand how different instructors are described in terms of teaching style, workload, exams, grading, and course format. PCC's official course information does not consolidate these instructor-specific student experiences, while individual reviews are scattered across separate professor pages.

---

## Document Sources
All corpus documents are written student reviews from Rate My Professors, organized by instructor.

I used a two-stage curation process to build a relevant and usable corpus. I began with 36 potential Pasadena City College mathematics instructors listed in the official PCC Fall 2026 schedule. I then narrowed the list to 22 instructors scheduled to teach regular MATH 005A (Single Variable Calculus I) sections. Instructors associated only with honors sections or other math courses were not included.

From those 22 current MATH 005A candidates, I selected the 12 instructors with enough written MATH 005A review data to support retrieval and cross-instructor comparison. I retained only reviews with written comments for MATH 005A, then standardized them into consistent local text documents. Each review record preserves its course label, review date, rating, difficulty, grade information when available, and written comment.

| # | Instructor reviewed |  Local file path | Original source URL  |
|---|------------------------------------|-----------------------|-----------------|
| 1 | Gonzaga Mendez — 9 written MATH 005A student reviews | `documents/gonzaga_mendez.txt` | https://www.ratemyprofessors.com/professor/2609879 |
| 2 | John Mathewson — 17 written MATH 005A student reviews | `documents/john_mathewson.txt` | https://www.ratemyprofessors.com/professor/1179033 |
| 3 | Roger Yang — 3 written MATH 005A student reviews | `documents/roger_yang.txt` | https://www.ratemyprofessors.com/professor/195939 |
| 4 | Erlend Weydahl — 4 written MATH 005A student reviews | `documents/erlend_weydahl.txt` | https://www.ratemyprofessors.com/professor/284762 |
| 5 | Frank Bermudez — 15 written MATH 005A student reviews | `documents/frank_bermudez.txt` | https://www.ratemyprofessors.com/professor/1700371 |
| 6 | Jay Cho — 5 written MATH 005A student reviews | `documents/jay_cho.txt` | https://www.ratemyprofessors.com/professor/205605 |
| 7 | Thomas Kowalski — 7 written MATH 005A student reviews | `documents/thomas_kowalski.txt` | https://www.ratemyprofessors.com/professor/2119025 |
| 8 | Nerses Abramyan — 18 written MATH 005A student reviews | `documents/nerses_abramyan.txt` | https://www.ratemyprofessors.com/professor/226835 |
| 9 | Irina Badalyan — 27 written MATH 005A student reviews | `documents/irina_badalyan.txt` | https://www.ratemyprofessors.com/professor/347864 |
| 10 | Mark Pavitch — 4 written MATH 005A student reviews | `documents/mark_pavitch.txt` | https://www.ratemyprofessors.com/professor/1661072 |
| 11 | Sandra Vazquez-Celaya — 22 written MATH 005A student reviews | `documents/sandra_vazquez_celaya.txt` | https://www.ratemyprofessors.com/professor/2255988 |
| 12 | Anahit Asadyan — 10 written MATH 005A student reviews | `documents/anahit_asadyan.txt` | https://www.ratemyprofessors.com/professor/2167794 |

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

**Model used:**  
I used `all-MiniLM-L6-v2` through ChromaDB's SentenceTransformer embedding function. I chose it because my corpus is small, the review chunks are short, and it runs locally without another API key.

**Production tradeoff reflection:**  
Even if cost were not an issue, I would not automatically switch models. I would first test whether a stronger model actually finds instructor-specific details better, such as class format or exam policies. A larger or API-hosted model could be slower and would add another dependency.

---

## Retrieval Test Results

**Query 1:**  
Are Asadyan's quizzes and tests like the homework?

Top returned chunks:
- **Rank 1 — `anahit_asadyan.txt`, Review 8 (2019):** “Quiz score will be added to the test.”
- **Rank 2 — `anahit_asadyan.txt`, Review 5 (2024):** Described clear lectures and opportunities to ask questions.
- **Rank 3 — `anahit_asadyan.txt`, Review 9 (2019):** “Her tests are taken primarily from the homework.”

Relevance explanation:  
This was a mixed result. Review 9 directly answers the question, and Review 8 is related to quizzes and tests. Review 5 is about lecture style, so it is a weaker match.

---

**Query 2:**  
How many tests does Gonzaga Mendez give?

Top returned chunks:
- **Rank 1 — `gonzaga_mendez.txt`, Review 2 (2024):** Said he allows two exam retakes.
- **Rank 2 — `gonzaga_mendez.txt`, Review 8 (2022):** “4 exams in total, 3 tests and 1 final.”
- **Rank 3 — `gonzaga_mendez.txt`, Review 1 (2026):** “His entire grade book is based off 3 tests + the final.”

Relevance explanation:  
Reviews 8 and 1 directly answer the question with the same test structure: three tests and one final. Review 2 is less direct, but it is still about exams in the same class.

---

**Query 3:**  
Was Jay Cho's MATH 005A class ever hybrid or online?

Top returned chunks:
- **Rank 1 — `jay_cho.txt`, Review 1 (2024):** “I took his hybrid course.”
- **Rank 2 — `jay_cho.txt`, Review 3 (2022):** “Class was hybrid, so the online lectures were pretty boring.”
- **Rank 3 — `jay_cho.txt`, Review 5 (2009):** Described the class as easy and said his lectures were clear.

Relevance explanation:  
The first two chunks directly answer the question because both describe the class as hybrid, and Review 3 also mentions online lectures. The third chunk is a weaker result because it does not discuss course format.

---

## Grounded Generation

**System prompt grounding instruction:**  
My system prompt tells the model to “Answer only from the retrieved student reviews” and to “Make only claims directly supported by the excerpts.” It also tells the model to describe claims as past reviewer reports, not current course policy. If the reviews do not support the question, it must return: `I don't have enough information in the collected reviews to answer that.` The model only receives the chunks returned by retrieval, and for questions that name one instructor, I remove chunks from other instructors before sending the context to the model.

**Post-retrieval relevance filter:**  
Retrieval returns up to 7 chunks. Before calling Groq, `generator.py` keeps chunks from the named instructor when the query identifies exactly one instructor, then keeps only chunks with a Chroma distance of `0.60` or lower. Only those filtered chunks are included in the LLM context and in the programmatically generated `Sources:` section. This reduces weaker matches, but evaluation showed that it can also remove relevant evidence when its distance is above the cutoff.

**How source attribution is surfaced in the response:**  
Each retrieved review is labeled with its source filename and review number. After the model answers, Python adds the `Sources:` section using the same chunks that were passed into generation. The LLM does not create its own citations.

---

## Example Responses

**Grounded response 1**

Query:  
Does Asadyan give extra credit?

Response:  
A past reviewer reported that Professor Asadyan gives extra credit, specifically mentioning that she gives everyone a chance to write down answers as extra credits, with the reviewer earning 12 points of extra credit. Another past reviewer also mentioned that quiz scores are considered as extra credit. However, a different past reviewer reported that Professor Asadyan does not provide extra credit.

Sources:
- anahit_asadyan.txt — Review 7
- anahit_asadyan.txt — Review 5
- anahit_asadyan.txt — Review 6
- anahit_asadyan.txt — Review 9
- anahit_asadyan.txt — Review 8
- anahit_asadyan.txt — Review 10
- anahit_asadyan.txt — Review 4
  
---

Query:  
Are Asadyan's quizzes and tests like the homework?

Response:  
A past reviewer reported that Professor Asadyan's tests are taken primarily from the homework. Another reviewer stated that quiz questions are based on the homework and the exams are based on homework and quiz. A reviewer also mentioned that the homework is similar to the test/quizzes.

A past reviewer reported that doing the homework is enough to do fine in the class, and another reviewer recommended studying the textbook problems as well and using outside sources of material to better chances.

Sources:
- anahit_asadyan.txt — Review 8
- anahit_asadyan.txt — Review 5
- anahit_asadyan.txt — Review 9
- anahit_asadyan.txt — Review 2
- anahit_asadyan.txt — Review 3
- anahit_asadyan.txt — Review 7
- anahit_asadyan.txt — Review 6

---

**Out-of-scope query**

Query:  
What is the weather forecast in Pasadena tomorrow?

System response (refusal):  
I don't have enough information in the collected reviews to answer that.

---

## Query Interface

**Input fields:**  
The app has one text box labeled `Ask about a MATH 005A instructor`. I can enter a question and either click the `Ask` button or press Enter.

**Output format:**  
The app shows a short answer in a text box below the question. For supported questions, it adds a `Sources:` section with the review filename and review number. For unsupported questions, it returns the fallback message instead of guessing.

**Sample Interaction Transcript**

> **User:** How many tests does Gonzaga Mendez give?
>
> **System:** A past reviewer reported that Gonzaga Mendez gives 3 tests and 1 final. Another reviewer also reported that the entire gradebook is based off 3 tests + the final.
>
> A past reviewer from 2022 reported that there are 4 exams in total, which includes 3 tests and 1 final.
>
> Sources:
> - gonzaga_mendez.txt — Review 2
> - gonzaga_mendez.txt — Review 8
> - gonzaga_mendez.txt — Review 1
> - gonzaga_mendez.txt — Review 3
> - gonzaga_mendez.txt — Review 5
> - gonzaga_mendez.txt — Review 6
> - gonzaga_mendez.txt — Review 7

---

## Evaluation Report

| # | System response (summarized)                                                                                                                                                              | Retrieval quality  | Response accuracy |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------- |
| 1 | Reported that tests were primarily from homework, quizzes and exams were based on homework, and homework was similar to tests and quizzes. It also included study advice from a reviewer. | Relevant           | Accurate          |
| 2 | Reported conflicting past reviews: 2019 reviewers described extra-credit opportunities, while a 2025 reviewer reported no extra credit.                                                   | Relevant           | Accurate          |
| 3 | Reported 3 tests plus 1 final; a 2022 review described 4 exams total.                                                                                                                     | Relevant           | Accurate          |
| 4 | Reported hybrid classes in 2022 and 2024, plus mostly online asynchronous lectures in 2023. It also added an irrelevant note that the 2009 review gave no course-format information.      | Partially relevant | Accurate          |
| 5 | I don't have enough information in the collected reviews to answer that.                                                                                                                  | Off-target         | Accurate          |


**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate


---

## Failure Case Analysis

**Question that failed:**  
Are any MATH 005A tests open book?

**What the system returned:**  
The system retrieved reviews discussing tests and book problems, then stated that no retrieved reviewer described whether tests were open book. It returned a grounded explanation with sources instead of the intended exact fallback message.

**Root cause (tied to a specific pipeline stage):**  
This was primarily a retrieval-and-evidence-selection limitation. Semantic retrieval treated “open book” and “book problems” as closely related, so chunks about tests based on textbook problems had low distances and passed the generation filter. However, those chunks did not directly establish whether students could use a book during an exam. The LLM then produced a reasonable evidence-limited summary rather than the exact fallback required by this project's test.

**What you would change to improve it:**  
A future version could use hybrid retrieval or a reranking/evidence-verification step for narrow factual questions. In this case, the system would distinguish evidence about exam format from evidence about textbook-derived questions by checking for direct support of concepts such as “open book,” “notes allowed,” or similar wording before generation.

---

## Spec Reflection
**One way the spec helped you during implementation:**  
The spec helped me break the project into smaller steps: chunking, retrieval, and generation. The evaluation questions also gave me specific things to test instead of just asking random questions.

**One way your implementation diverged from the spec, and why:**  
I originally planned to retrieve 5 chunks, but changed it to 7. When I tested the extra-credit question, the conflicting 2025 review only appeared at rank 7, so keeping 5 results would have missed it.

---

## AI Usage

**Instance 1**

- *What I gave the AI:* I showed Claude my review-file format, my code skeleton with docstring, and the chunking plan from `planning.md`.
- *What it produced:* It helped me debug and finish the `load_documents()` and `chunk_document()` functions.
- *What I changed or overrode:* I checked the code against my actual files and kept one full review as one chunk. I did not use fixed-size chunks because the reviews were already short. I also checked the maximum character length across all reviews and confirmed that none were long enough to need splitting.

**Instance 2**

- *What I gave the AI:* I showed Claude the retrieval output format and explained that answers needed to come only from retrieved reviews and include sources.
- *What it produced:* It helped draft the Groq generation code and the basic Gradio interface.
- *What I changed or overrode:* I made Python append the Sources section instead of trusting the LLM to cite correctly. I also changed `top_k` from 5 to 7 after testing showed that the conflicting extra-credit review was ranked seventh.
