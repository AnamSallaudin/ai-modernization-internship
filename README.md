# ERPNext – RAG-Based Code Intelligence Prototype

## Overview

This project is a **RAG-based code intelligence prototype** built on top of the ERPNext codebase, specifically focused on the **Sales Invoice** module.

The goal of the project is to demonstrate how structured knowledge can be extracted from a large, unfamiliar legacy codebase and made **retrievable** in a way that supports future LLM-based reasoning and generation.

Rather than starting directly with embeddings or chat interfaces, this project focuses on the **foundational layers** of a RAG system:
- code indexing
- structural extraction
- knowledge chunking
- retrieval

---

## Problem Statement

Large enterprise codebases like ERPNext are difficult to understand due to:
- size and complexity
- lack of centralized documentation
- implicit business logic spread across files

This project explores how **programmatic code analysis + retrieval** can help engineers answer questions such as:
- *Where is a specific business rule implemented?*
- *Which classes or functions are responsible for validation, calculation, or submission?*
- *How is a core domain object structured?*

---

## What This Project Does

The system is composed of three main stages:

### 1. Code Analysis (Indexing Layer)
**Script:** `src/analyzer.py`

- Recursively scans a target ERPNext module directory
- Extracts:
  - class names
  - function names
- Outputs structured metadata to `output/entities.json`

This step builds the **code index** that grounds the rest of the system.

---

### 2. Knowledge Chunking
**Script:** `src/chunker.py`

- Converts extracted entities into small, focused text chunks
- Each chunk represents a retrievable unit of knowledge
- Outputs chunks to `output/chunks.json`

These chunks form the **retrieval corpus** used by the RAG pipeline.

---

### 3. Retrieval (RAG-lite)
**Script:** `src/retriever.py`

- Accepts a natural-language query
- Retrieves the most relevant chunks using keyword-based scoring
- Returns grounded, source-linked results from the ERPNext codebase

This implements the **retrieval step** of a RAG system.
LLM-based generation is intentionally left out of scope for this iteration.

---

## Example Queries

From the project root:

```bash
python src/retriever.py "SalesInvoice"
python src/retriever.py "validation"
python src/retriever.py "calculate"
python src/retriever.py "submit"
