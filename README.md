# complaint-rag-chatbot

Retrieval-Augmented Generation (RAG) pipeline for analyzing CFPB complaint narratives and delivering actionable insights via an interactive AI chatbot.

##  Features

* **End-to-End Pipeline**: From data ingestion and cleaning, to text chunking, embedding, and semantic search.
* **FAISS Vector Store**: High-performance nearest-neighbor search over complaint chunks.
* **RAG Core**: Prompt template and retrieval logic to generate evidence-backed answers using an LLM.
* **Interactive UI**: Streamlit app for natural-language Q\&A with source citations.
* **Branch-per-Task Workflow**: Dedicated branches for Task 1–4 to isolate development.
* **CI & Testing**: GitHub Actions with linter (flake8) and pytest smoke tests.

## Repository Structure

```
complaint-rag-chatbot/
├── .github/workflows/ci.yml    # CI pipeline configuration
├── data/                       # Data folder (ignored raw files)
│   └── raw/                    # Raw CSVs (not tracked)
├── notebooks/                  # Exploration & Task notebooks
│   ├── eda.ipynb               # Task 1: EDA & Preprocessing
│   └── task2_chunk_embed.ipynb # Task 2: Chunking & Embedding
├── scripts/                    # Standalone Python scripts
│   ├── chunk_embed_index.py    # Task 2: FAISS index builder
│   └── clean_notebooks.py      # Utility: strip notebook widget metadata
├── src/                        # Core RAG pipeline modules
│   └── rag_pipeline.py         # Task 3: retrieve & generate logic
├── vector_store/               # Vector store output (ignored .bin, tracked metadata)
│   └── metadata.json
├── tests/                      # pytest tests
│   └── test_initial.py         # Smoke test
├── app.py                      # Task 4: Streamlit chat interface
├── .gitignore                  # Ignored files & folders
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🛠️ Getting Started

### Prerequisites

* Python 3.11
* Git
* (Optional) Google Colab for GPU-accelerated notebook runs

### Installation

```bash
# Clone the repo
git clone https://github.com/lhiwi/complaint-rag-chatbot.git
cd complaint-rag-chatbot

# Create and activate virtual environment
python -m venv .venv
# On Windows PowerShell:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### CI & Testing

* **Lint**: `flake8 src scripts tests`
* **Test**: `pytest -q`

GitHub Actions runs linting and tests on every push to `main`.

## 📚 Task Branches

* **`task1-eda`**: Exploratory Data Analysis & Preprocessing (notebooks/eda.ipynb)
* **`task2`**: Text Chunking, Embedding & FAISS Indexing (scripts/ & notebook)
* **`task3`**: Retrieval & Generation Core, Qualitative Evaluation
* **`task4`**: Interactive Streamlit chat application

Each branch should be merged into `main` via Pull Request when tasks are complete.

### Run Scripts Locally

```bash
# Build vector store (Task 2)
python scripts/chunk_embed_index.py
```

### Start Streamlit App (Task 4)

```bash
streamlit run app.py
```

