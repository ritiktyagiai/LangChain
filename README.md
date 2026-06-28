# 🚀 LangChain Learning Hub

> A comprehensive learning repository for mastering LangChain, building intelligent LLM applications with Python.

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Latest-00A67E?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Setup & Installation](#-setup--installation)
- [Quick Start](#-quick-start)
- [Module Guide](#-module-guide)
- [Tech Stack](#-tech-stack)
- [Environment Configuration](#-environment-configuration)
- [Troubleshooting](#-troubleshooting)
- [Learning Resources](#-learning-resources)

---

## 🎯 Overview

This project is a hands-on learning repository for exploring **LangChain**, a powerful framework for developing applications powered by large language models (LLMs). Through practical implementations, you'll learn how to:

- Integrate multiple LLM providers (Gemini, OpenAI, Anthropic)
- Build intelligent chatbots and conversational AI systems
- Work with embeddings for semantic search and document retrieval
- Chain operations for complex AI workflows

---

## ✨ Features

- 🤖 **LLM Integration** - Direct interaction with Google Gemini and other LLM providers
- 💬 **Chatbot Development** - Build interactive chat applications with conversation memory
- 📚 **Embeddings & RAG** - Document embedding and semantic search capabilities
- 🔌 **Multi-Provider Support** - OpenAI, Anthropic, Google Gemini, Hugging Face
- 🎓 **Educational Focus** - Well-documented code with step-by-step examples
- ⚙️ **Easy Setup** - Virtual environment management with requirements.txt

---

## 📁 Project Structure

```
LangChain/
├── 1. Model/
│   ├── 1. LLM/
│   │   └── gemini.py                 # Direct LLM interaction with Google Gemini
│   ├── 2. ChatBots/
│   │   └── chat-gemini.py           # Interactive chatbot implementation
│   ├── 3. Embedded/
│   │   ├── embed_document.py        # Document embedding generation
│   │   └── embed_query.py           # Query embedding for semantic search
│   ├── InstalltionVerify.py          # Verify LangChain installation
│   ├── requirements.txt              # Project dependencies
│   ├── steps.txt                     # Setup instructions
│   ├── .env                          # Environment variables (API keys)
│   └── venv/                         # Virtual environment directory
├── README.md                         # This file
└── .git/                             # Git repository
```

### Module Overview

### 1. Model

| Module | Purpose | Output |
|--------|---------|--------|
| **LLM** | Direct interaction with Large Language Models | Text responses |
| **ChatBots** | Conversational AI with context awareness | Interactive text |
| **Embeddings** | Convert documents/queries to vector representations | Numerical embeddings |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/) (optional)
- **API Keys** - For LLM providers (Gemini, OpenAI, Anthropic)

---

## 🔧 Setup & Installation

### Step 1: Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd LangChain

# Or simply navigate to your LangChain folder
cd LangChain
cd 1.\ Model
```

### Step 2: Create a Python Virtual Environment

Navigate to the Model directory first:

```bash
cd 1.\ Model
```

Then create the virtual environment:

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Verify Installation

```bash
python InstalltionVerify.py
```

A successful output will display the LangChain version and available integrations.

---

## ⚡ Quick Start

### 1. Set Up Environment Variables

Create a `.env` file in the project root with your API keys:

```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# OpenAI API (optional)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API (optional)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Hugging Face (optional)
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

**How to get API keys:**
- [Google Gemini API](https://ai.google.dev/tutorials/setup)
- [OpenAI API](https://platform.openai.com/account/api-keys)
- [Anthropic Claude API](https://console.anthropic.com/)
- [Hugging Face API](https://huggingface.co/settings/tokens)

### 2. Run Your First Example

```bash
# Test basic LLM functionality
python 1.\ LLM/gemini.py

# Start interactive chatbot
python 2.\ ChatBots/chat-gemini.py

# Generate embeddings
python 3.\ Embedded/embed_document.py
```

---

## 📚 Module Guide

### 1. LLM Module (`1. Model/1. LLM/`)

**File:** `gemini.py`

This module demonstrates direct interaction with Google's Gemini LLM.

**Key Concepts:**
- Initializing LLM instances
- Generating text responses
- Configuring model parameters
- Handling API responses

**Example Usage:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
response = llm.invoke("What is LangChain?")
print(response)
```

---

### 2. ChatBots Module (`1. Model/2. ChatBots/`)

**File:** `chat-gemini.py`

Build interactive chatbots with conversation memory and context awareness.

**Key Concepts:**
- Conversation history management
- Memory/context maintenance
- Chat message formatting
- Interactive prompt handling

**Example Usage:**
```python
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

memory = ConversationBufferMemory()
llm = ChatGoogleGenerativeAI(model="gemini-pro")
# Build conversational chain...
```

---

### 3. Embeddings Module (`1. Model/3. Embedded/`)

**Files:** 
- `embed_document.py` - Convert documents to embeddings
- `embed_query.py` - Convert queries to embeddings for search

**Key Concepts:**
- Document vectorization
- Semantic similarity
- Vector databases
- Retrieval-Augmented Generation (RAG)

**Example Usage:**
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
doc_embedding = embeddings.embed_query("Your document text here")
```

---

## 🛠️ Tech Stack

### Core Framework
- **LangChain** - Framework for building LLM applications
- **LangChain Core** - Core abstractions and interfaces

### LLM Providers
- **Google Gemini** - `langchain-google-genai`
- **OpenAI** - `langchain-openai`
- **Anthropic Claude** - `langchain-anthropic`
- **Hugging Face** - `langchain-huggingface`

### Supporting Libraries
- **python-dotenv** - Environment variable management
- **numpy** - Numerical computing
- **scikit-learn** - ML utilities

---

## 🔐 Environment Configuration

### .env File Setup

The `.env` file stores sensitive API keys and shouldn't be committed to version control.

**Create `.env` file:**
```bash
# Windows
echo. > .env

# macOS/Linux
touch .env
```

**Update `.gitignore` (if using Git):**
```
.env
venv/
__pycache__/
*.pyc
.DS_Store
```

### Loading Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

---

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError: No module named 'langchain'**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

**2. API Key not recognized**
- Verify `.env` file exists in project root
- Check API key is correct and has necessary permissions
- Restart your Python interpreter after updating `.env`

**3. Virtual environment not activating**
```bash
# Try explicit PowerShell execution
powershell -ExecutionPolicy Bypass -File venv\Scripts\Activate.ps1
```

**4. Import errors for specific providers**
```bash
# Install specific integration
pip install langchain-openai    # For OpenAI
pip install langchain-anthropic # For Anthropic
```

---

## 📖 Learning Resources

### Official Documentation
- [LangChain Official Docs](https://python.langchain.com/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [Google Gemini API Docs](https://ai.google.dev/)

### Tutorials & Guides
- [LangChain Quickstart](https://python.langchain.com/docs/get_started)
- [Building Chains](https://python.langchain.com/docs/modules/chains)
- [Memory & Context](https://python.langchain.com/docs/modules/memory)
- [Embeddings & Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)

### Related Concepts
- **Retrieval Augmented Generation (RAG)** - Combining retrieval with generation
- **Prompt Engineering** - Crafting effective prompts for LLMs
- **Vector Databases** - Storing and searching embeddings
- **Agents** - Autonomous LLM-powered systems

---

## 🎓 Learning Path

1. **Start:** Explore `1. LLM/gemini.py` to understand basic LLM interaction
2. **Progress:** Build conversational systems with `2. ChatBots/chat-gemini.py`
3. **Advanced:** Implement semantic search with `3. Embedded/`
4. **Challenge:** Combine modules to build a RAG system

---

## 💡 Tips for Learning

- ✅ Read and understand the code comments
- ✅ Experiment with different prompts and parameters
- ✅ Check LangChain documentation for API details
- ✅ Use print statements to debug and understand data flow
- ✅ Try implementing variations of the examples

---

## 📝 Next Steps

- [ ] Complete all three modules
- [ ] Integrate with your own LLM provider
- [ ] Build a custom chatbot application
- [ ] Implement Retrieval-Augmented Generation (RAG)
- [ ] Explore LangChain Agents
- [ ] Create a real-world application

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Found a bug or have an improvement? Feel free to open an issue or submit a pull request!

---

## 📞 Support

- 📚 Check the [Troubleshooting](#-troubleshooting) section
- 🔗 Visit [LangChain Documentation](https://python.langchain.com/)
- 💬 Ask questions in LangChain Discord/Community

---

## 🌟 Acknowledgments

This learning repository is built to help me to master LangChain and LLM development. Special thanks to the LangChain community for excellent documentation and tools.

---

**Happy Learning! 🎉** Start exploring LangChain and build amazing AI applications! 
