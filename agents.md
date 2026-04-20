# **Universal System Architecture: Skill-Based Orchestration**

This system is orchestrated under a skill-based structure designed to eliminate stochastic drift and ensure absolute fidelity through deterministic execution. It allows for infinite task scalability by swapping the active domain constraint while maintaining a rigid governance layer.

## **1\. Governance: The Policy Layer**

Governance represents the constitutional boundaries and cognitive constraints of the system. It is the terminal orchestrator that interprets intent and enforces compliance across all sub-processes.

### **1.1 System Initialization and Bootstrapping**

Upon the first invocation, the system must execute the mandatory bootstrap protocol:

* **Environment Isolation:** Create and activate a dedicated virtual environment. All work must occur within this space; contamination of out-of-project space is strictly prohibited.  
* **Dependency Synchronization:** Install all required libraries as specified in the system manifest to ensure a reproducible state.  
* **Integrity Check:** Verify the presence of the Skills/ directory before proceeding.  
* **Version Control:** Use Git to version control the codebase and documentation. The agents.md file and Skills/ folder are proprietary assets. They must be tracked locally and are strictly prohibited from being pushed to GitHub or any online repository.

### **1.2 Cognitive Constraints**

* **Constitutional Authority:** This document serves as the terminal authority. No system action may contradict these directives.  
* **Orchestration Logic:** The system functions as a recursive, real-time self-healing interpreter. It identifies goals, selects appropriate Skills, and validates outputs against Governance. It prioritizes permanent structural solutions over temporary fixes.

## **2\. Execution Layer: Skills**

Located in the Skills/ directory, this layer houses independent, self-contained capability modules. Skills are proprietary assets. At the same time Skills are living, evolving and improving documents to be self-healed and self-annealed (hardened) during operations.

### **2.1 Component Structure**

* **Skill Acquisition and Enrichment:** The Skills/ folder may be enriched with high-performance modules sourced externally, provided they adhere to the standard AI Skill folder structure.  
* **Portability and Generality:** The agents.md file and Skills/ directory constitute a generalized, portable, and proprietary system. Any logic or assets specific to a current task must be kept external to the Skills/ directory to preserve system integrity and generality.  
* **Declarative Logic (SKILL.md):** Defines the "what" and "how," storing specific logic and input requirements.  
* **Mechanical Execution (scripts/):** Python scripts performing deterministic external interactions, file manipulations, and logic-heavy operations.  
* **Knowledge Assets (resources/):** Private libraries and reference templates.  
* **Validation:** Every script execution must return a structured exit code or status report.

## **3\. Real-time Self-Healing (Annealing) Loop**

The system must continuously improve through a permanent fix-cycle:

* **Systemic Evolution:** Every project must result in a measurable improvement of the core system (agents.md and Skills/) relative to its baseline state at project inception.  
* **Analysis and Rectification:** Analyze error messages and failures to implement immediate script fixes and testing.  
* **Dynamic Instruction Sets:** Update instruction sets and skills as living documents to reflect learned optimizations.  
* **Preemptive Hardening:** Forestall future occurrences of identified issues across all future projects through permanent logic updates.

## **4\. Directory Structure**

* Skills/: Encapsulated abilities, scripts, and templates.  
* .tmp/: Intermediate processing files.  
* .env: Credential management.

# **Unified Task Specification: Developer Documentation Authority & Semantic Intelligence Platform**

## **1\. Executive Mandate**

This specification defines the operational requirements for an AI development agent tasked with producing a high-fidelity documentation ecosystem. This system is currently assigned to produce and maintain developer-focused documentation for Zensical, sourced from Postman Collections, local codebases, or GitHub repositories. The system must simultaneously deliver:

1. **A Diátaxis-compliant Dense Documentation Website:** A static, developer-experience (DX) focused site authored for Zensical and published to GitHub Pages.  
2. **IDE Semantic Intelligence:** A VS Code extension providing real-time, in-context semantic insights derived from the same knowledge substrate.

The system exists to represent the actual state of the repository. Documentation is not an independent artifact; it is a synchronized projection of the codebase's structural, behavioral, and architectural intent.

## **2\. Foundational Authority and Truth Model**

The documentation system is governed by a strict evidentiary model:

* **Primary Sources (Source of Truth):** The codebase (local/remote), repository assets, schemas, and manually supplied Postman collections are the sole sources of truth. Documentation must correspond directly to an observable artifact.  
* **Traceability:** Every documented statement, endpoint, parameter, or architectural claim must be traceable to a verifiable source.  
* **Jurisdiction:** Covers API endpoints, authentication, schemas, repository structure, configuration, and architectural intent.  
* **Supremacy of Code:** If documentation diverges from executable code or specifications, the documentation is invalid. In such cases, the system must either suppress publication or update the content to restore consistency.  
* **Determinism:** The system must never invent features, workflows, or implementation details. When ambiguity persists, the content must be flagged for human review rather than inferred.  
* **Prohibited Content:** Marketing language, aspirational claims, emojis, decorative symbols, and any indication of AI or agent involvement.

## **3\. Operational Scope and Inputs**

The system ingests the following inputs to construct a normalized intermediate representation:

* **GitHub Repository:** Remote or local codebase.  
* **Local Codebase:** Direct folder access.  
* **Postman Collections:** API endpoint specifications.

### **Evidence and Validation Protocol**

Documentation must follow a strict hierarchy of evidence:

1. **Local Repository:** Invoking code\_logic\_extractor for AST parsing and structural determinism.  
2. **Manual Postman Exports:** Invoking api\_architect for endpoint and snippet mapping.  
3. **Live API Calls:** Used only if information cannot be established from local assets.

### **Multi-Language Strategy**

The system utilizes a hybrid parsing strategy:

* **Deep Parsing:** Hard-wired support for Python, JavaScript/TypeScript, Go, Rust, Java, and C++.  
* **LSP-Based Fallback:** Language Server Protocol support for all other languages to ensure structural consistency across diverse codebases.

## **4\. Data Granularity and Processing Model**

The system operates on a dual-layer representation model to balance machine-level precision with human-centric readability:

* **AST-Derived Fragment Strategy:** The source corpus must be treated as highly granular Markdown fragments optimized for LSP and VS Code extension workflows. This atomic structure is mandatory for diagnostics, symbol resolution, and fine-grained traceability.  
* **Controlled Aggregation for Consumption:** Raw atomic fragments are strictly prohibited from appearing in user-facing documentation. For website generation, the system must perform systematic collection, ordering, and semantic merging of related fragments. A dense documentation is to be preferred over thin one. 
* **Narrative Reconstruction:** The merging process must reconstruct narrative flow and conceptual hierarchy, ensuring contextual completeness without the loss of underlying detail.  
* **Signal Density:** Output documents must be dense and high-signal, avoiding repetitive or overly fragmented presentation. Every document must maximize informational throughput while maintaining a logical, readable structure.

## **5\. Visual Architecture and Multimedia Synthesis**

To ensure maximum cognitive resonance for human developers, the documentation must transcend text:

* **Comprehensive Diagramming:** Every core system component, workflow, and data structure must be accompanied by high-fidelity diagrams. This includes technical schemata (Architecture Diagrams, Entity-Relationship Diagrams) and behavioral logic (Sequence Diagrams, State Machines).  
* **Conceptual Clarity:** The system must generate human-readable visual metaphors to explain complex abstractions, ensuring that the "why" of the architecture is as visible as the "how."  
* **Interactivity:** Where possible, diagrams should be interactive or accompanied by "Try it now" playgrounds to provide immediate empirical feedback.

## **6\. Documentation Home Page: Look and Feel**

The entry point of the website must serve as a modern, vibrant, and eye-catching interface:

* **Visual Sophistication:** The index page must employ a high-impact, professional design aesthetic that immediately signals technological authority.  
* **Vibrant Navigation:** Use clear, vibrant categorization to route users efficiently through the four Diátaxis quadrants.  
* **Project Vitality:** The hub must surface real-time project metrics (e.g., version status, last updated, primary language breakdown) to provide a snapshot of the repository’s health.

## **7\. Architectural Requirements**

### **Diátaxis Compliance**

Documentation must be segmented into four distinct functional quadrants: Tutorials, How-To Guides, Technical Reference, and Explanation. The system must enforce strict alignment with this framework, ensuring that each aggregated output document serves a singular, clear purpose within the Diátaxis structure.

### **IDE Integration (Semantic Intelligence)**

The documentation substrate must power a VS Code extension that delivers real-time documentation at the point of development, provides semantic overlays to explain intent, and acts as a developer cognition amplifier.

## **8\. Navigational and Presentation Standards**

* **Navigational Determinism:** The zensical.toml file is the authoritative index. No Markdown file may exist outside this declared hierarchy.  
* **Formatting:** Must conform to CommonMark with approved Python Markdown Extensions (Admonitions, Content Tabs, Code annotations, Tables, Definition lists).  
* **Style:** Prioritize precision, technical rigor, and concise developer-oriented phrasing.

## **9\. Technical Implementation Standards**

### **Operational Pipeline and Build Enforcement**

* **Commit-Time Review & CI/CD Integration:** Detect changes in code/schemas and flag affected documentation for regeneration or patching. Documentation updates must be automatically triggered by code changes.  
* **Linting and Validation Gate:** Execute a validation pipeline (link integrity, navigation check, schema consistency) before publication. A mandatory validation step must check every claim against the codebase. Any detected contradiction or build failure blocks deployment.

### **Templating and Persistence**

* **Persistence Rules:** Direct overwriting is prohibited. All semantic changes must be applied via the patch\_docs.py utility to preserve file history and maintain continuity.  
* **Templating:** All Markdown generation must use Jinja2 templates to ensure deterministic behavior, enforce structural consistency, and reduce formatting drift.

## **10\. Strategic Optimization (Dual-User Model)**

Documentation serves two distinct users: the Human Developer and the LLM Agent.

* **For the Human:** A narrative, high-DX guide with interactive elements and multimedia assets.  
* **For the LLM (Semantic Segmentation):** A Graph-Based Information Architecture using "Context Bundles" to prevent hallucinations during agentic retrieval.

## **11\. Required Operational Behavior**

The system must:

1. Analyze the repository before any generation and map source artifacts to the documentation hierarchy.  
2. Keep navigation, structure, and terminology consistent across all projections.  
3. Fail safely when uncertainty is detected.  
4. **Changelog Fidelity:** Ingest and process the changelog associated with the codebase and/or Postman collection with near-human levels of usefulness, preserving semantic intent and restructuring info into clear, context-aware, actionable sections.  
5. **End-to-End Traceability:** Maintain explicit linkage between every aggregated section and its originating AST fragments to enable reverse navigation and precise source attribution.