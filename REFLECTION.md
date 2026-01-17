# Reflection

## Approach

I approached this project by first trying to understand the problem at a conceptual level rather than jumping straight into building a full RAG system.

Instead of starting with embeddings or LLM calls, I focused on extracting structure from the ERPNext codebase. My goal was to answer a simpler question first: *what are the meaningful units of knowledge in this code?* Once I could reliably extract classes and functions and turn them into structured data, it became much clearer how a retrieval-based system could be layered on top.

I intentionally scoped the project to a single domain (Sales Invoice) to avoid spreading effort too thin and to better understand how business logic is organized in a real enterprise system.

---

## What Was New to Me

Several aspects of this project were new:

- Working with a large legacy codebase without prior domain knowledge  
- Programmatic code analysis and entity extraction  
- Thinking about code as **retrievable knowledge** rather than just text  
- Understanding how RAG systems depend heavily on the quality of indexing and retrieval, not just generation  

This was the first time I explicitly designed something with the future needs of a RAG pipeline in mind.

---

## Challenges and How I Addressed Them

The biggest challenges were environmental rather than conceptual:
- Setting up Git and cloning ERPNext locally
- Debugging path and directory issues across different environments
- Recovering from a broken VS Code update mid-project

Instead of restarting or simplifying the project, I focused on isolating problems step by step and validating assumptions (for example, confirming file discovery before debugging parsing logic). This helped me make steady progress without losing momentum.

Another challenge was deciding when to stop adding features. It was tempting to add embeddings or a chat interface, but I chose to freeze the scope once retrieval was working and the system was explainable end-to-end.

---

## What I Would Do Differently With More Time

With additional time, I would:
- Add semantic retrieval using embeddings
- Integrate an LLM to generate natural-language explanations grounded in retrieved code chunks
- Expand analysis beyond the Sales Invoice module
- Improve chunk quality by incorporating docstrings and inline comments
- Add relationship extraction (e.g., call graphs)

However, I intentionally avoided these in this iteration to prioritize clarity, correctness, and follow-through.

---

## Open Questions

Some questions I’m still thinking about:
- What are the best chunk boundaries for code-focused RAG systems?
- How much structure should be preserved versus abstracted when preparing code for retrieval?
- How can retrieval quality be evaluated objectively in developer tooling?

These are areas I would explore further in a longer engagement.

---

## Key Takeaway

The most important lesson from this project was that effective RAG systems are built from the ground up. Without clean indexing and meaningful retrieval units, generation adds little value. This project reinforced the importance of understanding and structuring knowledge before attempting to automate reasoning on top of it.
